def top_users_by_average(transactions, n):
    sorted_trans = {}
    for dic in transactions:
        if dic["user"] in sorted_trans:
            sorted_trans[dic["user"]].append(dic["amount"])
        else:
            sorted_trans[dic["user"]] = [dic["amount"]]

    dic_average = {}
    for key, values in sorted_trans.items():
        sum = 0
        for value in values:
            sum += value
        average = sum/len(values)
        dic_average[key] = average
    
    return [user for user, value in sorted(dic_average.items(), key = lambda user: user[1], reverse= True)[:n]]



transactions = [
    {"user": "alice", "amount": 250},
    {"user": "bob", "amount": 100},
    {"user": "alice", "amount": 750},
    {"user": "charlie", "amount": 300},
    {"user": "bob", "amount": 200},
    {"user": "diana", "amount": 500},
    {"user": "charlie", "amount": 900},
    {"user": "alice", "amount": 1000}
]


print(top_users_by_average(transactions, 2))