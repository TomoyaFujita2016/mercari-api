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
