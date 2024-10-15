from uib_inf100_graphics.simple import canvas, display

canvas.create_oval(60, 80, 140, 160)   # Head
canvas.create_line(100, 160, 100, 280) # Body
canvas.create_line(50, 180, 150, 180)  # Arms
canvas.create_line(100, 280, 50, 330)  # Left leg
canvas.create_line(100, 280, 150, 330) # Right leg

# canvas.create_oval(80, 105, 90, 115)   # Left eye
# canvas.create_oval(110, 105, 120, 115)   # Right eye
# canvas.create_arc(80, 140, 120, 130, start=180, extent=180, style='arc') # Smile


canvas.create_oval(260, 80, 340, 160)   # Head
canvas.create_line(300, 160, 300, 280) # Body
canvas.create_line(250, 180, 350, 180)  # Arms
canvas.create_line(300, 280, 250, 330)  # Left leg
canvas.create_line(300, 280, 350, 330) # Right leg

display(canvas)
