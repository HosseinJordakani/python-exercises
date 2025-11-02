# inventory_value.py
def total_value(products: dict) -> float:
    """Products is dict of product_name -> {'price': float, 'quantity': int}"""
    total = 0.0
    for info in products.values():
        total += info["price"] * info["quantity"]
    return total

if __name__ == "__main__":
    sample = {
        "coffee": {"price": 3.5, "quantity": 10},
        "tea": {"price": 2.0, "quantity": 5},
    }
    print("Total inventory value:", total_value(sample))
