class Player:
    health = 100
    hunger = 100
    damage = 10
    speed = 2

    technician_skill = 0
    admin_skill = 0
    ship_battle_skill = 0
    navigator_skill = 0

    def __init__(self, user_name):
        self.user_name = user_name

    def move(self):
        print("je bouge")