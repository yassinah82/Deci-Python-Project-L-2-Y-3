import time
import random


def print_pause(message):
    """Function to print message with a delay."""
    print(message)
    time.sleep(1.5)


class Character:
    """Character class to define player properties and actions."""
    def __init__(self, game_name, name, story, mission, special_power, guardian_fight, win_fight, final): ##initializing Objects
        self.game_name = game_name
        self.name = name
        self.story = story
        self.guardian_fight = guardian_fight
        self.mission = mission
        self.special_power = special_power
        self.health = 100
        self.score = 0
        self.special_power_unlocked = False
        self.win_fight = win_fight
        self.final = final

    def print_story(self):
        """Print the character's story."""
        print_pause("\n📖 The Story Begins With ...")
        print_pause(self.name)
        for line in self.story.split("\n"):
            print_pause(line)

    def print_mission(self):
        """Print the character's mission."""
        print_pause("\n🎯 Your Mission Now is:\n")
        print_pause(self.mission)


class Game:
    """Game class to handle the game mechanics."""
    def __init__(self, player):
        """Initialize the game with the given player."""
        self.player = player
        self.boss_health = 100

    def intro(self):
        """Introduction to the game."""
        print_pause("Welcome To...")
        print_pause(self.player.game_name)
        while True:
            usr_input = input('🎮 Want to Start the Game [Y/N]: ').upper()
            if usr_input == "N":
                print("👋 Okay, maybe next time! Zayn will be waiting...")
                return False
            elif usr_input == "Y":
                print(f"\n🌀 Welcome To {self.player.game_name}: Adventures Game 🧠💻")
                self.player.print_story()
                self.player.print_mission()
                return True
            else:
                print("Invalid input. Try again.")
    def get_super_power(self):
        """Let the player choose to take or leave a super power gem."""
        print_pause("While You Were wandering in The jungle you Found A Yellow Gem ")
        gem_input = input("Press 1 To Take It Press 2 To Leave It : ")

        if gem_input == "1":
            print_pause("WoW! You Have Unlocked Your First Super Power:")
            print(f"You {self.player.special_power}")
            self.player.special_power_unlocked = True
        elif gem_input == "2":
            print("Ohh! You Missed The Super Power Gem.")
        else:
            print('Please Choose Between "1" OR "2".')
            self.get_super_power()

    def the_guardian_fight(self):
        """Handle the main game fight against the Guardian."""
        for line in self.player.guardian_fight.split("\n"):
            print_pause(line)

        choice = input('Please Choose Between "1", "2" OR "3": ')

        if choice == "1":
            if self.player.special_power_unlocked:
                stop_input = input("You Opened His Source Code. Enter The Keyword to Stop the Loop: ").lower()

                if stop_input == "stop":
                    self.player.score += 100
                    print_pause(f"+100 Score Total Score: {self.player.score}")
                    self.boss_health = 0
                    self.end_game()
            else:
                print("You Tried to use power you don't have")
        elif choice == "2":
            self.option2()
        elif choice == "3":
            self.option3()
        else:
            print("Please Choose Between 1, 2 OR 3")
            self.the_guardian_fight()

    def option2(self):
        """Second option of the fight."""
        print("You notice a syntax error in its defense system.")
        if input("Press 1 to Exploit it: ") == "1":
            player_attack = random.randint(30, 50)
            self.player.score += player_attack
            self.boss_health -= player_attack
            print_pause(f"You Managed to Damage the Boss by {player_attack}%")
            print(f"+{player_attack} Score, Total Score: {self.player.score} ")
            enemy_attack = random.randint(5, 30)
            self.player.score -= enemy_attack
            self.player.health -= enemy_attack
            print_pause("But He Got Up and made a move on you")
            print_pause(f"Recursive Roar! You lost {enemy_attack} HP. Current HP: {self.player.health}")
            print_pause(f"-{enemy_attack} Score, Total Score: {self.player.score}")
            self.final()

    def option3(self):
        """Third option of the fight."""
        if random.randint(1, 2) == 1:
            print("The Guardian teleports behind you—‘Nothing personal, kid.’ You get hit and lose all HP.")
            self.player.health = 0
        else:
            print("You Have Escaped From Him. You're Very Lucky!")
            self.end_game()

    def final(self):
        """Handle the final decision and ending of the game."""
        for line in self.player.final.split("\n"):
            print_pause(line)

        choice = input("Enter your final choice (1, 2, or 3): ")

        if choice == "1":
            self.player.score += 50
            print_pause("You Rewrote His Core Code...")
            print_pause("Now The Guardian Is Free From Corruption 🌟")
            print(f"+50 Score, Total Score is: {self.player.score}")

        elif choice == "2":
            self.player.score -= 10
            print_pause("You Trapped The Guardian In An Infinite Loop 🔁")
            print_pause("Now He is in infinite pain.")
            print(f"-10 Score, Total Score is: {self.player.score}")

        elif choice == "3":
            self.player.score += 100
            print_pause("You Patched His Logic With Empathy 🧠❤️")
            print_pause("Now The Guardian Is Your Ally.")
            print(f"+100 Score, Total Score is: {self.player.score}")

        else:
            print("Invalid input. Try again.")
            return self.final()
        print("Now You Can Find The Backdoor to the Real World\n")
        self.end_game()

    def total_score(self):
        """Calculate and display the total score."""
        final_score = self.player.score + self.player.health
        print_pause(f"Score: {self.player.score} + Total Player Health: {self.player.health} = {final_score} ")
        print(f"Final Score: {final_score}")

    def end_game(self):
        """Handle the game over process."""
        for line in self.player.win_fight.split("\n"):
            print_pause(line)
        self.total_score()


