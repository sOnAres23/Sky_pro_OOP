import json
from typing import List, Dict, Any

from src.product import Product
from src.category import Category


def read_from_json(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, encoding="utf-8") as f:
        info_data = json.load(f)
    return info_data


def create_objects(info_file):
    categories = []
    for category in info_file:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = categories
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    data = read_from_json("../data/products.json")
    print(create_objects(data)[0].name)
