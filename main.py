import tkinter
import tkinter.messagebox as mb
import time
import random
import sys
import math
root = tkinter.Tk()
root.title("maze")
canvas = tkinter.Canvas(width=1920, height=1020, bg="black")
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
size = 90
def byouga(maps):
    global size, te, yosoku
    canvas.delete("fps", "block")
    yosoku_count = 0
    for y in range(8):
        for x in range(8):
            canvas.create_rectangle(x * size, y * size, x * size + size, y * size + size, fill="green", tag="block")
            filler = "white"
            if maps[y][x] == 0:
                filler = "green"
            if maps[y][x] == 1:
                filler = "black"
            if maps[y][x] == 2:
                filler = "white"
            if maps[y][x] != 0:
                canvas.create_oval(x * size, y * size, x * size + size, y * size + size, fill=filler, tag="block")
            ch1, ch2 = check(maps, x, y, te)
            if te == 1:
                filler = "black"
            if te == 2:
                filler = "white"
            if ch1:
                canvas.create_oval(x * size + size / 4, y * size + size / 4, x * size + size * 0.75, y * size + size * 0.75, fill=filler, tag="block")
                yosoku_count += 1
    if yosoku_count == 0:
        te = 3 - te
        if yosoku == 1:
            return 1
        else:
            yosoku = 1
            return 0
    else:
        if yosoku == 1:
            mb.showinfo("Reversi", "置ける場所がないためスキップされました。")
            yosoku = 0
        return 0
def put(maps, x, y):
    global size, clicked, te, count
    if y < size * 8 and x < size * 8 and clicked == 1:
        clicked = 0
        checker, mukis = check(maps, math.floor(x / size), math.floor(y / size), te)
        if checker:
            maps[math.floor(y / size)][math.floor(x / size)] = te
            maps = hanten(maps, math.floor(x / size), math.floor(y / size), mukis)
            if te == 1:
                te = 2
            else:
                te = 1
    return maps
def check(maps, x, y, te):
    global higher, lower
    aite =  3 - te
    mukis = []
    return1 = False
    if maps[y][x] == 0:
        try:
            if maps[y + 1][x] == aite and y != 7:
                for i in range(1, 8):
                    try:
                        if maps[y + i][x] == te:
                            return1 = True
                            mukis.append(1)
                            break
                        if maps[y + i][x] == 0:
                            break
                        if y + i == higher:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y - 1][x] == aite and y != 0:
                for i in range(1, 8):
                    try:
                        if maps[y - i][x] == te:
                            return1 = True
                            mukis.append(2)
                            break
                        if maps[y - i][x] == 0:
                            break
                        if y - i == lower:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y][x + 1] == aite and x != 7:
                for i in range(1, 8):
                    try:
                        if maps[y][x + i] == te:
                            return1 = True
                            mukis.append(3)
                            break
                        if maps[y][x + i] == 0:
                            break
                        if x + i == higher:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y][x - 1] == aite and x != 0:
                for i in range(1, 8):
                    try:
                        if maps[y][x - i] == te:
                            return1 = True
                            mukis.append(4)
                            break
                        if maps[y][x - i] == 0:
                            break
                        if x - i == lower:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y + 1][x + 1] == aite and x != 7 and y != 7:
                for i in range(1, 8):
                    try:
                        if maps[y + i][x + i] == te:
                            return1 = True
                            mukis.append(5)
                            break
                        if maps[y + i][x + i] == 0:
                            break
                        if x + i == higher or y + i == higher:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y - 1][x - 1] == aite and x != 0 and y != 0:
                for i in range(1, 8):
                    try:
                        if maps[y - i][x - i] == te:
                            return1 = True
                            mukis.append(6)
                            break
                        if maps[y - i][x - i] == 0:
                            break
                        if x - i == lower or y - i == lower:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y + 1][x - 1] == aite and x != 0 and y != 7:
                for i in range(1, 8):
                    try:
                        if maps[y + i][x - i] == te:
                            return1 = True
                            mukis.append(7)
                            break
                        if maps[y + i][x - i] == 0:
                            break
                        if y + i == higher or x - i == lower:
                            break
                    except:
                        break
        except:
            a = 0
        try:
            if maps[y - 1][x + 1] == aite and x != 7 and y != 0:
                for i in range(1, 8):
                    try:
                        if maps[y - i][x + i] == te:
                            return1 = True
                            mukis.append(8)
                            break
                        if maps[y - i][x + i] == 0:
                            break
                        if y - i == lower or x + i == higher:
                            break
                    except:
                        break
        except:
            a = 0
        return return1, mukis
    else:
        return False, False
