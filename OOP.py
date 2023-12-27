class StarCookie: # Pascal Case of naming for Classes
    milk = 0.5

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        print("The cookie is ready!")

star_cookie1 = StarCookie("Red",16)
StarCookie.milk = 0.2
#star_cookie1.weight = 15
#star_cookie1.color = "Red"

print(star_cookie1.weight)
print(star_cookie1.color)
print(star_cookie1.milk)
print(star_cookie1.__dict__)


star_cookie2 = StarCookie("Blue", 15)
print(star_cookie2.milk)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)
#star_cookie2.weight = 16
#star_cookie2.color = "Blue"

#print(star_cookie2.weight)
#-print(star_cookie2.color)

    #def sample_function(self):

class Youtube:
    def __init__(self, username, subscribers=0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


user1 = Youtube("DN")
print(user1.username)


user2 = Youtube("PK")
user1.subscribe(user2)
#user2.subscribers = 5
print(user2.username)
print(f"User1 subscribers: {user1.subscribers}")
print(f"User1 subscriptions: {user1.subscriptions}")
print(f"User2 subscribers: {user2.subscribers}")
print(f"User2 subscriptions: {user2.subscriptions}")