def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.direction = 'east'
    app.info_mode = False
    app.board_size = 15
    app.snake_size = 3
    app.head_pos = (0, 0)
    app.board = create_board(app, app.board_size, app.snake_size)
    app.state = 'welcome'
    app.move_made = True
    app.next_move = ''
    app.speed = 2
    app.speed_names = ['slow', 'normal', 'fast', 'insane']
    app.speeds = [120, 80, 40, 20] # milliseconds of delay, less is faster
    app.timer_delay = app.speeds[app.speed-1]
    app.setting = 'speed'
    app.fruit_images = [
        load_image('./images/apple.png'),
        load_image('./images/banana.png'),
        load_image('./images/watermelon.png')
        ]
    app.score = 0
    app.highscore = int(Path('highscore.txt').read_text(encoding='utf-8'))

def change_settings(app):
    app.snake_size = 3
    app.direction = 'east'
    app.board = create_board(app, app.board_size, app.snake_size)
    app.timer_delay = app.speeds[app.speed-1] # milliseconds
    app.score = 0
    app.highscore = int(Path('highscore.txt').read_text(encoding='utf-8'))

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.move_made and app.next_move != '':
        app.direction = app.next_move
        app.next_move = ''
    if not app.info_mode and app.state == 'active':
        move_snake(app)

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.state == 'active':
        if app.move_made:
            app.nextMove = ''
            if event.key in ['Up', 'w'] and app.direction != 'south':
                if app.direction != 'north':
                    app.move_made = False
                app.direction = 'north'
            elif event.key in ['Down', 's'] and app.direction != 'north':
                if app.direction != 'south':
                    app.move_made = False
                app.direction = 'south'
            elif event.key in ['Left', 'a'] and app.direction != 'east':
                if app.direction != 'west':
                    app.move_made = False
                app.direction = 'west'
            elif event.key in ['Right', 'd'] and app.direction != 'west':
                if app.direction != 'east':
                    app.move_made = False
                app.direction = 'east'
        else:
            if event.key in ['Up', 'w'] and app.direction != 'south':
                app.next_move = 'north'
            elif event.key in ['Down', 's'] and app.direction != 'north':
                app.next_move = 'south'
            elif event.key in ['Left', 'a'] and app.direction != 'east':
                app.next_move = 'west'
            elif event.key in ['Right', 'd'] and app.direction != 'west':
                app.next_move = 'east'

    if event.key == 'i':
        app.info_mode = not app.info_mode 
    if app.info_mode:
        if event.key == 'Space':
            move_snake(app)

    if app.state == 'gameover':
        if event.key.lower() in ['enter', 'return', 'r']:
            change_settings(app)
            app.state = 'active'
        if event.key == 'Space':
            app.state = 'welcome'
            change_settings(app)

    if app.state in ['welcome', 'help']:
        if event.key in ['Enter', 'Return']:
            change_settings(app)
            app.state = 'active'
            # app_started(app)
        if event.key == 'Down' and app.setting == 'speed':
            app.setting = 'size'
        if event.key == 'Up' and app.setting == 'size':
            app.setting = 'speed'
        if app.setting == 'speed':
            if event.key == 'Right' and app.speed < len(app.speeds):
                app.speed += 1
            if event.key == 'Left' and app.speed > 1:
                app.speed -= 1
        if app.setting == 'size':
            if event.key == 'Right' and app.board_size < 23:
                app.board_size += 1
            if event.key == 'Left' and app.board_size > 8:
                app.board_size -= 1
        if event.key.lower() == 'h':
            app.state = 'help' if app.state == 'welcome' else 'welcome'

