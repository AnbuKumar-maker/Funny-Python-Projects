import pygame
import random
import time

#This makes the ASCII codes of each key press avaiable by usign a more obvious
#variable name instead of a number
KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276
KEY_A = 97
KEY_Q = 113
KEY_S = 115


#The game is made of switching between different scenes, and each scene is its
#own function. The game goes from function to functions

#This function is the intro scene.
def intro():
    width = 500         #This sets the width and height of the intro scene
    height = 500

    pygame.init()       #This starts pygame

    #Music - This loads the music from the spiderman cartoon and plays in a loop
    pygame.mixer.init()
    pygame.mixer.music.load('90s_Spiderman.ogg')
    pygame.mixer.music.play(-1)

    #This sets the screen to be equal to the size we set
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/intro_background.png').convert_alpha()
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()

    #This is the text that will appear at the bottom of the screen
    intro_message = "Press S to Play"
    #change_dir_countdown = 120

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    print ("")
                elif event.key == KEY_S:
                    print ("")
                    stop_game = True    #This is the only key that leaves the scene
                elif event.key == KEY_LEFT:
                    print ("")
                elif event.key == KEY_RIGHT:
                    print ("")
            if event.type == pygame.QUIT:
                stop_game = True


        screen.blit(background_image, (0,0))   #This sets the scene to the intro

        font = pygame.font.Font(None, 25)      #No font specifically
        intro_text = font.render(intro_message, True, (255, 255, 255))
        screen.blit(intro_text, (100, 440))     #This puts the text onto the screen


        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

####end of Intro



#This function is the scene that shows when you win a battle
def thumbs_up():
    width = 500
    height = 500

    pygame.init()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load('thumbs_up.ogg')
    sound = pygame.mixer.Sound('i_am_spiderman.ogg')
    pygame.mixer.music.play(-1)
    sound.play()





    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/thumbs_up.png').convert_alpha()
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()

    thumbs_up_message = "You won!"
    intro_message = "Press S to Continue"
    #change_dir_countdown = 120

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    print ("")
                elif event.key == KEY_S:
                    print ("")
                    stop_game = True
                elif event.key == KEY_LEFT:
                    print ("")
                elif event.key == KEY_RIGHT:
                    print ("")
            if event.type == pygame.QUIT:
                stop_game = True


        screen.blit(background_image, (0,0))

        font = pygame.font.Font(None, 25)
        intro_text = font.render(intro_message, True, (255, 255, 255))
        thumbs_up_text = font.render(thumbs_up_message, True, (255, 255, 255))
        screen.blit(intro_text, (200, 440))
        screen.blit(thumbs_up_text, (250, 340))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

####end of Thumbs up


#This function shows the end scene
def ending():
    width = 500
    height = 500

    pygame.init()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load('90s_Spiderman.ogg')
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/ending.png').convert_alpha()
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()


    ending_message = "You Win!"
    #change_dir_countdown = 120

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_Q:
                    stop_game = True
                elif event.key == KEY_S:
                    stop_game = True
                elif event.key == KEY_LEFT:
                    print ("")
                elif event.key == KEY_RIGHT:
                    print ("")
            if event.type == pygame.QUIT:
                stop_game = True


        screen.blit(background_image, (0,0))

        font = pygame.font.Font(None, 100) #25
        ending_text = font.render(ending_message, True, (255, 255, 255))
        screen.blit(ending_text, (100, 440))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

####end of Ending


###Rhino fight_final

