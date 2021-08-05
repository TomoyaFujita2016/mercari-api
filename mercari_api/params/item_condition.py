from .simple_enum import SimpleEnum


class ItemCondition(SimpleEnum):
    ALL = ("condition_all", "すべて")
    NEW = ("item_condition_id[1]", "新品、未使用")
    EXCELLENT = ("item_condition_id[2]", "未使用に近い")
    VERY_GOOD = ("item_condition_id[3]", "目立った傷や汚れなし")
    FAIR = ("item_condition_id[4]", "やや傷や汚れあり")
    BAD = ("item_condition_id[5]", "傷や汚れあり")
    VERY_BAD = ("item_condition_id[6]", "全体的に状態が悪い")
