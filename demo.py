import os
import time
import keyboard
from termcolor import colored
import sys
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def interactive_menu(options, header = "", color = ""):
    current = 0
    while True:
        time.sleep(0.3)
        clear_console()
        print(colored(header, color))
        for i, option in enumerate(options):
            if i == current:
                print(colored(f"> {option}", "blue"))
            else:
                print(f"  {option}")
        key = keyboard.read_key()
        if key == "up":
            current = (current - 1) % len(options)
        elif key == "down":
            current = (current + 1) % len(options)
        elif key == "enter":
            return current

def println(msg, color = "white", speed = "Normal"):
    speeds = {
        "Slow":0.7,
        "Normal":1,
        "Fast":1.5
    }
    for m in msg.split("\n"):
        print(colored(m, color))
        start_time = time.time()
        while time.time() < start_time + max(len(m)/(10*speeds[speed]),2):
            if keyboard.is_pressed("space"):break
        time.sleep(0.05)
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
    
    def text_speed_menu(self):
        options = ["Slow", "Normal", "Fast", "Back"]
        option = interactive_menu(options, "Select Text Speed", "yellow")
        if option == 0:
            self.settings["text_speed"] = "Slow"
        elif option == 1:
            self.settings["text_speed"] = "Normal"
        elif option == 2:
            self.settings["text_speed"] = "Fast"
        elif option == 3:
            return
    
    def start_game(self):
        println("Welcome to Chilling Adventures of Adam Game - inspired from Chilling Adventures of Sabrina a Netflix show!", "cyan", self.settings["text_speed"])
        println("Welcome to CAOA core", "blue", self.settings["text_speed"])
        println("your Name is Adam", "white", self.settings["text_speed"])
        println("your 16th Birthday is tonight", "white", self.settings["text_speed"])
        println("you went to school", "white", self.settings["text_speed"])
        println("you saw your friend Annabel and Alaska", "white", self.settings["text_speed"])
        choice = interactive_menu(["Go to your class", "Hang out with them"], "What do you do?", "yellow")
        if choice == 1:  # Hang out
            println("you said : heeyyyyyy ! how are you? , I didn't see you since you started Organizing HCTG!", "white", self.settings["text_speed"])
            println("yeah there is a dumb one named Ahmed keeps submitting weird projects and I don't have time for this , Annabel said", "white", self.settings["text_speed"])
            println("Fund mangement for the YSWS is taking all of my time!, said Alaska", "white", self.settings["text_speed"])
            println("you are feeling something coming from your back", "white", self.settings["text_speed"])
            println("Steps sounds .....................", "white", self.settings["text_speed"])
            println("SURPRISEEEEEEEEEEEEE!!!! , someone give you a BD cake on your face", "white", self.settings["text_speed"])
            println("who ????? , you said", "white", self.settings["text_speed"])
            println("it's maxstellar !! your funny childhood friend! came back !", "white", self.settings["text_speed"])
            println("are you kidding me!!! are you here ?? ...... but How ? , you said", "white", self.settings["text_speed"])
            println("Yes I am here , I am back from Canada, my family decided to return to the US again, max said", "white", self.settings["text_speed"])
            println("your grandma told me how can I find you !, max said", "white", self.settings["text_speed"])
            println("you hugged each other!", "white", self.settings["text_speed"])
            println("you had a really good day with max , anna and alaska", "white", self.settings["text_speed"])
        else: 
            println("you went to class", "white", self.settings["text_speed"])
            println("it's too boring!", "white", self.settings["text_speed"])
            println("sir! can I go to bathroom !, you said", "white", self.settings["text_speed"])
            println("yes of course ! , teacher said", "white", self.settings["text_speed"])
            println("you are looking for your friends but you didn't find them !", "white", self.settings["text_speed"])
            println("you are feeling something coming from your back", "white", self.settings["text_speed"])
            println("Steps sounds .....................", "white", self.settings["text_speed"])
            println("surpriseeeeeeeeeeeeeeeeeee , someone give you a BD cake on your face ", "white", self.settings["text_speed"])
            println("who ????? , you said", "white", self.settings["text_speed"])
            println("it's maxstellar !! your funny childhood friend! came back !", "white", self.settings["text_speed"])
            println("are you kidding me!!! are you here ?? ...... but How ? , you said", "white", self.settings["text_speed"])
            println("Yes I am here , I am back from Canada, my family decided to return to the US again, max said", "white", self.settings["text_speed"])
            println("your grandma told me how can I find you !, max said", "white", self.settings["text_speed"])
            println("you hugged each other!", "white", self.settings["text_speed"])
            println("you saw Annable , Alaska", "white", self.settings["text_speed"])
            println("you and max went see them", "white", self.settings["text_speed"])
            println("you said : heeyyyyyy ! how are you? , I didn't see you since you started Organizing HCTG!", "white", self.settings["text_speed"])
            println("yeah there is a dumb one named Ahmed keeps submitting weird projects and I don't have time for this , Annabel said", "white", self.settings["text_speed"])
            println("Fund mangement for the YSWS is taking all of my time!, said Alaska", "white", self.settings["text_speed"])
            println("you had a really good day with anna , max and alaska", "white", self.settings["text_speed"])
        
        println("you finally went home after this big day", "white", self.settings["text_speed"])
        println("hey darling I missed youuuuuuuu ! give me a kiss,  mowa! mowa! , grandma said ", "white", self.settings["text_speed"])
        println("I missed you too, Where is the dinner I am soo HANGUREYYYYYY !!, you said", "white", self.settings["text_speed"])
        println("it's here but change your clothe first !!! ,grandma said", "white", self.settings["text_speed"])
        println("you went to bathroom , you flashbacked  ", "white", self.settings["text_speed"])
        println("my mam & dad died when I was in the age of 3 in a car accident", "white", self.settings["text_speed"])
        println("you have nobody except your grandma!", "white", self.settings["text_speed"])
        println("you had dinner and entered your room to find a shining box emit light", "white", self.settings["text_speed"])
        println("the door of the room closed , the window also closed you started screaming", "white", self.settings["text_speed"])
        println("grandmaaaaaaaaaaaaaa!!! grandmaaaaaa what is hapenning", "white", self.settings["text_speed"])
        println("\n--- To be continued ---", "magenta", self.settings["text_speed"])
        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    game = Game()
    game.menu()