def rhino_fight():
    # declare the size of the canvas
    width = 500
    height = 500


    pygame.init()


    # #Music
    pygame.mixer.init()
    pygame.mixer.music.load('fight.ogg')
    pygame.mixer.music.play(-1)

    #Sound effect
    sound = pygame.mixer.Sound('punch.ogg')


    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()

    # Game initialization
    rhino_fight_image = pygame.image.load('images/rhino_fight.png').convert_alpha()
    #hero_image = pygame.image.load('images/big_hero.png').convert_alpha()

    #RPG Data
    hero_health = 30
    hero_damage = 4

    orc_health = 20
    orc_damage = 2

    hero_message = "Press A to attack"
    orc_message = ""
    health_message = "Spider Man: %s/30HP" % hero_health
    orc_health_message = "Rhino: %s/20HP" % orc_health

    stop_game = False
    while not stop_game and orc_health > 0 and hero_health > 0:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    print ("Invalid Input")
                elif event.key == KEY_A:
                    sound.play()
                    hero_damage = random.randrange(1,6)
                    orc_damage = random.randrange(1,4)
                    hero_message = "You attack Rhino for %d damage!" % hero_damage
                    orc_message = "Rhino attacks you for %d damage!" % orc_damage
                    orc_health -= hero_damage
                    hero_health -= orc_damage
                    health_message = "Spider Man: %s/30HP" %str(hero_health)
                    orc_health_message = "Rhino: %s/20HP" %str(orc_health)
                elif event.key == KEY_LEFT:
                    print ("Invalid input")
                elif event.key == KEY_RIGHT:
                    print ("Invalid input")
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        # screen.fill(blue_color)

        # Game display

        screen.blit(rhino_fight_image, (0, 0))

        #200, 200, 100, 100
        pygame.draw.rect(screen, (0, 0, 0), (0, 400, 500, 100), 0)
        font = pygame.font.Font(None, 25)
        text = font.render("Rhino: I'll destroy you Spiderman!", True, (255, 255, 255))
        #attack_text = font.render("Press UP to attack", True, (255, 255, 255))
        hero_attack_text = font.render(hero_message, True, (255, 255, 255))
        orc_attack_text = font.render(orc_message, True, (255, 0, 0))
        health_text = font.render(health_message, True, (255, 255, 255))
        orc_health_text = font.render(orc_health_message, True, (255, 255, 255))
        screen.blit(text, (0, 400))
        #screen.blit(attack_text, (0, 450))
        screen.blit(hero_attack_text, (0, 440))
        screen.blit(orc_attack_text, (0, 460))
        screen.blit(health_text, (320, 400))
        screen.blit(orc_health_text, (320, 420))
        pygame.display.update()

        clock.tick(60)

    if orc_health > 0:
        #print "You died."
        print ("You Lose!")
    elif hero_health > 0:
        #print "Orc died."
        print ("")

    pygame.quit()
##End of rhino fight


###lizard fight final

def lizard_fight():
    # declare the size of the canvas
    width = 500
    height = 500


    pygame.init()


    # #Music
    pygame.mixer.init()
    pygame.mixer.music.load('fight.ogg')
    pygame.mixer.music.play(-1)

    #Sound effect
    sound = pygame.mixer.Sound('punch.ogg')


    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()

    # Game initialization
    #font = pygame.font.SysFont("comicsansms", 72)
    #text = font.render("Hello, World", True, (255, 255, 255))
    orc_image = pygame.image.load('images/lizard_fight.png').convert_alpha()
    #hero_image = pygame.image.load('images/big_hero.png').convert_alpha()


    #RPG Data
    hero_health = 30
    hero_damage = 4

    orc_health = 25
    orc_damage = 2

    hero_message = "Press A to attack"
    orc_message = ""
    health_message = "Spider Man: %s/30HP" % hero_health
    orc_health_message = "The Lizard: %s/25HP" % orc_health

    stop_game = False
    while not stop_game and orc_health > 0 and hero_health > 0:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    print ("Invalid Input")
                elif event.key == KEY_A:
                    sound.play()
                    hero_damage = random.randrange(1,6)
                    orc_damage = random.randrange(1,4)
                    hero_message = "You attack The Lizard for %d damage!" % hero_damage
                    orc_message = "The Lizard attacks you for %d damage!" % orc_damage
                    orc_health -= hero_damage
                    hero_health -= orc_damage
                    health_message = "Spider Man: %s/30HP" %str(hero_health)
                    orc_health_message = "The Lizard: %s/25HP" %str(orc_health)
                elif event.key == KEY_LEFT:
                    print ("Invalid input")
                elif event.key == KEY_RIGHT:
                    print ("Invalid input")
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        # screen.fill(blue_color)

        # Game display

        screen.blit(orc_image, (0, 0))

        #200, 200, 100, 100
        pygame.draw.rect(screen, (0, 0, 0), (0, 400, 500, 100), 0)
        font = pygame.font.Font(None, 25)
        text = font.render("The Lizard: RAAAAAAAAARGH!", True, (255, 255, 255))
        #attack_text = font.render("Press UP to attack", True, (255, 255, 255))
        hero_attack_text = font.render(hero_message, True, (255, 255, 255))
        orc_attack_text = font.render(orc_message, True, (255, 0, 0))
        health_text = font.render(health_message, True, (255, 255, 255))
        orc_health_text = font.render(orc_health_message, True, (255, 255, 255))
        screen.blit(text, (0, 400))
        #screen.blit(attack_text, (0, 450))
        screen.blit(hero_attack_text, (0, 440))
        screen.blit(orc_attack_text, (0, 460))
        screen.blit(health_text, (320, 400))
        screen.blit(orc_health_text, (320, 420))
        pygame.display.update()

        clock.tick(60)

    if orc_health > 0:
        #print "You died."
        print ("You Lose!")
    elif hero_health > 0:
        #print "Orc died."
        print ("")

    pygame.quit()
