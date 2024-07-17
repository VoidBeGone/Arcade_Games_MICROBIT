import machine
machine.mem32[0x50000708]=0x703
from microbit import*
import neopixel, random 
GZ_LEDS = neopixel.NeoPixel(pin0,64)
isthereablock="no"
ppc=0
spawn=(3,4)
usetemp=0
start=0
currenttempshape=""
newshape=0
rotation=0
ingamestuff=[0]
zain=0
randomblock=0
ranonvar=0
randomlist=[]
winninglist=[[56,57,58,59,60,61,62,63],[48,49,50,51,52,53,53,55],[40,41,42,43,44,45,46,47],[32,33,34,35,36,37,38,39],[24,25,26,27,28,29,30,31,32],[16,17,18,19,20,21,22,23],[8,9,10,11,12,13,14,15]]
madvar=0
randomvar2=0
spacesave=0
peterlist=[]
otherlist=[]
outoflist=[]
def choosing_block_random():
    global randomblock, spacesave
    if newshape==0:
        randomblock=random.randint(1,2)
        spacesave=0
def line():
    global usetemp,currenttempshape,newshape,ranonvar, rotation, randomblock, ppc
    if newshape==0 and randomblock==1:
            rotation=0
            usetemp=2
            for i in range(2):
                usetemp+=1
                GZ_LEDS[usetemp]=(1,1,2)
                GZ_LEDS.write()
            currenttempshape="line"
            newshape=1
            ranonvar=0
            ppc=0
def box():
    global usetemp,currenttempshape,newshape,ranonvar, rotation, ppc
    if newshape==0 and randomblock==2:
            rotation=0
            usetemp=3
            GZ_LEDS[usetemp]=(2,0,2)
            GZ_LEDS[usetemp+1]=(2,0,2)
            GZ_LEDS[usetemp+8]=(2,0,2)
            GZ_LEDS[usetemp+9]=(2,0,2)
            usetemp=11
            GZ_LEDS.write()
            currenttempshape="box"
            newshape=1
            ppc=0
            ranonvar=0
def player_input():
    global ppc, zain
    if pin13.read_digital()==0:
        ppc=130
    elif pin13.read_digital()==1 and ppc==130:
        ppc=0
    elif pin12.read_digital()==0:
        ppc=120
    elif pin12.read_digital()==1 and ppc==120:
        ppc=0
    elif pin14.read_digital()==0:
        ppc=140
    elif pin14.read_digital()==1 and ppc==140:
        ppc=0
    elif pin8.read_digital()==0:
        ppc=80
        zain=0
    elif pin8.read_digital()==1 and ppc==80:
        ppc=0
        zain=1
def dropping():
    global ppc, usetemp, currenttempshape, rotation, newshape, ranonvar, madvar
    for i in range(10):
        sleep(100)
        player_input()
        movement()
        rotation_block()
        winning_stuff()
        if ppc==0:
            player_input()
            movement()
            winning_stuff()
    if currenttempshape=="line":
                                if rotation==0:
                                    checking_move()
                                    if madvar==0 and usetemp+8<64:
                                            sleep(100)
                                            bruh=usetemp
                                            usetemp+=8
                                            GZ_LEDS[usetemp]=(1,1,2)
                                            GZ_LEDS[usetemp-1]=(1,1,2)
                                            GZ_LEDS.write()
                                            GZ_LEDS[bruh-1]=(0,0,0)
                                            GZ_LEDS[bruh]=(0,0,0)
                                            GZ_LEDS.write()
                                    elif madvar>0:
                                        ppc=0
                                        sleep(100)
                                        GZ_LEDS[usetemp]=(1,1,2)
                                        GZ_LEDS[usetemp-1]=(1,1,2)
                                        GZ_LEDS.write()
                                        saving_block_space()
                                        winning_stuff()
                                if rotation==1:
                                    checking_move()
                                    if madvar==0 and usetemp+16<64:
                                            sleep(100)
                                            bruh=usetemp
                                            usetemp+=8
                                            GZ_LEDS[usetemp]=(1,1,2)
                                            GZ_LEDS[usetemp+8]=(1,1,2)
                                            GZ_LEDS[bruh]=(0,0,0)
                                            GZ_LEDS.write()
                                    elif madvar>0 and usetemp+8<56:
                                            ppc=0
                                            sleep(100)
                                            bruh=usetemp
                                            GZ_LEDS[usetemp]=(1,1,2)
                                            GZ_LEDS[usetemp+8]=(1,1,2)
                                            GZ_LEDS.write()
                                            saving_block_space()
                                            winning_stuff()
    elif currenttempshape=="box":
                                checking_move()
                                if usetemp+8<64:
                                    checking_move()
                                    if madvar<1:
                                            sleep(100)
                                            bruh=usetemp
                                            usetemp+=8
                                            GZ_LEDS[bruh]=(2,0,2)
                                            GZ_LEDS[bruh+1]=(2,0,2)
                                            GZ_LEDS[usetemp]=(2,0,2)
                                            GZ_LEDS[usetemp+1]=(2,0,2)
                                            GZ_LEDS[bruh-7]=(0,0,0)
                                            GZ_LEDS[bruh-8]=(0,0,0)
                                            GZ_LEDS.write()
                                    elif madvar>0:
                                            sleep(100)
                                            bruh=usetemp
                                            GZ_LEDS[usetemp]=(2,0,2)
                                            GZ_LEDS[usetemp+1]=(2,0,2)
                                            GZ_LEDS[usetemp-7]=(2,0,2)
                                            GZ_LEDS[usetemp-8]=(2,0,2)
                                            GZ_LEDS.write()
                                            saving_block_space()
                                            winning_stuff()
