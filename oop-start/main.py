class User:
    def __init__(self,user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
    
    def add_follower(self):
        self.followers = self.followers+1


user_1 = User("001","Tom")

# user_1.id = "001"
# user_1.username = "Tom"
print(user_1.username)

print(user_1.followers, "Before add follower class call")

user_1.add_follower()

print(user_1.followers,"After adding follower")


# user_2 = User()
# user_2.id = "002"
# user_2.username = "Nathon"
# print(user_2.username)