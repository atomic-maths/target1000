import random


def roll_dice():
	return random.randint(1, 6)


def main():
	rolls = int(input("How many rolls would you like printed? "))
	i = 0
	while i < rolls:
		print(roll_dice())
		i += 1


if __name__ == "__main__":
	main()
