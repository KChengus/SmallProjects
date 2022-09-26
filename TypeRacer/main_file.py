import readTestFile
import pygame
import sys
import time
class Settings:
    def __init__(self):
        self.window_width = 1000
        self.window_height = 600
        self.colors = {"BLACK": (0, 0, 0), "WHITE": (224, 224, 244), "ORANGE": (250, 145, 8), "GREEN": (58, 203, 58),
                       "DARK_GRAY": (89, 101, 139), "LIGHT_GRAY": (202, 205, 216), "GRAY": (64, 64, 64)}
        font_change = 5 / 3
        self.your_text_size = 20
        self.text_size = int(self.your_text_size * font_change)# the font you want * the font_change will give you the right font size
        self.letter_fit_screen = int(self.window_width / self.your_text_size)
        self.center_letter_width = self.letter_fit_screen // 2
        self.text_style = "monospace"
        self.current_row = 0
        self.rest_rows = self.window_height // (self.your_text_size * 2) - 1 # exclude the current row
        self.single = False

        self.start_timer = 0 # temportary value

        #self.all_words = WordFile().read_content().split()
        self.all_words = readTestFile.words
        #print(self.all_words)
        self.amount_words = 100

        self.clock = pygame.time.Clock()
        self.fps = 100

        self.pause = True

        self.space_ascii = 32
        self.move_back = 0
        self.animation = False

        self.numbers_with_shift = {"1" : "!", "2": "\"", "3": "#", "4": "¤", "5": "%", "6":"&", "7":"/", "8":"(","9":")", "0":"="}
        # uk keyboard to swedish translation
        self.special_character_convergence = {"-": "+", ";":"ö","\'":"ä", "[":"å","\\":"\'","/":"-"}
        self.characters_with_shift = {
                                      'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
                                      'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
                                      'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
                                      'y': 'Y', 'z': 'Z', 'å': 'Å', 'ä': 'Ä', 'ö': 'Ö', "1" : "!", "2": "\"", "3": "#",
                                      "4": "¤", "5": "%", "6":"&", "7":"/", "8":"(","9":")", "0":"=", "+": "?",
                                      "." : ":", "," : ";", "-" : "_", "\'" : "*"
                                      }
class TypeRacer(Settings):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.running = False
        # text
        pygame.font.init()
        self.myfont = pygame.font.SysFont(self.text_style, self.text_size)
        #self.text_position = self.center_letter_width
        self.text_position = 0
    def reset(self):

        self.running = True
        self.current_key = " "
        #previous_words = " " * self.center_letter_width  # the previous words in the beginning are empty (only spaces)
        #self.words = previous_words + " ".join(self.all_words)
        self.words = " ".join(self.all_words)

    def main(self):
        self.reset()
        while self.running:
            self.handle_event()
            self.display() # last
            self.clock.tick(self.fps)

        print("Closing")
    def display(self):
        self.screen.fill(self.colors["DARK_GRAY"])
        self.display_text()
        pygame.display.update()

    def display_text(self):
        if self.text_position >= len(self.words): # if the writer has written all the words on screen
            final_time = time.time() - self.start_timer
            print("Timer:",round(final_time), 's')
            print("Word count:", len(self.words.split()))
            print("WPM:", round(len(self.words.split()) / (final_time / 60)) )
            self.running = False
        else:
            self.current_key = self.words[self.text_position]
            if self.single:
                self.display_single_line()
            else:
                self.display_multiple_lines()

    def display_single_line(self):
        # display previous words
        previous_textsurface = self.myfont.render(self.words[self.text_position - self.center_letter_width: self.text_position], False, self.colors["GRAY"],self.colors["DARK_GRAY"])

        # display current letter
        current_textsurface = self.myfont.render(self.current_key, False, self.colors["GREEN"], self.colors["WHITE"])

        # display next words
        next_textsurface = self.myfont.render(
            self.words[self.text_position + 1: self.text_position + self.center_letter_width], False,
            self.colors["LIGHT_GRAY"], self.colors["DARK_GRAY"])

        if self.animation:
            self.move_back += int(self.your_text_size / 20)
            if self.move_back >= self.your_text_size:
                self.animation = False
        # show text on screen
        self.screen.blit(previous_textsurface, (0 - self.move_back, 200))
        self.screen.blit(current_textsurface, (self.center_letter_width * self.your_text_size - self.move_back, 200))
        self.screen.blit(next_textsurface, ((self.center_letter_width + 1) * self.your_text_size - self.move_back, 200))

    def display_multiple_lines(self):
        if self.text_position % self.letter_fit_screen == 0:
            self.current_row = self.text_position // self.letter_fit_screen

        #finished words
        fin_letter = self.myfont.render(self.words[self.letter_fit_screen * self.current_row:self.text_position], False, self.colors["GREEN"], self.colors["DARK_GRAY"])
        self.screen.blit(fin_letter, (0, 0))

        #current letter
        cur_letter = self.myfont.render(self.words[self.text_position], False, self.colors["ORANGE"], self.colors["DARK_GRAY"])
        self.screen.blit(cur_letter, (self.text_position % self.letter_fit_screen * self.your_text_size, 0))


        #current unfinished row
        text = self.myfont.render(self.words[self.text_position + 1:self.letter_fit_screen * (self.current_row + 1)], False,  self.colors["LIGHT_GRAY"],self.colors["DARK_GRAY"])
        self.screen.blit(text, ((self.text_position + 1) % self.letter_fit_screen * self.your_text_size, 0))


        # rest of the rows
        for row in range(1, self.rest_rows + 1): # current row start at number 0
            text = self.myfont.render(self.words[self.letter_fit_screen * (row + self.current_row) : self.letter_fit_screen * ((row + self.current_row) + 1)], False, self.colors["LIGHT_GRAY"], self.colors["DARK_GRAY"])
            self.screen.blit(text, (0, self.your_text_size * 2 * row))

        pygame.draw.line(self.screen, self.colors["BLACK"], (self.text_position % self.letter_fit_screen * self.your_text_size, 2 * self.your_text_size), ((self.text_position % self.letter_fit_screen + 1) * self.your_text_size,2 * self.your_text_size), 5)


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.pause:
                    # start timer
                    self.start_timer = time.time()

                    self.pause = False
                all_keys = pygame.key.get_pressed()
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                    break
                pressed_key = chr(event.key)

                if pressed_key in self.special_character_convergence:
                    pressed_key = self.special_character_convergence[pressed_key]
                if (all_keys[pygame.K_LSHIFT] or all_keys[pygame.K_RSHIFT]):
                    if pressed_key not in self.characters_with_shift:
                        break
                    pressed_key = self.characters_with_shift[pressed_key]
                    print(pressed_key)
                if pressed_key == self.current_key:
                    #right key pressed
                    self.move_back = 0
                    self.animation = True
                    self.text_position += 1

                if event.key == pygame.K_BACKSPACE:
                    self.text_position -= 1

if __name__ == "__main__":
    TypeRacer().main()