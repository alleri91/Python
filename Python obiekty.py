# Gra

class GameCharacter:

    speed = 5
    
    def __init__ (self, name, width, height, x_pos, y_pos, cng_int_beh):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.cng_int_beh = cng_int_beh

        ## time for npc to move

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

    def reaction (self, time_of_react, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount + time_of_react * self.cng_int_beh
        self.y_pos += by_y_amount + time_of_react * self.cng_int_beh

character_0 = GameCharacter('char_0', 50, 100, 100, 100, 100,)

print(character_0.width)

character_0.width = 250

print(character_0.width)
character_0.move(50, 100)

print(character_0.x_pos)
print(character_0.y_pos)
print(character_0)


class PlayerCharacter(GameCharacter):

    speed = 10
    
    def __init__ (self, name, x_pos, y_pos):
       super().__init__ (name, 100, 100, x_pos, y_pos, 0)

    def move(self, by_y_amount):
        super().move(0, by_y_amount)

player_character = PlayerCharacter('P_1', 500, 500)

   
print(player_character.x_pos)
print(player_character.x_pos)
player_character.move(100)
print(player_character.y_pos)

class NonPlayerCharacter(GameCharacter):

    speed = 5

    def __init__(self, name, x_pos, y_pos, cng_int_beh):
        super().__init__(name, 150, 150, x_pos, y_pos, cng_int_beh)

    
    def reaction (self, time_of_react,):
        super().reaction(time_of_react, 100, 100)

npc_character = NonPlayerCharacter('npc_1', 100, 100, 25)

print(npc_character.cng_int_beh)
npc_character.move(18, 20)
npc_character.reaction(17)

print(npc_character.x_pos)
    
        
