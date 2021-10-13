import random
import time
import pygame

from pygame.display import update

#Initialises the pygame module
pygame.init()

#Sets the height and width of the window
width = 900
height = 900

#Creates the pygame clock
clock = pygame.time.Clock()

#Creates the color variables
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
purple = (255, 0, 255)
orange = (255, 150, 0)

#Sets the standard refresh rate of the window
FPS = 60

#Creates and initialises the fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
sortedFont = pygame.font.SysFont('comicsans', 100)

#The list that holds the bars to be drawn
bars = []

#Sets weather the program is paused
paused = False

#Sets which number of bars is selected
numberSelected = [False, True, False]

#Sets which sort is selected
sortSelected = [True, False, False]


#**Utility methods**


#Starts the program
def Start():
    clock = pygame.time.Clock()
    gameRunning = True
    dis.fill(white)
    #Creates 50 bars by default on the main menu
    createBars(50)
    #List containing the buttons on the screen
    buttonList = createButtons()
    while gameRunning:
        clock.tick(FPS)
        dis.fill(white)
        checkInput(buttonList)
        highlightButtons()
        #Render buttons
        for button in buttonList:
            button.render(dis)
        createGUI()
        drawBars(bars)
        pygame.display.update()

#Checks for user input on current buttons and quit button
def checkInput(buttonList):
    for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                pygame.quit()
                quit()
            for button in buttonList:
                button.get_event(event)

#Creates the buttons for the sort screen
def createSortScreenButtons():
    pauseButton = Button((700,80, 100,50), "Pause", 30, red, pause)
    resetButton = Button((815,50, 80,50), "Reset", 30, red, Start)
    buttonList = [pauseButton, resetButton]
    return buttonList