def movement():
    global currenttempshape, ppc, usetemp, newshape,ingamestuff,currenttempshape,ranonvar, rotation, madvar
    if currenttempshape=="line":
        if rotation==0:
            if ppc==130 and usetemp<56:
                    sleep(100)
                    bruh=usetemp
                    if usetemp!=7 and usetemp!=15 and usetemp!=23 and usetemp!=31 and usetemp!=39 and usetemp!=47 and usetemp!=55:
                        usetemp+=1
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp-1]=(1,1,2)
                        GZ_LEDS.write()
                        GZ_LEDS[bruh-2]=(0,0,0)
                        GZ_LEDS[bruh-1]=(0,0,0)
                        GZ_LEDS.write()
            elif ppc==120 and usetemp<56:
                    sleep(100)
                    bruh=usetemp
                    if (usetemp-1)%8!=0:
                        usetemp-=1
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp-1]=(1,1,2)
                        GZ_LEDS.write()
                        GZ_LEDS[bruh+1]=(0,0,0)
                        GZ_LEDS[bruh]=(0,0,0)
                        GZ_LEDS.write()
            elif ppc==140:
                checking_move()
                if madvar==0 and usetemp<56:
                        sleep(50)
                        bruh=usetemp
                        usetemp=usetemp+8
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp-1]=(1,1,2)
                        GZ_LEDS.write()
                        GZ_LEDS[bruh-1]=(0,0,0)
                        GZ_LEDS[bruh]=(0,0,0)
                        GZ_LEDS.write()
                elif madvar>0 and usetemp<56:
                        ppc=0
                        sleep(50)
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp-1]=(1,1,2)
                        GZ_LEDS.write()
                        saving_block_space()
        elif rotation==1:
            if ppc==130 and usetemp<48:
                    sleep(100)
                    bruh=usetemp
                    if usetemp!=7 and usetemp!=15 and usetemp!=23 and usetemp!=31 and usetemp!=39 and usetemp!=47 and usetemp!=55:
                        usetemp+=1
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp+8]=(1,1,2)
                        GZ_LEDS.write()
                        GZ_LEDS[bruh]=(0,0,0)
                        GZ_LEDS[bruh+8]=(0,0,0)
                        GZ_LEDS.write()
            elif ppc==120 and usetemp+8<56:
                    sleep(100)
                    bruh=usetemp
                    if (usetemp)%8!=0:
                        usetemp-=1
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp+8]=(1,1,2)
                        GZ_LEDS.write()
                        GZ_LEDS[bruh]=(0,0,0)
                        GZ_LEDS[bruh+8]=(0,0,0)
                        GZ_LEDS.write()
            elif ppc==140:
                checking_move()
                if madvar==0:
                    if usetemp+8<56:
                        sleep(50)
                        bruh=usetemp
                        usetemp+=8
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[usetemp+8]=(1,1,2)
                        GZ_LEDS[bruh]=(0,0,0)
                        GZ_LEDS.write()
                elif madvar>0:
                    ppc=0
                    sleep(50)
                    bruh=usetemp
                    GZ_LEDS[usetemp]=(1,1,2)
                    GZ_LEDS[usetemp+8]=(1,1,2)
                    GZ_LEDS.write()
                    saving_block_space()     
    if currenttempshape=="box" and ppc==130 and usetemp!=6 and usetemp!=14 and usetemp!=22 and usetemp!= 30 and usetemp!=38 and usetemp!=46 and usetemp!=54 and usetemp<56:
                    sleep(100)
                    bruh=usetemp
                    usetemp+=1
                    GZ_LEDS[usetemp]=(2,0,2)
                    GZ_LEDS[usetemp-8]=(2,0,2)
                    GZ_LEDS[usetemp-7]=(2,0,2)
                    GZ_LEDS[usetemp+1]=(2,0,2)
                    GZ_LEDS[bruh]=(0,0,0)
                    GZ_LEDS[bruh-8]=(0,0,0)
                    GZ_LEDS.write()            
    elif currenttempshape=="box" and ppc==120 and usetemp%8!=0 and usetemp<56:
                    sleep(100)
                    bruh=usetemp
                    usetemp-=1
                    GZ_LEDS[usetemp]=(2,0,2)
                    GZ_LEDS[usetemp-8]=(2,0,2)
                    GZ_LEDS[usetemp-7]=(2,0,2)
                    GZ_LEDS[usetemp+1]=(2,0,2)
                    GZ_LEDS[bruh+1]=(0,0,0)
                    GZ_LEDS[bruh-7]=(0,0,0)
                    GZ_LEDS.write()
    elif ppc==140 and currenttempshape=="box":
            checking_move()
            if madvar==0 and usetemp<55:
                            sleep(50)
                            bruh=usetemp
                            usetemp+=8
                            GZ_LEDS[bruh]=(2,0,2)
                            GZ_LEDS[bruh+1]=(2,0,2)
                            GZ_LEDS[usetemp]=(2,0,2)
                            GZ_LEDS[usetemp+1]=(2,0,2)
                            GZ_LEDS[bruh-7]=(0,0,0)
                            GZ_LEDS[bruh-8]=(0,0,0)
                            GZ_LEDS.write()
            if madvar>0:
                        ppc=0
                        sleep(50)
                        bruh=usetemp
                        GZ_LEDS[usetemp]=(2,0,2)
                        GZ_LEDS[usetemp+1]=(2,0,2)
                        GZ_LEDS[usetemp-7]=(2,0,2)
                        GZ_LEDS[usetemp-8]=(2,0,2)
                        GZ_LEDS.write()
                        saving_block_space()
