from microbit import*
import radio 
radio.on()
radiox=1
radio.config(group=radiox)
rrr=""
onf=0
ppc=0
player="x"
scr=0
vib=1
win=0
y=0
x=0
winp=0
player_list=[]
number_press=0
rad1=0
rad2=0
rad3=0
s=0
def logo():
    global radiox, onf
    if pin_logo.is_touched():
        if onf==1:
            radio.on()
            radio.config(group=radiox)
            display.show(Image.HAPPY)
            sleep(500)
            display.clear()
            onf=0
        elif onf==0:
            radio.off()
            display.show(Image.SAD)
            sleep(500)
            display.clear()
            onf=1

def screen():
    global scr, player, radiox,win
    if scr==0: 
        if player=="x":
            display.show(Image("90009:"
                            "09090:"
                          "00900:"
                          '09090:'
                          '90009'))
        elif player=="o":
            display.show(Image("09990:"
                            "90009:"
                          "90009:"
                          '90009:'
                          '09990'))
    elif scr==1:
        display.clear()
    elif win==1:
        display.show(Image.SURPRISED)
        
        
def sendwin():
    global rad1, rad2, rad3, win, s, vib
    if win==1:
       if s==0:
           for i in range(9):
               radio.config(group=i+1)
               radio.send("off")
               radio.send("off")
               radio.send("off")
           radio.config(group=rad1)
           radio.send("win")
           radio.config(group=rad2)
           radio.send("win")
           radio.config(group=rad3)
           radio.send("win")
           s=1
           vib=2
        
def vibrate():
    global vib, ppc
    if vib==0:
        pin1.write_digital(1)
        sleep(200)
        vib=1
    elif vib==1:
        pin1.write_digital(0)
    elif vib==2:
        pin1.write_digital(1)
        sleep(300)
        vib=1
        
def mb_input():
    global player, scr
    if button_b.get_presses():
        if player=="x":
            player="o"
        elif player=="o":
            player="x"
        scr=0
    elif button_a.get_presses():
        if player=="x":
            player="o"
        elif player=="o":
            player="x"
        scr=0
        
def radioC():
    global ppc, y, radiox, scr
    if ppc==130:
        scr=3
        if y==0:
            if radiox<9:
                radiox=radiox+1
                display.show(radiox)
                y=1
                sleep(500)
    elif ppc==120:
        scr=3
        if y==0:
            if radiox>1:
                radiox=radiox-1
                display.show(radiox)
                y=1
                sleep(500)
    radio.config(group=radiox)
    
def gz_input():
    global ppc, vib, scr, y, player, x
    if pin13.read_digital()==0:
        ppc=130
    elif pin13.read_digital()==1 and ppc==130:
        ppc=131
        scr=0
        y=0
    elif pin12.read_digital()==0:
        ppc=120
    elif pin12.read_digital()==1 and ppc==120:
        ppc=121
        scr=0
        y=0
    elif pin16.read_digital()==0 and ppc==161: 
        ppc=160
        display.clear()
        vib=0
        radio.send(str(player))
        scr=0
    elif pin16.read_digital()==1:
        ppc=161
        x=0

        
def saving_win():
    global ppc, radiox, x, player_list
    rrr=radio.receive()
    if rrr=="nice":
        player_list.append(radiox)
 

    
def remove_list_duplicates():
    global player_list
    player_list=list(dict.fromkeys(player_list))

    
def winning():
    global winp, win,scr, ppc, player_list,  rad1, rad2, rad3
    win_list = [ [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [1, 4, 7],
                  [2,5,8],
                  [3,6,9],
                  [1,5,9],
                   [3,5,7]]    
    player_list.sort()
    if len(player_list)>2:
        for i in range(len(win_list)):
           for h in range(len(player_list)): 
              if win_list[i][0]== player_list[h]:
                  for m in range(len(player_list)):
                      if win_list[i][1]==player_list[m]:
                          for l in range(len(player_list)):
                             if win_list[i][2]==player_list[l]:
                                 winp=3     
                                 rad1=player_list[h]
                                 rad2=player_list[m]
                                 rad3=player_list[l]
                             else:
                                 winp=winp
        
    if winp==3: 
       scr=4
       win=1

    
        
def radio_rec():
    global rrr, scr, x, onf, radiox
    if onf==0:
        rrr=str(radio.receive())
        if rrr=="nice":
            scr=3
            player_list.append(radiox)
            display.show(Image.HAPPY)
            x=1
            sleep(500)
            scr=0
        elif rrr=="alreadyyours":
            scr=3
            x=0
            display.show("?")
            sleep(500)
            scr=0
        elif rrr=="notyours":
            scr=3
            display.show(Image.SAD)
            x=0
            sleep(500)
            scr=0
    
def game_evaluation():
    global rrr
    

def main():
    logo()
    gz_input()
    mb_input()
    screen()
    vibrate()
    radioC()
    radio_rec()
    saving_win()
    remove_list_duplicates()
    winning()
    sendwin()
while True:
    main()