def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    if app.info_mode:
        canvas.create_text(5, 0, text=f'{app.state=} {app.head_pos=} {app.snake_size=} {app.direction=} {app.speed=} {app.timer_delay=} {app.board_size=} {app.move_made=} {app.next_move=}', anchor='nw')
    
    if app.state == 'active':
        draw_board(canvas, 25, 25, app.width-25, app.height-25, app.board, app.info_mode, app.fruit_images)
        if not app.info_mode:
            canvas.create_text(25, 0, text=f'Score: {app.score}', anchor='nw', font=('Courier new', 15, 'bold'))

    if app.state in ['welcome', 'help']:
        box_left = app.width/5
        box_right = app.width - app.width/5
        box_top = 100
        box_bottom = 200
        canvas.create_rectangle(25, 25, app.width-25, app.height-25, outline='', fill='#aad751')
        canvas.create_rectangle(box_left, box_top, box_right, box_bottom, outline='white', width=5)
        text_in_box(canvas, box_left+20, box_top, box_right-20, box_bottom, 'Welcome to snake!', fill='white')
        canvas.create_text(app.width/2, app.height/2+60, text="Press ENTER to start", font=('Courier new', 25, ''))
        canvas.create_text(app.width/2, app.height/2-60, text=f"SPEED: {app.speed} {f'({app.speed_names[app.speed-1]})'}", font=('Courier new', 25, 'bold' if app.setting=='speed' else 'normal'))
        canvas.create_text(app.width/2, app.height/2, text=f"SIZE: {app.board_size}x{app.board_size}", font=('Courier new', 25, 'bold' if app.setting=='size' else 'normal'))

        canvas.create_text(app.width-30, app.height-30, text="Press H for help", font=('Courier new', 20, ''), anchor='se')   
    if app.state == 'help':
        canvas.create_text(app.width/2, app.height/1.25, text="Use arrow keys to navigate this menu\nSpeed: 1-4\nSize: 8x8 - 23x23\nPress i to enable debug/info mode", font=('Courier new', 20, ''), justify='center')

    if app.state == 'gameover':
        box_left = app.width/5
        box_right = app.width - app.width/5
        box_top = 100
        box_bottom = 200
        canvas.create_rectangle(box_left, box_top, box_right, box_bottom, outline='red', width=5)
        text_in_box(canvas, box_left+20, box_top, box_right-20, box_bottom, text='Game Over!', fill='red')
        canvas.create_text(app.width/2, app.height/2-60, text=f"Score: {app.score}\nOn {app.speed_names[app.speed-1]} speed", font=('Courier new', 25, 'bold'), justify='center')
        canvas.create_text(app.width/2, app.height/2+60, text="Press ENTER or R to restart", font=('Courier new', 25, ''))
        canvas.create_text(app.width/2, app.height/2+120, text=f"Press SPACE for main menu", font=('Courier new', 25, ''))
        if app.score > app.highscore:
            canvas.create_text(app.width/2, app.height/2, text=f"New highscore!: {app.score} (Previous: {app.highscore})", font=('Courier new', 25, 'bold'), justify='center')
            Path('highscore.txt').write_text(str(app.score), encoding='utf-8')
        else:
            canvas.create_text(app.width/2, app.height/2, text=f"Highscore: {app.highscore}", font=('Courier new', 25, 'bold'), justify='center')


import random

fruits = ['apple', 'banana', 'strawberry']

def move_snake(app):
  app.head_pos = get_next_head_position(app.head_pos, app.direction)
  head_row, head_col = app.head_pos
  if not is_legal_move(app.head_pos, app.board):
    app.state = 'gameover'
    return
  if app.board[head_row][head_col] < 0:
    app.snake_size += 1
    app.score += 1
    add_random_fruit(app.board)
  else:
    subtract_one_from_all_positives(app.board)
  app.board[head_row][head_col] = app.snake_size
  app.move_made = True

def get_next_head_position(head_pos, direction):
  head_row, head_col = head_pos
  if direction == 'north':
    return head_row - 1, head_col
  if direction == 'south':
    return head_row + 1, head_col
  if direction == 'west':
    return head_row, head_col - 1
  if direction == 'east':
    return head_row, head_col + 1

def subtract_one_from_all_positives(grid):
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] > 0:
        grid[row][col] -= 1

def add_random_fruit(grid):
  possible_positions = []
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == 0:
        possible_positions.append((row, col))
  random_row, random_col = random.choice(possible_positions)
  random_fruit = random.choice(fruits)
  grid[random_row][random_col] = -1-fruits.index(random_fruit)

def is_legal_move(pos, board):
  pos_row, pos_col = pos
  board_limit_row = len(board)
  board_limit_col = len(board[0])
  if pos_row not in range(0, board_limit_row):
    return False
  if pos_col not in range(0, board_limit_col):
    return False
  if board[pos_row][pos_col] > 0: # The position has a part of the snake
    return False

  return True

def create_board(app, size, snake_size):
    board = [[0] * size for i in range(size)]
    random_snake_row = random.choice(range(3, size-2)) # Not all the way in the top or bottom
    random_snake_col = random.choice(range(snake_size-2, round(size/2))) # Left side
    board[random_snake_row][random_snake_col] = snake_size
    for i in range(1, snake_size):
      board[random_snake_row][random_snake_col-i] = snake_size-i
    add_random_fruit(board)
    app.head_pos = (random_snake_row, random_snake_col)
    return board

if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from snake_view import draw_board
    from uib_inf100_graphics.helpers import text_in_box, load_image
    from pathlib import Path
    run_app(width=900, height=700, title='Snake')
