import pickle

from params import brand, category, color, item_condition, shipping_payer


def save_brands():
    brands = dict()
    for ini in brand.resp["data"]:
        for name in ini["brands"]:
            if brands.get(name["name"], None) is not None:
                print(f"not None: {name['name']}")
            brands[name["sub_name"]] = name["id"]
    with open("pkl/brands.pkl", "wb") as f:
        pickle.dump(brands, f)


def save_item_conditions():
    item_conditions = dict()
    for con in item_condition.resp["data"]:
        item_conditions[con["name"]] = con["id"]
    print(item_conditions)

    with open("pkl/item_conditions.pkl", "wb") as f:
        pickle.dump(item_conditions, f)


def save_shipping_payers():
    shipping_payers = dict()
    for con in shipping_payer.resp["data"]:
        shipping_payers[con["name"]] = con["id"]
    print(shipping_payers)

    with open("pkl/shipping_payers.pkl", "wb") as f:
        pickle.dump(shipping_payers, f)


def save_category():
    categories = dict()
    for root_cate in category.resp["data"]:
        categories[root_cate["name"]] = {"id": root_cate["id"], "child": {}}
        for child_cate in root_cate["child"]:
            categories[root_cate["name"]]["child"][child_cate["name"]] = {
                "id": child_cate["id"],
                "child": {},
            }
            child_cate_child = child_cate.get("child", [])
            for g_child_cate in child_cate_child:
                categories[root_cate["name"]]["child"][child_cate["name"]]["child"][
                    g_child_cate["name"]
                ] = {"id": g_child_cate["id"]}
    print(categories.keys())
    print(len(categories.keys()))
    print(categories["レディース"]["child"].keys())
    print(len(categories["レディース"]["child"].keys()))
    with open("pkl/categories.pkl", "wb") as f:
        pickle.dump(categories, f)


def save_sale_status():
    sale_status = {"販売中": "on_sale", "売り切れ": "sold_out"}
    with open("pkl/sale_status.pkl", "wb") as f:
        pickle.dump(sale_status, f)


def save_shipping_method():
    shipping_method = {
        "匿名配送": "anonymous",
        "郵便局/コンビニ受取": "japan_post",
        "オプションなし": "no_option",
    }
    with open("pkl/shipping_method.pkl", "wb") as f:
        pickle.dump(shipping_method, f)


def save_colors():
    colors = dict()
    for con in color.resp["data"]:
        colors[con["name"]] = con["id"]
    print(colors)

    with open("pkl/colors.pkl", "wb") as f:
        pickle.dump(colors, f)


# save_brands()
# save_category()
# save_item_conditions()
# save_shipping_payers()
# save_shipping_method()
# save_sale_status()
save_colors()
