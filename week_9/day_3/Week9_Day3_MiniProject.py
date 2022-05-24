#MINIPROJECT
class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other_char):
        other_char.life -= self.attack  # not sure to have understood the instruction


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Hello! I am a Druid. My name is {self.name}.")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def flight(self, other_char):
        other_char.life = other_char.life - (0.75 * self.life + 0.75 * self.attack)


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Hello! I am a Warrior. My name is {self.name}.")

    def brawl(self, other_char):
        other_char.life -= 2 * self.attack
        self.life += 0.5 * self.attack

    def train(self):
        self.attack += 2
        self.life += 2

    @staticmethod
    def roar(other_char):
        other_char.attack -= 3

class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Hello! I am a Mage. My name is {self.name}.")

    @staticmethod
    def curse(other_char):
        other_char.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other_char):
        other_char.life -= self.attack/self.life


mage1 = Mage('Mage1')
mage2 = Mage('Mage2')
druid1 = Druid('Druid1')
warrior1 = Warrior('Warrior1')
warrior1.brawl(mage2)
print(warrior1.life)
print(warrior1.attack)
print(mage2.life)
print(mage2.attack)

