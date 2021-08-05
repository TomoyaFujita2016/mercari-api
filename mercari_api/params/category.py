from .simple_enum import SimpleEnum


class Category(SimpleEnum):
    LADYS = (1, "レディース")
    MENS = (2, "メンズ")
    BABY = (3, "ベビー・キッズ")
    INTERIOR = (4, "インテリア・住まい・小物")
    BOOK = (5, "本・音楽・ゲーム")
    TOY = (1328, "おもちゃ・ホビー・グッズ")
    COSME = (6, "コスメ・香水・美容")
    HOME_ELECTRONICS = (7, "家電・スマホ・カメラ")
    SPORTS_LEISURE = (8, "スポーツ・レジャー")
    HAND_MADE = (9, "ハンドメイド")
    TICKET = (1027, "チケット")
    CAR_MOTORCYCLE = (1318, "自動車・オートバイ")
    OTHER = (10, "その他")
