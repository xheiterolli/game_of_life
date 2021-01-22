import time
import numpy as np
import os


def update_frame(arr):
    new_arr = arr.copy()
    for i, row in enumerate(arr):
        for j, item in enumerate(row):
            # print(i, j, item)
            neighbors = 0
            if i > 0:
                if arr[i - 1][j] == 1:
                    neighbors += 1
            if i > 0 and j > 0:
                if arr[i - 1][j - 1] == 1:
                    neighbors += 1
            if i > 0 and j < len(row) - 1:
                if arr[i - 1][j + 1] == 1:
                    neighbors += 1
            if j < len(row) - 1:
                if arr[i][j + 1] == 1:
                    neighbors += 1
            if j > 0:
                if arr[i][j - 1] == 1:
                    neighbors += 1
            if i < len(arr) - 1:
                if arr[i + 1][j] == 1:
                    neighbors += 1
            if i < len(arr) - 1 and j > 0:
                if arr[i + 1][j - 1] == 1:
                    neighbors += 1
            if i < len(arr) - 1 and j < len(row) - 1:
                if arr[i + 1][j + 1] == 1:
                    neighbors += 1

            if arr[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_arr[i][j] = 0
                    # print(i, j, 'If 1')
                    # print(new_arr[i][j])

                    # show_frame(new_arr)

            if arr[i][j] == 0 and neighbors == 3:
                new_arr[i][j] = 1
                # print(i, j, 'If 2')
                # print(new_arr[i][j])
                # print()
                # show_frame(new_arr)
                # print()

            # print(i, j, 'Neighbors: ' + str(neighbors))

    return new_arr


def show_frame(arr):
    os.system("cls")

    for x in arr:
        for y in x:
            if y == 0:
                print('  ', end='')
            else:
                # print('██', end='')
                print(' 1', end='')

        print()


arr = np.random.randint(2, size=(150, 300))
# arr = np.zeros((10, 10))
show_frame(arr)
# print("--------------------------------------------------------")

for _ in range(10000):
    arr = update_frame(arr)
    show_frame(arr)
    # print("--------------------------------------------------------")
    time.sleep(0.0001)
