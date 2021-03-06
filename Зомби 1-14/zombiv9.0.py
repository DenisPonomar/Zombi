# -*- coding: utf-8 -*-
import sys, pygame, random, os, math, numpy as np
pygame.init()
pygame.mixer.init()
import PyQt4
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
sol_angle = 45
stars_radius = []
cos_stars_angle = []
sin_stars_angle = []
for i in range(1800):
    r = random.randint(0, 978)
    stars_radius.append(r)
    i = float(i)
    cos_stars_angle.append(math.cos(i/10*math.pi/180))
    sin_stars_angle.append(math.sin(i/10*math.pi/180))
def mathsc():
    global sol_angle
    sol_angle = sol_angle + 0.1
    if sol_angle >= 360:
        sol_angle = 0
    global xsol_stvol
    global ysol_stvol
    xsol_stvol = math.cos(sol_angle*math.pi/180)
    ysol_stvol = math.sin(sol_angle*math.pi/180)
    global col
    col = int(((ysol_stvol+1)/2)*198 + 25)
def Stars():
    s_col = 1 - (ysol_stvol+1)/2
    g = int(60 * s_col)
    global stars_angle
    for i in range(1800):
        if i == 1799:
            cos_stars_angle[i] = cos_stars_angle[0]
            sin_stars_angle[i] = sin_stars_angle[0]
        else:
            cos_stars_angle[i] = cos_stars_angle[i+1]
            sin_stars_angle[i] = sin_stars_angle[i+1]
    for i in range(180):
        pygame.draw.circle(screen, [0,g,240], [int(683+cos_stars_angle[i*10]*stars_radius[i]), int(700-sin_stars_angle[i*10]*stars_radius[i])], 1, 1)
def Solnce():
    global xsol_stvol
    global ysol_stvol
    pygame.draw.circle(screen, [255, 255, 0], [int(683+xsol_stvol*600), int(700-ysol_stvol*600)], 50, 0)
def Luna():
    global xsol_stvol
    global ysol_stvol
    pygame.draw.circle(screen, [255, 255, 255], [int(683-xsol_stvol*600), int(700+ysol_stvol*600)], 50, 0)
x1_oblako = 200
x2_oblako = 883
def Oblaka():
    global x1_oblako
    global x2_oblako
    if x1_oblako > -300:
        x1_oblako = x1_oblako - 1
    else:
        x1_oblako = 1366
        
    if x2_oblako > -300:
        x2_oblako = x2_oblako - 1
    else:
        x2_oblako = 1366
    pygame.draw.ellipse(screen,[col+32, col+32, col+32], ((x1_oblako,10),(300,150)), 0)
    pygame.draw.ellipse(screen,[col+32, col+32, col+32], ((x2_oblako,170),(300,150)), 0)
    

photo_zombie = []
for i in range(8):
    photo_zombie.append(pygame.image.load('image\walk_zombie\__Zombie01_Walk_00' + str(i) + '.png'))
def Back():
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 75, 35], 1)
    back_text = "Back"
    back_surf = score_font.render(back_text, 1, (0, 0, 0))
    screen.blit(back_surf, [10, 10])
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.pos[0] > 5 and event.pos[0] < 80:
            if event.pos[1] > 5 and event.pos[1] < 40:
                global restart
                global running
                restart = True
                running = False
def Zemlya():
    pygame.draw.rect(screen, [0, col, 0], [0, 650, 1366, 50], 0)
kol_snar = 2000
def Pushka():
    pygame.draw.rect(screen, [col, col, col], [0, 550, 100, 125], 0)
    pygame.draw.circle(screen, [col, col, col], [50, 550], 50, 0)
    pygame.draw.rect(screen, [0, 0, 0], [0, 550, 100, 2], 0)
    
    chislo = str(angle) + "??"
    score_surf = score_font.render(chislo, 1, (0, 0, 0))
    screen.blit(score_surf, [20, 560])

    chislo = str(int(kol_snar))
    score_surf = score_font.render(chislo, 1, (0, 0, 0))
    screen.blit(score_surf, [35, 520])
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



gravity = 0

