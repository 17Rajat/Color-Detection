import numpy as np
import pandas as pd
import cv2

image_path = 'pic2.jpg'

csv_path = 'colors.csv'
df = pd.read_csv(csv_path)

index = ['color', 'name', 'hex_value', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names = index, header = None)

#WE can access the values by below code
print(df.loc[1,'R'])

#To see whats in a pic/image
img = cv2.imread(image_path)
img = cv2.resize(img, (800,600))
print(img) #Its showing the array components of the image.

#let's initialize some variables
clicked = False #Initially we're not clicking any other button than leftdoubleclick
r = g = b = xpos = ypos = 0

#define a function which gives the color name of the pixels where our cursor points.
def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d<=minimum:
            minimum = d
            cname = df.loc[i, 'name']
    return cname

#print(get_color_name(0, 0, 0))


# We'll create a function which tells the position of our curser.
def draw_function(event, x, y, flags, params):
    #event = in which we click mouse button i.e left, right, middle.
    #x, y = position or coordinates
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpos, ypos
        clicked = True
        #Storing the coordinates in xpos and ypos varaibles
        xpos = x
        ypos = y
        #print(x,y)
        b,g,r = img[y,x] #in open cv the format is BGR 
        b = int(b)
        g = int(g)
        r = int(r)
        print(b,g,r)
#We'll code to display the image
cv2.namedWindow('image') #it creates a new window to display the image
cv2.setMouseCallback('image', draw_function)
# cv2.imshow('image', img) #it shows/render the image
# cv2.waitKey(0) #it shows the output image untill we manually turn if off by clicking 'cross'.
# cv2.destroyAllWindows() # After clicking 'cross' it shuts the image window off.
        
# Here we'll show the strip in which RGB info will be shown
while True:
    cv2.imshow('image',img)
    if clicked:
        cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)
        text = get_color_name(r,g,b) + 'R=' + str(r) + 'G=' + str(g) + 'B=' + str(b)
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA) #Puts the above text on a image 
        if r+g+b <= 500:
            cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
            
    if cv2.waitKey(20) & 0xFF == 27: #Escape key or 200 seconds
        break
    
cv2.destroyAllWindows()
