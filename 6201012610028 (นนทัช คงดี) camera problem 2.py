###################################################################
# File: camera_test but i don't have problem 2
# Date: 2020-07-29
###################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys

# For windows 10, install VideoCapture 
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#videocapture

# Open Terminal in VSCode and run the following command
# $  pip install VideoCapture 


scr_w, scr_h = 1280, 720
pygame.init()
# this class for make mini square
class block() :
    # make a data of aquare
    def __init__(self,left,top,rw,rh) :
        self.left = left
        self.top = top
        self.rw = rw
        self.rh = rh
        self.rect = (left ,top ,rw ,rh)
    # function for draw a square
    def draw(self,im) :
        self.im = im
        pygame.draw.rect(  self.im, (0,255,0), self.rect,1)
        surface.blit(  self.im, (self.left ,self.top ,self.rw ,self.rh), self.rect )
# function for check if position for mouse in some areas
def cheak(pos,Rect_list,img) :
    for r in Rect_list :
        if int(r.left) <int(pos[0]) < int(r.left)+rw and int(r.top) <int(pos[1]) < int(r.top+rh) :

            return r

        else : 
            pass
# this function is same of cheak but it's return index from image
def cheak2(pos,Rect_list,img) :
    for r in range(len(Rect_list)) :
        if int(Rect_list[r].left) <int(pos[0]) < int(Rect_list[r].left)+rw and int(Rect_list[r].top) <int(pos[1]) < int(Rect_list[r].top+rh) :

            return r

        else : 
            pass

# set screen display 
screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
# list for get emtry square class
rect_list = []
# list for get image square class
current = []


 # draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        square = block(i*rw, j*rh, rw, rh)
        rect_list.append(square)

img = None
is_running = True 
while is_running:
    # draw emtry square
    for f in rect_list :
        f.draw(surface)
    # draw the image
    if len(current) > 0 :
        for g in current :
            g.draw(img)



    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
        # check your cursor if you put button down
        if e.type == pygame.MOUSEBUTTONDOWN :
            # get position for your mouse
            pos = pygame.mouse.get_pos()
            # check position if it's in areas of image
            op = cheak(pos,rect_list,img)
            # if you click on edge of square
            if op == None :
                pass

            else :
                # check the image for do not replace itself
                if op not in current :
                    current.append(op)
                # check if you click on itself
                else :
                    print("hey")
                    op1 = cheak(pos,current,img)
                    op11 = cheak2(pos,current,img)
        # for check your cursor if you pull button up
        if e.type == pygame.MOUSEBUTTONUP :
            # get position for your mouse
            pos2 = pygame.mouse.get_pos()
            op3 = cheak(pos2,current,img)
            # check if your cursor is in area and not itself
            if op3 in current and  op3 != op :
                op2 = cheak(pos2,current,img)
                op1.rect, op2.rect = op2.rect, op1.rect

                print("swap complete")
                

                
    # try to capture the next image from the camera 
    img = pygame.image.load("C:/Users/User/Desktop/image2.jpg")
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h



    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()


print('Done....')
#print(rect_list)
###################################################################