def saving_block_space():
    global usetemp, ingamestuff, currenttempshape, ranonvar, rotation
    if currenttempshape=="line" and rotation==0:
            ingamestuff.append(usetemp)
            ingamestuff.append(usetemp-1)
            space_saver()
    elif currenttempshape=="line" and rotation==1:
                ingamestuff.append(usetemp)
                ingamestuff.append(usetemp+8)
                space_saver()
    elif currenttempshape=="box":
            ingamestuff.append(usetemp)
            ingamestuff.append(usetemp+1)
            ingamestuff.append(usetemp-8)
            ingamestuff.append(usetemp-7)
            space_saver()
        
def saving_block():
    global usetemp, newshape,ingamestuff,currenttempshape,ranonvar, rotation
    if ranonvar==0 and currenttempshape=="line" and usetemp>55:
                saving_block_space()
    elif ranonvar==0 and currenttempshape=="line" and usetemp+8>=55:
                saving_block_space()
    elif ranonvar==0 and currenttempshape=="box" and usetemp>55:
                saving_block_space()                   
def rotation_block():
    global ppc, usetemp, currenttempshape, rotation, zain
    if currenttempshape=="line" and rotation==0 and ppc==80 and zain==0:
                    sleep(100)
                    bruh=usetemp
                    if 7<usetemp<56:
                        usetemp-=8
                        GZ_LEDS[usetemp]=(1,1,2)
                        GZ_LEDS[bruh]=(1,1,2)
                        GZ_LEDS.write()
                        GZ_LEDS[bruh-1]=(0,0,0)
                        GZ_LEDS.write()
                        rotation=1
                        zain=1
    elif currenttempshape=="line" and rotation==1 and ppc==80 and zain==0:
                    sleep(100)
                    bruh=usetemp
                    if 7<usetemp<56 and usetemp%8!=0:
                            usetemp+=8
                            GZ_LEDS[usetemp]=(1,1,2)
                            GZ_LEDS[usetemp-1]=(1,1,2)
                            GZ_LEDS.write()
                            GZ_LEDS[bruh]=(0,0,0)
                            GZ_LEDS.write()
                            rotation=0
                            zain=1
def space_saver():
    global rotation, newshape, currenttempshape,rotation, ranonvar, spacesave,madvar
    if spacesave==0:
        madvar=0
        rotation=0
        newshape=0
        currenttempshape=""
        rotation=0
        ranonvar=1
        spacesave=1
        
