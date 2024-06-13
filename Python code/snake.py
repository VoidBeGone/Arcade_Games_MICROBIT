from microbit import *
import neopixel
import random
import machine
machine.mem32[0x50000700] = 0x703
gz_led = neopixel.NeoPixel(pin0,64)
snake_colour = (0,5,0)
food_colour = (5,0,0)
no_colour = (0,0,0)
y= []
z=[]
i = 0
m = 9
snake_len = 3
play = True
temp=[]
do = "n"
sigh=0
start=0
stop = 0
var = 0
peterthinkin=0
janiesborderofmexico=[]
x = random.randint(0,64)
snaket=[9]
list2=[]
l=0
dontbreak=0
rand=0
counter=0
def apple():
    global x, i, z, stop, var, j, l,counter
    if stop==0:
            z=0
            if z == 0:
                counter=0
                x = random.randint(0,63)
                z=1
                l=0
            if z==1:
                for i in range(len(janiesborderofmexico)):
                    counter+=1
                    if x == janiesborderofmexico[i]:
                        z = 0
                    elif x!=janiesborderofmexico[i]:
                        l+=1    
                for j in range(len(snaket)):
                    counter+=1
                    if x == snaket[j]:
                        z = 0
                    elif x!=snaket[j]:
                        l+=1
                if l==counter:
                    z=2
                    stop=1
                    counter=0
                    gz_led[x] = food_colour
                    gz_led.write()
def fat():
    global x,snake_len, m,stop
    if stop==1:
        if m==x:
            snake_len+=1
            stop=0
                     
def move():
    global snake_colour, x, y,m, snake_len, direction,temp, i, j, do,sigh,start,peterthinkin, snaket,list2
    if pin13.read_digital() == 0:
        if 2==2:
            m+= 1
            snaket.append(m)
            if len(snaket)==snake_len+1:
                gz_led[snaket[0]]=(0,0,0)
                snaket.remove(snaket[0])
                for i in range(len(snaket)):
                    list2.append(snaket[i])
                list2.reverse()
                for i in range(len(list2)-1):
                    if m==list2[i+1]:
                        display.scroll("Game Over")
                list2.clear()
              
            
        do = "n"
        j = 0
    elif pin14.read_digital() == 0:
         if 2==2:
            m+= 8
            snaket.append(m)
            if len(snaket)==snake_len+1:
                gz_led[snaket[0]]=(0,0,0)
                snaket.remove(snaket[0])
                for i in range(len(snaket)):
                    list2.append(snaket[i])
                list2.reverse()
                for i in range(len(list2)-1):
                    if m==list2[i+1]:
                        display.scroll("Game Over")
                list2.clear()
         do = "n"
         j = 0
    elif pin12.read_digital() == 0:
         if 2==2:
            m-= 1
            snaket.append(m)
            if len(snaket)==snake_len+1:
                gz_led[snaket[0]]=(0,0,0)
                snaket.remove(snaket[0])
                for i in range(len(snaket)):
                    list2.append(snaket[i])
                list2.reverse()
                for i in range(len(list2)-1):
                    if m==list2[i+1]:
                        display.scroll("Game Over")
                list2.clear()
         do = "n"
         j = 0
    elif pin8.read_digital() == 0:
         if 2==2:
            m-=8
            snaket.append(m)# this is currently appending where your going to 
            if len(snaket)==snake_len+1:
                gz_led[snaket[0]]=(0,0,0)
                snaket.remove(snaket[0])
                for i in range(len(snaket)):
                    list2.append(snaket[i])
                list2.reverse()
                for i in range(len(list2)-1):
                    if m==list2[i+1]:
                        display.scroll("Game Over")
                list2.clear()
         do = "n"
         j = 0
    sleep(100)
    gz_led[m] = snake_colour
    sleep(50)
    gz_led.write()
    
def janiesborder():
    global janiesborderofmexico, dontbreak
    if dontbreak==0:
        changethis=0
        for i in range(8):
            gz_led[changethis]=(1,1,1)
            gz_led[changethis+56]=(1,1,1)
            gz_led.write()
            janiesborderofmexico.append(changethis)
            janiesborderofmexico.append(changethis+56)
            changethis+=1
        changethis=0
        for i in range(8):
            gz_led[changethis]=(1,1,1)
            gz_led[changethis+7]=(1,1,1)
            gz_led.write()
            janiesborderofmexico.append(changethis)
            janiesborderofmexico.append(changethis+7)
            changethis+=8
        dontbreak=1

def janiesmurder():
    global janiesborderofmexico, y, m
    if 3==3:
        for i in range(len(janiesborderofmexico)):
            if janiesborderofmexico[i]==m:
                display.scroll("Game Over")
                for m in range(64):
                    gz_led[m] = no_colour


while play == True:
    janiesborder()
    fat()
    move()
    janiesmurder()
    apple()


