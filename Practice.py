class User():
    def __init__(self,userid,username,password):
        self.userid = userid
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers += 1
        self.following +=1

user1= User('001',"Vatsal",456123)
user2 = User('002',None,456123)

user1.follow(user2)

print(f"""
      user id is: {user1.userid} 
      user name is: {user1.username} 
      password is: {user1.password}
      followers : {user1.followers}
      following : {user1.following}
""")

print(f"""
      user id is: {user2.userid} 
      user name is: {user2.username} 
      password is: {user2.password}
      followers : {user2.followers}
      following : {user2.following}
""")

# print(f"""
#       user id is: {user2.userid} 
#       user name is: {user2.username} 
#       password is: {user2.pswd}
# """)

# class Car:
#     def __init__(self,seats,colour):
#         self.seats = seats
#         self.colour = colour

# my_car = Car(5,"red")
# print(my_car.seats,my_car.colour,)