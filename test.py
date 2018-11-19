from random import randint


def print_welcome_message():
    print("Welcome to hangman game, please tell me your name")
    player_name = input()
    print("Hello " + player_name + " I hope that you'll have fun!")

def get_random_word():
    words_file = open("words.txt", "r")
    all_words = words_file.read().split()
    random_index = randint(0, len(all_words)-1)

    random_word = all_words[random_index]
    random_word = random_word.lower()
    return random_word

def read_letter():
    letter = ""
    print("Enter a letter")
    letter = input()
    if len(letter) == 1:
        letter = letter.lower()
    else:
        letter = None

    return letter

def make_display_string(selected_word):
    display_string = []
    for char in selected_word:
        display_string.append("*")
    return display_string

def update_display_string(selected_word, display_string, letters):
    for i, char in enumerate(selected_word):
        if not(char in letters):
            display_string[i] = "*"
        else:
            display_string[i] = selected_word[i]

def draw_screen(display_string, number_of_lives):
    print("Lives left: ", number_of_lives)
    pretty_display = ""
    for char in display_string:
        pretty_display += char + " "
    print(pretty_display)

def player_guessed(selected_word, letter) -> bool:
    if letter in selected_word:
        return True
    return False

def check_win(display_string):
    if "*" in display_string:
        return False
    return True

def main():
    number_of_lives = 5
    player_won = False
    selected_word = get_random_word()
    display_string = make_display_string(selected_word)
    
    

    print_welcome_message()
    letters = set([])

    while number_of_lives > 0 and player_won == False:

        draw_screen(display_string, number_of_lives)
        letter = read_letter()

        if letter == None:
            print("Enter a letter!!!!!!!!!")
            continue
        

        if player_guessed(selected_word, letter):
            letters.add(letter)
            update_display_string(selected_word, display_string, letters)
        else:
            number_of_lives -= 1
        
        if check_win(display_string):
            player_won = True

    if player_won:
        print("Congratulations, you won!")
        print("Word was " + selected_word)

    else:
        print("You lost, better luck next time")    
    print("Word was " + selected_word)
    
    exit()

if __name__ == "__main__":
    main()
    
