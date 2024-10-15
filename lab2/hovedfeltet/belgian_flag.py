
def draw_belgian_flag(canvas, flag_left, top, flag_right, bottom):
    # TOOD: replace this function body with code to draw the Belgian flag
    canvas.create_rectangle(flag_left, top, flag_right, bottom)

    flag_width = flag_right - flag_left
    black_width = flag_width / 3
    black_left = flag_left
    black_right = black_left + black_width
    canvas.create_rectangle(black_left, top, black_right, bottom, fill='black')

    flag_width = flag_right - flag_left
    yellow_width = flag_width / 3
    yellow_left = flag_left + yellow_width
    yellow_right = yellow_left + yellow_width
    canvas.create_rectangle(yellow_left, top, yellow_right, bottom, fill='yellow')

    flag_width = flag_right - flag_left
    red_width = flag_width / 3
    red_left = flag_right - red_width
    red_right = flag_right
    canvas.create_rectangle(red_left, top, red_right, bottom, fill='red')
    ...