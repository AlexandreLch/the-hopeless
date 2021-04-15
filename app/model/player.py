class Player:
    health = 100
    fighting = 0
    mecanics = 0
    cook = 0
    navigation = 0

    def __init__(self, user_name):
        self.user_name = user_name

    def move(self):
        print("je bouge")