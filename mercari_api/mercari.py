from typing import List, Optional

import lxml.html
import requests
from bs4 import BeautifulSoup

from .logger import log
from .params.category import Category
from .params.item_condition import ItemCondition
from .params.sales_status import SalesStatus
from .params.shipping_payer import ShippingPayer
from .params.size import Size
from .params.sort_order import SortOrder


class Mercari:
    BASE_URL = "https://www.mercari.com"
    SEARCH_URL = f"{BASE_URL}/jp/search/"
    CSS_SELECTOR = {
        "items-box": "div.l-content > section > div.items-box-content.clearfix",
        "item-section": "section.items-box",
        "item-price": "div.items-box-price",
        "item-name": "h3.items-box-name",
        "item-like": "div > span",
    }

    def __init__(self):
        pass

    def __get_request(self, url: str):
        headers = {
            "User-Agent": "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'"
        }
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code != 200:
            log.error(response)
            raise ConnectionError()
        return response

    def make_url(
        self,
        page: int = 1,
        sort_order: Optional[str] = None,
        keyword: Optional[str] = None,
        category_root: Optional[str] = None,
        brand_name: Optional[str] = None,
        size_group: Optional[str] = None,
        size_child: Optional[List[str]] = None,
        price_max: Optional[int] = None,
        price_min: Optional[int] = None,
        item_conditions: List[Optional[str]] = None,
        shipping_payer: Optional[str] = None,
        sales_status: Optional[SalesStatus] = None,
    ):
        """
        Args:
            page (int): ページ番号,
            sort_order (Optional[SortOrder]): ソート順
            keyword (Optional[str]): キーワード
            category_root (Optional[Category]): 親カテゴリ(例: メンズ)
            brand_name (Optional[str]): ブランド名(例: シャネル)
            size_group (Optional[Size]): サイズグループ(例: メンズ靴のサイズ)
            size_child (Optional[Size]): 子サイズ(例: 25.5cm)
            price_max (Optional[int]): 最大価格
            price_min (Optional[int]): 最小価格 item_conditions (List[Optional[ItemCondition]]): 商品の状態(例: 未使用に近い) shipping_payer (Optional[ShippingPayer]): 配送料の負担(例:着払い) sales_status (Optional[SalesStatus]): 販売状況(例: 販売中)

        """
        output_url = Mercari.SEARCH_URL
        if page:
            output_url += f"?page={page}"
        if sort_order:
            output_url += f"&sort_order={sort_order}"
        if keyword:
            output_url += f"&keyword={keyword}"
        if category_root:
            output_url += f"&category_root={category_root}"
        if brand_name:
            output_url += f"&brand_name={brand_name}"
        if size_group:
            output_url += f"&size_group={size_group}"
        if size_child:
            for value in size_child:
                output_url += f"&{value}=1"
        if price_max:
            output_url += f"&price_max={price_max}"
        if price_min:
            output_url += f"&price_min={price_min}"
        if item_conditions:
            # ALLがあれば全部追加
            if ItemCondition.ALL in item_conditions:
                for value in ItemCondition:
                    output_url += f"&{value}=1"
            # 無ければ素直に受け取ったものを追加
            else:
                for value in item_conditions:
                    output_url += f"&{value}=1"
        if shipping_payer:
            # ALLがあれば全部追加
            if ShippingPayer.ALL in shipping_payer:
                for value in ShippingPayer:
                    output_url += f"&{value}=1"
            # 無ければ素直に受け取ったものを追加
            else:
                for value in shipping_payer:
                    output_url += f"&{value}=1"
        if sales_status:
            # ALLがあれば全部追加
            if SalesStatus.ALL in sales_status:
                for value in SalesStatus:
                    output_url += f"&{value}=1"
            # 無ければ素直に受け取ったものを追加
            else:
                for value in sales_status:
                    output_url += f"&{value}=1"
        return output_url

    def fetch_items(
        self,
        page: int = 1,
        sort_order: Optional[str] = None,
        keyword: Optional[str] = None,
        category_root: Optional[str] = None,
        brand_name: Optional[str] = None,
        size_group: Optional[str] = None,
        size_child: Optional[List[str]] = None,
        price_max: Optional[int] = None,
        price_min: Optional[int] = None,
        item_conditions: Optional[List[str]] = None,
        shipping_payer: Optional[List[str]] = None,
        sales_status: Optional[List[str]] = None,
    ):
        log.debug(f"page={page}")
        url = self.make_url(
            page=page,
            sort_order=sort_order,
            keyword=keyword,
            category_root=category_root,
            brand_name=brand_name,
            size_group=size_group,
            size_child=size_child,
            price_max=price_max,
            price_min=price_min,
            item_conditions=item_conditions,
            shipping_payer=shipping_payer,
            sales_status=sales_status,
        )
        log.debug(f"URL: {url}")
        response = self.__get_request(url)
        items = self.scrape(response)
        log.debug(f"Collected items: {len(items)}")
        return items

    def scrape(self, response) -> list:
        items = []
        soup = BeautifulSoup(response.text, "lxml")
        items_box = soup.select(Mercari.CSS_SELECTOR["items-box"])
        if len(items_box) == 0:
            return items
        items_box = items_box[0]

        for item_section in items_box.select(Mercari.CSS_SELECTOR["item-section"]):
            # 価格を抽出
            price_trans = str.maketrans("", "", ",¥")
            price_elements = item_section.select(Mercari.CSS_SELECTOR["item-price"])
            if len(price_elements) == 0:
                price = -1
            else:
                price = price_elements[0].text.translate(price_trans)
            # 商品名を抽出
            name_elements = item_section.select(Mercari.CSS_SELECTOR["item-name"])
            if len(name_elements) == 0:
                name = "-"
            else:
                name = name_elements[0].text
            # 商品URLを抽出
            url_element = item_section.find("a")
            if url_element is None:
                url = ""
            else:
                url = Mercari.BASE_URL + url_element.get("href")
            # いいね数を抽出
            like_elements = item_section.select(Mercari.CSS_SELECTOR["item-like"])
            if len(like_elements) == 0:
                like = 0
            else:
                like = like_elements[0].text

            items.append({"price": price, "name": name, "url": url, "like": like})
        return items
