from os import curdir
import sqlite3, random

# Verbindung zur DB aufbauen
conn = sqlite3.connect("game.db")

def update_data(player_name: str, guesses: int):
    """
    function that writes a guess to the database
    :param guess: integer that the user guessed
    :param bool: if the guess was correct
    """
    curs = conn.cursor()
    curs.execute(f"update player set guesses = ? WHERE player_name = ?", (guesses, player_name))
    conn.commit()

def get_guess():
    """
    Function that asks user for a numerical input
    returns: int between 1 and 100
    """
    while True:
        try:
            guess = int(input("Please guess a number between 1 and 100 \n"))
            if guess > 0 and guess < 101:
                return guess
            else:
                print("Number not between 0 and 100")
                continue
        except Exception as e:
            print("Something went wrong, please guess again")
            pass


def end_game(player_name):
    """
    function that outputs data and highscores on game end
    :param player_name: name of current player
    """
    # output player data
    cursor = conn.cursor()
    cursor.execute("SELECT * from player where player_name = ?", (player_name, ))
    row = cursor.fetchall()[0]
    print(f"Congrats {row[1]}, you took {row[2]} guesses to guess {row[3]}! \n")
    conn.commit()

    # output highscores
    cursor.execute(f"SELECT player_name, guesses FROM player ORDER BY guesses ASC")
    rows = cursor.fetchall()
    print("The top 10 players are: \n")
    for r in range(10):
        print(rows[r][0] , f" with {rows[r][1]} guesses! \n")

    # close database connection
    conn.close()



def game_loop():
    """
    Actual game execution loop
    """
    continue_playing = True
    while continue_playing:
        guesses = 0

        # Loop through guesses 
        while True:
            guesses += 1

            # Call function for user guess input
            curr_guess = get_guess()

            # End execution on correct guess
            if curr_guess == winning_num:
                print("YOU WON!!!")

                # Write guessesto the sqlite database
                update_data(player_name, guesses)
                end_game(player_name)
                break

        # 7) Ask user if they want to keep playing
        continue_playing = input("Continue playing (y/n)? \n") == "y"

def prepare_db():
    global player_name, winning_num, player_id

    # 1) Ask player for name
    player_name = str(input("Choose a name: \n"))

    # 2) Generate a random winning number
    winning_num = random.randint(0, 100)
    print("Advanced AI chose a random number between 1 and 100.... \n")

    # 3) Make entry in db for this playery
    curs = conn.cursor()
    curs.execute("INSERT INTO player (player_name, guesses, correctnumber) VALUES (?, ?, ?)", (player_name, 0, winning_num))
    conn.commit()

prepare_db()
game_loop()