#**********************************
import machine
machine.mem32[0x50000708]=0x703
#**********************************
from microbit import*
import neopixel,music
GZ_LEDS = neopixel.NeoPixel(pin0,64)
current_player=""
player_possible=""
current_TTT_cell = 0
border_color = (0,10,0)
player_x_marked_color = (10,0,0)
player_x_temp_color = (50,0,0)
player_o_marked_color=(0,0,10)
no_color = (0,0,0)
GZ_TTT_cells = [[],
                [0,1,9,8],     [3,4,12,11],   [6,7,15,14], 
                [24,25,33,32], [27,28,36,35], [30,31,39,38],
                [48,49,57,56], [51,52,60,59], [54,55,63,62]]
ppc=0
current_TTT_cell = 0
z=""
randomvar=0
gameplay=0
y=0
movement=0
move=0
on=0
winx=0
wino=0
winpx=0
wscrx=[]
wscro=[]
winpo=0
player_list_x=[]
player_list_o=[]
game=[[''],[''],['']
     ,[''],[''],['']
     ,[''],[''],['']]

def border():
    global y, GZ_LEDS
    xborder1=2
    xborder2=5
    yborder1=16
    yborder2=40
    if y==0:
        for i in range(8):
            GZ_LEDS[xborder1]=border_color
            GZ_LEDS[xborder2]=border_color
            xborder2+=8
            xborder1+=8
            y=1
    if y==1:
        for i in range(8):
            GZ_LEDS[yborder1]=border_color
            GZ_LEDS[yborder2]=border_color
            yborder1+=1
            yborder2+=1
            y=2
    GZ_LEDS.write()
    
def player():
    global current_player, player_possible, on
    if gameplay==0:
        if on==0:
            if button_a.get_presses():
                player_possible="x"
            if button_b.get_presses():
                player_possible="o"

def player_save():
    global player_possible, current_player,on
    if gameplay==0:
        if on==0:
            if player_possible!="":
                if pin_logo.is_touched():
                    current_player=player_possible
                    border()
                    music.play(music.JUMP_UP,pin2)
                    on=1
            
def disp():
    global player_possible
    if gameplay==0:
        if player_possible=="":
            display.show("?")
        if current_player=="":
            if player_possible=="x":
                display.show(Image("90009:"
                                        "09090:"
                                      "00900:"
                                      '09090:'
                                      '90009'))
            elif player_possible=="o":
                display.show(Image("09990:"
                                        "90009:"
                                      "90009:"
                                      '90009:'
                                      '09990'))
        if current_player=="x":
            display.show(Image("90009:"
                                        "09090:"
                                      "00900:"
                                      '09090:'
                                      '90009'))
        elif current_player=="o":
            display.show(Image("09990:"
                                        "90009:"
                                      "90009:"
                                      '90009:'
                                      '09990'))
            
def gz_input():
    global ppc, movement,on, winx, wino, gameplay
    if gameplay==0:
        if on==1:
            if pin13.read_digital()==0:
                ppc=130
            elif pin13.read_digital()==1 and ppc==130:
                ppc=131
                movement=0
            elif pin12.read_digital()==0:
                ppc=120
            elif pin12.read_digital()==1 and ppc==120:
                ppc=121
                movement=0
            elif pin15.read_digital()==0:
                ppc=150
            elif pin15.read_digital()==1 and ppc==150:
                ppc=151  
            
         
def moving_the_box():
    global move , ppc, movement, on, current_TTT_cell, winx, wino, gameplay
    if gameplay==0:
        if on==1:
            if ppc==120:
                if move>1:
                    if movement==0:
                        move-=1
                        movement=1
                        current_TTT_cell=1
            elif ppc==130:
                if move<=8:
                    if movement==0:
                        move=move+1
                        movement=1
                        current_TTT_cell=1
            