##End of lizard fight


#Sandman fight
def sandman_fight():
    # declare the size of the canvas
    width = 500
    height = 500


    pygame.init()


    # #Music
    pygame.mixer.init()
    pygame.mixer.music.load('fight.ogg')
    pygame.mixer.music.play(-1)

    #Sound effect
    sound = pygame.mixer.Sound('punch.ogg')


    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()

    # Game initialization
    #font = pygame.font.SysFont("comicsansms", 72)
    #text = font.render("Hello, World", True, (255, 255, 255))
    orc_image = pygame.image.load('images/sandman_fight.png').convert_alpha()
    #hero_image = pygame.image.load('images/big_hero.png').convert_alpha()


    #RPG Data
    hero_health = 30
    hero_damage = 4

    orc_health = 30
    orc_damage = 2

    hero_message = "Press A to attack"
    orc_message = ""
    health_message = "Spider Man: %s/30HP" % hero_health
    orc_health_message = "Sandman: %s/30HP" % orc_health

    stop_game = False
    while not stop_game and orc_health > 0 and hero_health > 0:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    print ("Invalid Input")
                elif event.key == KEY_A:
                    sound.play()
                    hero_damage = random.randrange(1,7)
                    orc_damage = random.randrange(1,4)
                    hero_message = "You attack Sandman for %d damage!" % hero_damage
                    orc_message = "Sandman attacks you for %d damage!" % orc_damage
                    orc_health -= hero_damage
                    hero_health -= orc_damage
                    health_message = "Spider Man: %s/30HP" %str(hero_health)
                    orc_health_message = "Sandman: %s/30HP" %str(orc_health)
                elif event.key == KEY_LEFT:
                    print ("Invalid input")
                elif event.key == KEY_RIGHT:
                    print ("Invalid input")
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        # screen.fill(blue_color)

        # Game display

        screen.blit(orc_image, (0, 0))

        #200, 200, 100, 100
        pygame.draw.rect(screen, (0, 0, 0), (0, 400, 500, 100), 0)
        font = pygame.font.Font(None, 25)
        text = font.render("Sandman: I'm gonna squash you!", True, (255, 255, 255))
        #attack_text = font.render("Press UP to attack", True, (255, 255, 255))
        hero_attack_text = font.render(hero_message, True, (255, 255, 255))
        orc_attack_text = font.render(orc_message, True, (255, 0, 0))
        health_text = font.render(health_message, True, (255, 255, 255))
        orc_health_text = font.render(orc_health_message, True, (255, 255, 255))
        screen.blit(text, (0, 400))
        #screen.blit(attack_text, (0, 450))
        screen.blit(hero_attack_text, (0, 440))
        screen.blit(orc_attack_text, (0, 460))
        screen.blit(health_text, (320, 400))
        screen.blit(orc_health_text, (320, 420))
        pygame.display.update()

        clock.tick(60)

    if orc_health > 0:
        #print "You died."
        print ("You Lose!")
    elif hero_health > 0:
        #print "Orc died."
        print ("")

    pygame.quit()
##End of Sandman fight




