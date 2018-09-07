import random, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def shell_sort(list_number):
     
    list_size = len(list_number)
    gap = list_size//2
 
    while gap > 0:
 
        for i in range(gap,list_size):
 
            temp = list_number[i]
            yield list_number
            j = i
            while  j >= gap and list_number[j-gap] >temp:
                list_number[j] = list_number[j-gap]
                j -= gap
            list_number[j] = temp
        gap //= 2
    

if __name__ == "__main__":
    a = [x + 1 for x in range(100)]
    random.seed(time.time())
    random.shuffle(a)
    N = len(a)
    title = "Shell sort"
    generator = shell_sort(a)

    fig, ax = plt.subplots()
    ax.set_title(title)


    bar_rects = ax.bar(range(len(a)), a, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(a, rects, iteration):
        for rect, val in zip(rects, a):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()

