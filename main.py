from random import randint
from Data import data
from Art import logo
from Art import vs


def game_body():
    data1 = data[randint(0, 49)]
    data2 = data[randint(0, 49)]
    global score
    if data1 != data2:
        print(f"{logo}\nA - {data1['name']}, {data1['description']} and {data1['country']}\n{vs}\n"
              f"B - {data2['name']}, {data2['description']} and {data2['country']}\nYour score is score : {score}.")
        popular = input("Who is the most popular? A or B.\n").upper()
        if popular == "A" and data1['follower_count'] > data2['follower_count']:
            score += 1
            print(f"You right! Your score is score : {score}.")
            game_body()
        elif popular == "A" and data1['follower_count'] < data2['follower_count']:
            print("You wrong!")
        elif popular == "B" and data1['follower_count'] > data2['follower_count']:
            print("You wrong!")
        elif popular == "B" and data1['follower_count'] < data2['follower_count']:
            score += 1
            print(f"You right! Your score is score : {score}.")
            game_body()
    else:
        print("Sorry for same cele. Please try again!")
        game_body()


start = True
while start:
    score = 0
    game = input("Do you want to start the game? Yes(y) or No(n).\n")
    if game == "y":
        game_body()
    elif game == "n":
        start = False
    else:
        print("You have wrong typing. Please try again!")
        pass