import sys
import pygame
import os
import time
import keyboard
from termcolor import colored

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
        
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

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
    
    def game_over(self, reason):
        println(f"\n--- GAME OVER ---", "red", self.settings["text_speed"]) 
        println(reason, "red", self.settings["text_speed"]) 
        input("Press Enter to return to the main menu...")
        self.menu()
    
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
        println("Welcome to CAOA core Press Space to skip", "blue", self.settings["text_speed"])
        println("\n--- Chapter 1 ---", "magenta", self.settings["text_speed"])
        println("your Name is Adam", "white", self.settings["text_speed"])
        println("your 16th Birthday is tonight", "white", self.settings["text_speed"])
        println("you went to school", "white", self.settings["text_speed"])
        println("you saw your friend Annabel and Alaska", "white", self.settings["text_speed"])
        choice = interactive_menu(["Go to your class", "Hang out with them"], "What do you do?", "yellow")
        if choice == 1:
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
        println("grandmaaaaaaaaaaaaaa!!! grandmaaaaaa what is hapenning", "red", self.settings["text_speed"])
        
        println("\n--- Chapter 2 ---", "magenta", self.settings["text_speed"])
        println("grandmaaaaaa !!  what is Hapenning, you said", "white", self.settings["text_speed"])
        println("You saw a box Emits Light. a Paper flies up from the box!", "white", self.settings["text_speed"])
        choice3 = interactive_menu(["Read it", "Run"], "What do you do?", "blue")
        if choice3 == 1:
            println("All the Doors have colsed and there were fire emited from the box ", "white", self.settings["text_speed"])
            println(" a Deep voice Says, READ", "red", self.settings["text_speed"])
        println(" you saw words written by blood in that paper; says, You are Adam Spellman, the ninth grandchild of the witch Sabrina Spellman, and it's your turn.", "white", self.settings["text_speed"])
        println("A knife from the box struck your hand, and blood began to flow, turning blue, and splattered onto the paper. Then another paper appeared that read: 'You are now ready to use your powers!' ", "red", self.settings["text_speed"])
        println("in this moment you a.........................", "white", self.settings["text_speed"])
        println("You wake up! and find tht it was a Nightmare", "white", self.settings["text_speed"])
        println("your are feeling powerful and very Active", "white", self.settings["text_speed"])
        println("Your grandma isn't home!", "white", self.settings["text_speed"])
        
        choice2 = interactive_menu(["Go to your School", "Stay at home"], "What do you do?", "blue")
        if choice2 == 0:
            println("you went to school to find Max !", "white", self.settings["text_speed"])
            println("you shook hands with him and tell him. Hey buddddd!", "white", self.settings["text_speed"])
            println("but wait! while you were shaking hands with max your hand were hearting you as hell", "white", self.settings["text_speed"])
            println("you looked in your hand to find a cut on it. woooowhhhhh wtf is this, max said", "white", self.settings["text_speed"])
            println("you relized it wasn't a nightmare IT WAS ALL REAL ! sh*t!", "white", self.settings["text_speed"])
            choice4 = interactive_menu(["Tell Max what happend" , "Lie on him and tell him anything else"], "What do you do?","blue")
            if choice4 == 0:
                println(".....................................", "white", self.settings["text_speed"])
                println("hey hey tell me what happend bro!!! , max said", "white", self.settings["text_speed"])
                println("you started telling max about yesterday's Night", "white", self.settings["text_speed"])
                println("is this an Archie comics novel ? lol haha", "white", self.settings["text_speed"])
                println("I am talking for real Max. Listean to me! ALL I HAVE TOLD YOU HAPPEND ! , you said", "white", self.settings["text_speed"])
                println("bro chill you are being so weired, max said", "white", self.settings["text_speed"])
                println("hey hey YOU ARE DONE ! , you said", "white", self.settings["text_speed"])
                println("max said , you have changed. I can't take it anymore", "white", self.settings["text_speed"])
                println("it's fine we are not friends anymore ! I HATE YOU ! , you said", "white", self.settings["text_speed"])
                println("you ran straight to your home crying.", "white", self.settings["text_speed"])
                println("you didn't find your grandma home! . where IS SHEEEEEEE !  ,you said", "white", self.settings["text_speed"])
                choice5 = interactive_menu(["go search for her" , "Stay at home and wait for her"],"What do you do?","blue")
                if choice5 == 0:
                    println("you went to search for her beside your house", "white", self.settings["text_speed"])
                    println("you keeped moving around the house until you saw ............", "white", self.settings["text_speed"])
                    println("you saw a tall man his face covered by a white thing and you started running", "white", self.settings["text_speed"])
                    println("the man killed you ran after you and you are dead", "white", self.settings["text_speed"])
                    self.game_over("The tall man caught you")
                else:
                    println("you waited for her and stayed in your home", "white", self.settings["text_speed"])
                    println("Max is crying at his house, I lost my best Friends for a silly conflict this isn't right, max said", "white", self.settings["text_speed"])
                    println("I have to go to Adam's and try to be sorry, I was very rude at him. max said", "white", self.settings["text_speed"])
                    println("Max knocked the door, you opened it and told him 'What ???' ", "white", self.settings["text_speed"])
                    println("max said ,I cam to say sorry about what happened but you were saying a sci-fi story and yo. shhhhhhhhhhhhhh , you said", "white", self.settings["text_speed"])
                    println("just LEAVE ! you said. I cam all the way to your house to tell me leave huh ?", "white", self.settings["text_speed"])
                    println("before you start screaming again at max you heard a big crash sound came from the kitchen", "white", self.settings["text_speed"])
                    println("you went to the kitchen", "white", self.settings["text_speed"])
                    println("you saw a tall man his face covered by a white thing and you started running", "white", self.settings["text_speed"])
                    println("the man killed you ran after you and you are dead", "white", self.settings["text_speed"])
                    self.game_over("The tall man was waiting")
            else:
                println("you lied at him", "white", self.settings["text_speed"])
                println("He knew that you lied at him", "white", self.settings["text_speed"])
                println("you lost Max's trust!", "red", self.settings["text_speed"])
                println("Max walked away disappointed and said to you , you are very bad lier ", "white", self.settings["text_speed"])
                println("You returned home alone...", "white", self.settings["text_speed"])  
                println("Your grandma still wasn't there...", "white", self.settings["text_speed"]) 
                println("You fell asleep waiting","white", self.settings["text_speed"]) 
                println("To be continued in Chapter 3...", "magenta", self.settings["text_speed"]) 
                input("Press Enter to return to the main menu...")
                return
        else:
            println("you stayed home watching TV waiting for your grandma. but, she didn't come home.", "white", self.settings["text_speed"])
            println("you called Max ! woooooow", "white", self.settings["text_speed"])
            println("he came with the a lot of snacks", "white", self.settings["text_speed"])
            println("you had fun togther until you heard a noise from the Kitchen", "red", self.settings["text_speed"])
            println("Max said what the hell is this? don't mind , you said", "white", self.settings["text_speed"])
            
            choice7 = interactive_menu(["Ignore it", "Check it alone", "Go with Max"], "What do you do?", "yellow")
            if choice7 == 1:
                println("You go alone and the tall man kills you!", "red", self.settings["text_speed"])
                self.game_over("Never go alone dumb")
                return
            if choice7 == 2:
                println("The tall man killed both of you!", "red", self.settings["text_speed"])
                self.game_over("Max couldn't save you (sorry max)") 
                return            
            
            println("you held the cold can of cola but your hand hurted you as hell", "white", self.settings["text_speed"])
            println("you looked ate your hand to find a cut", "white", self.settings["text_speed"])
            println("you remebred what happend last night and relized it wasn't a dream. woooowhhhhh wtf is this, max said", "white", self.settings["text_speed"])
            println("you started telling max about yesterday's Night", "white", self.settings["text_speed"])
            
            choice8 = interactive_menu(["Tell everything", "Lie to him", "Show the cut"], "How do you respond?", "yellow") 
            if choice8 == 1:
                println("you started saying random dumb things and Max doesn't believe you and leaves. You die alone that night. (I couldn't find another end for this lol)", "red", self.settings["text_speed"]) 
                self.game_over("Honesty is the best policy... (الكدب ملهوش رجلين)") 
                return            
            
            println("is this an Archie comics novel ? lol haha", "white", self.settings["text_speed"])
            println("I am talking for real Max. Listean to me! ALL I HAVE TOLD YOU HAPPEND ! , you said", "white", self.settings["text_speed"])
            println("bro chill you are being so weired, max said", "white", self.settings["text_speed"])
            println("you started sreaming on max , hey YOU ARE DONE ..... ", "white", self.settings["text_speed"])
            
            choice9 = interactive_menu(["say sorry", "Keep screaming", "Walk away"], "What do you do?", "yellow") 
            if choice9 == 1:
                println("While screaming, the tall man appears and kills you!", "red", self.settings["text_speed"])
                self.game_over("Your anger made you killed you!") 
                return
            if choice9 == 2: 
                println("You leave Max alone and he gets killed. Then the tall man finds you.", "red", self.settings["text_speed"]) 
                self.game_over("Never abandon your friends b**")
                return 
            
            println("while you were screaming with max you heard a big crash sound from the kitchen", "white", self.settings["text_speed"])
            
            choice10 = interactive_menu(["Stand your ground", "Run", "Hide"], "What's your instinct?", "yellow")
            if choice10 == 1:
                println("The door is locked! The tall man catches you easily.", "red", self.settings["text_speed"]) 
                self.game_over("There's no escape...")
                return
            if choice10 == 2: 
                println("You hide, but the demon senses your magic and finds you.", "red", self.settings["text_speed"])
                self.game_over("You cannot hide from evil")
                return
        
        println("oh what happend , max said", "white", self.settings["text_speed"])
        println("I have no idea , you said. max said, We have to go to see", "white", self.settings["text_speed"])
        println("you went to see the kitchen to find the glasses crashed on the floor and then then ......... then", "red", self.settings["text_speed"])
        println("a very tall person with no face appeared. ", "red", self.settings["text_speed"])
        println("max said, we have to run right ?", "white", self.settings["text_speed"])
        println("I think ruuuutuuunununnununununuununnuunnnnn, you said.", "white", self.settings["text_speed"])
        println("all the doors and the windows of the kitchen closed Immediatlly. sh*t you said.", "white", self.settings["text_speed"])
        
        choice11 = interactive_menu(["Use your magic", "Sacrifice for Max", "Give up"], "What do you do?", "yellow")
        if choice11 == 2:
            println("You give up hope and the tall man kills you both.", "red", self.settings["text_speed"])
            self.game_over("Never give up...")
            return
        
        println("we're dead we're dead, max said. the tall man in white started speaking, I came to kill you and to drink your blood you son of sabrina the b*tch. I will start with your little Asian Friend. max screamed while the tall raised him up and started to kill him", "white", self.settings["text_speed"])
        println("you heared sound saying, 'Hunc daemonem punio!' three times", "white", self.settings["text_speed"])
        println("you didn't know what to do. you started saying these words three times", "white", self.settings["text_speed"])
        println("after you finished a white light came from your cut in your hand. you pointed your hand at the tall one", "white", self.settings["text_speed"])
        println("the tall one screamed ooooooohohohohohohhhhhhh and then he dissapeared.", "white", self.settings["text_speed"])
        println("WHAT THE FREAK ??????????????????? , max said", "white", self.settings["text_speed"])
        println("Adam! I think I started to believe the story you told me about! max said", "white", self.settings["text_speed"])
        println("see!, you said. max said, What is this and what we have to do and what the hell you have done with your hand I don't understand ANYTHING !", "white", self.settings["text_speed"])
        println("I don't know but I know how can we understand ! you said.", "white", self.settings["text_speed"])
        println("you went to your room with max to see the box that emites light", "white", self.settings["text_speed"])
        println("there were a book inside you opended the first page to read :", "white", self.settings["text_speed"])
        println("if you are reading this now this means you are 16 years old \n I am sabrina spellman your 9th great grandmother I was half mortal half witch. like you ! \n magic is running into your blood. you should use it to save the world again! I know you will do it cause you did it before ! \n (you will understand well what I mean but not now) you should follor my instructions you will find in this book and you will make it .", "red", self.settings["text_speed"])
        println("you opened the second page to find these words :", "white", self.settings["text_speed"])
        println("I was a normal witch until a crisis happened. The world was in danger. The only way to save my coven and world is to give up my magic and the magic of the next my 8th generations as a offering for the ..... for the ..........", "white", self.settings["text_speed"])
        println("However, You are the 9th , the one who will have the magic back. Demons won't let you alive. you need to be brave and punish them. you will find a book in the box to learn how to use your magic. you have read too much today!", "white", self.settings["text_speed"])
        println("the book closed and you can't open it !", "white", self.settings["text_speed"])
        println("you and max Slept in the room until you woke up at 7 am", "white", self.settings["text_speed"])
        println("Adam! Adaaaaaaam! you will get late to the school. knock knock knock", "white", self.settings["text_speed"])
        println("max opened the door to find Annabel and Alaska saying , why are you at Adam's home?", "white", self.settings["text_speed"])
        println("oh! I was watching movies with Adam and then .......", "white", self.settings["text_speed"])
        println("And then we fall sleep , Adam said", "white", self.settings["text_speed"])
        println("oh Hey Adam! good morning, Annabel & Alaska said", "white", self.settings["text_speed"])
        println("hey! I am not in the mood of school. me too , Annabel Said", "white", self.settings["text_speed"])
        println("then let's stay at home and play some games yaaaayyyyyy, Max said", "white", self.settings["text_speed"])
        println("knock knock knock knock", "white", self.settings["text_speed"])
        println("yes? Who is there?", "white", self.settings["text_speed"])
        println("I am your grandma you dumb *** ", "white", self.settings["text_speed"])
        println("oh grandma where were you? I was worried!", "white", self.settings["text_speed"])
        println("I was at my friend's House, However, why are your friends is here. you have to clean up these mess you made. grandma said", "white", self.settings["text_speed"])
        println("uh! Nevermined I will take care of this!", "white", self.settings["text_speed"])
        println("you heard Annabel screaming from your room, ahhhhh help help oooooh", "white", self.settings["text_speed"])
        println("you ran to your room to find her fly and there is a weird woman trying to kill her", "white", self.settings["text_speed"])
        println("Annabel is dead", "red", self.settings["text_speed"])
        println("Max is Screaming, Alaska is Screaming, Grandma fall into a coma.", "red", self.settings["text_speed"])
        println("everything is wrong.................", "red", self.settings["text_speed"])
        println("the tall man returned again and killed YOU", "red", self.settings["text_speed"])
        println("the tall man killed Max and Alaska", "red", self.settings["text_speed"])
        println("\n--- To Be continued ---", "magenta", self.settings["text_speed"])

        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    game = Game()
    game.menu()