if __name__ == "__main__":

# Main game loop
    while True:

        zayn = Character(
            game_name="Zayn the Code Trapped",
            name="Zayn",
            story="""Zayn was pulling an all-nighter working on his first ever game.\n
                    One moment he was typing print("Hello World"), the next—BOOM🔥—the screen flashes🔦,\n
                    the lights flicker, and he’s sucked inside his own code.\n
                    Now he’s trapped in a world made of bugs, functions,\n
                    and corrupted memory. Everything is written in Python...\n
                    and it’s all trying to stop him from escaping.""",
            mission="""Escape the world of code, find the backdoor in the system,\n
                    and return to reality before he becomes part of the game forever.""",
            special_power='Can "Hack" parts of the world (e.g. breaking some codes by editing them)',
            guardian_fight="""Your Have Found a Monster
                            He is the Guardian of the Infinite Loop
                            Its voice echoed in binary:
                            YOU DO NOT BELONG HERE, ZAYN.
                            YOU SEEK THE BACKDOOR. IT IS NOT FOR BEGINNERS.
                            PREPARE TO BE TERMINATED.\n
                            What will you do?
                            1. ⚔️ Attack with your Super Power (if available)
                            2. 🧠 Use logic to solve its code and disable it
                            3. 🏃‍♂️ Run away (risk: 50% chance of death)""",
            final="""The Guardian is weak...
                    its code is unraveling.\n
                    What would you do?
                    1. Rewrite its core and free it from corruption
                    2. Trap it in an infinite loop for eternity
                    3. Patch its logic to make it friendly""",
            win_fight="""You defeated the Guardian!
                        You Found A Glowing and Shiny Door
                        As You Walk Through It...
                        You Wake Up in Your Room
                        It Was All a Dream...
                        Or Was it?..
                        \nGAME ENDS 🔚""",
        )

        game = Game(zayn)
        if game.intro() is True:
            game.get_super_power()
            game.the_guardian_fight()

        replay = input("\n🎮 Do you want to play again? [Y/N]: ").upper()
        if replay != "Y":
            print("👋 Thanks for playing! See you in another dimension 🌀")
            break