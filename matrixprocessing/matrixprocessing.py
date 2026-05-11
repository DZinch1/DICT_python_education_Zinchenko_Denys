class Matrix:
    @staticmethod
    def read_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return None
        new_matrix = Matrix(self.rows, self.cols, self.matrix[:])
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[i][j] += other[i][j]
        return new_matrix

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_matrix = Matrix(self.rows, self.cols, self.matrix[:])
            for row in new_matrix:
                for j in range(self.cols):
                    row[j] *= other
            return new_matrix
        else:
            if self.cols != other.rows:
                return None
            new_matrix = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        new_matrix[i][j] += self[i][k] * other[k][
                            j]
            return new_matrix

    def transpose(self, option):
        if option == 1:
            new_matrix = Matrix(self.cols, self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix[j][i] = self[i][j]
            return new_matrix
        elif option == 2:
            new_matrix = Matrix(self.cols, self.rows)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_row = self.cols - j - 1
                    new_col = self.rows - i - 1
                    new_matrix[new_row][new_col] = self[i][j]
            return new_matrix
        elif option == 3:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                for j in range(self.rows):
                    new_matrix[i][j] = self[i][self.cols - j - 1]
            return new_matrix
        elif option == 4:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                for j in range(self.rows):
                    new_matrix[i][j] = self[self.rows - i - 1][j]
            return new_matrix

    def determinant(self):
        if self.rows != self.cols:
            return None
        if self.rows == 1:
            return self[0][0]
        if self.rows == 2:
            return self[0][0] * self[1][1] - self[1][0] * self[0][1]
        determinant = 0
        for i in range(self.rows):
            determinant += self[0][i] * self.cofactor(0, i)
        return determinant

    def cofactor(self, row, col):
        matrix_copy = [row.copy() for row in self.matrix]
        del matrix_copy[row]
        for i in range(self.rows - 1):
            del matrix_copy[i][col]
        new_matrix = Matrix(self.rows - 1, self.rows - 1, matrix_copy)
        return new_matrix.determinant() * (-1) ** (row + col)

    def inverse(self):
        determinant = self.determinant()
        if determinant is None or determinant == 0:
            return None
        cofactor_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                cofactor_matrix[i][j] = self.cofactor(i, j)
        return cofactor_matrix.transpose() * (1 / determinant)

    def __str__(self):
        string = ""
        for row in self.matrix:
            string += " ".join([str(a) for a in row]) + "\n"
        return string


def get_matrix(size_prompt, matrix_prompt):
    def read_size(prompt):
        while True:
            try:
                parts = input(prompt).split()
                if len(parts) != 2:
                    raise ValueError
                r, c = int(parts[0]), int(parts[1])
                if r <= 0 or c <= 0:
                    raise ValueError
                return r, c
            except ValueError:
                print("Invalid input. Please enter two positive integers separated by space.")

    def read_row(prompt, cols):
        while True:
            user_input = input(prompt).strip().split()
            if len(user_input) != cols:
                print(f"Invalid input. Expected {cols} values.")
                continue
            row = []
            has_float = False
            valid = True
            for tok in user_input:
                try:
                    val = int(tok)
                except ValueError:
                    try:
                        val = float(tok)
                        has_float = True
                    except ValueError:
                        valid = False
                        break
                row.append(val)
            if not valid:
                print("Invalid input. Please enter numeric values.")
                continue
            if has_float:
                row = [float(x) for x in row]
            else:
                row = [int(x) for x in row]
            return row

    rows, cols = read_size(size_prompt)
    print(matrix_prompt)
    matrix = []
    for _ in range(rows):
        matrix.append(read_row(">", cols))
    return Matrix(rows, cols, matrix)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = Matrix.read_int("Your choice: >")

        res = None
        if choice == 0:
            break
        if choice == 1:
            a = get_matrix("Enter size of first matrix: ",
                           "Enter first matrix:")
            b = get_matrix("Enter size of second matrix: ",
                           "Enter second matrix:")
            res = a + b
        elif choice == 2:
            a = get_matrix("Enter size of matrix: ", "Enter matrix:")
            while True:
                s = input("Enter constant: >").strip()
                try:
                    scalar = int(s)
                except ValueError:
                    try:
                        scalar = float(s)
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                        continue
                break
            res = a * scalar
        elif choice == 3:
            a = get_matrix("Enter size of first matrix: ",
                           "Enter first matrix:")
            b = get_matrix("Enter size of second matrix: ",
                           "Enter second matrix:")
            res = a * b
        elif choice == 4:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            Matrix.option = Matrix.read_int("Your choice: >")
            if Matrix.option not in [1, 2, 3, 4]:
                while True:
                    print("Invalid choice. Please select a valid option.")
                    Matrix.option = Matrix.read_int("Your choice: >")
                    if Matrix.option in [1, 2, 3, 4]:
                        break
            a = get_matrix("Enter matrix size: ", "Enter matrix:")
            res = a.transpose(Matrix.option)
        elif choice == 5:
            a = get_matrix("Enter matrix size: ", "Enter matrix:")
            res = a.determinant()
        elif choice == 6:
            a = get_matrix("Enter matrix size: ", "Enter matrix:")
            res = a.inverse()
        if res is None:
            if choice == 6:
                print("This matrix doesn't have an inverse.")
            else:
                print("The operation could not be performed")
        else:
            print("The result is:")
            print(res)


if __name__ == "__main__":
    main()
