from pprint import pprint

from mercari_api import Mercari
from mercari_api.params import (
    Category,
    ItemCondition,
    SalesStatus,
    ShippingPayer,
    Size,
    SortOrder,
)


def main():
    mercari = Mercari()
    params = {
        "page": 1,
        "sort_order": SortOrder.CREATED_DESC,
        "keyword": "iPhone12 pro",
        "category_root": Category.HOME_ELECTRONICS,
        "brand_name": "アップル",
        # "size_group": Size.BabyCloth.id(),
        # "size_child": [Size.BabyCloth._60cm, Size.BabyCloth._80cm],
        "price_max": 80000,
        "price_min": 50000,
        "item_conditions": [ItemCondition.ALL],
        "shipping_payer": [ShippingPayer.ALL],
        "sales_status": [SalesStatus.ON_SALE],
    }
    items = mercari.fetch_items(**params)
    pprint(items)


if __name__ == "__main__":
    main()
