import machine
machine.mem32[0x50000708]=0x703
from microbit import*
import neopixel, random
GZ_LEDS = neopixel.NeoPixel(pin0,64)
#32 and 24
#31 an 39
move1=25
move2=30
ppc1=0
ppc2=0
start1=0
start2=0
moveb=27
move1list=[]
move2list=[]
startb=0
listb=[]
startbmove=0
border=[]
LorR=0
touched=0
updown=3
sigh=0
asd=0
def borderg():
    global border
    bro=0
    bro2=56
    for i in range(8):
        GZ_LEDS[bro]=(2,1,3)
        GZ_LEDS[bro2]=(2,1,3)
        GZ_LEDS.write()
        bro2+=1
        bro+=1
    bro=0
    bro2=7
    for i in range(8):
        GZ_LEDS[bro]=(2,1,3)
        GZ_LEDS[bro2]=(2,1,3)
        GZ_LEDS.write()
        bro2+=8
        bro+=8
def player_one():
    global move1, start1,move1list
    if start1==0:
        GZ_LEDS[move1]=(3,3,3)
        GZ_LEDS[move1+8]=(3,3,3)
        GZ_LEDS.write()
        move1list=[move1,move1+8]
        start1=1
        
def player_two():
    global move2,start2, move2list
    if start2==0:
        GZ_LEDS[move2]=(3,3,3)
        GZ_LEDS[move2+8]=(3,3,3)
        GZ_LEDS.write()
        move2list=[move2,move2+8]
        start2=1
        
def player_input():
    global ppc1,ppc2
    if pin14.read_digital()==0:
        ppc1=140
    elif pin14.read_digital()==1 and ppc1==140:
        ppc1=0
    elif pin8.read_digital()==0:
        ppc1=80
    elif pin8.read_digital()==1 and ppc1==80:
        ppc1=0
    elif pin15.read_digital()==0:
        ppc2=150
    elif pin15.read_digital()==1 and ppc2==150:
        ppc2=0
    elif pin16.read_digital()==0:
        ppc2=160
    elif pin16.read_digital()==1 and ppc2==160:
        ppc2=0
        
def movement_player_one():
    global ppc1, move1, move2,ppc2, move2list, move1list
    if ppc1==80:
        if move1!=9:
            sleep(150)
            oldmove1=move1
            move1=move1-8
            GZ_LEDS[move1]=(3,3,3)
            GZ_LEDS[move1+8]=(3,3,3)
            GZ_LEDS[oldmove1+8]=(0,0,0)
            GZ_LEDS.write()
            move1list=[move1, move1+8]
            ppc1=0
    elif ppc1==140:
        if move1+8!=49:
            sleep(150)
            oldmove1=move1
            move1=move1+8
            GZ_LEDS[move1]=(3,3,3)
            GZ_LEDS[move1+8]=(3,3,3)
            GZ_LEDS[oldmove1]=(0,0,0)
            GZ_LEDS.write()
            move1list=[move1,move1+8]
            ppc2=0
    elif ppc2==150:
        if move2!=14:
            sleep(150)
            oldmove2=move2
            move2=move2-8
            GZ_LEDS[move2]=(3,3,3)
            GZ_LEDS[move2+8]=(3,3,3)
            GZ_LEDS[oldmove2+8]=(0,0,0)
            GZ_LEDS.write()
            move2list=[move2,move2+8]
            ppc2=0
    elif ppc2==160:
        if move2+8!=54:
            sleep(150)
            oldmove2=move2
            move2=move2+8
            GZ_LEDS[move2]=(3,3,3)
            GZ_LEDS[move2+8]=(3,3,3)
            GZ_LEDS[oldmove2]=(0,0,0)
            GZ_LEDS.write()
            move2list=[move2,move2+8]
            ppc2=0
            
