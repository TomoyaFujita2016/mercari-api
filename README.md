# mercari-api
## Installation
- poetry
```
poetry add git+https://github.com/TomoyaFujita2016/mercari-api.git#main
```
- pip
```
pip3 install git+https://github.com/TomoyaFujita2016/mercari-api.git#main
```
## Sample
```python
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

"""Out
[DEBUG] [2021-08-05 21:18:35,718] [mercari.py:133] page=1
[DEBUG] [2021-08-05 21:18:35,718] [mercari.py:148] URL: https://www.mercari.com/jp/search/?page=1&sort_order=created_desc&keyword=iPhone12 pro&category_root=7&brand_name=アップル&price_max=80000&price_min=50000&condition_all=1&item_condition_id[1]=1&item_condition_id[2]=1&item_condition_id[3]=1&item_condition_id[4]=1&item_condition_id[5]=1&item_condition_id[6]=1&shipping_payer_all=1&shipping_payer_id[1]=1&shipping_payer_id[2]=1&status_on_sale=1
[DEBUG] [2021-08-05 21:18:36,563] [mercari.py:151] Collected items: 109
[{'like': 0,
  'name': '新品未開封品！ iPhone 12 mini 64GB SIMフリー レッド',
  'price': '79800',
  'url': 'https://www.mercari.com/jp/items/m85197570279/'},
 {'like': '20',
  'name': 'Iphone 12 pro 128GB ジャンク',
...略...
"""
```
