from .simple_enum import SimpleEnum


class ShippingPayer(SimpleEnum):
    ALL = ("shipping_payer_all", "すべて")
    CASH_ON_SHIPPING = ("shipping_payer_id[1]", "着払い(購入者負担)")
    FEE_INCLUDED = ("shipping_payer_id[2]", "送料込み(出品者負担)")
