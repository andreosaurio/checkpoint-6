class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("Andreosaurio", "my_pwd")

print(user1.username)
print(user1.password)
