import matplotlib.pyplot as plt
file=open("3x_1.txt",'w')
# a=int(input("Enter the value"))
b=2
l=[]
c=[]
while (b<=1000):
    l=[]
    a=b
    file.write(f"{a}")
    if(a<10):
     file.write("    ")
    else:
      file.write("   ")
    while (a!=1):
        if(a % 2 ==0):
         a=a//2 
        else:
         a=(3*a)+1
        l.append(a)
    if(len(l)<10):
     file.write(f"{len(l)}    [{','.join(map(str, l))}]\n")
    if(len(l)>=10):
      file.write(f"{len(l)}   [{','.join(map(str, l))}]\n")
    c.append(len(l))
    b=b+1
plt.plot(c)
plt.grid(True)
plt.show()   
file.close()

import numpy as np
import sounddevice as sd




wave_array = np.array(c)

sd.play(wave_array, samplerate=44100)
sd.wait()  

