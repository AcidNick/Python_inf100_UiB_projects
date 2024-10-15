from uib_inf100_graphics.simple import canvas, display
from color_train import color_train_A, color_train_B, color_train_C

colors1 = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
colors2 = ['black', 'white', 'black', 'white', 'black', 'white']
colors3 = ['#800080', '#8B008B', '#9400D3', 
           '#9932CC', '#8A2BE2', '#9370DB', 
           '#7B68EE', '#6A5ACD', '#483D8B', 
           '#0000FF', '#0000CD', '#00008B', 
           '#000080', '#191970', '#00008B']

color_train_A(canvas, 10, 10, colors1)
color_train_A(canvas, 10, 20, colors2)
color_train_A(canvas, 10, 40, colors3)

color_train_B(canvas, 50, 195, 300, 10, colors1)
color_train_B(canvas, 50, 150, 150, 30, colors2)
color_train_B(canvas, 50, 180, 50, 15, colors3)

color_train_C(canvas, 200, 380, 350, 400, colors1)
color_train_C(canvas, 80, 360, 350, 380, colors2)
color_train_C(canvas, 80, 380, 200, 400, colors3)

display(canvas)
