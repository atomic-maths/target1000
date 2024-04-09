import random
from dice import roll_dice
from grid import Grid
from strategy import auto_pick_position

def debug(msg, show_debug):
	if(show_debug):
			print(msg)

def run_game(show_debug):
	grid = Grid()
	
	while not grid.is_complete():
		roll = roll_dice()
		debug("Rolled a " + str(roll), show_debug)
		auto_pick_position(roll, grid)
		
	score = grid.score_complete_grid()
	if(show_debug): grid.pretty_print()
	return score


def benchmark(runs):   
	i=0
	score_total=0
	
	while i < runs:
		i+=1
		score = run_game(False)
		score_total+=score

	print("\n")  
	print("benchmark = " + str(score_total/runs)) 

def main():
	benchmark_runs = 100000
	option = int(input("Would you like to (1) show a debug or (2) run a benchmark? "))
	if (option==2): return benchmark(benchmark_runs)
	
	print("Score was ", run_game(True))
	 
	 
if __name__ == "__main__":
		main()

