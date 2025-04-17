def top_spenders_by_month(transactions: list, month: str, top_n: int) -> list:
    filtered = [dic for dic in transactions if dic["timestamp"][:7] == month]

    dic_sum = {}
    for trans in filtered:
        dic_sum[trans["user_id"]] = dic_sum.get(trans["user_id"], 0) + trans["amount"]
    print(dic_sum)

    sort =sorted(dic_sum.items(), key = lambda item: item[1], reverse= True)

    result = []
    for user in sort:
        result.append({"user_id" : user[0], "total_spent" : user[1]})

    return result[:top_n]


transactions = [
    {"user_id": 1, "amount": 150.0, "category": "food", "timestamp": "2024-12-01 10:15:00"},
    {"user_id": 2, "amount": 200.0, "category": "books", "timestamp": "2024-12-02 14:20:00"},
    {"user_id": 1, "amount": 350.0, "category": "electronics", "timestamp": "2024-12-05 18:45:00"},
    {"user_id": 3, "amount": 500.0, "category": "fashion", "timestamp": "2024-11-30 23:59:59"},
    {"user_id": 2, "amount": 800.0, "category": "food", "timestamp": "2024-12-10 08:10:00"},
    {"user_id": 3, "amount": 300.0, "category": "food", "timestamp": "2024-12-12 12:00:00"}
]

print(top_spenders_by_month(transactions, "2024-12", 2))