import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter elements of {name} row by row:")
    data = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        data.append(row)

    return np.array(data)


def print_matrix(name, matrix):
    print(f"\n{name}:")
    print(matrix)


def main():
    print("=== MATRIX OPERATIONS TOOL ===")

    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")

    while True:
        print("\n--- MENU ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Transpose A")
        print("5. Transpose B")
        print("6. Determinant A")
        print("7. Determinant B")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            if A.shape == B.shape:
                result = A + B
                print_matrix("A + B", result)
            else:
                print("Matrices must have same dimensions")

        elif choice == "2":
            if A.shape == B.shape:
                result = A - B
                print_matrix("A - B", result)
            else:
                print("Matrices must have same dimensions")

        elif choice == "3":
            if A.shape[1] == B.shape[0]:
                result = np.dot(A, B)
                print_matrix("A x B", result)
            else:
                print("Matrix multiplication not possible")

        elif choice == "4":
            print_matrix("Transpose of A", A.T)

        elif choice == "5":
            print_matrix("Transpose of B", B.T)

        elif choice == "6":
            if A.shape[0] == A.shape[1]:
                print("Determinant of A:", np.linalg.det(A))
            else:
                print("A is not square matrix")

        elif choice == "7":
            if B.shape[0] == B.shape[1]:
                print("Determinant of B:", np.linalg.det(B))
            else:
                print("B is not square matrix")

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
    
