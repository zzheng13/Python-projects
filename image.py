from cImage import *


# this is the grayScale(image)
def grayScale(originalImage):

    width = originalImage.getWidth()
    height = originalImage.getHeight()
    newImage = EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            originalPixel = originalImage.getPixel(x,y)
            r = (originalPixel.red + originalPixel.green + originalPixel.blue) // 3
            newPixel = Pixel(r,r,r)
            newImage.setPixel(x, y, newPixel)
    return newImage



  
# this is lighten(image,percentIncrease)
def lighten(image,a):

    width = image.getWidth()
    height = image.getHeight()
    newImage = EmptyImage(width,height)
    for x in range(width):
        for y in range(height):
            imagePixel = image.getPixel(x,y)
            r = imagePixel.red * (a) + imagePixel.red
            g = imagePixel.green * (a) + imagePixel.green
            b = imagePixel.blue * (a) + imagePixel.blue
            if r < 0:
                r = 0
            if r > 255:
                r = 255
            if g < 0:
                g = 0
            if g > 255:
                g = 255
            if b < 0:
                b = 0
            if b > 255:
                b = 255
            newPixel = Pixel(r, g, b)
            newImage.setPixel(x, y, newPixel)
    return newImage





# this is rotate90
def rotate90(image):

    width = image.getWidth()
    height = image.getHeight()
    newImage = EmptyImage(height,width)
    
    for y in range(height):
        for x in range(width):
            oldImagePixel = image.getPixel(x,y)
            newImage.setPixel(height - y -1 ,x, oldImagePixel)
            
    return newImage


# this is #4 blur(image)

def blur(Image):
    width = Image.getWidth()
    height = Image.getHeight()
    newImage = EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            
            BlurredPixel = getBlurredPixel(Image,x,y) 
            newImage.setPixel(x, y, BlurredPixel)
    return newImage



def getSafePixel(Image,x,y):
    width = Image.getWidth() 
    height = Image.getHeight()
    if x < 0:
        x = 0
    if x >= width:
        x = width - 1
    if y < 0:
        y = 0
    if y >= height:
        y = height - 1
        
    newImagePixel = Image.getPixel(x,y)
    return newImagePixel



def getBlurredPixel(Image,x,y):
    p1 = getSafePixel(Image,x - 1, y - 1) 
    p2 = getSafePixel(Image,x, y -1 )
    p3 = getSafePixel(Image,x+1,y-1)
    p4 = getSafePixel(Image,x-1,y)
    p5 = getSafePixel(Image,x,y)
    p6 = getSafePixel(Image,x+1,y)
    p7 = getSafePixel(Image,x-1,y+1)
    p8 = getSafePixel(Image,x,y+1)
    p9 = getSafePixel(Image,x+1,y+1)

    r_new = (p1.red+p2.red+p3.red+p4.red+p5.red+p6.red+p7.red+p8.red+p9.red)//9
    g_new = (p1.green+p2.green+p3.green+p4.green+p5.green+p6.green+p7.green+p8.green+p9.green)//9
    b_new = (p1.blue+p2.blue+p3.blue+p4.blue+p5.blue+p6.blue+p7.blue+p8.blue+p9.blue)//9
    newPixel = Pixel(r_new, g_new, b_new)
    
    return newPixel 

#5 I have two functions which are edges(it has getEdgePixel function) and edgesInverted(getEdgePixel1 function) 


def edges(Image):
    width = Image.getWidth()
    height = Image.getHeight()
    newImage = EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            
            Pixel = getEdgePixel(Image,x,y) 
            newImage.setPixel(x, y, Pixel)
    return newImage


def edgesInverted(Image):
    width = Image.getWidth()
    height = Image.getHeight()
    newImage = EmptyImage(width, height)
    for x in range(width):
        for y in range(height):
            
            Pixel = getEdgePixel1(Image,x,y) 
            newImage.setPixel(x, y, Pixel)
    return newImage


def getSafePixel(Image,x,y):
    width = Image.getWidth() 
    height = Image.getHeight()
    if x < 0:
        x = 0
    if x >= width:
        x = width - 1
    if y < 0:
        y = 0
    if y >= height:
        y = height - 1
        
    newImagePixel = Image.getPixel(x,y)
    return newImagePixel



def getEdgePixel(Image,x,y):
    p2 = getSafePixel(Image,x, y -1 )#
    p4 = getSafePixel(Image,x-1,y)#
    p5 = getSafePixel(Image,x,y)#
    p6 = getSafePixel(Image,x+1,y)#
    p8 = getSafePixel(Image,x,y+1)#
    

    r_new = (p2.red+p4.red+p6.red+p8.red) - 4*p5.red 
    if r_new < 0:
        r_new = 0
    if r_new > 255:
        r_new = 255
    g_new = (p2.green+p4.green+p6.green+p8.green) - 4*p5.green
    if g_new < 0:
        g_new = 0
    if g_new > 255:
        g_new = 255
    b_new = (p2.blue+p4.blue+p6.blue+p8.blue) - 4*p5.blue
    if b_new < 0:
        b_new = 0
    if b_new > 255:
        b_new = 255
    newPixel = Pixel(r_new, g_new, b_new)
    
    return newPixel 


def getEdgePixel1(Image,x,y):
    p2 = getSafePixel(Image,x, y -1 )#
    p4 = getSafePixel(Image,x-1,y)#
    p5 = getSafePixel(Image,x,y)#
    p6 = getSafePixel(Image,x+1,y)#
    p8 = getSafePixel(Image,x,y+1)#
    

    r_new = (p2.red+p4.red+p6.red+p8.red) - 4*p5.red + 255
    if r_new < 0:
        r_new = 0
    if r_new > 255:
        r_new = 255
    g_new = (p2.green+p4.green+p6.green+p8.green) - 4*p5.green +255
    if g_new < 0:
        g_new = 0
    if g_new > 255:
        g_new = 255
    b_new = (p2.blue+p4.blue+p6.blue+p8.blue) - 4*p5.blue+ 255
    if b_new < 0:
        b_new = 0
    if b_new > 255:
        b_new = 255
    newPixel = Pixel(r_new, g_new, b_new)
    
    return newPixel 

#6 sharpen(iamge)

def sharpen(Image):
    newEdgeImage = edges(Image)
    image = subtractImage(Image,newEdgeImage)

    return image
    
    
def subtractImage(originalImage, secondImage):


    width = originalImage.getWidth()

    height = originalImage.getHeight()

    newImage = EmptyImage(width, height)

    for x in range(width):
        for y in range(height):
            originalPixel = originalImage.getPixel(x,y)
            pixel = secondImage.getPixel(x,y)
            
            r = (originalPixel.red - pixel.red)
            if r < 0:
                r = 0
            if r > 255:
                r = 255
            g = (originalPixel.green - pixel.green)
            if g < 0:
                g = 0
            if g > 255:
                g = 255
            b = (originalPixel.blue - pixel.blue)
            if b < 0:
                b = 0
            if b > 255:
                b = 255
            newPixel = Pixel(r,g,b)
            newImage.setPixel(x, y, newPixel)
    return newImage
            
            
            
    
def showImage(Image):

    win = ImageWin("Show Image",Image.getWidth(), Image.getHeight())
    Image.draw(win)





original = Image("USF_LM.gif")

x = sharpen(original)


showImage(x)























            



