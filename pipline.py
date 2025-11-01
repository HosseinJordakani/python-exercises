def in_prd(products):
    for product , info in products.items():
        if info["quantity"] > 0:
            yield product , info
def expensive(products):
    for product , info in products:
        if info["price"] > 100:
            yield product , info
def total_value(products):
    for product, info in products:
        total_value = info["price"] * info["quantity"]
        yield total_value
products = {
    "coffee": {"price": 120, "quantity": 50},
    "tea": {"price": 80, "quantity": 30},
    "milk": {"price": 60, "quantity": 0},
    "cookie": {"price": 200, "quantity": 10},
    "juice": {"price": 150, "quantity": 25}
}

pip_t_v = total_value(expensive(in_prd(products)))
values = list(pip_t_v)
avg_t_v = round(sum(values) / len(values),3)
print(avg_t_v)
