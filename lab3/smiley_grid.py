# smiley_grid.py
from smiley import draw_smiley

def draw_smiley_line(y, size, n):
    for i in range(n):
        x = i*size
        draw_smiley(canvas, x, y, size)

def draw_smiley_grid(size, n):
    for i in range(n):
        draw_smiley_line(i*size, size, n)
    
if __name__ == '__main__':
    from uib_inf100_graphics.simple import canvas, display
    draw_smiley_grid(70, 5)
    display(canvas)
