import tkinter
from tkinter import messagebox
import json
import pygame
import random
data_file = "Score.json"   #file nam ewhere user data is stored
def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)  #reads JSON data and converts it into a python dictionary
    except FileNotFoundError:
        return {}
# Save data to file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file) #.dump is used to write something directly to the file
def main_window():
    def login(data):
        User_name = username_entry.get()  # gets user name typed in the username box
        password = password_entry.get()   # gets password typed in the password box        
        if User_name in data:  #checks if name already exists
            if data[User_name]['password'] == password:  #checks if password matches the stored password
                main_window.destroy()#the Tkinter window will get removed and pygame will begin
                print("Login successful!")
                main(User_name)#pygame will begin with the user name that is inputed
            else:
                print("Incorrect password.")
                return None
        else:
            print("New user. Please register.")
            data[User_name] = {"password": password, "High Score" : 0}  #creates new user entry in the file2\222222222222
            save_data(data) #saves the data of the new user
            print("Registration successful!")
            main_window.destroy()
            main(User_name)
            return User_name
    main_window = tkinter.Tk()  #creates an main window
    main_window.title = ("Login Window")  #sets title of the screen
    window_width = 240
    window_height = 100
    screen_width= main_window.winfo_screenwidth()
    screen_height= main_window.winfo_screenheight()
    x= (screen_width-window_width)//2 # calculate x position for centering the window
    y = (screen_height-window_height)//2 # calculate y position for centering the window
    main_window.geometry(f"{window_width}x{window_height}+{x}+{y}") #sets window size and position
    main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    username_label = tkinter.Label(main_window, text = "Username")
    username_label.grid(row = 0,column = 0,padx = 5,pady = 5)
    password_label = tkinter.Label(main_window, text = "password")
    password_label.grid(row = 1,column = 0,padx = 5,pady = 5)
    username_entry = tkinter.Entry(main_window)
    username_entry.grid(row = 0,column = 1,padx =5,pady= 5)
    password_entry = tkinter.Entry(main_window)
    password_entry.grid(row = 1,column = 1,padx =5,pady= 5)
    data = load_data()  
    login_button = tkinter.Button(main_window, text = "login",command = lambda:login(data))#lamda is used to pass function with it going through with blank values
    #The lambda function waits for the button to be clicked and it is used when we have to pass an argument in the function
    login_button.grid(row = 2,column = 1)
    main_window.mainloop() #keeps window running
pygame.init()
#these are all the sound effects used in the game
#we did this using pygame.mixer.Sound
playing_sound_easy = pygame.mixer.Sound("01. Ground Theme.mp3")
playing_sound_hard = pygame.mixer.Sound("02. Underground Theme.mp3")
jump_sound = pygame.mixer.Sound("poppop.ai - mario jump sound effect.mp3")
bullet_sound = pygame.mixer.Sound("sm64_bullet_bill_blaster.wav")
coin_sound = pygame.mixer.Sound("sm64_red_coin_1.wav")
game_over = pygame.mixer.Sound("sm64_game_over.wav")
jump_sound.set_volume(0.2)
coin_sound.set_volume(1.2)
bullet_sound.set_volume(1.2)
#these are the dimensions of the screen
WIDTH = 1000
HEIGHT = 600
def screen(WIDTH,HEIGHT):
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()#this is to get fps of the game and make it use for the game in further
FPS = 30
pygame.display.set_caption("Final Culminating")
# Background image
bkImage = pygame.image.load("bk.png")
#this is line code used for loading background image in the game
bkImage = pygame.transform.scale(bkImage, (WIDTH, HEIGHT))#This is used to tranform the image and adjust it to the width and hight of the screen
#these are all the attributes of the games which change according to the difficulty chosen
player_speed = 15
player_jump = 60
lives = 5
gravity = 2
num_players = 1
min_bullet_speed = 15
max_bullet_speed = 25
Bull_number = 8
lives = 10
score = 0
level = 300
last_time = 0
highscore = 0
coin_number = 10
sound_state = ""
# Parent sprite class used by all game objects
# Stores image, position, scale, and drawing functionality
class sprite:
    def __init__(self,adde,scale,x,y):
        self.img_path = adde
        self.scale = scale
        self.x = x
        self.y = y
        self.location = (self.x,self.y)
        self.sprite_img = pygame.image.load(self.img_path)
        self.sprite_img = pygame.transform.scale(self.sprite_img, (self.scale,self.scale))
        self.rect = self.sprite_img.get_rect(center = (self.x,self.y))
    def draw(self):
        self.rect.center = (self.x, self.y)
        screen.blit(self.sprite_img,self.rect)
    def getWidth(self):
        return self.__sprite_img.get_width()#this is to get the width and height of the spirite
    def getHeight(self):    
        return self.__sprite_image.get_height()
    def getx(self):
        return self.x
