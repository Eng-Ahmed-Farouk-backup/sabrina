from interactive_console import *
import sys

class Game:
    def __init__(self):
        self.settings = {
            "text_speed": "Normal"
        }
    
    def menu(self):
        while True:
            options = ["Start Game", "Settings", "Exit"]
            option = interactive_menu(options, "Welcome to Chilling Adventures of Adam!", "yellow")
            if option == 0:
                self.start_game()
            elif option == 1:
                self.settings_menu()
            elif option == 2:
                println("Thanks for playing!", "yellow")
                sys.exit()
    
    def settings_menu(self):
        options = ["Text Speed", "Back"]
        while True:
            option = interactive_menu(options, "Settings", "yellow")
            if option == 0:
                self.text_speed_menu()
            elif option == 1:
                return
    
