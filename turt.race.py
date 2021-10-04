import turtle
import random
#player one establish
player_1=turtle.Turtle()
player_1.color("red")
player_1.shape("turtle")
player_1.penup()
player_1.goto(-200,100)
#player two establish
player_2 = player_1.clone()
player_2.color("blue")
player_2.penup()
player_2.goto(-200,-100)
#player one setup
player_1.goto(300,100)
player_1.rt(90)
player_1.fd(60)
player_1.lt(90)
player_1.pendown()
player_1.circle(40)
player_1.penup()
player_1.goto(-200,100)
#player two setup
player_2.goto(300,-100)
player_2.rt(90)
player_2.fd(60)
player_2.lt(90)
player_2.pendown()
player_2.circle(40)
player_2.penup()
player_2.goto(-200,-100)
die = [1,2,3,4,5,6] #....die declare/////
player_2.pendown()
player_1.pendown()
print("player 1 is red")
print("player 2 is blue")
for i in range(20):
    if player_1.pos() >= (300,100):
        print("Player 1 Wins!")
        break
    elif player_2.pos() >= (300,-100):
        print("Player 2 Wins!")
        break
    else:
        player_1_turn = input("Press 'Enter' to roll the die (player 1) ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ",die_outcome)
        print("The number of steps will be: ",20*die_outcome)
        player_1.fd(20*die_outcome)
        player_2_turn = input("Press 'Enter' to roll the die (player 2) ")
        d = random.choice(die)
        print("The result of the die roll is: ",die_outcome)
        print("The number of steps will be: ",20*die_outcome)
        player_2.fd(20*die_outcome)
