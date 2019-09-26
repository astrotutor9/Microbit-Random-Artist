# Write your code here :-)
from microbit import *
from random import randint

# obtain pixel value for an on 9 or off 0
def LED_value():
    LED = randint(0, 1)
    if LED == 1:  # if it is 1 change to 9 (a bright LED)
        return 9
    return LED  # if it is zero then leave as is

# build a number list from values from above
def image_values():
    line = []                  # create an empty list
    for onoff in range(0, 5):  # for each of the 5 LED
        LED = LED_value()      # get either a zero or 9
        line.append(LED)       # build the row of 0/9
    return line                # send line list back

# building a line of text from image_values above
def build_row():
    line = image_values()      # obtain the line list above
    row = ""                   # create an empty string
    for LED in line:           # for each 0/9 convert to string
        row = row + str(LED)   # then add to row string
    return row                 # send string list back

while True:
    rowA = build_row() + ":"  # build first line
    rowB = build_row() + ":"  # build second line
    rowC = build_row() + ":"  # build third line
    rowD = build_row() + ":"  # build fourth line
    rowE = build_row()        # build fifth line without :

    all_rows = (rowA) + (rowB) + (rowC) + (rowD) + (rowE)

    # display the produced image
    random_image = Image(all_rows)
    display.show(random_image)
    print(all_rows)
    sleep(500)
