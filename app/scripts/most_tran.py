def top_categories_by_total(transactions, n):
    sorted_dic = {}

    for trans in transactions:
        sorted_dic[trans["category"]] = sorted_dic.get(trans["category"], 0) + trans["amount"]
    
    print(sorted_dic)
    
    return [category for category, sum in sorted(sorted_dic.items(), key = lambda item:item[1], reverse= True)][:n]


transactions = [
    {"category": "electronics", "amount": 1200},
    {"category": "books", "amount": 200},
    {"category": "books", "amount": 300},
    {"category": "fashion", "amount": 400},
    {"category": "electronics", "amount": 800},
    {"category": "home", "amount": 1000},
    {"category": "fashion", "amount": 100},
    {"category": "home", "amount": 700}
]
print(top_categories_by_total(transactions, 3))