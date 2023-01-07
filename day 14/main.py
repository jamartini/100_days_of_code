import art
import game_data
import random

print(art.logo)
def get_A_index():
    A_index = random.randint(0,len(game_data.data)-1)
    return A_index

index_A = get_A_index()

def get_B_index():
    B_index = random.randint(0,len(game_data.data)-1)
    return B_index

index_B = get_B_index()
while index_A == index_B:
    index_B = get_B_index()

def game(a, b):
    print(f"Compare A: {game_data.data[a]['name']}, a {game_data.data[a]['description']}, from {game_data.data[a]['country']}.")
    print(art.vs)
    print(f"Against B: {game_data.data[b]['name']}, a {game_data.data[b]['description']}, from {game_data.data[b]['country']}.")

def answer_verifier(a, b, answer):
    if answer == "A":
        if game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
          return True  
        else:
          return False              
    elif answer == "B":
        if game_data.data[b]['follower_count'] > game_data.data[a]['follower_count']:
            return True
        else:
            return False

game(index_A, index_B)
answer = input("Who has more followers? Type 'A' or 'B': ")
is_correct = answer_verifier(index_A, index_B, answer)
score = 0

while is_correct:
    score += 1
    index_A = index_B
    index_B = get_B_index()
    while index_A == index_B:
        index_B = get_B_index()
    print(art.logo)
    print(f"You're right! Current score: {score}")
    game(index_A, index_B)
    answer = input("Who has more followers? Type 'A' or 'B': ")
    is_correct = answer_verifier(index_A, index_B, answer)

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")  