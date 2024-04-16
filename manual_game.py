from dice import roll_dice
from grid import Grid


def game():
	grid = Grid()

	while not grid.is_complete():
		print("\nRolling the dice...")
		roll = roll_dice()
		print("You rolled a", roll)
		print("Choose where to place the number")
		grid.pretty_print()
		x, y = manually_pick_position(roll, grid)
		grid.set_value(x, y, roll)

	score = grid.score_complete_grid()
	print("You scored: " + str(score))


def manually_pick_position(roll, grid):
	def get_x_y():
		x = int(input("Enter x value 0-2: "))
		y = int(input("Enter y value 0-2: "))
		return x, y

	x, y = get_x_y()
	while grid.has_value_been_set(x, y):
		print("You cannot place a number on a cell that already has a number")
		print("You rolled a", roll)
		x, y = get_x_y()
	return x, y


def main():
	game()


if __name__ == "__main__":
	main()
