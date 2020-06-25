import random

winscore = 0

losescore = 0

tiescore = 0

def play():
	global winscore, losescore, tiescore
	gameEnd = False
	win = False
	tie = False
	lose = False

	computerChoices = ["Rock", "Paper", "Scissors"]

	computer = random.choice(computerChoices)

	print("Make a choice of rock, paper, or scissors")
	player = input()
	print(computer)
	if computer == "Rock" and player == "paper":
		print("Player wins! Computer chose rock.")
		gameEnd = True
		win = True
		winscore += 1

	elif computer == "Paper" and player == "paper":
		print("Tie! Computer chose paper.")
		gameEnd = True
		tie = True
		tiescore += 1

	elif computer == "Scissors" and player == "paper":
		print("Computer wins! Computer chose scissors.")
		gameEnd = True
		lose = True
		losescore += 1

	elif computer == "Rock" and player == "rock":
		print("Tie! Computer chose paper.")
		gameEnd = True
		tie = True
		tiescore += 1

	elif computer == "Paper" and player == "rock":
		print("Computer wins! Computer chose scissors.")
		gameEnd = True
		lose = True
		losescore += 1

	elif computer == "Scissors" and player == "rock":
		print("Player wins! Computer chose rock.")
		gameEnd = True
		win = True
		winscore += 1

	elif computer == "Scissors" and player == "scissors":
		print("Tie! Computer chose paper.")
		gameEnd = True
		tie = True
		tiescore += 1

	elif computer == "Rock" and player == "scissors":
		print("Computer wins! Computer chose scissors.")
		gameEnd = True
		lose = True
		losescore += 1

	elif computer == "Paper" and player == "scissors":
		print("Player wins! Computer chose rock.")
		gameEnd = True
		win = True
		winscore += 1

while True:
	play()