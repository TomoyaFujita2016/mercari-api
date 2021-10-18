import os
import pickle


def load_pkl(path: str):
    with open(path, "rb") as f:
        value = pickle.load(f)
    return value


pkl_dir = os.path.dirname(os.path.abspath(__file__)) + "/pkl/"

Brand = load_pkl(pkl_dir + "brands.pkl")
Category = load_pkl(pkl_dir + "categories.pkl")
ItemCondition = load_pkl(pkl_dir + "item_conditions.pkl")
SaleStatus = load_pkl(pkl_dir + "sale_status.pkl")
ShippingMethod = load_pkl(pkl_dir + "shipping_method.pkl")
ShippingPayer = load_pkl(pkl_dir + "shipping_payers.pkl")
Color = load_pkl(pkl_dir + "colors.pkl")

if __name__ == "__main__":
    from pprint import pprint

    # Brand = load_pkl(pkl_dir + "brands.pkl")
    # pprint(Brand)

    #Category = load_pkl(pkl_dir + "categories.pkl")
    #pprint(Category)

    #ItemCondition = load_pkl(pkl_dir + "item_conditions.pkl")
    #pprint(ItemCondition)

    #SaleStatus = load_pkl(pkl_dir + "sale_status.pkl")
    #pprint(SaleStatus)

    #ShippingMethod = load_pkl(pkl_dir + "shipping_method.pkl")
    #pprint(ShippingMethod)
    # ShippingPayer = load_pkl(pkl_dir + "shipping_payers.pkl")
    #pprint(ShippingPayer)
    Color = load_pkl(pkl_dir + "colors.pkl")
    pprint(Color)

    # print("-----Brand------")
    # for key in list(Brand.keys())[:5]:
    #    print("{", f"'{key}': {Brand[key]}", "}")

    # print("-----Category------")
    # pprint(Category["メンズ"])

    # print("-----ItemCondition------")
    # pprint(ItemCondition)

    # print("-----SaleStatus------")
    # pprint(SaleStatus)

    # print("-----ShippingMethod------")
    # pprint(ShippingMethod)

    # print("-----ShippingPayer------")
    # pprint(ShippingPayer)

    # print("-----Color------")
    # pprint(Color)
