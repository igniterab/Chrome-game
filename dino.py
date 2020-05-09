import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return True
     

def isCollide(data):

    
    for i in range(450, 500):
        for j in range(220, 270):
            if data[i, j] < 90 and data[i, j] > 50 :
                hit("up")
                return True
    

    # Draw the rectangle for birds
    for i in range(450, 500 ):
        for j in range(150, 220):
            if data[i, j] <= 50:
                hit("down")
                return True
    return False

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    #hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        #print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(450, 500):
            for j in range(220, 270):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(450, 500):
            for j in range(150, 220):
                data[i, j] = 171

        image.show()
        break
        '''

