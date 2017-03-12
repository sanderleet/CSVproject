import csv
# using nested lists, instead numPy


teh_filepath = "simpleEX1.csv"

def print_matrix(matrix):
    pass


# From Matrix, return an array, of the Column with the Header name.


def return_column_from_matrix_as_array(victim_matrix, victim_header):
    header_index = 0
    for item in range(len(victim_matrix[0])):
        if victim_matrix[0][item] == victim_header:
            header_index = item
    returning_array = len(victim_matrix)
    for items in range(len(victim_matrix[header_index])):
        returning_array[items] = victim_matrix[header_index][items]
    return returning_array


def return_column_from_csv(file_path, victim_header):
    pass

# Create a matrix from .csv file


def return_matrix_from_csv(file_path):
    # check for file

    if file_path[-4:] != ".csv":
        print("File Error\n Are you sure '{File_path}' is correct? \n Press y or n ".format(File_path=file_path))
        if str(input("choice: ")) == "n":
            print("Ending")
            return
    print("Good path")
    matrix_rows = 0
    matrix_columns = 0
    print("Counting Rows and columns...")
    scanning_rows = csv.reader(open(file_path))

    for row in scanning_rows:
        if matrix_rows == 1:
            for items in row:
                matrix_columns += 1
        matrix_rows += 1

    print("Rows: {rows} \nColumns: {columns}".format(rows=matrix_rows, columns=matrix_columns))
    print("\nConstructing a matrix, a nested list...")






return_matrix_from_csv(teh_filepath)

