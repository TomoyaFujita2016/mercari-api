import os
import pickle


def load_pkl(path: str):
    with open(path, "rb") as f:
        value = pickle.load(f)
    return value


pkl_dir = os.path.dirname(os.path.abspath(__file__)) + "/pkl/"

brand = load_pkl(pkl_dir + "brands.pkl")
category = load_pkl(pkl_dir + "categories.pkl")
item_condition = load_pkl(pkl_dir + "item_conditions.pkl")
sale_status = load_pkl(pkl_dir + "sale_status.pkl")
shipping_method = load_pkl(pkl_dir + "shipping_method.pkl")
shipping_payer = load_pkl(pkl_dir + "shipping_payers.pkl")
color = load_pkl(pkl_dir + "colors.pkl")
