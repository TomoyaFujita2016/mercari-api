from .simple_enum import SimpleEnum


class _Cloth(SimpleEnum):
    XXS = ("size_id[153]", "XXS以下")
    XS = ("size_id[154]", "XS(SS)")
    S = ("size_id[2]", "S")
    M = ("size_id[3]", "M")
    L = ("size_id[4]", "L")
    XL = ("size_id[5]", "XL(LL)")
    _2XL = ("size_id[155]", "2XL(3L)")
    _3XL = ("size_id[156]", "3XL(4L)")
    _4XL = ("size_id[157]", "4XL(5L)以上")
    FREE_SIZE = ("size_id[7]", "FREE SIZE")

    @staticmethod
    def id():
        return "1"

    @staticmethod
    def name():
        return "洋服のサイズ"


class _MensShoes(SimpleEnum):
    _23_5cm = ("size_id[133]", "23.5cm以下")
    _24cm = ("size_id[134]", "24cm")
    _24_5cm = ("size_id[135]", "24.5cm")
    _25cm = ("size_id[136]", "25cm")
    _25_5cm = ("size_id[137]", "25.5cm")
    _26cm = ("size_id[9]", "26cm")
    _26_5cm = ("size_id[10]", "26.5com")
    _27cm = ("size_id[11]", "27cm")
    _27_5cm = ("size_id[12]", "27.5cm")
    _28cm = ("size_id[13]", "28cm")
    _28_5cm = ("size_id[138]", "28.5cm")
    _29cm = ("size_id[139]", "29cm")
    _29_5cm = ("size_id[140]", "29.5cm")
    _30cm = ("size_id[141]", "30cm")
    _30_5cm = ("size_id[142]", "30.5cm")
    _31cm_or_more = ("size_id[143]", "31cm以上")

    @staticmethod
    def id():
        return "2"

    @staticmethod
    def name():
        return "メンズ靴のサイズ"


class _LadysShoes(SimpleEnum):
    _20cm = ("size_id[144]", "20cm以下")
    _20_5cm = ("size_id[145]", "20.5cm")
    _21cm = ("size_id[146]", "21cm")
    _21_5cm = ("size_id[147]", "21.5cm")
    _22cm = ("size_id[148]", "22cm")
    _22_5cm = ("size_id[16]", "22.5cm")
    _23cm = ("size_id[17]", "23cm")
    _23_5cm = ("size_id[18]", "23.5cm")
    _24cm = ("size_id[19]", "24cm")
    _24_5cm = ("size_id[20]", "24.5cm")
    _25cm = ("size_id[21]", "25cm")
    _25_5cm = ("size_id[22]", "25.5cm")
    _26cm = ("size_id[149]", "26cm")
    _26_5cm = ("size_id[150]", "26.5cm")
    _27cm = ("size_id[151]", "27cm")
    _27_5cm_or_more = ("size_id[152]", "27.5cm以上")

    @staticmethod
    def id():
        return "3"

    @staticmethod
    def name():
        return "レディース靴のサイズ"


class _Skirt(SimpleEnum):
    _60cm = ("size_id[34]", "60cm以下")
    _70cm = ("size_id[35]", "~70cm")
    _80cm = ("size_id[36]", "~80cm")
    _90cm = ("size_id[37]", "~90cm")
    _90cm_or_more = ("size_id[38]", "90cm以上")

    @staticmethod
    def id():
        return "6"

    @staticmethod
    def name():
        return "スカートのサイズ"


class _KidsCloth(SimpleEnum):
    _100cm = ("size_id[40]", "100cm")
    _110cm = ("size_id[41]", "110cm")
    _120cm = ("size_id[42]", "120cm")
    _130cm = ("size_id[43]", "130cm")
    _140cm = ("size_id[44]", "140cm")
    _150cm = ("size_id[45]", "150cm")
    _160cm = ("size_id[55]", "160cm")

    @staticmethod
    def id():
        return "7"

    @staticmethod
    def name():
        return "キッズ服のサイズ"


class _BabyKidsShoes(SimpleEnum):
    _10_5cm = ("size_id[47]", "10_5cm以下")
    _11cm_11_5cm = ("size_id[48]", "11cm・11.5cm")
    _12cm_12_5cm = ("size_id[49]", "12cm・12.5cm")
    _13cm_13_5cm = ("size_id[50]", "13cm・13.5cm")
    _14cm_14_5cm = ("size_id[51]", "14cm・14.5cm")
    _15cm_15_5cm = ("size_id[52]", "15cm・15.5cm")
    _16cm_16_5cm = ("size_id[53]", "16cm・16.5cm")
    _17cm_or_more = ("size_id[54]", "17cm以上")

    @staticmethod
    def id():
        return "8"

    @staticmethod
    def name():
        return "ベビー・キッズ靴のサイズ"


class _BabyCloth(SimpleEnum):
    _60cm = ("size_id[56]", "60cm")
    _70cm = ("size_id[57]", "70cm")
    _80cm = ("size_id[58]", "80cm")
    _90cm = ("size_id[59]", "90cm")
    _95cm = ("size_id[60]", "95cm")

    @staticmethod
    def id():
        return "9"

    @staticmethod
    def name():
        return "ベビー服のサイズ"


