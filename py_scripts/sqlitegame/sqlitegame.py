import sqlite3, random

# Verbindung zur DB aufbauen
conn = sqlite3.connect("game.db")


def write_guess(guess, correct):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO guess(guess, correct) VALUES (?, ?);", (guess, correct))
    conn.commit()

def get_guess():
    while True:
        try:
            guess = int(input("Please guess a number between 1 and 100 \n"))
            return guess
        except Exception as e:
            print("Something went wrong, please guess again")
            pass

def game_loop():
    continue_playing = True
    while continue_playing:
        winning_num = random.randint(0, 100)
        print(winning_num, " IS NUM")
        print("Advanced AI chose a random number between 1 and 100.... \n")
        while True:
            curr_guess = get_guess()
            write_guess(curr_guess, curr_guess == winning_num)
            if curr_guess == winning_num:
                print("YOU WON!!!")
                break
        continue_playing = input("Continue playing (y/n)? \n") == "y"

game_loop()




