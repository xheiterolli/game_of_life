import time
import numpy as np
import os

def print_title_card():
    space = "                                                                           "
    title = space + "  _____                      ___  __   _ ___   \n" + space + " / ___/__ ___ _  ___   ___  / _/ / /  (_) _/__ \n" + space + "/ (_ / _ `/  ' \/ -_) / _ \/ _/ / /__/ / _/ -_)\n" + space + "\___/\_,_/_/_/_/\__/  \___/_/  /____/_/_/ \__/ \n"
    os.system("cls")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(title)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def update_frame(arr):

    new_arr = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]

    for i, row in enumerate(arr):
        for j, item in enumerate(row):
            new_arr[i][j] = arr[i][j]

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
    # os.system("cls")

    for x in arr:
        for y in x:
            if y == 0:
                print('  ', end='')
            else:
                print('██', end='')
                # print(' 1', end='')

        print()

def print_glider(arr):

    #   ██
    #     ██
    # ██████

    i = 5
    arr[0 + i][1 + i] = 1
    arr[1 + i][2 + i] = 1
    arr[2 + i][0 + i] = 1
    arr[2 + i][1 + i] = 1
    arr[2 + i][2 + i] = 1

def print_stable(arr):

    # ████
    #   ████
    #     ██

    i = 5
    arr[0 + i][0 + i] = 1
    arr[0 + i][1 + i] = 1
    arr[1 + i][1 + i] = 1
    arr[1 + i][2 + i] = 1
    arr[2 + i][2 + i] = 1

def print_preset(val):

    arr = [[0 for i in range(100)] for j in range(50)]

    if val == 1:
        print_glider(arr)
    elif val == 2:
        print_stable(arr)
    elif val == 3:
        arr = np.random.randint(2, size=(50, 100))

    show_frame(arr)

    for _ in range(10000):
        time.sleep(.07)
        print_title_card()
        arr = update_frame(arr)
        show_frame(arr)

print_title_card()
print("1. Glider")
print("2. Stable Community")
print("3. Random Generation")
val = input("Choose a preset: ")
print_preset(int(val))
