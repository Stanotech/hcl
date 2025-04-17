def top_sells(transactions, n_top):
    total_earn = {}
    for trans_dic in transactions:
        total_earn[trans_dic["product"]] = total_earn.get(trans_dic["product"], 0) + trans_dic["price_per_unit"]*trans_dic["quantity"]

    final = []
    for product in (sorted(total_earn.items(), key = lambda item:item[1], reverse= True)[:n_top]):
        final.append({"product" : product[0], "total_spent" : product[1]})

    return final

transactions = [
    {"user_id": 1, "product": "Laptop", "quantity": 1, "price_per_unit": 5000},
    {"user_id": 2, "product": "Laptop", "quantity": 2, "price_per_unit": 5000},
    {"user_id": 3, "product": "Mouse", "quantity": 3, "price_per_unit": 100},
    {"user_id": 1, "product": "Keyboard", "quantity": 4, "price_per_unit": 200},
    {"user_id": 2, "product": "Mouse", "quantity": 2, "price_per_unit": 100},
    {"user_id": 3, "product": "Keyboard", "quantity": 5, "price_per_unit": 200},
]

print(top_sells(transactions, 2))