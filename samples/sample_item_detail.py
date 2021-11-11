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

resp = mercari.get_item_detail("m56454167448")
print(resp)
resp = mercari.get_item_detail("m78249369097")
print(resp)

resp = mercari.search_from_user_id("737300647", price_max=40000)
print(resp)
