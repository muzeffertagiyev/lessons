class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.followers_name = ''
        self.following_name = ''

    def follow(self, user):
        user.followers += 1
        user.followers_name += self.username + ','
        self.following_name += user.username
        self.following += 1


user_1 = User('001', 'Nicat')
user_2 = User('002', 'Azer')
user_3 = User('003', 'Emin')

user_1.follow(user_2)
user_2.follow(user_1)
user_3.follow(user_1)
user_3.follow(user_2)
print(f"{user_1.username} follows {user_1.following_name}")
print(f"{user_1.username}'s followers: {user_1.followers_name}")
print(f"{user_2.username} follows {user_2.following_name}")
print(f"{user_2.username}'s followers: {user_2.followers_name}")



