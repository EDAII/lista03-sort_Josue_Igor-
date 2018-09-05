import pylab
import random
import os
import imageio
import numpy as np
def selectionsort_anim(a):
    x = range(len(a))
    for j in range(len(a)-1):
        iMin = j
        for i in range(j+1,len(a)):
            if a[i] < a[iMin]: 
                iMin = i
            if iMin != j:
                a[iMin], a[j] = a[j], a[iMin]

        pylab.plot(x,a,'k.',markersize=6)
        pylab.savefig("images/img" + '%04d' % j + ".png")
        pylab.clf()

a = random.sample(range(1000),100)
selectionsort_anim(a)
png_dir = 'images/'
images = []
name = "img00"
i = 0;
for file_name in os.listdir(png_dir):

    if(i<10):
        num_str = str(i)
        name_file = name + "0" + num_str + ".png"
    else:
        num_str = str(i)
        name_file = name + num_str+".png"
    if os.path.abspath(name_file):
        file_path = os.path.join(png_dir, name_file)
        images.append(imageio.imread(file_path))

    i+=1

imageio.mimsave('grics.gif', images, duration = 0.5)