# Inherits from the sprite and then gets added to bullet_move
# This class is mainly for making bullets and moving them
class bullet(sprite):
    def __init__(self,adde,scale,x,y):
        super().__init__(adde,scale,x,y)#used for inheriting attributes from the parent classs
        self.bull_speed = random.randint(min_bullet_speed,max_bullet_speed)
    def move(self):#used for movement
        self.x -= self.bull_speed
        if self.x<0:
            self.x = WIDTH
            self.y = random.randint(self.scale,420)
    def getx(self):#extra function is used in future
        return self.x
    def relocate(self):#extra function is used in future
        self.x = WIDTH
        self.y = random.randint(self.scale,420)
# This is the class where the bullets are made and then stored in a list. 
class bullet_move():
    def __init__(self):
        self.bullets = []
    def make(self):
        b = random.randint(WIDTH,WIDTH+500)
        a = random.randint(0,400)
        for bull in range(Bull_number):
            temp_bull = bullet("Bullet-removebg-preview.png",50,b,a)
            self.bullets.append(temp_bull)
    def display(self):
        for bull in self.bullets:
            bull.draw()
    def move(self):
        for bull in self.bullets:
            bull.move()
#This class created the sprite that the player moves using arrow keys 
class Player(sprite):
    def __init__(self,adde,scale,x,y):
        super().__init__(adde,scale,x,y)
    def move(self,events):
        for event in events:#this specifically to have one key input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.y>0:
                    self.y -= player_jump
                    jump_sound.play()
        keys = pygame.key.get_pressed()#this is to have keys pressed and not needing to press repeatedl
        if self.y<445:
            self.y += gravity
        if keys[pygame.K_LEFT] and self.x > player_speed:
            self.x -= player_speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.scale - player_speed:
            self.x += player_speed
        if keys[pygame.K_DOWN] and self.y < 410:
            self.y += player_jump
#this is the class same as bullet_move where the player sprite is stored in a list and is moved by calling the fucntion
class Players:
    def __init__(self):
        self.sprites = []
    def make(self):
        temp_play = Player("mario (2).png",100,100,450)
        self.sprites.append(temp_play)
    def display(self):
        for z in self.sprites:
            z.draw()
    def move(self,events):
        for z in self.sprites:
            z.move(events)
#This class similar to bullet inherits from the sprite class and is used for making and moving the coins
class Coin(sprite):
    def __init__(self,adde,scale,x,y):
        super().__init__(adde,scale,x,y)
    def move(self):
        self.x -= 5
        if self.x <= 0:
            self.x = random.randint(WIDTH,WIDTH+20000)
    def relocate(self):
        self.x = random.randint(WIDTH,WIDTH+20000)
        self.y = 470
#This class similar to bullet_move stores all the coin objects that are made and make them move
class Coinslist():
    def __init__(self):
        self.coins = []
    def spawn(self):
        for i in range(coin_number):
            x = random.randint(WIDTH,WIDTH+20000)
            tempcoin = Coin("Coin.png",50,x,450)
            self.coins.append(tempcoin)
    def display(self):
        for z in self.coins:
            z.draw()
    def move(self):
        for z in self.coins:
            z.move()
# heart class is used for displaying the hearts at the top left corner of the screen
class heart(sprite):
    def __init__(self,adde,scale,x,y):
        super().__init__(adde,scale,x,y)
#this class stores all the hearts that are made and displayes them according to the variable live
class heartlist:
    def __init__(self):
        self.hearts = []
    def make(self,live):
        for i in range(live):
            tempheart = heart("Heart-removebg-preview.png",50,20+(i*35),25)
            self.hearts.append(tempheart)
    def display(self):
        for i in self.hearts:
            i.draw()
# Font settings
textfont = pygame.font.SysFont("Arial", 40)#this is the code that is used for setting font settings of the text
Endgametext = pygame.font.SysFont("Times New Roman", 40)
#this is the def that I took from internet to display multiple lines of text
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
text = "In this game you will be Controlling the charachter with the arrow keys " \
       "to avoid the bullets that are coming from the right side and get score for each coin that you collect. \n"
