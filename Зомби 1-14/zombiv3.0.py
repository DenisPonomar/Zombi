# -*- coding: utf-8 -*-
import sys, pygame, random, os, math
pygame.init()
pygame.mixer.init()
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("window.ui")[0]

class MyWindowClass(QtGui.QMainWindow, QtGui.QWidget, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        chislo_Vse_Game_Name = len(Vse_Game_Name[0])
        for i in range(chislo_Vse_Game_Name):
            button_Vse_Game_Name = QtGui.QPushButton(str(Vse_Game_Name[0][i]), self)
            button_Vse_Game_Name.setGeometry(100, (270+i*50), 100, 35)
            massiv_button_Vse_Game_Name.append(button_Vse_Game_Name)

            delete_Vse_Game_Name = QtGui.QPushButton(str(Vse_Game_Name[0][i]), self)
            delete_Vse_Game_Name.setGeometry(450, (270+i*50), 100, 35)
            delete_Vse_Game_Name.setStyleSheet("background: red")
            massiv_delete_Vse_Game_Name.append(delete_Vse_Game_Name)
        for i in range(chislo_Vse_Game_Name):
            label = QtGui.QLabel("score: " + str(Vse_Game_Name[1][i]), self)
            label.move(220, (270+i*50))
            label.setFixedSize(150, 30)
            massiv_label.append(label)
        for i in range(len(Vse_Game_Name[0])):
            massiv_button_Vse_Game_Name[i].clicked.connect(self.button_clicked1)
            massiv_delete_Vse_Game_Name[i].clicked.connect(self.button_clicked2)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_button_Vse_Game_Name[i].deleteLater)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_delete_Vse_Game_Name[i].deleteLater)
            massiv_delete_Vse_Game_Name[i].clicked.connect(massiv_label[i].deleteLater)
        self.game.clicked.connect(self.button_clicked0)
        if len(Vse_Game_Name[0]) < 4:
            hight_QWidget = 480
        else:
            hight_QWidget = (300+len(Vse_Game_Name[0])*50)
        QtGui.QWidget.setFixedSize(self, 640, hight_QWidget)
    def button_clicked0(self):
        global Game_Name
        if self.name.text() == "":
            Game_Name = "ANONIM"
        else:
            Game_Name = self.name.text()
        if Game_Name not in Vse_Game_Name[0]:
            Vse_Game_Name[0].append(str(Game_Name))
            Vse_Game_Name[1].append('0')
        f = open('Vse_Game_Name.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        myQExampleScrollArea.close()
        
    def button_clicked1(self):
        sender = self.sender()
        global Game_Name
        Game_Name = sender.text()
        myQExampleScrollArea.close()
        
    def button_clicked2(self):
        sender = self.sender()
        i = sender.text()
        index =  Vse_Game_Name[0].index(str(i))
        del Vse_Game_Name[1][index]
        Vse_Game_Name[0].remove(i)

        f = open('Vse_Game_Name.txt', 'w')
        f.write(str(Vse_Game_Name) + '\n')
        f.close()
        
class QExampleScrollArea (QtGui.QScrollArea, QtGui.QWidget ):
    def __init__ (self, parentQWidget = None):
        super(QtGui.QScrollArea, self).__init__(parentQWidget)
        QtGui.QWidget.setFixedSize(self, 660, 480)
        self.myAnnotator = MyWindowClass(self)
        self.setWidget(self.myAnnotator)

    def mousePressEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mousePressEvent(self, eventQMouseEvent)
        self.myAnnotator.mousePressEvent(eventQMouseEvent)

    def mouseReleaseEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mouseReleaseEvent(self, eventQMouseEvent)
        self.myAnnotator.mouseReleaseEvent(eventQMouseEvent)

    def mouseMoveEvent (self, eventQMouseEvent):
        QtGui.QScrollArea.mouseMoveEvent(self, eventQMouseEvent)
        self.myAnnotator.mouseMoveEvent(eventQMouseEvent)

    def wheelEvent (self, eventQWheelEvent):
        self.myAnnotator.wheelEvent(eventQWheelEvent)
massiv_label = []
massiv_delete_Vse_Game_Name = []
massiv_button_Vse_Game_Name = []

Vse_Game_Name = []
f = open('Vse_Game_Name.txt', 'r')
Vse_Game_Name = (eval(f.readlines()[0]))

app = QtGui.QApplication(sys.argv)
myQExampleScrollArea = QExampleScrollArea()
myQExampleScrollArea.show()

app.exec_()

if "Game_Name" not in locals():
    sys.exit()

size = width, height = 1366, 700
screen = pygame.display.set_mode(size)
def Back():
    pygame.draw.rect(screen, [223, 223, 223], [5, 35, 75, 35], 1)
    back_text = "Back"
    back_surf = score_font.render(back_text, 1, (223, 223, 223))
    screen.blit(back_surf, [10, 40])
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.pos[0] > 5 and event.pos[0] < 80:
            if event.pos[1] > 35 and event.pos[1] < 70:
                global restart
                global running
                restart = True
                running = False
def Zemlya():
    pygame.draw.rect(screen, [0, 223, 0], [0, 650, 1366, 50], 0)
def Pushka():
    pygame.draw.rect(screen, [223, 223, 223], [0, 550, 100, 125], 0)
    pygame.draw.circle(screen, [223, 223, 223], [50, 550], 50, 0)
    pygame.draw.rect(screen, [0, 0, 0], [0, 550, 100, 2], 0)
    
    chislo = str(angle) + "°"
    score_surf = score_font.render(chislo, 1, (0, 0, 0))
    screen.blit(score_surf, [20, 520])
angle = 45.0
def Stvol():
    global angle
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT] and angle >= 0.5:
        angle = angle - 0.5
    if keystate[pygame.K_LEFT] and angle <= 89.5:
        angle = angle + 0.5

    global xcos_stvol
    global ysin_stvol
    xcos_stvol = math.cos(angle*math.pi/180)
    ysin_stvol = math.sin(angle*math.pi/180)
        
    org_spriteImg = pygame.image.load('image\stvol.jpg').convert_alpha()
    spriteImg = pygame.transform.rotate(org_spriteImg, angle)
    spriteRect = spriteImg.get_rect()
    spriteRect.center = (50, 550)
    screen.blit(spriteImg, spriteRect)
