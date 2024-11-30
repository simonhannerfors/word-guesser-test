import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guessit!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 35)

# Load words from a file
def load_word_bank(file_path="words.txt"):
    try:
        with open(file_path, "r") as file:
            return [line.strip().lower() for line in file if len(line.strip()) == 5]
    except FileNotFoundError:
        print("Error: 'words.txt' not found. Using a default word list.")
        return ["apple", "berry", "grape", "peach", "lemon"]

# Display text on the screen
def draw_text(text, x, y, color=BLACK, font=font):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

# Main game function
def play_game():

    word_bank = load_word_bank()
guessed_words = []
max_turns = 6
current_turn = 1
input_text = ""
game_over = False
feedback = ""

    # Game loop

running = True
while running:
    screen.fill(WHITE)  # Clear screen

    # Draw the game state
    draw_text("Guessit!", WIDTH // 2 - 100, 20, font=font, color=RED)
    draw_text(f"Turn: {current_turn}/{max_turns}", 20, 80)

    # Display the word with correctly guessed letters in place
    displayed_word = " ".join([ch if ch in guessed_words else "_" for ch in active_word])
    draw_text("Word: " + displayed_word, 20, 150)

    draw_text("Guessed Words: " + ", ".join(guessed_words), 20, 220, font=small_font)

    if game_over:
        draw_text(feedback, 20, 300, color=GREEN if active_word in guessed_words else RED)
        draw_text("Press R to restart or Q to quit.", 20, 400, font=small_font)
    else:
        draw_text("Type your guess:", 20, 300)
        draw_text(input_text, 20, 350, font=small_font)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:  # Restart the game
                    active_word = random.choice(word_bank)
                    guessed_words = []
                    current_turn = 1
                    input_text = ""
                    game_over = False
                    feedback = ""
                if event.key == pygame.K_q:  # Quit the game
                    running = False
            else:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(input_text) == 5 and input_text.isalpha():
                        if input_text in guessed_words:
                            feedback = "You already guessed that!"
                        else:
                            guessed_words.append(input_text)
                            # Check for correct word
                            if input_text == active_word:
                                feedback = "Congratulations! You guessed the word!"
                                game_over = True
                            else:
                                current_turn += 1
                                if current_turn > max_turns:
                                    feedback = f"Game Over! The word was '{active_word}'."
                                    game_over = True
                                else:
                                    feedback = "Incorrect! Try again."
                    else:
                        feedback = "Please enter a valid 5-letter word."
                    input_text = ""
                else:
                    if len(input_text) < 5 and event.unicode.isalpha():
                        input_text += event.unicode

    pygame.display.flip()  # Update the screen




