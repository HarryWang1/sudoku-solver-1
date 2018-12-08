"""
    Given the elements and the grid size, this class helps in printing the sudoku
"""


class PrintSudoko:
    def __init__(self, elements, grid_size):
        self.grid_size = grid_size
        self.row = grid_size * grid_size

        output_string = ""

        for i in range(self.row):
            for j in range(self.row):
                number = elements[i][j]

                output_string += str(number) + self.__padding(number)  # the number and the padding it should get
                output_string += self.__get_cutoff_string(j, " ")  # separate grids horizontally

            output_string += self.__get_cutoff_string(i, "\n")  # separate grids vertically

        output_string = output_string[:len(output_string)-4]  # remove the two trailing "\n"

        print(output_string)

        # write to a file
        # f = open("sa.txt", "w")
        # f.write(output_string)


    def __get_cutoff_string(self, i, string):
        if self.__cutoff_grid(i):
            return string * 2
        else:
            return string

    def __cutoff_grid(self, i):
        i += 1

        if i % self.grid_size == 0:
            return True
        else:
            return False

    def __padding(self, number):
        # length of the number, 16 => 2, 225 => 3
        max_count = len(str(self.row))
        number_count = len(str(number))

        difference = max_count - number_count

        blank_space = " " * difference
        return blank_space



# Testing

# testing with a 2x2 grid
elements12 = [1,2] * 2
elements22 = [3,4] * 2
elements42 = [elements12] + [elements22]
elements_testing2 = elements42 * 2

# testing with a 3x3 grid
elements13 = [1,2,3] * 3
elements23 = [4,5,6] * 3
elements33 = [7,8,9] * 3
elements43 = [elements13] + [elements23] + [elements33]
elements_testing3 = elements43 * 3

# Testing with a 4x4 gridsize
elements14 = [1,2,3,4] * 4
elements24 = [5,6,7,8] * 4
elements34 = [9,10,11,12] * 4
elements44 = [13,14,15,16] * 4
elements54 = [elements14] + [elements24] + [elements34] + [elements44]
elements_testing4 = elements54 * 4

#PrintSudoko(elements_testing2, 2)
#PrintSudoko(elements_testing3, 3)
#PrintSudoko(elements_testing4, 4)