####Rhino overworld
def rhino():
    #Rhino Overworld final
    class Character(object):
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.x_dir = 1
            self.y_dir = 1
            self.image = image
            self.alive = True


        def displayCharacter(self,screen):
            if self.alive == True:
                screen.blit(self.image, (self.x,self.y))
            else:
                print ("dead")

        def move_character(self):
            self.x += self.x_dir
            self.y += self.y_dir

        def change_direction(self):

            rand_direction = random.randint(0,7)

            if rand_direction == 0:   # top or north
                self.x_dir = 0
                self.y_dir = -1

            elif rand_direction == 1:  #right or east
                self.x_dir = 1
                self.y_dir = 0

            elif rand_direction == 2:  #down or south
                self.x_dir =0
                self.y_dir = 1

            elif rand_direction == 3:  #left or west
                self.x_dir =-1
                self.y_dir = 0

            elif rand_direction == 4:   # Northeast - topright
                self.x_dir = 1
                self.y_dir = -1

            elif rand_direction == 5:  # Northwest - top left
                self.x_dir = -1
                self.y_dir = -1

            elif rand_direction == 6:  # Southwest - bottom left
                self.x_dir = -1
                self.y_dir = 1

            elif rand_direction == 7:  # South east - bottom right
                self.x_dir = 1
                self.y_dir = 1

        def off_screen(self):
            if self.y < 0:      #top
                self.y =  500
            else:
                self.y -= 5

            if self.x > 500:    #right
                self.x = 0
            else:
                self.x += 5

            if self.y > 500:     #down
                self.y =  0
            else:
                self.y += 5

            if self.x < 0:       #left
                self.x =  500
            else:
                self.x -= 5


    class Rhino(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/rhino.png').convert_alpha()
            self.x = x
            self.y = y
            self.x_dir = 2
            self.y_dir = 0
            self.alive = True

    #Transforming to Ball
    class Ball(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/hero.png').convert_alpha()
            self.x = x
            self.y = y
            self.speed_x = 0
            self.speed_y = 0
            self.alive = True

        def update(self):
            self.x += self.speed_x
            self.y += self.speed_y

        # def off_screen(self):
        #     if self.y < 31:      #top
        #         self.y = 31
        #
        #     if self.x > 450:    #right
        #         self.x = 450
        #
        #     if self.y > 418:     #down
        #         self.y =  418
        #
        #     if self.x < 31:       #left
        #         self.x =  31

        # Spiderman
        def off_screen(self):
            if self.y < 0:      #top
                self.y = 0

            if self.x > 460:    #right
                self.x = 460

            if self.y >= 445:     #down
                self.y =  445

            if self.x < 0:       #left
                self.x =  0


    #Screen
    width = 500
    height = 500
    # blue_color = (97, 159, 182)

    pygame.init()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load('Spiderman.ogg')
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/rhino_background.png').convert_alpha()
    monster = pygame.image.load('images/rhino.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    change_dir_countdown = 120

    # Game initialization

    monster = Rhino(50,50)
    ball = Ball(256,240)


    stop_game = False
    change_dir_counter = 0       # original change_dir_count
    while not stop_game:
        for event in pygame.event.get():

# this is for controlling the hero with the keyboard, declared keys at
#the top of the page, and set controls in the pygame.event.get()


            #Ball Smooth keys
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        # Game logic

        monster.move_character()    #moves monster around

# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1
        if change_dir_counter == 120:
            monster.change_direction()   # changes monster direction
            change_dir_counter = 0

        monster.off_screen()             #keeps monster on screen
        ball.off_screen()                #keeps hero inside screen


        #Colission Detection
        if ball.x + 32 < monster.x:
            pass
            # print "No Collision"
        elif monster.x + 32 < ball.x:
            pass
            # print "No Collision"
        elif ball.y + 32 < monster.y:
            pass
            # print "No Collision"
        elif monster.y + 32 < ball.y:
            pass
            # print "No Collision"
        else:
            #print "Collision!"
            monster.alive = False
            rhino_fight()
            break



        # Game logic
        ball.update()

        # screen.fill(blue_color)

        screen.blit(background_image, (0,0))
        # screen.blit(monster, (monster.x,monster.y))
        monster.displayCharacter(screen)
        ball.displayCharacter(screen)
        #screen.blit(monster, (x_dir,y_dir))
        # screen.blit(hero, (256,240))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
####Rhino Overworld


####Lizard overworld
def lizard():

    class Character(object):
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.x_dir = 1
            self.y_dir = 1
            self.image = image
            self.alive = True


        def displayCharacter(self,screen):
            if self.alive == True:
                screen.blit(self.image, (self.x,self.y))
            else:
                print ("dead")

        def move_character(self):
            self.x += self.x_dir
            self.y += self.y_dir

        def change_direction(self):

            rand_direction = random.randint(0,7)

            if rand_direction == 0:   # top or north
                self.x_dir = 0
                self.y_dir = -1

            elif rand_direction == 1:  #right or east
                self.x_dir = 1
                self.y_dir = 0

            elif rand_direction == 2:  #down or south
                self.x_dir =0
                self.y_dir = 1

            elif rand_direction == 3:  #left or west
                self.x_dir =-1
                self.y_dir = 0

            elif rand_direction == 4:   # Northeast - topright
                self.x_dir = 1
                self.y_dir = -1

            elif rand_direction == 5:  # Northwest - top left
                self.x_dir = -1
                self.y_dir = -1

            elif rand_direction == 6:  # Southwest - bottom left
                self.x_dir = -1
                self.y_dir = 1

            elif rand_direction == 7:  # South east - bottom right
                self.x_dir = 1
                self.y_dir = 1

        def off_screen(self):
            if self.y < 0:      #top
                self.y =  500
            else:
                self.y -= 5

            if self.x > 500:    #right
                self.x = 0
            else:
                self.x += 5

            if self.y > 500:     #down
                self.y =  0
            else:
                self.y += 5

            if self.x < 0:       #left
                self.x =  500
            else:
                self.x -= 5


    class Lizard(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/lizard.png').convert_alpha()
            self.x = x
            self.y = y
            self.x_dir = 2
            self.y_dir = 0
            self.alive = True

    #Transforming to Ball
    class Ball(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/hero.png').convert_alpha()
            self.x = x
            self.y = y
            self.speed_x = 0
            self.speed_y = 0
            self.alive = True

        def update(self):
            self.x += self.speed_x
            self.y += self.speed_y

        # def off_screen(self):
        #     if self.y < 0:      #top
        #         self.y = 0
        #
        #     if self.x > 500:    #right
        #         self.x = 500
        #
        #     if self.y > 500:     #down
        #         self.y =  500
        #
        #     if self.x < 0:       #left
        #         self.x =  0

        # Spiderman
        def off_screen(self):
            if self.y < 0:      #top
                self.y = 0

            if self.x > 460:    #right
                self.x = 460

            if self.y >= 445:     #down
                self.y =  445

            if self.x < 0:       #left
                self.x =  0

    #Screen
    width = 500
    height = 500
    # blue_color = (97, 159, 182)

    pygame.init()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load('Spiderman.ogg')
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/lizard_background.png').convert_alpha()
    monster = pygame.image.load('images/lizard.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    change_dir_countdown = 120

    # Game initialization

    monster = Lizard(50,50)
    ball = Ball(256,240)


    stop_game = False
    change_dir_counter = 0       # original change_dir_count
    while not stop_game:
        for event in pygame.event.get():

# this is for controlling the hero with the keyboard, declared keys at
#the top of the page, and set controls in the pygame.event.get()


            #Ball Smooth keys
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        # Game logic

        monster.move_character()    #moves monster around

# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1
        if change_dir_counter == 120:
            monster.change_direction()   # changes monster direction
            change_dir_counter = 0

        monster.off_screen()             #keeps monster on screen
        ball.off_screen()                #keeps hero inside screen


        #Colission Detection
        if ball.x + 32 < monster.x:
            pass
            # print "No Collision"
        elif monster.x + 32 < ball.x:
            pass
            # print "No Collision"
        elif ball.y + 32 < monster.y:
            pass
            # print "No Collision"
        elif monster.y + 32 < ball.y:
            pass
            # print "No Collision"
        else:
            #print "Collision!"
            monster.alive = False
            lizard_fight()
            break



        # Game logic
        ball.update()

        #screen.fill(blue_color)

        screen.blit(background_image, (0,0))
        # screen.blit(monster, (monster.x,monster.y))
        monster.displayCharacter(screen)
        ball.displayCharacter(screen)
        #screen.blit(monster, (x_dir,y_dir))
        # screen.blit(hero, (256,240))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
####Lizard Overworld



####Sandman overworld
def sandman():

    class Character(object):
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.x_dir = 1
            self.y_dir = 1
            self.image = image
            self.alive = True


        def displayCharacter(self,screen):
            if self.alive == True:
                screen.blit(self.image, (self.x,self.y))
            else:
                print ("dead")

        def move_character(self):
            self.x += self.x_dir
            self.y += self.y_dir

        def change_direction(self):

            rand_direction = random.randint(0,7)

            if rand_direction == 0:   # top or north
                self.x_dir = 0
                self.y_dir = -1

            elif rand_direction == 1:  #right or east
                self.x_dir = 1
                self.y_dir = 0

            elif rand_direction == 2:  #down or south
                self.x_dir =0
                self.y_dir = 1

            elif rand_direction == 3:  #left or west
                self.x_dir =-1
                self.y_dir = 0

            elif rand_direction == 4:   # Northeast - topright
                self.x_dir = 1
                self.y_dir = -1

            elif rand_direction == 5:  # Northwest - top left
                self.x_dir = -1
                self.y_dir = -1

            elif rand_direction == 6:  # Southwest - bottom left
                self.x_dir = -1
                self.y_dir = 1

            elif rand_direction == 7:  # South east - bottom right
                self.x_dir = 1
                self.y_dir = 1

        def off_screen(self):
            if self.y < 0:      #top
                self.y =  500
            else:
                self.y -= 5

            if self.x > 500:    #right
                self.x = 0
            else:
                self.x += 5

            if self.y > 500:     #down
                self.y =  0
            else:
                self.y += 5

            if self.x < 0:       #left
                self.x =  500
            else:
                self.x -= 5


    class Sandman(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/sandman.png').convert_alpha()
            self.x = x
            self.y = y
            self.x_dir = 2
            self.y_dir = 0
            self.alive = True

    #Transforming to Ball
    class Ball(Character):
        def __init__(self, x, y):
            self.image = pygame.image.load('images/hero.png').convert_alpha()
            self.x = x
            self.y = y
            self.speed_x = 0
            self.speed_y = 0
            self.alive = True

        def update(self):
            self.x += self.speed_x
            self.y += self.speed_y

        # def off_screen(self):
        #     if self.y < 0:      #top
        #         self.y = 0
        #
        #     if self.x > 500:    #right
        #         self.x = 500
        #
        #     if self.y > 500:     #down
        #         self.y =  500
        #
        #     if self.x < 0:       #left
        #         self.x =  0

        # Spiderman
        def off_screen(self):
            if self.y < 0:      #top
                self.y = 0

            if self.x > 460:    #right
                self.x = 460

            if self.y >= 445:     #down
                self.y =  445

            if self.x < 0:       #left
                self.x =  0


    #Screen
    width = 500
    height = 500
    # blue_color = (97, 159, 182)

    pygame.init()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load('Spiderman.ogg')
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/sandman_background.png').convert_alpha()
    monster = pygame.image.load('images/sandman.png').convert_alpha()
    hero = pygame.image.load('images/hero.png').convert_alpha()
    pygame.display.set_caption('Spiderman Game')
    clock = pygame.time.Clock()

    change_dir_countdown = 120

    # Game initialization

    monster = Sandman(50,50)
    ball = Ball(256,240)


    stop_game = False
    change_dir_counter = 0       # original change_dir_count
    while not stop_game:
        for event in pygame.event.get():

# this is for controlling the hero with the keyboard, declared keys at
#the top of the page, and set controls in the pygame.event.get()


            #Ball Smooth keys
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
        # Game logic

        monster.move_character()    #moves monster around

# this changes the direct by adding 1 to the original change_dir_count = 0
# every 120 seconds it changes direction
        change_dir_counter += 1
        if change_dir_counter == 120:
            monster.change_direction()   # changes monster direction
            change_dir_counter = 0

        monster.off_screen()             #keeps monster on screen
        ball.off_screen()                #keeps hero inside screen


        #Colission Detection
        if ball.x + 32 < monster.x:
            pass
            # print "No Collision"
        elif monster.x + 32 < ball.x:
            pass
            # print "No Collision"
        elif ball.y + 32 < monster.y:
            pass
            # print "No Collision"
        elif monster.y + 32 < ball.y:
            pass
            # print "No Collision"
        else:
            #print "Collision!"
            monster.alive = False
            sandman_fight()
            break



        # Game logic
        ball.update()

        #screen.fill(blue_color)

        screen.blit(background_image, (0,0))
        # screen.blit(monster, (monster.x,monster.y))
        monster.displayCharacter(screen)
        ball.displayCharacter(screen)
        #screen.blit(monster, (x_dir,y_dir))
        # screen.blit(hero, (256,240))

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
####Sandman Overworld

def main():
    intro()
    rhino()
    thumbs_up()
    lizard()
    thumbs_up()
    sandman()
    thumbs_up()
    ending()

if __name__ == '__main__':
    main()