font = pygame.font.SysFont('Comic Sans', 55)
#these rects are used as buttons in the main menu
text_1 = textfont.render("Easy Mode", True, (255, 255, 0), (170, 0, 0))
textrect_1 = text_1.get_rect(center=(350, 420))#this is to set the blit the text with center at the desired co-ordinate
text_2 = textfont.render("Hard Mode", True, (255, 255, 0), (170, 0, 0))
textrect_2 = text_2.get_rect(center=(WIDTH-350, 420))
help_text = textfont.render("Help", True, (255, 255, 0), (170, 0, 0))
help_rect = help_text.get_rect(center=(50,45))
close = textfont.render("Close", True, (255, 255, 0), (170, 0, 0))
close_rect = close.get_rect(center=(900,45))
logo_img = pygame.image.load("C:\\Users\\Bandhanjot\\OneDrive\\Desktop\\ISC4U\\Final Culminating\\logocoinss-removebg-preview.png")#this is the logo
logo_img = pygame.transform.scale(logo_img, (400,400))
logo_img_rect = logo_img.get_rect(center = (500,200))
exit_text = textfont.render("Exit", True, (255, 255, 0), (170, 0, 0))
exit_rect = exit_text.get_rect(center=(950,45))
# Game loop
def main(User_name="Player"):
    #all the variable used inside the loop are globalised
    global player_speed, player_jump, lives, gravity, min_bullet_speed, max_bullet_speed, Bull_number,lives,score,highscore,coin_number,sound_state
    data = load_data()#this is to load set highscore as the one that was saved before
    if User_name in data:
        highscore = data[User_name]["High Score"]
    screen(WIDTH,HEIGHT)
    gameState = "main"# this is the state of the game, it is done for making the code simpler as the code is divided into 3 parts that is main that is selection of the level,start is the phase where the game is played and the end the past of the game where scores and other options are present    
    while True:
        clock.tick(FPS)
        last_time = pygame.time.get_ticks()#This is to get the current time of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:#this is used to get the various function with mouse
                pos = pygame.mouse.get_pos()#this is to get the position of the mouse click
                #this particular rectangle is to set the level easy
                if gameState == "main" and textrect_1.collidepoint(pos):#if the mouse click the space of the rectangle the if will get activated
                    gameState = "Start"#this is to change the state of the game to start
                    playing_sound_easy.play(-1) # -1 loops it indefinitely
                    sound_state = "Easy"
                    player_speed = 15
                    player_jump = 60
                    lives = 10
                    gravity = 2
                    num_players = 1
                    min_bullet_speed = 5
                    max_bullet_speed = 15
                    Bull_number = 5
                    coin_number = 10
                    score = 0
                #this elif and the rectangle is for level hard of the game which can be seen as the changes in the different variables which increases the difficulty of the game
                elif gameState == "main" and textrect_2.collidepoint(pos):
                    gameState = "Start"
                    playing_sound_hard.play(-1)
                    sound_state = "Hard"
                    player_speed = 15
                    player_jump = 60
                    lives = 5
                    gravity = 2
                    num_players = 1
                    min_bullet_speed = 15
                    max_bullet_speed = 25
                    Bull_number = 8
                    coin_number = 20
                    score = 0
                #this elif is if help rect is pressed then game state will change to help and the help text which explain the mechanics of the game is appeared
                elif gameState == "main" and help_rect.collidepoint(pos):
                    gameState = "help"
                #this is to get to the main screen form the help screen
                elif gameState == "help" and close_rect.collidepoint(pos):
                    gameState = "main"
                #this is used if you want to close the game from the start menu.
                elif gameState == "main" and exit_rect.collidepoint(pos):
                    pygame.quit()
                    exit()
                elif gameState == "end" and play_again_text_rect.collidepoint(pos):#this elif is used so that when after the game is finished and this rectangle where play again is writen is pressed to change the game state to main so that player have the option to select a different difficulty and restart the game
                    gameState = "main"
                elif gameState == "end" and quit_text_rect.collidepoint(pos):
                    #this is so that after the quit box is clicked the game shuts down
                    pygame.quit()
                    exit()
        if gameState == "main":
            # Main menu
            #this is the screen of the game where the instructions are blit and the buttons for play again and quit are writen
            screen.blit(bkImage, (0, 0))#this is to blit the background image
            screen.blit(text_1, textrect_1)#this is to blit the easy mode text and text rectangle
            screen.blit(text_2, textrect_2)#this is to blit the hard mode text and text rectangle
            screen.blit(help_text, help_rect)# this is to blit Help and rectangle
            screen.blit(logo_img,logo_img_rect)# this is to blit the logo
            screen.blit(exit_text,exit_rect)# this is to blit Exit and rectangle
        elif gameState == "help":
            screen.blit(bkImage, (0, 0))#this is to blit the background image
            blit_text(screen, text, (40,50), font)#this is to blit the instructions
            screen.blit(close, close_rect)#this is to close the help screen and get exit to the main screen
        elif gameState == "Start":
            #all the objects are created at the start before the actual game loop
            play = Players()
            play.make()
            scroll = 0
            co = Coinslist()
            co.spawn()
            bulls = bullet_move()
            bulls.make()
            run = True
            while run:
                clock.tick(FPS)
                #this for the scrolling background
                for i in range(0,2):
                    screen.blit(bkImage,(i * WIDTH + scroll,0))
                scroll -= 5
                if abs(scroll)> WIDTH:
                    scroll = 0
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        run = False
                #allt the objects are blitted and moved using these codes
                heartssss = heartlist()
                heartssss.make(lives)
                play.move(events)
                bulls.move()
                co.move()
                play.display()
                bulls.display()
                co.display()
                heartssss.display()
                #this is collision detection where we see if objects from one list collide with objects from another list then specific actions will be taken
                #this is for collision with bullets
                for sprite in play.sprites:
                    for bullet in bulls.bullets:
                        if sprite.rect.colliderect(bullet.rect):
                            lives -= 1#this will reduce one life
                            bullet_sound.play()#sound effect of bullet hit is played
                            bullet.relocate()#bullet get moved to a different location
                #this is for collision with coins 
                for sprite in play.sprites:
                    for coin in co.coins:
                        if sprite.rect.colliderect(coin.rect):
                            score += 5#this will increase the score by 5 and special sound is played
                            coin_sound.play()
                            coin.relocate()#coin gets relocated
                pygame.display.update() #this updates all the cordiantes of the sprites
                #If you have 0 lives then the theme song will end and game over sound will be played and the game loop will close
                if lives <= 0 and sound_state == "Easy":
                    playing_sound_easy.stop()
                    game_over.play()
                    run = False
                if lives <= 0 and sound_state == "Hard":
                    playing_sound_hard.stop()
                    game_over.play()
                    run = False
            #once the gameloop is closed gamestate will change to end and end screen is showen
            if run == False:
                gameState = "end"
        elif gameState == "end":
            # End screen
            if score>highscore:#this is the high score function during one setion taht is the score is greater than the current high score then the highscore is updated
                highscore = score
                data = load_data()
                if User_name in data:
                    data[User_name]["High Score"] = highscore
                else:
                    data[User_name] = {"password": "", "High Score": highscore}
                save_data(data)
                print(highscore)
            screen.blit(bkImage, (0, 0))#this is to blit the background screen
            end_text = textfont.render("Game Over! Final Score: {}".format(score), True, (225, 255, 255),(0, 0, 0))#this is to render game over and Final score text at the end of the game
            end_rect = end_text.get_rect(center = (500,120))
            screen.blit(end_text,end_rect)#this is to blit the end_text and the given cords
           
            highscore_text = textfont.render("High Score is : {}".format(highscore), True, (225, 255, 255),(0, 0, 0))#this is to render the high score text
            highscore_rect = highscore_text.get_rect(center=(500, 220))
            screen.blit(highscore_text,highscore_rect)#this is to blit high score at the end of the game
            play_again_text = Endgametext.render("Play Again", True, (0, 255, 0),(0, 0, 0))#this is to show play again text with green font and black background
            quit_text = Endgametext.render("Quit", True, (255, 0, 0),(0, 0, 0))#this is to render quit text with red font and black background

            play_again_text_rect = play_again_text.get_rect(center=(500, 320))#this is to get rectangle around the play again text and setting it being center at the given cords
            quit_text_rect = quit_text.get_rect(center=(500,405))#this is to get rectangle around the quit text and setting it being center at the given cords
           
            #this is to blit the text with the rectangle
            screen.blit(play_again_text, play_again_text_rect)
            screen.blit(quit_text, quit_text_rect)
        pygame.display.update()
if __name__ ==  '__main__':
    main_window()#this for running the code