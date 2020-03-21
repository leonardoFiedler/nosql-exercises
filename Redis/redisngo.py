import redis

# Assuming the default config
r = redis.Redis(host='localhost', port=6379, db=0)

NUMBERS_LIST_NAME = "numbers"

def get_numbers_list():
    '''
        Returns the range list of values [0, 99]
    '''
    return [x for x in range(1, 100)]

def generate_set_number():
    '''
        Generates the set of numbers to use in cards values
    '''

    numbers = get_numbers_list()
    r.sadd(NUMBERS_LIST_NAME, *numbers)

def generate_random_cartela_values(cartela_key):
    '''
        Generate the random list of cards with 15 values to each cards.
    '''
    generated_cartela = r.srandmember(NUMBERS_LIST_NAME, number=15)
    r.rpush(cartela_key, *generated_cartela)

def initialize_score_player(score_key):
    '''
        Initializes the score of the player, based on key passed as parameter.
    '''
    r.set(score_key, 0)

def generate_cards(N=50):
    '''
        Generates all the cards.
        N - number of cards. Default: 50.
    '''
    for i in range(0, N):
        cartela = f"{i:02d}"
        name = f"user:{cartela}"
        user_name = f"user{cartela}"
        cartela_name = f"cartela:{cartela}"
        score_name = f"score:{cartela}"

        r.hset(name, "name", user_name)
        r.hset(name, "bcartela", cartela_name)
        r.hset(name, "bscore", score_name)

        generate_random_cartela_values(cartela_name)
        initialize_score_player(score_name)


def get_number_round():
    '''
        This function pops one value from numbers set and return to be used in game
    '''
    return int(r.spop(NUMBERS_LIST_NAME))

def play_game(N=50):
    '''
        This function implements the game routine

        N - number of players in game
    '''
    round = 0
    winner = False

    while not winner:
        round += 1
        number = get_number_round()
        found_round = []
        print("Current Round: {0}".format(round))
        print("Generated number: {0}".format(number))

        for player in range(0, N):
            cartela = f"{player:02d}"
            name = f"user:{cartela}"
            player_info = r.hgetall(name)
            value_find = r.lrem(player_info[b"bcartela"], 1, number)

            if (value_find > 0):
                found_round.append(name)
                r.incr(player_info[b"bscore"])

                # Verify the en of game after 15 rounds
                if (round > 14):
                    player_score = int(r.get(player_info[b"bscore"]))

                    if (player_score >= 15):
                        winner = True
                        print("Winner is {0}".format(name))
                        break
        
        if (not winner):
            print("Players that got points on this round: {0}".format(",".join(found_round)))
            print("\n")

def clean_data():
    r.flushall()

def initialize():
    clean_data()
    generate_set_number()

if __name__ == "__main__":
    initialize()
    generate_cards()
    play_game()