def checking_move():
    global madvar, currenttempshape, ppc, ingamestuff, usetemp
    if currenttempshape=="box" and ppc==140:
            for i in range(len(ingamestuff)):
                if usetemp+8==ingamestuff[i] or usetemp+9==ingamestuff[i]:
                    madvar+=1
    elif ppc==0 and currenttempshape=="box":
            for i in range(len(ingamestuff)):
                if usetemp+8==ingamestuff[i] or usetemp+9==ingamestuff[i]:
                    madvar+=1
    elif currenttempshape=="line" and rotation==0:
            for i in range(len(ingamestuff)):
                if usetemp+8==ingamestuff[i] or usetemp+7==ingamestuff[i]:
                    madvar+=1
    elif rotation==1 and currenttempshape=="line":
            for i in range(len(ingamestuff)):
                if usetemp+16 ==ingamestuff[i]:
                    madvar+=1
                    
def winning_stuff():
    global ingamestuff, winninglist, randomlist, randomvar2, peterlist, otherlist, outoflist
    if len(ingamestuff)>=8:
        ingamestuff.sort(reverse=True)
        randomlist5=[]
        listout=[]
        listin=[]
        outoflist.clear()
        for p in range(len(ingamestuff)):
            outoflist.append(ingamestuff[p])
        for i in range(len(winninglist)):
            randomvar2=0
            for h in range(8):
                for j in range(len(ingamestuff)):
                    if ingamestuff[j]==winninglist[i][h]:
                        randomvar2+=1
                        randomlist.append(ingamestuff[j])
                        remove_list_duplicates()
            if i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6:
                if randomvar2!=8:
                    randomlist.clear()
                if randomvar2==8:
                    randomvar2=0
                    if i!=1:
                        for s in range(len(randomlist)):
                            ingamestuff.remove(randomlist[s])#i mean this line 
                            #this is the line where you cant clear a line above it
                            outoflist.remove(randomlist[s]) 
                            GZ_LEDS[randomlist[s]]=(0,0,0)
                            GZ_LEDS.write()
                            randomlist.sort()
                        for m in range(len(ingamestuff)):
                                if i==0:
                                    if 0<ingamestuff[m]<56:
                                            listout.append(ingamestuff[m])
                                            listin.append(ingamestuff[m]+8)
                                if i==2:
                                    if 0<ingamestuff[m]<40:
                                                listout.append(ingamestuff[m])
                                                listin.append(ingamestuff[m]+8)
                                if i==3:
                                    if 0<ingamestuff[m]<32:
                                        listout.append(ingamestuff[m])
                                        listin.append(ingamestuff[m]+8)
                                if i==4:
                                    if 0>ingamestuff[m]<24:
                                        listout.append(ingamestuff[m])
                                        listin.append(ingamestuff[m]+8)
                                if i==5:
                                   if 0>ingamestuff[m]<16:
                                        listout.append(ingamestuff[m])
                                        listin.append(ingamestuff[m]+8)
                        for h in range(len(listout)):
                            ingamestuff.remove(listout[h])
                            GZ_LEDS[listout[h]]=(0,0,0)
                        for g in range(len(listin)):
                            ingamestuff.append(listin[g])
                            GZ_LEDS[listin[g]]=(0,0,5)
                        GZ_LEDS.write() 
                    if i==1:
                        sad=7
                        if sad==7:
                            pls=[48,49,50,51,52,53,54,55]
                            for w in range(len(pls)):
                                    ingamestuff.remove(pls[w])
                                    outoflist.remove(pls[w]) 
                                    GZ_LEDS[pls[w]]=(0,0,0)
                                    GZ_LEDS.write()
                                    randomlist.sort()
                            for m in range(len(ingamestuff)):
                                    if 0<ingamestuff[m]<48:
                                        listout.append(ingamestuff[m])
                                        listin.append(ingamestuff[m]+8)
                            for h in range(len(listout)):
                                ingamestuff.remove(listout[h])
                                GZ_LEDS[listout[h]]=(0,0,0)
                            for g in range(len(listin)):
                                ingamestuff.append(listin[g])
                                GZ_LEDS[listin[g]]=(0,0,5)
                            GZ_LEDS.write() 
                            sad=0
                randomlist5.clear(), listin.clear(), listout.clear(), otherlist.clear(), peterlist.clear(), randomlist.clear()                
def remove_list_duplicates():
    global randomlist
    randomlist=list(dict.fromkeys(randomlist))
while True:
    choosing_block_random()
    line()
    box()
    player_input()
    movement()
    rotation_block()
    dropping()
    saving_block()
    winning_stuff()
    
        
