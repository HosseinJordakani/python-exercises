# filter_expensive.py
def expensive_products(products, threshold=100):
    for name, info in products.items():
        if info.get("price", 0) > threshold:
            yield name, info

if __name__ == "__main__":
    products = {"A": {"price": 50}, "B": {"price": 150}}
    for p in expensive_products(products):
        print(p)
