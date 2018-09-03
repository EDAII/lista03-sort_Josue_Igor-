import pylab
import random
import os
import imageio

def selectionsort_anim(a):
    x = range(len(a))
    for j in range(len(a)-1):
        iMin = j
        for i in range(j+1,len(a)):
            if a[i] < a[iMin]: # find the smallest value
                iMin = i
            if iMin != j: # place the value into its proper location
                a[iMin], a[j] = a[j], a[iMin]
  # plotting
        pylab.plot(x,a,'k.',markersize=6)
        pylab.savefig("images/img" + '%04d' % j + ".png")
        pylab.clf() # figure clear

# running the algorithm
a = random.sample(range(1000),100)
selectionsort_anim(a) # sorting
png_dir = 'images/'
images = []
name = "img00"
i = 0;
for file_name in os.listdir(png_dir):

    if(i<10):
        num_str = str(i)
        name_file = name + "0" + num_str + ".png"
        print(name_file)
    else:
        num_str = str(i)
        name_file = name + num_str+".png"
        print(name_file)
    if os.path.basename(name_file):
        print("entrei aqui")
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))

    i+=1

imageio.mimsave('grics.gif', images)
