from uib_inf100_graphics.simple import canvas, display

# Head
canvas.create_oval(100, 50, 300, 250, fill="yellow")

# Eyes
canvas.create_oval(145, 80, 185, 130, fill="black")
canvas.create_oval(215, 80, 255, 130, fill="black")
canvas.create_oval(160, 100, 170, 110, fill="white")
canvas.create_oval(230, 100, 240, 130-20, fill="white")

# Mouth
canvas.create_oval(150, 180, 250, 150, fill="red")
# canvas.create_arc(150, 200, 250, 220, fill="red", start=150, extent=240)

display(canvas)