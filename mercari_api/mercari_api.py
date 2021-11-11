import re
from typing import List, Optional

from web_adapter import WebAdapter
from web_adapter.materials import URL, ElementHint, Type


class MercariAPI:
    BASE_URL = URL("https://jp.mercari.com/search{query}")
    ITEM_URL = URL("https://jp.mercari.com/item/{item_id}")
    USER_URL = URL("https://jp.mercari.com/user/profile/{user_id}")
    EH_ITEM = ElementHint("ul > li > a > mer-item-thumbnail", Type.CSS_SELECTOR)
    EH_ITEM_ONSALE = ElementHint(
        "ul > li > a > mer-item-thumbnail:not([sticker])", Type.CSS_SELECTOR
    )
    EH_LIKE = ElementHint(
        'mer-icon-button[data-testid="icon-heart-button"]', Type.CSS_SELECTOR
    )
    EH_COMMENT = ElementHint(
        'mer-tooltip[text="コメント"] > mer-icon-button', Type.CSS_SELECTOR
    )
    EH_USERLINK = ElementHint(
        'a[data-location="item:seller_info:link:go_user_profile"]', Type.CSS_SELECTOR
    )

    def __init__(self, is_headless=True):
        self.web_adapter = WebAdapter(is_headless=is_headless)

    def make_query(
        self,
        page: int = 1,
        keyword: Optional[str] = None,
        category_id: Optional[int] = None,
        c_category_id: Optional[int] = None,
        gc_category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        item_condition_id: Optional[List[int]] = None,
        shipping_payer_id: Optional[int] = None,
        color_id: Optional[List[int]] = None,
        shipping_method: Optional[str] = None,
        sale_status: Optional[str] = None,
        limit: Optional[int] = None,
    ):
        query = f"?page={page}"

        # keyword
        if keyword is not None:
            query += f"&keyword={keyword}"

        # category
        if category_id is not None:
            category_id = category_id
            query += f"&t1_category_id={category_id}"
        if c_category_id is not None:
            category_id = c_category_id
            query += f"&t2_category_id={c_category_id}"
        if gc_category_id is not None:
            category_id = gc_category_id
            query += f"&t3_category_id={gc_category_id}"
        if any([category_id, c_category_id, gc_category_id]):
            query += f"&category_id={category_id}"

        # brand
        if brand_id is not None:
            query += f"&brand_id={brand_id}"

        # price
        if price_min is not None:
            query += f"&price_min={price_min}"
        if price_max is not None:
            query += f"&price_max={price_max}"

        # item_condition
        if item_condition_id not in [None, []]:
            item_condition_id = [str(item) for item in item_condition_id]
            query += f"&item_condition_id={','.join(item_condition_id)}"

        # shipping_payer
        if shipping_payer_id is not None:
            query += f"&shipping_payer_id={shipping_payer_id}"

        # color
        if color_id not in [None, []]:
            color_id = [str(item) for item in color_id]
            query += f"&color_id={','.join(color_id)}"

        # shipping_method
        if shipping_method is not None:
            query += f"&shipping_method={shipping_method}"

        # sale_status
        if sale_status is not None:
            query += f"&status={sale_status}"

        # limit
        if limit is not None:
            query += f"&limit={limit}"

        return query

    def search(
        self,
        page: int = 1,
        keyword: Optional[str] = None,
        category_id: Optional[int] = None,
        c_category_id: Optional[int] = None,
        gc_category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        item_condition_id: Optional[List[int]] = None,
        shipping_payer_id: Optional[int] = None,
        color_id: Optional[List[int]] = None,
        shipping_method: Optional[str] = None,
        sale_status: Optional[str] = None,
        limit: Optional[int] = None,
    ):
        query = self.make_query(
            page=page,
            keyword=keyword,
            category_id=category_id,
            c_category_id=c_category_id,
            gc_category_id=gc_category_id,
            brand_id=brand_id,
            price_min=price_min,
            price_max=price_max,
            item_condition_id=item_condition_id,
            shipping_payer_id=shipping_payer_id,
            color_id=color_id,
            shipping_method=shipping_method,
            sale_status=sale_status,
            limit=limit,
        )
        url = MercariAPI.BASE_URL.fnew(query=query)
        self.web_adapter.get_page(url)
        return self.scrape_item_info()

    def scrape_item_info(self, on_sale_only=False):
        """
        Execute this after self.search()!
        """
        if on_sale_only:
            eh = MercariAPI.EH_ITEM_ONSALE
        else:
            eh = MercariAPI.EH_ITEM

        item_info = []
        items = self.web_adapter.find_elements(eh)
        for item in items:
            item_info.append(
                {
                    "item_id": re.search(
                        r"(?P<item_id>m[0-9]+)", item.get_attribute("src")
                    ).group("item_id"),
                    "price": item.get_attribute("price"),
                    "thumbnail": item.get_attribute("src"),
                    "title": item.get_attribute("item-name"),
                }
            )
        return item_info

    def get_item_detail(self, item_id: str):
        url = MercariAPI.ITEM_URL.fnew(item_id=item_id)
        self.web_adapter.get_page(url)
        resp = self.scrape_item_detail()
        resp["item_id"] = item_id
        return resp

    def scrape_item_detail(self):
        like = 0
        like_element = self.web_adapter.find_element(MercariAPI.EH_LIKE)
        if like_element is not None:
            try:
                like = int(like_element.get_attribute("label"))
            except Exception:
                like = 0

        comment = 0
        comment_element = self.web_adapter.find_element(MercariAPI.EH_COMMENT)
        if comment_element is not None:
            try:
                comment = int(comment_element.get_attribute("label"))
            except Exception:
                comment = 0

        user_id = ""
        userid_element = self.web_adapter.find_element(MercariAPI.EH_USERLINK)
        if userid_element is not None:
            userurl = userid_element.get_attribute("href")
            user_id = re.search(r"/user/profile/(?P<user_id>[0-9]+)", userurl).group(
                "user_id"
            )
        return {"like": like, "comment": comment, "user_id": user_id}

    def search_from_user_id(
        self,
        user_id: str,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
    ):
        if price_max is None:
            price_max = 10e12  # 1兆
        if price_min is None:
            price_min = -1
        url = MercariAPI.USER_URL.fnew(user_id=user_id)
        self.web_adapter.get_page(url)
        items = self.scrape_item_info(on_sale_only=True)

        filtered_items = []
        for item in items:
            if price_min <= int(item["price"]) <= price_max:
                filtered_items.append(item)
        return filtered_items
