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

def merge_sort(list_number, start, end):
    if end <= start:
        return

    middle = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(list_number, start, middle)
    yield from merge_sort(list_number, middle + 1, end)
    yield from merge(list_number, start, middle, end)
    yield list_number

def merge(list_number, start, middle, end):

    merged = []
    left_list = start
    right_list = middle + 1

    while left_list <= middle and right_list <= end:
        if list_number[left_list] < list_number[right_list]:
            merged.append(list_number[left_list])
            left_list += 1
        else:
            merged.append(list_number[right_list])
            right_list += 1

    while left_list <= middle:
        merged.append(list_number[left_list])
        left_list += 1

    while right_list <= end:
        merged.append(list_number[right_list])
        right_list += 1

    for i, sorted_val in enumerate(merged):
        list_number[start + i] = sorted_val
        yield list_number


if __name__ == "__main__":
    numbers_elements = int(input("Digite o numero de elementos a serem ordenados: "))
    algorithm_sorted_type = "Escolha o algoritimo de ordenacao:\n(m)erge \n(s)hell\n"
    method = input(algorithm_sorted_type)

    list_numbers = random.sample(range(numbers_elements), numbers_elements)
    # list_numbers = [x + 1 for x in range(numbers_elements)]
    # random.seed(time.time())
    # random.shuffle(list_numbers)

    if method == "s":
        title_algorithm = "Shell sort"
        generator = shell_sort(list_numbers)
    elif method == "m":
        title_algorithm = "Merge sort"
        generator = merge_sort(list_numbers, 0, numbers_elements - 1)
    else:
        print("Opcao Invalida")

    fig, ax = plt.subplots()
    ax.set_title(title_algorithm)


    bar_rects = ax.bar(range(len(list_numbers)), list_numbers, align="edge")

    ax.set_xlim(0, numbers_elements)
    ax.set_ylim(0, int(1.07 * numbers_elements))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(list_numbers, rects, iteration):
        for rect, val in zip(rects, list_numbers):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()
