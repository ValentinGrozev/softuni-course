def draw_figure(number):
    if number == 0:
        return

    print("*" * number)

    draw_figure(number - 1)

    print("#" * number)


element = int(input())
draw_figure(element)
