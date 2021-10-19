import re
from typing import List, Optional

from web_adapter import WebAdapter
from web_adapter.materials import URL, ElementHint, Type


class MercariAPI:
    BASE_URL = URL("https://jp.mercari.com/search{query}")
    EH_ITEM = ElementHint("ul > li > a > mer-item-thumbnail", Type.CSS_SELECTOR)

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
        #print(url)
        self.web_adapter.get_page(url)
        return self.scrape_item_info()

    def scrape_item_info(self):
        """
        Execute this after self.search()!
        """
        item_info = []
        items = self.web_adapter.find_elements(MercariAPI.EH_ITEM)
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
