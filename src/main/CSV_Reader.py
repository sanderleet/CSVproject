import csv

# using nested lists, instead numPy


teh_filepath = "simpleEX1.csv"


def print_column(row):
    for item in row:
        print(item)


def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=", ")
        print()


# From Matrix, return an array, of the Column with the Header name.


def return_column_from_matrix_as_array(victim_matrix, victim_header):
    header_index = victim_matrix[0].index(victim_header)
    returning_array = []
    for rows in victim_matrix:
        returning_array.append(rows[header_index])
    return returning_array


def append_column_into_matrix(victim_matrix, victim_column):
    if victim_matrix == []:
        buffer_matrix = [[]for item in range(len(victim_column))]
    else:
        buffer_matrix = victim_matrix
    print(buffer_matrix)
    for index, row in enumerate(victim_column):
        buffer_matrix[index].append(victim_column[index])
    return buffer_matrix


def return_column_from_csv(file_path, victim_header):
    pass


# Create a matrix from .csv file


def return_matrix_from_csv(file_path):
    if file_path[-4:] != ".csv":
        print("File Error\n Are you sure '{File_path}' is correct? \n Press y or n ".format(File_path=file_path))
        if str(input("choice: ")) == "n":
            print("Ending")
            return

    scanning_rows = csv.reader(open(file_path))
    return_matrix = []

    for row in scanning_rows:
        return_matrix_row = []
        for item in row:
            return_matrix_row.append(item)
        return_matrix.append(return_matrix_row)
    return return_matrix


def construct_new_matrix_by_columns(victim_matrix):
    buffer_matrix = []
    while True:
        victim_header = str(input("Give Column Name: "))
        victim_column = return_column_from_matrix_as_array(victim_matrix, victim_header)
        buffer_matrix = append_column_into_matrix(buffer_matrix,victim_column)

        if str(input("Add more Columns?\nYes or No: ")) == "no":
            print("Ending")
            return buffer_matrix