class _TV(SimpleEnum):
    _20inch = ("size_id[90]", "～20インチ")
    _20_26inch = ("size_id[91]", "20～26インチ")
    _26_32inch = ("size_id[92]", "26～32インチ")
    _32_37inch = ("size_id[93]", "32～37インチ")
    _37_40inch = ("size_id[94]", "37～40インチ")
    _40_42inch = ("size_id[95]", "40～42インチ")
    _42_46inch = ("size_id[96]", "42～46インチ")
    _46_52inch = ("size_id[97]", "46～52インチ")
    _52_60inch = ("size_id[98]", "52～60インチ")
    _60inch_or_more = ("size_id[99]", "60インチ～")

    @staticmethod
    def id():
        return "14"

    @staticmethod
    def name():
        return "テレビのサイズ"


class _CameraLens(SimpleEnum):
    _NIKON_F_MOUNT = ("size_id[114]", "ニコンFマウント")
    _CANON_EF_MOUNT = ("size_id[115]", "キヤノンEFマウント")
    _PENTAX_K_MOUNT = ("size_id[116]", "ペンタックスKマウント")
    _PENTAX_Q_MOUNT = ("size_id[117]", "ペンタックスQマウント")
    _FOUR_THIRDS_MOUNT = ("size_id[118]", "フォーサーズマウント")
    _MICRO_FOUR_THIRDS_MOUNT = ("size_id[119]", "マイクロフォーサーズマウント")
    _A_MOUNT = ("size_id[120]", "α Aマウント")
    _E_MOUNT = ("size_id[121]", "α Eマウント")
    _NIKON_1_MOUNT = ("size_id[122]", "ニコン1マウント")
    _CANON_EF_M_MOUNT = ("size_id[123]", "キヤノンEF-Mマウント")
    _X_MOUNT = ("size_id[124]", "Xマウント")
    _SIGMA_SA_MOUNT = ("size_id[125]", "シグマSAマウント")

    @staticmethod
    def id():
        return "17"

    @staticmethod
    def name():
        return "カメラレンズのサイズ"


class _Motorcycle(SimpleEnum):
    _50cc = ("size_id[76]", "50cc以下")
    _51cc_125cc = ("size_id[77]", "51cc-125cc")
    _126cc_250cc = ("size_id[78]", "126cc-250cc")
    _251cc_400cc = ("size_id[79]", "251cc-400cc")
    _401cc_750cc = ("size_id[80]", "401cc-750cc")
    _751cc_or_more = ("size_id[81]", "751cc以上")

    @staticmethod
    def id():
        return "12"

    @staticmethod
    def name():
        return "オートバイのサイズ"


class _Helmet(SimpleEnum):
    _XS = ("size_id[82]", "XSサイズ以下")
    _S = ("size_id[83]", "Sサイズ")
    _M = ("size_id[84]", "Mサイズ")
    _L = ("size_id[85]", "Lサイズ")
    _XL = ("size_id[86]", "XLサイズ")
    _XXL = ("size_id[87]", "XXLサイズ以上")
    _FREE_SIZE = ("size_id[88]", "フリーサイズ")
    _KIDS = ("size_id[89]", "子ども用")

    @staticmethod
    def id():
        return "13"

    @staticmethod
    def name():
        return "ヘルメットのサイズ"


class _Tire(SimpleEnum):
    _12inch = ("size_id[158]", "12インチ")
    _13inch = ("size_id[67]", "13インチ")
    _14inch = ("size_id[68]", "14インチ")
    _15inch = ("size_id[69]", "15インチ")
    _16inch = ("size_id[70]", "16インチ")
    _17inch = ("size_id[71]", "17インチ")
    _18inch = ("size_id[72]", "18インチ")
    _19inch = ("size_id[73]", "19インチ")
    _20inch = ("size_id[74]", "20インチ")
    _21inch = ("size_id[75]", "21インチ")
    _22inch = ("size_id[159]", "22インチ")
    _23inch = ("size_id[160]", "23インチ")
    _24inch = ("size_id[161]", "24インチ")

    @staticmethod
    def id():
        return "11"

    @staticmethod
    def name():
        return "タイヤのサイズ"


class _Skiing(SimpleEnum):
    _140cm = ("size_id[126]", "140cm～")
    _150cm = ("size_id[127]", "150cm～")
    _160cm = ("size_id[128]", "160cm～")
    _170cm = ("size_id[129]", "170cm～")
    skiing_board = ("size_id[130]", "スキーボード")
    kids = ("size_id[131]", "子ども用")
    other = ("size_id[132]", "その他")

    @staticmethod
    def id():
        return "18"

    @staticmethod
    def name():
        return "スキーのサイズ"


class _Snowboard(SimpleEnum):
    _135cm_140cm = ("size_id[100]", "135cm-140cm未満")
    _140cm_145cm = ("size_id[101]", "140cm-145cm未満")
    _145cm_150cm = ("size_id[102]", "145cm-150cm未満")
    _150cm_155cm = ("size_id[103]", "150cm-155cm未満")
    _155cm_160cm = ("size_id[104]", "155cm-160cm未満")
    _160cm_165cm = ("size_id[105]", "160cm-165cm未満")
    _165cm_170cm = ("size_id[106]", "165cm-170cm未満")

    @staticmethod
    def id():
        return "15"

    @staticmethod
    def name():
        return "スノーボードのサイズ"


class Size:
    Cloth = _Cloth
    MensShoes = _MensShoes
    LadysShoes = _LadysShoes
    Skirt = _Skirt
    KidsCloth = _KidsCloth
    BabyKidsShoes = _BabyKidsShoes
    BabyCloth = _BabyCloth
    TV = _TV
    CameraLens = _CameraLens
    Motorcycle = _Motorcycle
    Helmet = _Helmet
    Tire = _Tire
    Skiing = _Skiing
    Snowboard = _Snowboard
