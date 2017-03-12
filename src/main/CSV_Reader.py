import csv
# using nested lists, instead numPy


teh_filepath = "simpleEX1.csv"

def print_matrix(matrix):
    pass


# From Matrix, return an array, of the Column with the Header name.


def return_column_from_matrix_as_array(victim_matrix, victim_header):
    header_index = victim_matrix[0].index(victim_header)

    print("Header index: {header}".format(header=header_index))
    returning_array = []
    for rows in victim_matrix:
        returning_array.append(rows[header_index])
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
    scanning_rows = csv.reader(open(file_path))
    return_matrix = []

    for row in scanning_rows:
        return_matrix_row = []
        for item in row:
            return_matrix_row.append(item)
        return_matrix.append(return_matrix_row)
    return return_matrix


print(return_matrix_from_csv(teh_filepath))
print(return_column_from_matrix_as_array(return_matrix_from_csv(teh_filepath), "pop2010"))

