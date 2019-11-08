# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

# class Soldier:
#     def __init__(self,name,weapon):
#         self.name = name
#         self.weapon = weapon


# class Guns:
#     def fire(self,bullets):
#         self.bullets = 100
#         print(self.name + "has" )
#         return self.bullets

# class Act_of_Shooting(Soldier,Guns):
#     print(" ")

# soldier_1 = Soldier("Ryan", "Ak47")
# print(soldier_1)
# print(soldier_1.fire)
# need to change

class Soldier:
    def __init__(self, name):
        self.name = name

class Gun:
    def __init__(self, make='AK47'):
        self.make = make

class Act_of_Shooting(Soldier, Gun):
    def __init__(self, *args):
        Soldier.__init__(self, *args)
        self.bullets = 5

    def fill_bullets(self, num):
        self.bullets += num

    def gun_fire(self):
        if self.bullets:
            print('tigi-tigitishh')
            self.bullets -= 1
        else:
            print('no bullets')

soldier = Act_of_Shooting ('Rayan')
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.fill_bullets(10)
soldier.gun_fire()