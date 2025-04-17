def top_users(users, n):
    return [user for user, score in (sorted(users.items(), key = lambda user: (user[1], user[0]), reverse = True)[:n])]


users = {
    "alice": 150,
    "bob": 200,
    "charlie": 200,
    "david": 180,
    "eve": 120
}

print(top_users(users, 3))