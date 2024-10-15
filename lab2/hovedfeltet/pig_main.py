# pig_main.py
from uib_inf100_graphics.simple import canvas, display
from pig_head import draw_head
from pig_body import draw_body

draw_body(canvas, 80,100,320,300)
draw_head(canvas, 290, 110, 60)

display(canvas)