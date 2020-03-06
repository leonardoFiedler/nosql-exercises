import redis

# Assuming the default config
r = redis.Redis(host='localhost', port=6379, db=0)

def get_numbers_list():
    return [x for x in range(1, 100)]

def generate_random_cartela_values(cartela_key):
    numbers = get_numbers_list()
    r.sadd("numbers", numbers)
    generated_cartela = r.srandmember("numbers", number=15)
    
    

'''
Generates all the cards.
N - number of cards. Default: 50.
'''
def generate_cards(N=50):
    
    for i in range(0, N):
        cartela = f"{i:02d}"
        name = f"user:{cartela}"
        user_name = f"user{cartela}"
        cartela_name = f"cartela:{cartela}"
        score_name = "score:00"

        # print(cartela)
        # print(name)
        r.hset(name, "name", user_name)
        r.hset(name, "bcartela", cartela_name)
        r.hset(name, "bscore", score_name)

        generate_random_cartela_values(cartela_key)


if __name__ == "__main__":
    generate_cards()
