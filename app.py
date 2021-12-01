import pygame
from pygame.locals import *
from student import *
class Text:
    """
    Create a text object.
    """

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None#'timesnewroman'
        self.fontsize = 25
        self.fontcolor = Color('white')
        self.set_font()
        self.render()
        
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)
    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    def draw(self):
        """Draw the text image to the screen."""
        App.interface_screen.blit(self.img, self.rect)


class App:
    """
    Create a single-window app with multiple scenes.
    """

    def __init__(self):
        """
        Initialize pygame and the application.
        """
        pygame.init()
        bottom_panel_height = 280
        screen_width = 652
        screen_height = 460 + bottom_panel_height
        
        App.actual_screen = pygame.display.set_mode((screen_width, screen_height))
        App.simulation_screen = pygame.Surface((screen_width, 460))
        App.interface_screen = pygame.Surface((screen_width, 280))
        
        pygame.display.set_caption('Lochwynne University')
        background = pygame.Surface(App.actual_screen.get_size())
        App.running = True
        
    def draw_bg():
        """
        Function for drawing background
        """            
        #background image
        background_img = pygame.image.load('images/gates.png').convert_alpha()
        App.simulation_screen.blit(background_img, (0, 0))
    
    def remove_text():
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 40)

        font_surface = font.render("original", True, pygame.Color("white"));

        screen.fill(pygame.Color("black")) # erases the entire screen surface
        font_surface = font.render("edited", True, pygame.Color("white"));
    def draw_text(text):
        line_number = 0
        for line in text:
            my_text = Text(line, pos = (0, line_number*20))
            my_text.draw()
            line_number += 1
            App.remove_text()
        
        
    def fight(Student1, Student2):
        """"
        Allow two Students to fight each other
        """
        # Print fight information
        text_array = [f"{Student1.name}", f"TYPE: {Student1.type}", f"ATTACK: {Student1.attack}"
                      ,f"DEFENSE: {Student1.defense}", f"LVL: {Student1.lvl}", "VS", f"{Student2.name}",
                      f"TYPE: {Student2.type}", f"ATTACK: {Student2.attack}", f"DEFENSE: {Student2.defense}", 
                      f"LVL: {Student2.lvl}"]
        App.draw_text(text_array)
        return
        pygame.time.wait(2)
        
        # Consider type advantages
        version = ['Cerebral','Phytogaia','Zoomor','Mantrador','Null']
        for i,k in enumerate(version):
            if Student1.type == k:
                # Both are same type
                if Student2.type == k:
                    string_1_attack = 'Its not very effective...'
                    string_2_attack = 'Its not very effective...'

                # Student2 is STRONG
                if Student2.type == version[(i+1)%3]:
                    Student2.attack *= 2
                    Student2.defense *= 2
                    Student1.attack /= 2
                    Student1.defense /= 2
                    string_1_attack = 'Its not very effective...'
                    string_2_attack = 'Its super effective!'

                # Student2 is WEAK
                if Student2.type == version[(i+2)%3]:
                    Student1.attack *= 2
                    Student1.defense *= 2
                    Student2.attack /= 2
                    Student2.defense /= 2
                    string_1_attack = 'Its super effective!'
                    string_2_attack = 'Its not very effective...'
        # Now for the actual fighting...
        # Continue while Student still have health
        while (Student1.bars > 0) and (Student2.bars > 0):
            # Print the health of each Student
            text_array = [f"{Student1.name}    HLTH  {Student1.health}",
                          f"{Student2.name}    HLTH   {Student2.health}",
                          f"Go {Student1.name}!"]
            App.draw_text(text_array)
            text_array = []
            for i, x in enumerate(Student1.abilities):
                output = (f"{i+1}.", x)
                text_array.append(output)
                
                
            text_array.append("Pick a move: ")
            App.draw_text(text_array)
            #user picks move
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        text_array  = [f"{Student1.name} used {Student1.abilities[0]}!"] 
                    if event.key == pygame.K_2:
                        text_array  = [f"{Student1.name} used {Student1.abilities[1]}!"]
                    if event.key == pygame.K_3:
                        text_array  = [f"{Student1.name} used {Student1.abilities[2]}!"] 
                    if event.key == pygame.K_4:
                        text_array  = [f"{Student1.name} used {Student1.abilities[3]}!"]  
            App.draw_text(text_array)
            pygame.time.wait(1)
            text_array = (string_1_attack)
            App.draw_text(text_array)
            # Determine damage
            Student2.bars -= Student1.attack
            Student2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Student2.bars+.1*Student2.defense)):
                Student2.health += "="

            pygame.time.wait(1)
            # Print the health of each Student
            text_array = [f"{Student1.name}    HLTH  {Student1.health}",
                          f"{Student2.name}    HLTH   {Student2.health}"]
            App.draw_text(text_array)
            pygame.time.wait(1)

            # Check to see if Student fainted
            if Student2.bars <= 0:
                text_array = [f"... {Student2.name} fainted."]
                App.draw_text(text_array)
                break

            # Student2s turn
            text_array = [f"Go {Student2.name}!"]
            App.draw_text(text_array)
            text_array = []
            for i, x in enumerate(Student2.abilities):
                text_array.append(f"{i+1}.", x)
                
            text_array.append("Pick a move: ")
            App.draw_text(text_array)
            
            #user picks move
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        text_array  = [f"{Student2.name} used {Student2.abilities[0]}!"] 
                    if event.key == pygame.K_2:
                        text_array  = [f"{Student2.name} used {Student2.abilities[1]}!"]
                    if event.key == pygame.K_3:
                        text_array  = [f"{Student2.name} used {Student2.abilities[2]}!"] 
                    if event.key == pygame.K_4:
                        text_array  = [f"{Student2.name} used {Student2.abilities[3]}!"]  
            App.draw_text(text_array)
            pygame.time.wait(1)
            text_array = (string_2_attack)
            App.draw_text(text_array)
            # Determine damage
            Student1.bars -= Student2.attack
            Student1.health = ""

            # Add back bars plus defense boost
            for j in range(int(Student1.bars+.1*Student1.defense)):
                Student1.health += "="

            pygame.time.wait(1)
            # Print the health of each Student
            text_array = [f"{Student1.name}    HLTH  {Student1.health}",
                          f"{Student2.name}    HLTH   {Student2.health}"]
            App.draw_text(text_array)
            pygame.time.wait(1)

            # Check to see if Student fainted
            if Student1.bars <= 0:
                text_array = [f"... {Student1.name} fainted."]
                App.draw_text(text_array)
                break

    def run(self,student1, student2):
        App.draw_bg()
        
        """
        Run the main event loop.
        """
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
            App.actual_screen.blit(App.simulation_screen, (0,0))
            App.actual_screen.blit(App.interface_screen, (0,460))
            pygame.display.flip()
            App.fight(student1,student2)
            #pygame.display.update()

        pygame.quit()