def display_gz():
    global move, current_TTT_cell, winx, wino, game, gameplay
    if gameplay==0:
        if current_TTT_cell==1:
            if current_player=="x":
                if GZ_LEDS[GZ_TTT_cells[move][0]]!=player_x_marked_color and GZ_LEDS[GZ_TTT_cells[move][0]]!=player_o_marked_color:
                    for j in range(4):
                        GZ_LEDS[GZ_TTT_cells[move][j]]=player_x_marked_color
                        GZ_LEDS.write()
                        sleep(25)
                        GZ_LEDS[GZ_TTT_cells[move][j]]=no_color
                        GZ_LEDS.write()
                if GZ_LEDS[GZ_TTT_cells[move][0]]==player_x_marked_color or GZ_LEDS[GZ_TTT_cells[move][0]]==player_o_marked_color:
                    for h in range(4):
                        GZ_LEDS[GZ_TTT_cells[move][h]]=(0,0,0)
                        GZ_LEDS.write()
                        sleep(25)
                        if game[move-1][0]=="o":
                            GZ_LEDS[GZ_TTT_cells[move][h]]=player_o_marked_color
                            GZ_LEDS.write()
                        elif game[move-1][0]=="x":
                            GZ_LEDS[GZ_TTT_cells[move][h]]=player_x_marked_color
                            GZ_LEDS.write()
            elif current_player=="o":
                if GZ_LEDS[GZ_TTT_cells[move][0]]!=player_x_marked_color and GZ_LEDS[GZ_TTT_cells[move][0]]!=player_o_marked_color:
                    for j in range(4):
                        GZ_LEDS[GZ_TTT_cells[move][j]]=player_o_marked_color
                        GZ_LEDS.write()
                        sleep(25)
                        GZ_LEDS[GZ_TTT_cells[move][j]]=no_color
                        GZ_LEDS.write()
                if GZ_LEDS[GZ_TTT_cells[move][0]]==player_x_marked_color or GZ_LEDS[GZ_TTT_cells[move][0]]==player_o_marked_color:
                    for h in range(4):
                        GZ_LEDS[GZ_TTT_cells[move][h]]=(0,0,0)
                        GZ_LEDS.write()
                        sleep(25)
                        if game[move-1][0]=="o":
                            GZ_LEDS[GZ_TTT_cells[move][h]]=player_o_marked_color
                            GZ_LEDS.write()
                        elif game[move-1][0]=="x":
                            GZ_LEDS[GZ_TTT_cells[move][h]]=player_x_marked_color
                            GZ_LEDS.write()
                    
def selection_box():
    global ppc, move, player_list_x, current_player, game, gameplay
    if gameplay==0:
        if move>=1:
            if ppc==150:
                if current_player=="x":
                    current_player="o"
                    if game[move-1][0]=="":
                        game[move-1][0]="x"
                        player_list_x.append(move)
                        music.play(music.POWER_UP,pin2)
                        for j in range(4):
                             GZ_LEDS[GZ_TTT_cells[move][j]]=player_x_marked_color
                             GZ_LEDS.write()
                    elif game[move-1][0]=="x":
                        music.play(music.BA_DING,pin2)
                        current_player="x"
                    elif game[move-1][0]=="o":
                        music.play(music.POWER_DOWN,pin2)
                        current_player="x"
                    ppc=151
            if ppc==150:
                if current_player=="o":
                    current_player="x"
                    if game[move-1][0]=="":
                        game[move-1][0]="o"
                        player_list_o.append(move)
                        music.play(music.POWER_UP,pin2)
                        for j in range(4):
                             GZ_LEDS[GZ_TTT_cells[move][j]]=player_o_marked_color
                             GZ_LEDS.write()
                       
                    elif game[move-1][0]=="o":
                        music.play(music.BA_DING,pin2)
                        current_player="o"
                    elif game[move-1][0]=="x":
                        music.play(music.POWER_DOWN,pin2)
                        current_player="o"
                    ppc=151
  
def remove_list_duplicates():
    global player_list_o, player_list_x
    player_list_o=list(dict.fromkeys(player_list_o))
    player_list_x=list(dict.fromkeys(player_list_x))
    
