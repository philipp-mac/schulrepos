import sqlite3, random

# Verbindung zur DB aufbauen
conn = sqlite3.connect("game.db")

def update_data(player_name: str, guesses: int):
    """
    function that writes player data to the database
    :param player_name: name the player gave for themselves
    :param guesses: number of guesses the player needed
    """
    curs = conn.cursor()
    curs.execute("""UPDATE player SET guesses = ? 
                    WHERE player_name = ? AND
                    id=(SELECT MAX(id) from player WHERE player_name=?);""",
                    (guesses, player_name, player_name,))
    conn.commit()

def get_guess():
    """
    function that asks user for a numerical guess from STDIN
    returns: int between 0 and 100
    """
    while True:
        try:
            guess = int(input("Please guess a number between 1 and 100 \n"))
            if guess >= 0 and guess < 101:
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
    # output player data from player with the current name and the highest id
    cursor = conn.cursor()
    cursor.execute("""SELECT * from player WHERE player_name=? AND
                    id=(SELECT MAX(id) from player WHERE player_name=? );""",
                    (player_name, player_name,))
    row = cursor.fetchall()[0]
    print(f"Congrats {row[1]}, you took {row[2]} guesses to guess {row[3]}! \n")
    conn.commit()

    # output highscores
    cursor.execute("SELECT player_name, guesses FROM player ORDER BY guesses ASC")
    rows = cursor.fetchall()
    print("~~~~ The top 10 players are:")
    for r in range(min(len(rows), 10)):
        print(r, " - ", rows[r][0] , f" with {rows[r][1]} guesses! ")

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

            # end execution on correct guess
            if curr_guess == winning_num:
                print("YOU WON!!!")

                # write player data to sqlite database
                update_data(player_name, guesses)

                # finally, output player score and highscores
                end_game(player_name)
                break
                
            else:
                print("Incorrect, please guess again..")


        # Ask user if they want to keep playing
        continue_playing = input("Continue playing (y/n)? \n") == "y"

def prepare_db():
    global player_name, winning_num, player_id

    # 1) Ask player for name
    player_name = str(input("Choose a name: \n"))

    # 2) Generate a random winning number
    winning_num = random.randint(0, 100)
    if input("Wanna cheat? Enter the password?") == "tbs1":
        print(winning_num, " is the winning number")
    print("Advanced AI chose a random number between 1 and 100.... \n")

    # 3) Make entry in db for player's session
    curs = conn.cursor()
    curs.execute("INSERT INTO player (player_name, guesses, correctnumber) VALUES (?, ?, ?)", (player_name, 0, winning_num))
    conn.commit()

prepare_db()
game_loop()