def hanten(maps, x, y, mukis):
    global te, higher, lower
    aite =  3 - te
    try:
        if 1 in mukis:
            i = 0
            while True:
                if y + i == higher:
                    break
                i += 1
                if maps[y + i][x] == te:
                    break
                maps[y + i][x] = te
                

    except:
        a = 0
    try:
        if 2 in mukis:
            i = 0
            while True:
                if y - i == lower:
                    break
                i += 1
                if maps[y - i][x] == te:
                    break
                maps[y - i][x] = te
                

    except:
        a = 0
    try:
        if 3 in mukis:
            i = 0
            while True:
                if x + i == higher:
                    break
                i += 1
                if maps[y][x + i] == te:
                    break
                maps[y][x + i] = te
                

    except:
        a = 0
    try:
        if 4 in mukis:
            i = 0
            while True:
                if x - i == lower:
                    break
                i += 1
                if maps[y][x - i] == te:
                    break
                maps[y][x - i] = te
                

    except:
        a = 0
    try:
        if 5 in mukis:
            i = 0
            while True:
                if y + i == higher or x + i == higher:
                    break
                i += 1
                if maps[y + i][x + i] == te:
                    break
                maps[y + i][x + i] = te
                

    except:
        a = 0
    try:
        if 6 in mukis:
            i = 0
            while True:
                if y - i == lower or x - i == lower:
                    break
                i += 1
                if maps[y - i][x - i] == te:
                    break
                maps[y - i][x - i] = te
                

    except:
        a = 0
    try:
        if 7 in mukis:
            i = 0
            while True:
                if y + i == higher or x - i == lower:
                    break
                i += 1
                if maps[y + i][x - i] == te:
                    break
                maps[y + i][x - i] = te
                

    except:
        a = 0
    try:
        if 8 in mukis:
            i = 0
            while True:
                if y - i == lower or x + i == higher:
                    break
                i += 1
                if maps[y - i][x + i] == te:
                    break
                maps[y - i][x + i] = te
                

    except:
        a = 0
    return maps
def on_click(event):
    global mouse_x, mouse_y, clicked
    clicked = 1
    mouse_x, mouse_y = event.x, event.y
canvas.bind("<Button-1>", on_click)
te = 1
higher = 7
lower = 0
clicked = 0
mouse_x = 0
mouse_y = 0
yosoku = 0
while True:
    fpser = time.time()
    time.sleep(0.01)
    maps = put(maps, mouse_x, mouse_y)
    stop = byouga(maps)
    canvas.create_text(1000, 500, text=f"fps:{str(1 / (time.time() - fpser))[:4]}", tag="fps", fill="white")
    canvas.update()
    if stop:
        break
black_count = 0
white_count = 0
for y in range(8):
    for x in range(8):
        if maps[y][x] == 1:
            black_count += 1
        elif maps[y][x] == 2:
            white_count += 1
if black_count > white_count:
    mb.showinfo("Reversi", f"black win!(black:{black_count}, white:{white_count})")
elif white_count > black_count:
    mb.showinfo("Reversi", f"white win!(black:{black_count}, white:{white_count})")
else:
    mb.showinfo("Reversi", "draw!")
sys.exit()