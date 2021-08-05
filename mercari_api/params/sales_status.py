from .simple_enum import SimpleEnum


class SalesStatus(SimpleEnum):
    ON_SALE = ("status_on_sale", "販売中")
    SOLD_OUT = ("status_trading_sold_out", "売り切れ")
    ALL = ("status_all", "すべて")
