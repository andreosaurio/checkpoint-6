class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("Andreosaurio", "my_pwd")

print("Username:", user1.username)
print("Password:", user1.password)