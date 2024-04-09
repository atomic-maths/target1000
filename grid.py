import random

class Grid:
    
    def __init__(self):
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def pretty_print(self):
        h_line = '+---+---+---+'
        for row in self.grid:
            print(h_line)
            print('|', end='')
            for cell in row:
                print(f' {cell} |', end='')
            print()  # Newline at the end of the row
        print(h_line)


    def cartesian_to_array(self, x, y):
        row = 2 - y
        col = x
        return row, col


    def is_complete(self):
        return self.number_filled_cells() == 9
        

    def score_complete_grid(self):
        if not self.is_complete():
            raise Exception("Grid is incomplete!")
        total = 0
        for row in self.grid:
            row_total = row[0] * 100 + row[1] * 10 + row[2]
            total += row_total
        return total-1000
    
    def is_grid_empty(self):
        return self.number_filled_cells()==0


    def number_filled_cells(self):
        filled = 0
        for row in self.grid:
            for cell in row:
                if cell > 0:
                    filled+=1
        return filled
    
    def set_value(self, x, y, val):
        if self.has_value_been_set(x,y):
            raise Exception("Cannot overwrite value")
        row, col = self.cartesian_to_array(x, y)
        self.grid[row][col] = val

    
    def has_value_been_set(self, x, y):
        row, col = self.cartesian_to_array(x, y)
        return self.grid[row][col] != 0
    
    
    def fill_next_empty_space(self, val):
        col = 2
        while col > -1:
            row = 0
            while row < 3:
                if(self.grid[row][col] == 0):
                    self.grid[row][col] = val
                    return
                row+=1
            col-=1

    
    def get_value(self, x, y):
        row, col = self.cartesian_to_array(x, y)
        return self.grid[row][col]
    
    
    def eval_last_column(self):
        return sum([val[2] for val in self.grid])
    

    def eval_mid_column(self):
        return sum([val[1] for val in self.grid])
    

    def eval_first_column(self):
        return sum([val[0] for val in self.grid])


def main():
   grid = Grid()
   grid.set_value(2,2,6)
   grid.pretty_print()


if __name__ == "__main__":
    main()

