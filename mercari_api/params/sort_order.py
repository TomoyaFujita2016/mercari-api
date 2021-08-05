from .simple_enum import SimpleEnum


class SortOrder(SimpleEnum):
    PRICE_ASC = ("price_asc", "価格の安い順")
    PRICE_DESC = ("price_desc", "価格の高い順")
    CREATED_DESC = ("created_desc", "出品の新しい順")
    LIKE_DESC = ("like_desc", "いいね!の多い順")
