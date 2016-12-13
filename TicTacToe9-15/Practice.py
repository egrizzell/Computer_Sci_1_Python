import glib

#import pictures (create list)
img = ['i0.png', 'i1.png', 'i2.png', 'i3.png', 'i4.png', 'i5.png',
       'i6.png', 'i7.png', 'i8.png']
pic = []
for i in img:
    a = glib.load_image(i)
    pic.append(a)

#create window
winW = 600
winH = 600

glib.open_window(winW, winH)

#show pictures
cordX = 100
cordY = 100

#column1
space_list = ['0i', '1i', '2i', '3i', '4i', '5i', '6i', '7i', '8i']

for i in range(0, 3):
    space_list[i] = glib.show_image(pic[i], cordX, cordY)
    cordY = cordY + 175
#column2
cordX = cordX + 175
cordY = 100

for i in range(3, 6):
    space_list[i] = glib.show_image(pic[i], cordX, cordY)
    cordY = cordY + 175
#column3
cordX = cordX + 175
cordY = 100

for i in range(6, 9):
    space_list[i] = glib.show_image(pic[i], cordX, cordY)
    cordY = cordY + 175

#assign players

p1n = input("What is the oldest players name? ")
print("hello, ", p1n, ", nice to meet you, you are player1")

p2n = input("What is the youngest players name? ")
print("hello, ", p2n, ", nice to meet you, you are player2")

p_symbol = input("Player2 would you like to be X or O? ")
if p_symbol == 'X':
    print("Player2 is X and Player1 is O")
    p2symbol = glib.load_image("xPic.png")
    p1symbol = glib.load_image("oPic.png")
else:
    print("Player2 is O and Player1 is X")
    p2symbol = glib.load_image("oPic.png")
    p1symbol = glib.load_image("xPic.png")

print("Lets start the game!")
    
#Creating turns
for i in range(0, 4):
    glib.open_window(winW, winH)
    print(p1n, 'its your turn')
    move = int(input("What space?"))

    if move == 0:
        glib.show_image(p1symbol, 100, 100)

    if move == 1:
        glib.show_image(p1symbol, 100, 275)
    
    if move == 2:
        glib.show_image(p1symbol, 100, 450)

    if move == 3:
        glib.show_image(p1symbol, 275, 100)

    if move == 4:
        glib.show_image(p1symbol, 275, 450)

    if move == 5:
        glib.show_image(p1symbol, 275, 275)

    if move == 6:
        glib.show_image(p1symbol, 450, 100)

    if move == 7:
        glib.show_image(p1symbol, 450, 275)

    if move == 8:
        glib.show_image(p1symbol, 450, 450)

    print(p2n, 'its your turn')
    move = int(input("What space?"))
    
    if move == 0:
        glib.show_image(p2symbol, 100, 100)

    if move == 1:
        glib.show_image(p2symbol, 100, 275)
    
    if move == 2:
        glib.show_image(p2symbol, 100, 450)

    if move == 3:
        glib.show_image(p2symbol, 275, 100)

    if move == 4:
        glib.show_image(p2symbol, 275, 450)

    if move == 5:
        glib.show_image(p2symbol, 275, 275)

    if move == 6:
        glib.show_image(p2symbol, 450, 100)

    if move == 7:
        glib.show_image(p2symbol, 450, 275)

    if move == 8:
        glib.show_image(p2symbol, 450, 450)         
            
