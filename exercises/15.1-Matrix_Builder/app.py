#Import random

#Create the function below:
def matrixBuilder(rows_and_columns):
    full_matrix_list = []
    row_matrix_list = []
    for row in range(0,rows_and_columns):
        
        for column in range(0, rows_and_columns):
            row_matrix_list.append(1)
        
    
        full_matrix_list.extend([row_matrix_list] * rows_and_columns)
        return full_matrix_list
print(matrixBuilder(5))