#Draws the bars green and displays sorted text when the sort is completed
def completedSortSequence(barList):
    text = "Sorted!"
    draw_text = sortedFont.render(text, 1, black)
    j = 0
    #Displays all bars in green
    while j <= len(barList) - 1:
        pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
        pygame.draw.rect(dis, green, (50+ j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
        j += 1
    #Displayes the "Sorted" text on screen
    dis.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    #Shows this for 3s
    pygame.time.delay(3000) 

#Initialises the number of bars selected with a random value
def createBars(number):
    global numberSelected
    #Sets number to selected number
    if number == 10:
        numberSelected = [True, False, False]
    elif number == 50:
        numberSelected = [False, True, False]
    else:
        numberSelected = [False, False, True]
    #Sets barwidth to size of interface - 100 for borders
    barWidth = (width-100)//number
    #Temporary list to hold the newly created bars
    barList = []
    i = 0
    #Creates the number of bars selected, with a random value to each and adds it to barList
    while i <= number - 1:
        tempBarHeight = random.randrange(0,round(height-160), 1)
        tempBar = [barWidth, tempBarHeight]
        barList.append(tempBar)
        i += 1
    #Sets the global variable bars to the new list barList
    global bars
    bars = barList

#Updates the sort method array with the selected sort method
def setSortMethod(method):
    global sortSelected
    if method == "bubble":
        sortSelected = [True, False, False]
    elif method == "selection":
        sortSelected = [False, True, False]
    else:
        sortSelected = [False, False, True]

#Highlights each selected buttton green
def highlightButtons():
    #Depending on which button is selected it adds a green rectange slightly wider than the original button
    if numberSelected[0] == True:
        pygame.draw.rect(dis, green, (195, 5, 160, 60))
    elif numberSelected[1] == True:
        pygame.draw.rect(dis, green, (355, 5, 160, 60))
    else:
        pygame.draw.rect(dis, green, (515, 5, 185, 60))
    if sortSelected[0] == True:
        pygame.draw.rect(dis, green, (175, 75, 160, 60))
    elif sortSelected[1] == True:
        pygame.draw.rect(dis, green, (335, 75, 180, 60))
    else:
        pygame.draw.rect(dis, green, (515, 75, 185, 60))      

#Creates the buttons for the pause screen
def createPauseScreenButtons():
    playButton = Button((700,80, 100,50), "Play", 30, red, pause)
    resetButton = Button((815,50, 80,50), "Reset", 30, red, Start)
    buttonList = [playButton, resetButton]
    return buttonList

#Pauses the program and creates a play button to restart the program
def pause():
    global paused
    buttonList = createPauseScreenButtons()
    #Updates the global variable if already paused
    if paused == True:
        paused = False
    else:
        paused = True
    #If not paused enter the paused mode
    while paused:
        clock.tick(FPS)
        checkInput(buttonList)
        for button in buttonList:
            button.render(dis)
        pygame.display.update()

#Starts when the sort button is pressed, it then sorts based on the selected sort method
def sort():
    #Calls the sort method thats selected baed on the sortSelected list variable
    if sortSelected[0] == True:
        bubbleSort(bars)
    elif sortSelected[1] == True:
        selectionSort()
    else:
        insertionSort(bars)     

#Initialises the buttons to be used in the main menu
def createButtons():
    tenValueButton = Button((200, 10, 150, 50), "10", 20, red, createBars, 10)
    fiftyValueButton = Button((360, 10, 150, 50), "50", 20, red, createBars, 50)
    oneHundredValueButton = Button((520, 10, 175, 50), "100", 20, red, createBars, 100)
    bubbleSortButton = Button((180, 80, 150, 50), "Bubble sort", 65, red, setSortMethod, "bubble")
    SelectionSortButton = Button((340, 80, 170, 50), "Selection sort", 75, red, setSortMethod, "selection")
    InsertionSortButton = Button((520, 80, 175, 50), "Insertion sort", 75, red, setSortMethod, "insertion")
    sortButton = Button((700, 10, 100,50), "Sort", 30, red, sort)
    resetButton = Button((815,50, 80,50), "Reset", 30, red, Start)
    buttonsList = [tenValueButton,oneHundredValueButton,fiftyValueButton,bubbleSortButton, SelectionSortButton,InsertionSortButton,sortButton, resetButton]
    return buttonsList

#Buttons class which can execute a method when pressed
class Button:
    def __init__(self, rect, text, leftShift, color, command1, argument1 = None):
        text = font_style.render(text, True, yellow)
        self.color = color
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(self.color)
        self.image.blit(text, [self.rect.size[0]/2 - leftShift, self.rect.size[1]/2 - 15])
        self.command1 = command1
        self.argument1 = argument1
    def render(self, screen):
        screen.blit(self.image, self.rect)
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if self.argument1 == None:
                    self.command1()
                else:
                    self.command1(self.argument1)

#Draws the bars that have been initialised
def drawBars(barList):
    j = 0
    #Draws all the buttons in the barList
    while j <= len(barList) - 1:
        pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
        pygame.draw.rect(dis, red, (50+ j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
        j += 1


#**GUI creating methods**


#Creates the basic color and text of the main menu
def createGUI():
    numberText = "Number to sort: "
    sortText = "Sort method: "
    numberText = font_style.render(numberText, True, black)
    sortText = font_style.render(sortText, True, black)
    pygame.Surface.blit(dis, numberText, (10, 20))
    pygame.Surface.blit(dis, sortText, (30, 90))
    pygame.draw.rect(dis, black,(43.5,140,width - 87, height - 150))
    pygame.draw.rect(dis, white,(48.5,145,width - 97, height - 160))

#Creates the basic color and text of the sort screen
def createSortScreen():
    sortingText = "Sorting... "
    sortingText = sortedFont.render(sortingText, True, black)
    pygame.Surface.blit(dis, sortingText, (300, 40))
    pygame.draw.rect(dis, black,(43.5,140,width - 87, height - 150))
    pygame.draw.rect(dis, white,(48.5,145,width - 97, height - 160))

#Displays the text and draws all bars green to show it's sorted
def completedSortSequence(barList):
    text = "Sorted!"
    draw_text = sortedFont.render(text, 1, black)
    j = 0
    #Draws all bars in barList in green
    while j <= len(barList) - 1:
        pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
        pygame.draw.rect(dis, green, (50+ j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
        j += 1
    #Display sorted text
    dis.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000) 


#**Selection sort methods**

#Sorts using selection sort
def selectionSort():
    buttonList = createSortScreenButtons()
    i = 0
    j = 0
    barList = bars
    #Traverses each element in the list
    for i in range (len(barList)):
        jMin = i
        #Traverses each element further in the list than element i
        for j in range (i+1, len(barList)):
            setSelectionSortRefreshRate(barList)
            checkInput(buttonList)
            for button in buttonList:
                button.render(dis)
            #If selected element is smaller than current min, set it as the new min
            if(barList[j] < barList[jMin]):
                jMin = j
            updateSelectionSortBars(barList, i, jMin, j)
        #Swap the current smallest element with the current element
        barList[i], barList[jMin] = barList[jMin], barList[i]
    completedSortSequence(barList)
    Start()

#Updates the bars to show the visual representation of the selection sort
def updateSelectionSortBars(barList, i, jMin, currentJ):
    updating = True
    while updating:
        createSortScreen()
        j = 0
        #Draws each bar
        while j < len(barList):
            #Draws each bar thats already been sorted in green
            if j < i:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, green, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draws the current minimum element as blue
            elif j == jMin:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, blue, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draws the current inspected element as purple
            elif j == currentJ:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, purple, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draws the default bar red
            else:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, red, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
        pygame.display.update()
        updating = False

#Sets the refresh rate for each number of bars
def setSelectionSortRefreshRate(barList):
    if len(barList) == 10:
        clock.tick(FPS/20)
    elif len(barList) == 50:
        clock.tick(FPS/3)
    elif len(barList) == 100:
        clock.tick(FPS)


#**Bubble sort methods**

#Sort using bubble sort method
def bubbleSort(newList):
    i = 0
    buttonList = createSortScreenButtons()
    #Travers through each element in the list
    while i < len(newList):
        checkInput(buttonList)
        for button in buttonList:
            button.render(dis)
        #Flag element to check if any changes have been made
        flag = 0
        j = 0
        #Traverses through each element before the end sorted element
        while j + i < (len(newList) - 1):
            checkInput(buttonList)
            for button in buttonList:
                button.render(dis)
                #If current element is larger than the element after, swap them
                if newList[j ] > newList[j +1]:
                    higherNum = newList[j ]
                    newList[j] = newList[j +1]
                    newList[j +1] = higherNum
                    flag += 1 
                #Draw the new updated list of bars
                updateBubbleSortBars(newList, j, i)
            j += 1
        #If no changes are made, the list is sorted, so end
        if flag == 0:
            break
        i += 1
    #Ensures i is the end element, incase the list is sorted early
    i = len(newList)
    updateBubbleSortBars(newList, j, i)
    completedSortSequence(newList)
    Start()

#Updates the bars to show the visual representation of the bubble sort
def updateBubbleSortBars(barList,passedJ, passedI):
    updating = True
    while updating:
        setBubbleSortRefreshRate(barList)
        createSortScreen()
        j = 0
        #Draws all the bars
        while j < len(barList):
            #If the bar is sorted, draw in green
            if j >= len(barList) - passedI:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, green, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draw the current element as blue
            elif j-1 == passedJ:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, blue, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draw the bar in red by default
            else:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, red, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
                
        updating = False
    pygame.display.update()

#Sets the refresh rate for each number of bars
def setBubbleSortRefreshRate(barList):
    if len(barList) == 10:
        clock.tick(FPS/5)
    elif len(barList) == 50:
        clock.tick(FPS)
    elif len(barList) == 100:
        clock.tick(FPS*4)


#**Insertion sort methods**

#Sorts using insertion sort method
def insertionSort(barList):
    # Traverse through 1 to len(barList)
    buttonList = createSortScreenButtons()
    for i in range(1, len(barList)):
        key = barList[i]
        # Move elements of barList[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < barList[j] :
            checkInput(buttonList)
            for button in buttonList:
                button.render(dis)
            barList[j + 1] = barList[j]
            j -= 1
            #Draw the updated bars
            updateInsertionSortBars(barList, i, j, key)
        #The next element is now the key to compare
        barList[j + 1] = key
    createSortScreen()
    completedSortSequence(barList)
    Start()

#Updates the bars to show the visual representation of the insertion sort
def updateInsertionSortBars(barList, passedI, passedJ, key):
    updating = True
    while updating:
        setInsertionSortRefreshRate(barList)
        createSortScreen()
        j = 0
        #Draw all bars in barList
        while j < len(barList):
            #If the element is the current largest element thats been inserted draw in green
            if j == passedI:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, green, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
            #Draw the current element thats being inserted in blue
            elif j == passedJ + 1:
                pygame.draw.rect(dis, black, (50 + j*key[0]-1, 145, key[0]-1, key[1]+1))
                pygame.draw.rect(dis, blue, (50 + j*key[0], 145, key[0]-3, key[1]))
                j += 1
            #Draw the bar red by default
            else:
                pygame.draw.rect(dis, black, (50 + j*barList[j][0]-1, 145, barList[j][0]-1, barList[j][1]+1))
                pygame.draw.rect(dis, red, (50 + j*barList[j][0], 145, barList[j][0]-3, barList[j][1]))
                j += 1
                
        updating = False
    pygame.display.update() 

#Sets the refresh rate for each numbher of bars
def setInsertionSortRefreshRate(barList):
    if len(barList) == 10:
        clock.tick(FPS/30)
    elif len(barList) == 50:
        clock.tick(FPS/2)
    elif len(barList) == 100:
        clock.tick(FPS)


dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Application")
Start()


