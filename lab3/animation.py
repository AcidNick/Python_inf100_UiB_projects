from uib_inf100_graphics.simple import canvas, display

y_pos_px = 100
y_vel_px_s = 0
radius = 20
gravity_px_s2 = 100
time_delta_s = 0.1     # Som standard viser display et bilde i 0.1 sekunder

while True:
    # La tiden gå
    y_vel_px_s += gravity_px_s2 * time_delta_s
    y_pos_px += y_vel_px_s * time_delta_s 

    if y_pos_px >= 400-25:
        y_vel_px_s = -y_vel_px_s

    # Tegne
    canvas.create_oval(200 - radius, y_pos_px - radius,
                       200 + radius, y_pos_px + radius, fill="red")
    display(canvas)