def ball():
    global moveb, startb, listb,startbmove, LorR, touched, asd, updown, sigh
    if startb==0:
        GZ_LEDS[moveb]=(3,0,0)
        GZ_LEDS[moveb+8]=(3,0,0)
        GZ_LEDS[moveb+9]=(3,0,0)
        GZ_LEDS[moveb+1]=(3,0,0)
        GZ_LEDS.write()
        listb=[moveb,moveb+8,moveb+1,moveb+9]
        startb=1
    if startbmove==0:
        LorR=random.randint(0,1)
        startbmove=1
    if LorR==0:
        if asd==0:
            sleepfunc()
            movepast=moveb
            moveb-=1
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast+1]=(0,0,0)
            GZ_LEDS[movepast+9]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=1
        elif updown==0:
            sleepfunc()
            movepast=moveb
            moveb-=8
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast+8]=(0,0,0)
            GZ_LEDS[movepast+9]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=1
            updown=3
        elif updown==1:
            sleepfunc()
            movepast=moveb
            moveb+=8
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast]=(0,0,0)
            GZ_LEDS[movepast+1]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=1
            updown=3
        elif asd==1:
            sleepfunc()
            movepast=moveb
            moveb-=1
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast+1]=(0,0,0)
            GZ_LEDS[movepast+9]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=2
        elif asd==2:
            asd=3
            sleepfunc()
            movepast=moveb
            moveb-=1
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast+1]=(0,0,0)
            GZ_LEDS[movepast+9]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]

    elif LorR==1:
        if asd==0:
            sleepfunc()
            movepast=moveb
            moveb+=1
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast]=(0,0,0)
            GZ_LEDS[movepast+8]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=1
        elif updown==0:
            sleepfunc()
            movepast=moveb
            moveb-=8
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast+8]=(0,0,0)
            GZ_LEDS[movepast+9]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=1
            updown=3
        elif updown==1:
            sleepfunc()
            movepast=moveb
            moveb+=8
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast]=(0,0,0)
            GZ_LEDS[movepast+1]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=1
            updown=3
        elif asd==1:
            sleepfunc()
            movepast=moveb
            moveb+=1
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast]=(0,0,0)
            GZ_LEDS[movepast+8]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
            asd=2
        elif asd==2:
            asd=3
            sleepfunc()
            movepast=moveb
            moveb+=1
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast]=(0,0,0)
            GZ_LEDS[movepast+8]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
def testingball():
    global LorR, listb, moveb, move1list, move2list,asd,start1,start2, sigh, updown
    if len(listb)!=0 and len(move1list)!=0 and len(move2list)!=0:
        if listb[0]-1==move1list[0] or listb[0]-1==move1list[1] or listb[1]-1==move1list[0] or listb[1]-1==move1list[1]:
            if listb[0]-1==move1list[0] and listb[1]-1==move1list[1]:
                LorR=1
                asd=0
            elif listb[0]-1==move1list[1] and listb[1]-1!=move1list[0]:
                LorR=1
                asd=0
                updown=1
                sigh=0
            elif listb[1]-1==move1list[0] and listb[0]-1!=move1list[1]:
                LorR=1
                asd=0
                updown=0
                sigh=0
        elif listb[2]+1==move2list[0] or listb[3]+1==move2list[0] or listb[2]+1==move2list[1] or listb[3]+1==move2list[1]:
            if listb[2]+1==move2list[0] and listb[3]+1==move2list[1]:
                LorR=0
                asd=0
            elif listb[2]+1==move2list[1] and listb[3]+1!=move2list[0]:
                LorR=0
                asd=0
                updown=1
                sigh=0
            elif listb[3]+1==move2list[0] and listb[2]+1!=move2list[1]:
                LorR=0
                asd=0
                updown=0
                sigh=0
def sleepfunc():
    for i in range(10):
        sleep(10)
        player_one()
        player_two()
        player_input()
        movement_player_one()
def janiesucks():
    global LorR, asd
    if asd==3:
        if LorR==0:
            lol=0
            for i in range(64):
                GZ_LEDS[lol]=(25,25,25)
                lol+=1
                GZ_LEDS.write()
            sleep(500)
            lol=0
            for i in range(64):
                GZ_LEDS[lol]=(0,0,0)
                lol+=1
                GZ_LEDS.write()
            asd=4
        if LorR==1:
            lol=0
            for i in range(64):
                GZ_LEDS[lol]=(25,25,25)
                lol+=1
                GZ_LEDS.write()
            sleep(500)
            lol=0
            for i in range(64):
                GZ_LEDS[lol]=(0,0,0)
                lol+=1
                GZ_LEDS.write()
            asd=4
def touchingborder():
    global listb, moveb
    if listb[0]==1 or listb[0]==2 or listb[0]==3 or listb[0]==4 or listb[0]==5 or listb[0]==6:
            sleepfunc()
            movepast=moveb
            moveb+=8
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast]=(0,0,0)
            GZ_LEDS[movepast+1]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
    elif listb[1]==57 or listb[1]==58 or listb[1]==59 or listb[1]==60 or listb[1]==61 or listb[1]==62:
            sleepfunc()
            movepast=moveb
            moveb-=8
            GZ_LEDS[moveb]=(3,0,0)
            GZ_LEDS[moveb+8]=(3,0,0)
            GZ_LEDS[moveb+9]=(3,0,0)
            GZ_LEDS[moveb+1]=(3,0,0)
            GZ_LEDS[movepast+8]=(0,0,0)
            GZ_LEDS[movepast+9]=(0,0,0)
            GZ_LEDS.write()
            listb=[moveb,moveb+8,moveb+1,moveb+9]
while True:
    borderg()
    testingball()
    player_one()
    player_two()
    player_input()
    ball()
    touchingborder()
    movement_player_one()
    #janiesucks()
 