popal = False
class Ball:
    def __init__(self, xcos_stvol, ysin_stvol, x_snaryad, y_snaryad):
        self.gravity = 0
        self.xcos_stvol = xcos_stvol
        self.ysin_stvol = ysin_stvol
        self.x_snaryad = x_snaryad
        self.y_snaryad = y_snaryad
        self.x_speed = 10
        self.y_speed = 10
        
    def fly(self):
        if pause == False:
            self.x_snaryad = self.x_snaryad + self.x_speed * self.xcos_stvol
            self.y_snaryad = self.y_snaryad + self.y_speed * self.ysin_stvol - self.gravity
            self.gravity = self.gravity + 0.1

        self.x_snar = int(50+self.xcos_stvol*125+self.x_snaryad)
        self.y_snar = int(550-self.ysin_stvol*125-self.y_snaryad)
        pygame.draw.circle(screen, [255, 255, 255], [self.x_snar, self.y_snar], 10, 0)

        for k in range(5):
            if self.x_snar > massiv_coor_zombie[k] and self.x_snar < (massiv_coor_zombie[k]+200) and self.y_snar > 527 and self.y_snar < 720:
                global popal
                popal = True
                massiv_coor_zombie[k] = massiv_coor_zombie[k] + 1366
                global score
                global record
                if record == score:
                    record = record + 1
                score = score + 1
                
            if massiv_coor_zombie[k] < 100:
            
                chislo = "Game Over, " + str(Game_Name)
                score_surf = go_score_font.render(chislo, 1, (0, 0, 0))
                screen.blit(score_surf, [300, 250])
                global go_time
                go_time = go_time + 0.02
                if go_time > 5:
                    global restart
                    global running
                    restart = True
                    running = False
        
balls = [] 

x_zombie = 1166
massiv_coor_zombie = []
z_time = 0
for i in range(5):
    uy = x_zombie + i*273
    massiv_coor_zombie.append(uy)
go_time = 0
score = 0
go_score_font = pygame.font.Font(None, 100)
def Zombie():
    global massiv_coor_zombie
    for i in range(5):
        photo_zombie1 = pygame.transform.scale(photo_zombie[int(z_time)], (200, 173))
        if pause == False:
            massiv_coor_zombie[i] = massiv_coor_zombie[i] - 2
        screen.blit(photo_zombie1, (massiv_coor_zombie[i], 527))
                

index1 =  Vse_Game_Name[0].index(str(Game_Name))
record = int(Vse_Game_Name[1][index1])

score_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

pause = False
pause_time = 0
start_time = 0
time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mathsc()
    
    screen.fill([0, 0, col])

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_DOWN] and pause_time < 10:
        pause = True
        start_time = 0
    if pause == True:
        pause_time = pause_time + 1
        score_surf = go_score_font.render("Pause", 1, (0, 0, 0))
        screen.blit(score_surf, [600, 250])
        
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_DOWN] and pause_time > 10:
        pause = False
        start_time = 0
    if pause == False:
        start_time = start_time + 1
    if start_time > 1:
        pause_time = 0
        
    z_time = z_time + 0.2
    if int(z_time) == 8:
        z_time = 0
    Stars()
    Solnce()
    Luna()
    Oblaka()
    
    Zemlya()
    
    Back()
    Stvol()
    
    Pushka()
    
    Zombie()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP] and kol_snar > 1 and time%5 == 1:
        pygame.draw.circle(screen, [255, 255, 255], [int(50+xcos_stvol*125), int(550-ysin_stvol*125)], 50, 0)
        myBall = Ball(xcos_stvol, ysin_stvol, 0, 0)
        balls.append(myBall)
        kol_snar = kol_snar - 1

    time = time + 1

    kol_snar = kol_snar + 0.04

    if len(balls) == 225:
            balls.pop(0)
    for i in range(len(balls)):
        balls[i].fly()
    if popal == True:
        balls.pop(0)
        if len(balls) > 0:
            balls.pop(0)
        popal = False
        
    ochki = "Score: " + str(int(score))
    score_surf = score_font.render(ochki, 1, (0, 0, 0))
    screen.blit(score_surf, [10, 40])

    ochki_record = "Record: "+ str(int(record))
    score_surf_record = score_font.render(ochki_record, 1, (0, 0, 0))
    screen.blit(score_surf_record, [10, 70])

    pygame.display.flip()
    clock.tick(50)
pygame.quit()

index_record =  Vse_Game_Name[0].index(str(Game_Name))
Vse_Game_Name[1][index_record] = str(int(record))
f = open('Vse_Game_Name.txt', 'w')
f.write(str(Vse_Game_Name) + '\n')
f.close()
if "restart" in locals():
    if restart == True:
        os.system("zombiv9.0.py")
