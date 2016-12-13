import glib

line_list = []
llist = []

file = 'Colorado_480x480.txt'

#Write a function called read_file that takes a topographical
#file filename and returns a list-of-lists containing the data in that file.

def read_file(file):
    f = open(file, 'r')
    for line in f.readlines():
        l = line.split()
        line_list.append(l)
    for row in range(0, len(line_list)):
        for col in range(len(line_list[row])):
            line_list[row][col] = int(line_list[row][col])
    return line_list

#Write a function called normalize that takes the list-of-lists
#of topographical data and scales it so that the lowest value is 0 and the highest
#is 255.

def max_list(line_list):
    high = line_list[0][0]
    for row in line_list:
        for val in row:
            if val > high:
                high = val
    return high

def min_list(line_list):
    low = line_list[0][0]
    for row in line_list:
        for val in row:
            if val < low:
                low = val
    return low

low2 = 0
high2 = 255

def scale(low, high, value, low2, high2):
    sc = ((value - low)/(high - low)) * (high2 - low2)
    sc = int(round(sc, 0))
    return sc

"""
Write a function called normalize that takes the list-of-lists of topographical data and scales it so that the lowest
value is 0 and the highest is 255. Scaling, if you haven't done it, is just like converting numbers to percentages
(e.g. 3 points on a 5 point test is 60 percent). But instead of scaling to 0-100, you want 0-255. This will require figuring out the
lowest and highest values in the list-of-lists. Your function can either change the values in the list-of-lists or create a new list-of-lists.
"""

def normalize(file, line_list, low2, high2):
    l_l = read_file(file)
    hi = max_list(l_l)
    lo = min_list(l_l)
    n_list = []
    for i in l_l:
        new_list = []
        for j in i:
            x = scale(lo, hi, j, low2, high2)
            new_list.append(x)
        n_list.append(new_list)
    return n_list


"""
Write a function called display that takes the list-of-lists from nomalize and
uses glib to create a new image (of the correct width and height), set the pixels
of that image to reflect a grayscale image of the elevation data, and return the image object.
    The updated glib has a new create_image function to create an initially blank image of a certain size.
    The example we did in class of getting access to the pixels in any image is up on the module page
    To set gray values, just set all three pixel channels (R, G and B) to the same value. (0,0,0) is
    black, while (255,255,255) is white.
"""
def display(file, line_list, low2, high2):
    norm = normalize(file, line_list, low2, high2)
    glib.open_window(500, 500)
    im = glib.create_image(480, 480)
    px = glib.get_pixels(im)
    for i in range(0, 480):
        for j in range(0, 480):
            c = px.getpixel(i, j)
            value = norm[i][j]
            px.setpixel(i, j, (value, value, value))
    glib.show_image(im, 250, 250)
    glib.update()

display(file, line_list, low2, high2)
