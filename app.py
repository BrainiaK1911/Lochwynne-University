import pygame
from pygame.locals import *

class Text:
    """
    Create a text object.
    """

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
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
        
    
    def battle_system(text):
        my_text = Text(text, pos = (0, 0))
        my_text.draw()
        
    def draw_bg():
        """
        Function for drawing background
        """            
        #background image
        background_img = pygame.image.load('images/gates.png').convert_alpha()
        App.simulation_screen.blit(background_img, (0, 0))

    def run(self):
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
            
            pygame.display.update()

        pygame.quit()
