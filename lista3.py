import pylab, random
import numpy as np
import imageio
import os, re

def quick_sort(list_for_sort,start, end,k):
    x = range(len(list_for_sort))
    i = start
    j = end-1
    pivot = list_for_sort[start]
    while(i<=j):
        while(list_for_sort[i]<pivot and i<end):
            i +=1

        while(list_for_sort[j]>pivot and j>start):
            j -=1
       
        if(i<=j):
            list_for_sort[i], list_for_sort[j] = list_for_sort[j], list_for_sort[i]
            i +=1
            j -=1
    if(j> start):
        pylab.plot(x,list_for_sort,'k.',markersize=6)
        pylab.savefig("images/img" + '%04d' % j + ".png")
        pylab.clf()
        k +=1
        quick_sort(list_for_sort,start,j+1,k )
    if(i<end):
        pylab.plot(x,list_for_sort,'k.',markersize=6)
        pylab.savefig("images/img" + '%04d' % j + ".png")
        pylab.clf()
        k+=1
        quick_sort(list_for_sort, i, end,k )

values = random.sample(range(1000),100)

k = 0
quick_sort(values,0,100,k)

png_dir = "images/"
images = []
files = os.listdir(png_dir)
ordered_files = sorted(files, key=lambda x: (int(re.sub('\D','',x)),x))
for file_name in ordered_files:
    file_path = os.path.join(png_dir, file_name)
    images.append(imageio.imread(file_path))


imageio.mimsave('grics.gif', images, duration = 0.5)




