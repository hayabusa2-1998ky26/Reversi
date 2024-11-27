import tkinter
import tkinter.messagebox as mb
import time
import sys
import math
root = tkinter.Tk()
root.title("Reversi")
size = 90
canvas = tkinter.Canvas(width=size * 8, height=size * 8, bg="black")
canvas.pack()

maps = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
# back ground
for y in range(8):
    for x in range(8):
        canvas.create_rectangle(x * size, y * size, x * size + size, y * size + size, fill="green", tag="background")
circle = 0.1
x_list = [2, 6, 2, 6]
y_list = [2, 6, 6, 2]
for i in range(0, 4):
    canvas.create_oval((x_list[i] + circle) * size, (y_list[i] + circle) * size, (x_list[i] - circle) * size, (y_list[i] - circle) * size, fill="black", tag="background")

def screen(maps): # Screening
    global size, player, can
    try: # tkinter includes a Try statement because an error occurs when the window is forcibly terminated.
        canvas.delete("block")
        can_count = 0
        for y in range(8):
            for x in range(8):
                # stone
                filler = "white"
                if maps[y][x] == 1:
                    filler = "black"
                if maps[y][x] == 2:
                    filler = "white"
                if maps[y][x] != 0:
                    canvas.create_oval(x * size, y * size, x * size + size, y * size + size, fill=filler, tag="block")
                ch1, ch2 = check(maps, x, y, player)
                if player == 1:
                    filler = "black"
                if player == 2:
                    filler = "white"
                if ch1:
                    can_size = 0.1
                    canvas.create_oval(x * size + size * (1 - can_size) * 0.5, y * size + size * (1 - can_size) * 0.5, x * size + size * (1 - (1 - can_size) * 0.5), y * size + size * (1 - (1 - can_size) * 0.5), fill=filler, tag="block")
                    can_count += 1
        canvas.update()
        # It runs when there is no place to put it
        if can_count == 0:
            player = 3 - player
            # If it gets skipped twice
            if can == 1:
                return 1
            else:
                can = 1
                return 0
        else:
            if can == 1:
                mb.showinfo("Reversi", "It was skipped because there was no place to put the piece.")
                can = 0
            return 0
    except:
        print("Ended.")
        sys.exit()
def put(maps, x, y): # Putting a stone.
    global size, clicked, player, count
    if y < size * 8 and x < size * 8 and clicked == 1:
        clicked = 0
        put_x, put_y = math.floor(x / size), math.floor(y / size)
        checker, angles = check(maps, put_x, put_y, player)
        if checker:
            maps[put_y][put_x] = player
            maps = hanten(maps, put_x, put_y, angles)
            if player == 1:
                player = 2
            else:
                player = 1
    return maps
def check(maps, x, y, player): # Checking to see if you can place the stone in that location.
    aite =  3 - player
    angles = []
    return1 = False
    y_list = [1, -1, 0, 0, 1, -1, 1, -1]
    x_list = [0, 0, 1, -1, 1, -1, -1, 1]
    if maps[y][x] == 0:
        for j in range(8):
            try:
                if maps[y + y_list[j]][x + x_list[j]] == aite:
                    for i in range(1, 8):
                        try:
                            if maps[y + i * y_list[j]][x + i * x_list[j]] == player:
                                return1 = True
                                angles.append(j + 1)
                                break
                            if maps[y + i * y_list[j]][x + i * x_list[j]] == 0:
                                break
                            if y_list[j] == 1 and y + i == 7:
                                break
                            if y_list[j] == -1 and y - i <= 0:
                                break
                            if x_list[j] == 1 and x + i == 7:
                                break
                            if x_list[j] == -1 and x - i <= 0:
                                break
                        except:
                            break
            except:
                a = 0
        return return1, angles
    else:
        return False, False
def hanten(maps, x, y, angles): # Rotate the stones.
    global player
    aite =  3 - player
    #         ↑,  ↓, →, ←, ┐, └,  ┘,  ┌
    y_list = [1, -1, 0, 0, 1, -1, 1, -1]
    x_list = [0, 0, 1, -1, 1, -1, -1, 1]
    for j in range(8):
        try:
            if j + 1 in angles:
                i = 0
                while True:
                    if y_list[j] == 1 and y + i == 7:
                        break
                    if y_list[j] == -1 and y - i <= 0:
                        break
                    if x_list[j] == 1 and x + i == 7:
                        break
                    if x_list[j] == -1 and x - i <= 0:
                        break
                    i += 1
                    if maps[y + i * y_list[j]][x + i * x_list[j]] == player:
                        break
                    maps[y + i * y_list[j]][x + i * x_list[j]] = player
        except:
            a = 0
    return maps
def on_click(event): # If click
    global mouse_x, mouse_y, clicked
    clicked = 1
    mouse_x, mouse_y = event.x, event.y

# When click
canvas.bind("<Button-1>", on_click)

# values
player = 1
clicked = 0
mouse_x = 0
mouse_y = 0
can = 0

# main loop
while True:
    time.sleep(0.01)
    maps = put(maps, mouse_x, mouse_y)
    stop = screen(maps)
    if stop:
        break

black_count = 0
white_count = 0
for y in range(8):# Counting stone
    for x in range(8):
        if maps[y][x] == 1:
            black_count += 1
        elif maps[y][x] == 2:
            white_count += 1
if black_count > white_count:# Screening winner
    mb.showinfo("Reversi", f"black win!(black:{black_count}, white:{white_count})")
elif white_count > black_count:
    mb.showinfo("Reversi", f"white win!(black:{black_count}, white:{white_count})")
else:
    mb.showinfo("Reversi", "draw!")
sys.exit()