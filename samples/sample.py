import time

from mercari_api import MercariAPI
from mercari_api.params import (
    Brand,
    Category,
    Color,
    ItemCondition,
    SaleStatus,
    ShippingMethod,
    ShippingPayer,
)

# print(category["メンズ"])
mercari = MercariAPI()

root_category = Category["家電・スマホ・カメラ"]
child_category = root_category["child"]["スマートフォン/携帯電話"]
grand_child_category = child_category["child"]["スマートフォン本体"]
params = {
    "page": 1,
    "keyword": "iphone",
    "category_id": root_category["id"],
    "c_category_id": child_category["id"],
    "gc_category_id": grand_child_category["id"],
    "brand_id": Brand["Apple"],
    "price_min": 200,
    "price_max": 150000,
    "item_condition_id": [ItemCondition["新品、未使用"], ItemCondition["目立った傷や汚れなし"]],
    "shipping_payer_id": ShippingPayer["送料込み(出品者負担)"],
    "color_id": [Color["グレイ系"], Color["ブラック系"]],
    "shipping_method": ShippingMethod["匿名配送"],
    "sale_status": SaleStatus["販売中"],
    "limit": 5,
}

resp = mercari.search(**params)
print(resp)
# limit = 25000
# error_cnt = 0
# resp = mercari.search(**params)
# print(resp)
# exit()
# for i in range(limit):
#     print(f"[*]{i}/{limit}, error: {error_cnt}")
#     start_time = time.perf_counter()
#     try:
#         resp = mercari.search(**params)
#     except Exception as e:
#         print(f"[*]error is occured! {e}")
#         error_cnt += 1
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#     print(f"{elapsed_time} sec, {len(resp)} items")