def wins():
    global winpx,winpo,scr,player_list_o, wscrx,wscro, player_list_x, winx, wino, gameplay, z
    if gameplay==0:
        win_list = [ [1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [1, 4, 7],
                      [2,5,8],
                      [3,6,9],
                      [1,5,9],
                       [3,5,7]]    
        player_list_x.sort()
        if len(player_list_x)>2:
            for i in range(len(win_list)):
                for h in range(len(player_list_x)): 
                    if win_list[i][0]== player_list_x[h]:
                        for m in range(len(player_list_x)):
                            if win_list[i][1]==player_list_x[m]:
                                for l in range(len(player_list_x)):
                                    if win_list[i][2]==player_list_x[l]:
                                        winpx=3     
                                        wscrx.append(player_list_x[h])
                                        wscrx.append(player_list_x[m])
                                        wscrx.append(player_list_x[l])
                                    else:
                                        winpx=winpx
        if winpx==3: 
            winx+=1
            z="x"
        player_list_o.sort()
        if len(player_list_o)>2:
            for i in range(len(win_list)):
                for h in range(len(player_list_o)): 
                    if win_list[i][0]== player_list_o[h]:
                        for m in range(len(player_list_o)):
                            if win_list[i][1]==player_list_o[m]:
                                for l in range(len(player_list_o)):
                                    if win_list[i][2]==player_list_o[l]:
                                        winpo=3     
                                        wscro.append(player_list_o[h])
                                        wscro.append(player_list_o[m])
                                        wscro.append(player_list_o[l])
                                    else:
                                        winpo=winpo
        if winpo==3:
            wino+=1
            z="o"
          
        
def winning():
    global win, wscrx, wscro,scrremove,randomvar, wino, y,gameplay, z
    if gameplay==0:
        if z=="x":
            if randomvar==0:
                for i in range(9):
                    for j in range(4):
                        GZ_LEDS[GZ_TTT_cells[i+1][j]]=no_color
                        GZ_LEDS.write()
                for k in range(4):
                    GZ_LEDS[GZ_TTT_cells[wscrx[0]][k]]=player_x_marked_color
                    GZ_LEDS.write()
                for m in range(4):
                    GZ_LEDS[GZ_TTT_cells[wscrx[1]][m]]=player_x_marked_color
                    GZ_LEDS.write()
                for l in range(4):
                    GZ_LEDS[GZ_TTT_cells[wscrx[2]][l]]=player_x_marked_color
                    GZ_LEDS.write()
                y=0
                border()
                sleep(500)
                music.play(music.NYAN,pin2)
                #music.play(music.NYAN)
                
                gameplay=1
                z=""
                randomvar=1
        elif z=="o":
            if randomvar==0:
                for i in range(9):
                    for j in range(4):
                        GZ_LEDS[GZ_TTT_cells[i+1][j]]=no_color
                        GZ_LEDS.write()
                for k in range(4):
                    GZ_LEDS[GZ_TTT_cells[wscro[0]][k]]=player_o_marked_color
                    GZ_LEDS.write()
                for m in range(4):
                    GZ_LEDS[GZ_TTT_cells[wscro[1]][m]]=player_o_marked_color
                    GZ_LEDS.write()
                for l in range(4):
                    GZ_LEDS[GZ_TTT_cells[wscro[2]][l]]=player_o_marked_color
                    GZ_LEDS.write()
                y=0
                border()
                sleep(500)
                music.play(music.NYAN,pin2)
                #music.play(music.NYAN)
                
                gameplay=1
                z=""
                randomvar=1
                
def reset():
    global game, gameplay
    if gameplay==0:
        if game[0][0]!="":
            if game[1][0]!="":
                if game[2][0]!="":
                    if game[3][0]!="":
                        if game[4][0]!="":
                            if game[5][0]!="": 
                                if game[6][0]!="":
                                    if game[7][0]!="":
                                        if game[8][0]!="":
                                            wins()
                                            winning()
                                            gameplay=1
                
def gamereset():
    global gameplay, player_list_o, player_list_x, game, on, player_possible, current_player, y,current_TTT_cell, move, movement, ppc, randomvar, winpx, winpo, wscrx, wscro
    if gameplay==1:
        for i in range(9):
            for k in range(4):
                GZ_LEDS[GZ_TTT_cells[i+1][k]]=no_color
                GZ_LEDS.write()
        player_list_o.clear()
        player_list_x.clear()
        game=[[''],[''],['']
         ,[''],[''],['']
         ,[''],[''],['']]
        on=0
        player_possible=""
        current_player=""
        ppc=0
        current_TTT_cell = 0
        randomvar=0
        gameplay=0
        y=0
        movement=0
        move=0
        on=0
        winpx=0
        wscrx=[]
        wscro=[]
        winpo=0
        xborder1=2
        xborder2=5
        yborder1=16
        yborder2=40
        y=0
        if y==0:
            for i in range(8):
                GZ_LEDS[xborder1]=no_color
                GZ_LEDS[xborder2]=no_color
                xborder2+=8
                xborder1+=8
                y=1
        if y==1:
            for i in range(8):
                GZ_LEDS[yborder1]=no_color
                GZ_LEDS[yborder2]=no_color
                yborder1+=1
                yborder2+=1
                y=2
        GZ_LEDS.write()
        y=0
        gameplay=3
        
    if gameplay==3:
        if pin12.read_digital()==0 or pin13.read_digital()==0 or pin14.read_digital()==0 or pin15.read_digital()==0 or pin16.read_digital()==0 or pin8.read_digital()==0:
            gameplay=0
 
while True:
    player()
    disp()
    player_save()
    gz_input()
    moving_the_box()
    selection_box()
    display_gz()
    remove_list_duplicates()
    wins()
    reset()
    gamereset()
    winning()
    
