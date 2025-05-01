import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        self.__player1 = player1
        self.__player2 = player2

        pass

    def attack(self, attacker: Character, defender: Character) -> None:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack.
        Args:
            attacker (Character): The attacker.
            defender (Character): The defender. 
        """

        attack_value = random.randint(1, 6)
        defender.health -= attack_value
        print(f"{attacker.name} attacks {defender.name} for {attack_value} damage!")

        if defender.health <= 0:
            print(f"{defender.name} has been defeated!")

    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """
        print("Battle begins!")
        while self.__player1.health > 0 and self.__player2.health > 0:
            self.attack(self.__player1, self.__player2)  # Player 1 attacks Player 2
            if self.__player2.health <= 0:
                print(f"{self.__player1.name} wins the battle!")
                break

            self.attack(self.__player2, self.__player1)  # Player 2 attacks Player 1
            if self.__player1.health <= 0:
                print(f"{self.__player2.name} wins the battle!")
                break