x_snaryad = 0
y_snaryad = 0
x_speed = 10
y_speed = 10
x_cos = 0
y_sin = 0
gravity = 0
vystrel = False
def Snaryad():

    global vystrel
    global x_snar
    global y_snar
    if vystrel == False:
        global x_snaryad
        global y_snaryad
        global x_speed
        global y_speed
        global gravity
        global x_cos
        global y_sin
        pygame.draw.circle(screen, [255, 255, 255], [int(50+xcos_stvol*125+x_snaryad), int(550-ysin_stvol*125-y_snaryad)], 10, 0)
        x_snar = int(50+xcos_stvol*125+x_snaryad)
        y_snar = int(550-ysin_stvol*125-y_snaryad)
        
        x_snaryad = 0
        y_snaryad = 0
        x_speed = 10
        y_speed = 10
        x_cos = 0
        y_sin = 0
        gravity = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
        x_cos = xcos_stvol
        y_sin = ysin_stvol

    if vystrel == True:
        x_snaryad = x_snaryad + x_speed * x_cos
        y_snaryad = y_snaryad + y_speed * y_sin - gravity
        gravity = gravity + 0.1
        pygame.draw.circle(screen, [255, 255, 255], [int(50+x_cos*125+x_snaryad), int(550-y_sin*125-y_snaryad)], 10, 0)
        x_snar = int(50+x_cos*125+x_snaryad)
        y_snar = int(550-y_sin*125-y_snaryad)
    if int(550-y_sin*125-y_snaryad) > 700:
        vystrel = False
x_zombie = 1166
massiv_coor_zombie = []
z_time = 0
for i in range(5):
    uy = x_zombie + i*250
    massiv_coor_zombie.append(uy)
def Zombie():
    photo_zombie = pygame.image.load('image\walk_zombie\__Zombie01_Walk_00' + str(int(z_time)) + '.png').convert_alpha()
    photo_zombie = pygame.transform.scale(photo_zombie, (200, 173))
    global massiv_coor_zombie
    for i in range(5):
        massiv_coor_zombie[i] = massiv_coor_zombie[i] - 2
        screen.blit(photo_zombie, (massiv_coor_zombie[i], 527))
        
        if "x_snar" and "y_snar" in globals():
            if x_snar > massiv_coor_zombie[i] and x_snar < (massiv_coor_zombie[i]+200) and y_snar > 527:
                massiv_coor_zombie[i] = massiv_coor_zombie[i] + 1366
                global vystrel
                vystrel = False
score_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 255])

    z_time = z_time + 0.2
    if int(z_time) == 8:
        z_time = 0
    Zemlya()
    Zombie()
    
    Back()
    Stvol()
    Snaryad()
    Pushka()
    
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
         pygame.draw.circle(screen, [255, 255, 255], [int(50+xcos_stvol*125), int(550-ysin_stvol*125)], 50, 0)
         vystrel = True

    pygame.display.flip()
    clock.tick(50)
pygame.quit()
if "restart" in locals():
    if restart == True:
        os.system("zombiv3.0.py")
