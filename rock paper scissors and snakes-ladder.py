import time
import random
import sys
print('WELCOME TO THE WORLD OF GAMES.')
print('___________________________________________________')
time.sleep(1)
print('Which game you want to play?')
choice = input('Enter: 1 for Rock, Paper and Scissors; 2 for Snakes and Ladders ->')
print('Starting the game...')
time.sleep(1)

if choice == '1':
    print('Welcome to the ROCK | PAPER | SCISSORS')
    print('-----------------------------------------------')
    print('You have three turns to play the game.')
    turns = 3
    while turns > 0:
        index = 3-turns
        print('Choose your hand:')
        print('0 for ROCK, 1 for PAPER, 2 for SCISSORS')
        user_score = [0,0,0]
        comp_score = [0,0,0]
        yourTurn = input('Your hand ->')
        computerTurn = str(random.randint(0,2))
        if yourTurn == '0':
            userHand = 'ROCK'
        elif yourTurn == '1':
            userHand = 'PAPER'
        else:
            userHand = 'SCISSORS'
        if computerTurn == '0':
            compHand = 'ROCK'
        elif computerTurn == '1':
            compHand = 'PAPER'
        else:
            compHand = 'SCISSORS'
        print('Your hand ->'+userHand)
        print('Computer hand ->'+compHand)
        print('Calculating score...')
        time.sleep(1)
        if yourTurn == '0':
            if computerTurn == '1':
                print('Oops! You lose this round')
                comp_score[index] = 1
                user_score[index] = 0
            elif computerTurn == '2':
                print('Hurray! You won this round')
                comp_score[index] = 0
                user_score[index] = 1
            else:
                print('Round draw')
                comp_score[index] = 0
                user_score[index] = 0
                
        elif yourTurn == '1':
            if computerTurn == '1':
                print('Round draw')
                comp_score[index] = 0
                user_score[index] = 0
            elif computerTurn == '2':
                print('Oops! You lose this round')
                comp_score[index] = 1
                user_score[index] = 0
            else:
                print('Hurray! You won this round')
                comp_score[index] = 0
                user_score[index] = 1
        elif yourTurn == '2':
            if computerTurn == '1':
                print('Hurray! You won this round')
                comp_score[index] = 0
                user_score[index] = 1
            elif computerTurn == '2':
                print('Round Draw')
                comp_score[index] = 0
                user_score[index] = 0
            else:
                print('Oops! You lose this round')
                comp_score[index] = 1
                user_score[index] = 0
        turns -= 1
    print('Calculating final scores...')
    time.sleep(1)
    scored_user = sum(user_score)
    scored_comp = sum(comp_score)
    print("You scored: "+str(scored_user))
    print("Computer scored: "+str(scored_comp))
    if scored_user > scored_comp:
        print('Hurray! You won the game.')
    elif scored_user < scored_comp:
        print('Oops! You lost the game')
    else:
        print('Game draw')
elif choice == '2':
    

    # just of effects. add a delay of 1 second before performing any action
    SLEEP_BETWEEN_ACTIONS = 1
    MAX_VAL = 100
    DICE_FACE = 6

    # snake takes you down from 'key' to 'value'
    snakes = {
        8: 4,
        18: 1,
        26: 10,
        39: 5,
        51: 6,
        54: 36,
        56: 1,
        60: 23,
        75: 28,
        83: 45,
        85: 59,
        90: 48,
        92: 25,
        97: 87,
        99: 63
    }

    # ladder takes you up from 'key' to 'value'
    ladders = {
        3: 20,
        6: 14,
        11: 28,
        15: 34,
        17: 74,
        22: 37,
        38: 59,
        49: 67,
        57: 76,
        61: 78,
        73: 86,
        81: 98,
        88: 91
    }

    player_turn_text = [
        "Your turn.",
        "Go.",
        "Please proceed.",
        "Lets win this.",
        "Are you ready?",
        "",
    ]

    snake_bite = [
        "boohoo",
        "bummer",
        "snake bite",
        "oh no",
        "dang"
    ]

    ladder_jump = [
        "woohoo",
        "woww",
        "nailed it",
        "oh my God...",
        "yaayyy"
    ]


    def welcome_msg():
        msg = """
        Welcome to Snake and Ladder Game.
    

        Rules:
          1. Initally both the players are at starting position i.e. 0. 
             Take it in turns to roll the dice. 
             Move forward the number of spaces shown on the dice.
          2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
          3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
          4. The first player to get to the FINAL position is the winner.
          5. Hit enter to roll the dice.

        """
        print(msg)


    def get_player_names():
        player1_name = None
        while not player1_name:
            player1_name = input("Please enter a valid name for first player: ").strip()

        player2_name = None
        while not player2_name:
            player2_name = input("Please enter a valid name for second player: ").strip()

        print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
        return player1_name, player2_name


    def get_dice_value():
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        dice_value = random.randint(1, DICE_FACE)
        print("Its a " + str(dice_value))
        return dice_value


    def got_snake_bite(old_value, current_value, player_name):
        print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


    def got_ladder_jump(old_value, current_value, player_name):
        print("\n" + random.choice(ladder_jump).upper() + " ########")
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


    def snake_ladder(player_name, current_value, dice_value):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            got_snake_bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            got_ladder_jump(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value


    def check_win(player_name, position):
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        if MAX_VAL == position:
            print("\n\n\nThats it.\n\n" + player_name + " won the game.")
            print("Congratulations " + player_name)
            print("\nThank you for playing the game.\n\n")
            sys.exit(1)


    def start():
        welcome_msg()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        player1_name, player2_name = get_player_names()
        time.sleep(SLEEP_BETWEEN_ACTIONS)

        player1_current_position = 0
        player2_current_position = 0

        while True:
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player1_name + " moving....")
            player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

            check_win(player1_name, player1_current_position)

            input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player2_name + " moving....")
            player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

            check_win(player2_name, player2_current_position)


    if __name__ == "__main__":
        start()


    
