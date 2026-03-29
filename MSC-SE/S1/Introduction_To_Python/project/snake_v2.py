import random
import time
import turtle

# Playfield width (grid area only).
SCREEN_WIDTH = 600
# Playfield height (grid area only).
SCREEN_HEIGHT = 600
# Top HUD space for score + bonus bar.
HUD_HEIGHT = 120
# Total window height.
WINDOW_HEIGHT = SCREEN_HEIGHT + HUD_HEIGHT
# Grid cell size, snake moves in these increments.
STEP = 20
# Initial frame delay (smaller = faster).
START_DELAY = 0.12
# Base points per normal food.
POINTS_PER_FOOD = 10  
# Bonus food gives double points.
BONUS_MULTIPLIER = 2  
# Spawn bonus after this many normal foods.
BONUS_EATS_TRIGGER = 5  
# Bonus food lifetime (seconds).
BONUS_DURATION = 10  
# Bonus timer bar width.
BAR_WIDTH = 220  
# Bonus timer bar height.
BAR_HEIGHT = 12  
# Bar Y-position inside HUD.
BAR_TOP_Y = WINDOW_HEIGHT // 2 - 50  
# Menu button width.
BUTTON_WIDTH = 160
# Menu button height.
BUTTON_HEIGHT = 50
# Extra click buffer for reliability.
BUTTON_CLICK_PADDING = 8
# Neutral border color on black.
BORDER_COLOR = "gray"  



def setup_screen():
    """Create and configure the Turtle window."""
    screen = turtle.Screen()
    screen.title("Snake - Intro to Python Project")
    screen.bgcolor("black")
    screen.setup(width=SCREEN_WIDTH, height=WINDOW_HEIGHT)
    screen.tracer(0)  # Manual repaint for smoother animation.
    return screen


def make_segment(color="green", shape="square"):
    """Create a snake segment (body or head)."""
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape(shape)
    segment.color(color)
    segment.penup()  # Move without drawing trails.
    return segment


def make_food():
    """Create the normal (red) food turtle."""
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)  # Temporary start position.
    return food


def make_bonus_food():
    """Create the bonus (gold) food turtle, hidden by default."""
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("gold")
    food.penup()
    food.hideturtle()
    return food


def make_scoreboard():
    """Create a turtle dedicated to HUD text."""
    score_turtle = turtle.Turtle()
    score_turtle.speed(0)
    score_turtle.color("white")
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.goto(0, WINDOW_HEIGHT // 2 - 30)
    return score_turtle


def draw_score(score_turtle, score, high_score, mode):
    """Render the current score line in the HUD."""
    score_turtle.clear()
    score_turtle.write(
        f"Score: {score}  High Score: {high_score}  Mode: {mode.title()}",
        align="center",
        font=("Arial", 16, "normal"),
    )


def make_bonus_point_bar_turtle(color):
    """Create a turtle used to draw the bonus bar."""
    bar = turtle.Turtle()
    bar.speed(0)
    bar.hideturtle()
    bar.color(color)
    bar.penup()
    return bar


def draw_bonus_point_bar_frame(frame_turtle, left_x, top_y, width, height):
    """Draw the outline of the bonus timer bar."""
    frame_turtle.clear()
    frame_turtle.goto(left_x, top_y)
    frame_turtle.pendown()
    for _ in range(2):
        frame_turtle.forward(width)
        frame_turtle.right(90)
        frame_turtle.forward(height)
        frame_turtle.right(90)
    frame_turtle.penup()


def draw_bonus_point_bar_fill(fill_turtle, left_x, top_y, width, height, progress):
    """Draw the filled portion of the bonus timer bar."""
    fill_turtle.clear()
    fill_width = max(0, int(width * progress))
    if fill_width == 0:
        return
    fill_turtle.goto(left_x, top_y)
    fill_turtle.begin_fill()
    fill_turtle.pendown()
    fill_turtle.forward(fill_width)
    fill_turtle.right(90)
    fill_turtle.forward(height)
    fill_turtle.right(90)
    fill_turtle.forward(fill_width)
    fill_turtle.right(90)
    fill_turtle.forward(height)
    fill_turtle.right(90)
    fill_turtle.penup()
    fill_turtle.end_fill()


def draw_button(button_turtle, center_x, center_y, text, fill_color):
    """Draw one button and return its clickable bounds."""
    button_turtle.setheading(0)
    half_w = BUTTON_WIDTH // 2
    half_h = BUTTON_HEIGHT // 2
    left = center_x - half_w
    top = center_y + half_h
    button_turtle.color("white", fill_color)
    button_turtle.goto(left, top)
    button_turtle.pendown()
    button_turtle.begin_fill()
    for _ in range(2):
        button_turtle.forward(BUTTON_WIDTH)
        button_turtle.right(90)
        button_turtle.forward(BUTTON_HEIGHT)
        button_turtle.right(90)
    button_turtle.end_fill()
    button_turtle.penup()
    button_turtle.goto(center_x, center_y - 10)
    button_turtle.write(text, align="center", font=("Arial", 14, "bold"))
    return (left, left + BUTTON_WIDTH, center_y - half_h, center_y + half_h)


def draw_overlay():
    """Draw a full-screen overlay so menus sit above the game."""
    overlay = turtle.Turtle()
    overlay.hideturtle()
    overlay.speed(0)
    overlay.penup()
    overlay.setheading(0)
    overlay.color("black", "black")
    overlay.goto(-SCREEN_WIDTH // 2, WINDOW_HEIGHT // 2)
    overlay.begin_fill()
    overlay.pendown()
    overlay.forward(SCREEN_WIDTH)
    overlay.right(90)
    overlay.forward(WINDOW_HEIGHT)
    overlay.right(90)
    overlay.forward(SCREEN_WIDTH)
    overlay.right(90)
    overlay.forward(WINDOW_HEIGHT)
    overlay.end_fill()
    overlay.penup()
    return overlay


def wait_for_button_choice(screen, buttons):
    """Block until the user clicks one of the given buttons."""
    selection = {"value": None}  # Mutable so nested handler can update it.

    def on_click(x, y):
        for button in buttons:
            left, right, bottom, top = button["bounds"]
            if (
                left - BUTTON_CLICK_PADDING
                <= x
                <= right + BUTTON_CLICK_PADDING
                and bottom - BUTTON_CLICK_PADDING
                <= y
                <= top + BUTTON_CLICK_PADDING
            ):
                selection["value"] = button["key"]
                return

    screen.listen()
    screen.onscreenclick(on_click)
    screen.update()
    while selection["value"] is None:
        screen.update()
        # Keeps CPU usage reasonable while waiting.
        time.sleep(0.01)  
    screen.onscreenclick(None)
    return selection["value"]


def choose_mode(screen):
    """Show the start menu and return 'easy', 'normal', or 'hard'."""
    overlay = draw_overlay()
    prompt = turtle.Turtle()
    prompt.hideturtle()
    prompt.color("white")
    prompt.penup()
    prompt.goto(0, 120)
    prompt.write("Choose a mode", align="center", font=("Arial", 18, "bold"))

    buttons = []
    labels = [("Easy", "easy"), ("Normal", "normal"), ("Hard", "hard")]
    xs = [-180, 0, 180]
    for idx, (label, key) in enumerate(labels):
        btn = turtle.Turtle()
        btn.speed(0)
        btn.hideturtle()
        btn.penup()
        bounds = draw_button(btn, xs[idx], 20, label, "#2a2a2a")
        buttons.append({"key": key, "bounds": bounds, "turtle": btn})

    selection = wait_for_button_choice(screen, buttons)
    prompt.clear()
    prompt.hideturtle()
    for button in buttons:
        button["turtle"].clear()
        button["turtle"].hideturtle()
    overlay.clear()
    overlay.hideturtle()

    return selection


def choose_post_game(screen, score, high_score):
    """Show game-over menu and return 'replay' or 'menu'."""
    overlay = draw_overlay()
    prompt = turtle.Turtle()
    prompt.hideturtle()
    prompt.color("white")
    prompt.penup()
    prompt.goto(0, 160)
    prompt.write("Game Over", align="center", font=("Arial", 20, "bold"))
    prompt.goto(0, 125)
    prompt.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Arial", 14, "normal"),
    )
    prompt.goto(0, 95)
    prompt.write("Replay or Menu?", align="center", font=("Arial", 14, "normal"))

    buttons = []
    labels = [("Replay", "replay"), ("Menu", "menu")]
    xs = [-120, 120]
    for idx, (label, key) in enumerate(labels):
        btn = turtle.Turtle()
        btn.speed(0)
        btn.hideturtle()
        btn.penup()
        bounds = draw_button(btn, xs[idx], 0, label, "#2a2a2a")
        buttons.append({"key": key, "bounds": bounds, "turtle": btn})

    selection = wait_for_button_choice(screen, buttons)
    prompt.clear()
    prompt.hideturtle()
    for button in buttons:
        button["turtle"].clear()
        button["turtle"].hideturtle()
    overlay.clear()
    overlay.hideturtle()

    return selection


def build_maze():
    """Return wall coordinates for hard mode."""
    walls = set()
    max_x = SCREEN_WIDTH // 2 - STEP * 2
    max_y = SCREEN_HEIGHT // 2 - STEP * 2

    # Left/right verticals with small gaps.
    for y in range(-max_y, max_y + 1, STEP):
        if y not in (-40, -20, 0, 20, 40):
            walls.add((-200, y))
        if y not in (-120, -100, -80):
            walls.add((200, y))

    # Top row + center row with gaps.
    for x in range(-max_x, max_x + 1, STEP):
        if x not in (-60, -40, -20, 0, 20):
            walls.add((x, 160))
        if x not in (-20, 0, 20):
            walls.add((x, 0))

    # Bottom arms shortened to keep the center open.
    bottom_arm = 120
    for x in range(-max_x, -max_x + bottom_arm + STEP, STEP):
        walls.add((x, -160))
    for x in range(max_x - bottom_arm, max_x + STEP, STEP):
        walls.add((x, -160))

    # Extra interior segments to shape movement.
    for x in range(-140, -60 + STEP, STEP):
        walls.add((x, 80))
    for x in range(60, 140 + STEP, STEP):
        walls.add((x, -80))

    walls.discard((0, 0))  # Keep the spawn cell clear.
    return list(walls)


def draw_maze(wall_positions):
    """Stamp wall blocks for the hard-mode maze."""
    wall_turtle = turtle.Turtle()
    wall_turtle.speed(0)
    wall_turtle.shape("square")
    wall_turtle.color("gray")
    wall_turtle.penup()
    for x, y in wall_positions:
        wall_turtle.goto(x, y)
        wall_turtle.stamp()
    wall_turtle.hideturtle()
    return wall_turtle


def draw_border(wrap_walls):
    """Draw the playfield border; dotted if wrapping is enabled."""
    border = turtle.Turtle()
    border.hideturtle()
    border.speed(0)
    border.color(BORDER_COLOR)
    max_x = SCREEN_WIDTH // 2 - STEP
    max_y = SCREEN_HEIGHT // 2 - STEP
    half_step = STEP // 2
    edge_x = max_x + half_step
    edge_y = max_y + half_step
    if wrap_walls:
        border.penup()
        for x in range(-max_x, max_x + 1, STEP):
            border.goto(x, edge_y)
            border.dot(6)
            border.goto(x, -edge_y)
            border.dot(6)
        for y in range(-max_y, max_y + 1, STEP):
            border.goto(-edge_x, y)
            border.dot(6)
            border.goto(edge_x, y)
            border.dot(6)
    else:
        border.penup()
        border.goto(-edge_x, edge_y)
        border.pendown()
        border.goto(edge_x, edge_y)
        border.goto(edge_x, -edge_y)
        border.goto(-edge_x, -edge_y)
        border.goto(-edge_x, edge_y)
        border.penup()
    return border


def position_key(position):
    """Normalize a turtle position to grid coordinates."""
    return (int(round(position[0])), int(round(position[1])))


def place_food(food, occupied_positions):
    """Place food on a random empty grid cell."""
    max_x = SCREEN_WIDTH // 2 - STEP
    max_y = SCREEN_HEIGHT // 2 - STEP
    while True:
        x = random.randrange(-max_x, max_x + 1, STEP)
        y = random.randrange(-max_y, max_y + 1, STEP)
        if (x, y) not in occupied_positions:
            food.goto(x, y)
            return


def main():
    """Main game loop and state management."""
    screen = setup_screen()
    mode = choose_mode(screen)
    wrap_walls = mode == "easy"
    maze_enabled = mode == "hard"
    head = make_segment(color="white", shape="triangle")
    food = make_food()
    bonus_food = make_bonus_food()
    score_turtle = make_scoreboard()
    bar_frame = make_bonus_point_bar_turtle("white")
    bar_fill = make_bonus_point_bar_turtle("yellow")

    direction = "stop"  # "stop" means no movement until input.
    score = 0
    high_score = 0
    delay = START_DELAY

    segments = []
    normal_eats = 0
    bonus_active = False
    bonus_expires_at = 0.0
    wall_positions = set()
    wall_turtle = None
    border_turtle = draw_border(wrap_walls)
    if maze_enabled:
        wall_positions = set(build_maze())
        wall_turtle = draw_maze(wall_positions)

    def occupied_positions(include_food=True, include_bonus=True):
        """Return all blocked grid cells (snake, walls, food)."""
        positions = {position_key(head.position())}
        for segment in segments:
            positions.add(position_key(segment.position()))
        for wall in wall_positions:
            positions.add(wall)
        if include_food:
            positions.add(position_key(food.position()))
        if include_bonus and bonus_active:
            positions.add(position_key(bonus_food.position()))
        return positions

    def deactivate_bonus():
        """Hide bonus food and clear its bar."""
        nonlocal bonus_active
        bonus_active = False
        bonus_food.hideturtle()
        bar_frame.clear()
        bar_fill.clear()

    def spawn_bonus():
        """Spawn bonus food and start its countdown."""
        nonlocal bonus_active, bonus_expires_at
        bonus_active = True
        bonus_expires_at = time.time() + BONUS_DURATION
        bonus_food.showturtle()
        place_food(bonus_food, occupied_positions(include_food=True, include_bonus=False))
        left_x = -BAR_WIDTH // 2
        draw_bonus_point_bar_frame(bar_frame, left_x, BAR_TOP_Y, BAR_WIDTH, BAR_HEIGHT)

    def update_bonus_bar():
        """Refresh the bonus timer bar each frame."""
        if not bonus_active:
            return
        remaining = bonus_expires_at - time.time()
        if remaining <= 0:
            deactivate_bonus()
            return
        progress = remaining / BONUS_DURATION
        left_x = -BAR_WIDTH // 2
        draw_bonus_point_bar_fill(bar_fill, left_x, BAR_TOP_Y, BAR_WIDTH, BAR_HEIGHT, progress)

    def apply_mode(new_mode):
        """Apply a new mode and rebuild borders/maze."""
        nonlocal mode, wrap_walls, maze_enabled, wall_positions, wall_turtle, border_turtle
        mode = new_mode
        wrap_walls = mode == "easy"
        maze_enabled = mode == "hard"
        if border_turtle:
            border_turtle.clear()
            border_turtle.hideturtle()
        border_turtle = draw_border(wrap_walls)
        if wall_turtle:
            wall_turtle.clear()
            wall_turtle.hideturtle()
            wall_turtle = None
        wall_positions = set(build_maze()) if maze_enabled else set()
        if maze_enabled:
            wall_turtle = draw_maze(wall_positions)

    def reset_state():
        """Reset snake, score, and speed after a game over."""
        nonlocal score, delay, direction, normal_eats
        head.goto(0, 0)
        direction = "stop"
        head.setheading(0)
        for segment in segments:
            segment.hideturtle()
        segments.clear()
        score = 0
        delay = START_DELAY
        normal_eats = 0
        deactivate_bonus()
        place_food(food, occupied_positions(include_food=False, include_bonus=False))
        draw_score(score_turtle, score, high_score, mode)

    def handle_game_over():
        """Pause, show game-over menu, then restart."""
        nonlocal direction
        direction = "stop"
        deactivate_bonus()
        time.sleep(0.6)
        choice = choose_post_game(screen, score, high_score)
        if choice == "menu":
            apply_mode(choose_mode(screen))
        reset_state()

    def set_head_heading(new_direction):
        """Rotate the head to point in the travel direction."""
        headings = {"up": 90, "right": 0, "down": 270, "left": 180}
        head.setheading(headings[new_direction])

    def go_up():
        """Set direction to up unless reversing."""
        nonlocal direction
        if direction != "down":
            direction = "up"
            set_head_heading(direction)

    def go_down():
        """Set direction to down unless reversing."""
        nonlocal direction
        if direction != "up":
            direction = "down"
            set_head_heading(direction)

    def go_left():
        """Set direction to left unless reversing."""
        nonlocal direction
        if direction != "right":
            direction = "left"
            set_head_heading(direction)

    def go_right():
        """Set direction to right unless reversing."""
        nonlocal direction
        if direction != "left":
            direction = "right"
            set_head_heading(direction)

    def move():
        """Advance the head one grid cell."""
        x, y = head.position()
        if direction == "up":
            head.sety(y + STEP)
        elif direction == "down":
            head.sety(y - STEP)
        elif direction == "left":
            head.setx(x - STEP)
        elif direction == "right":
            head.setx(x + STEP)

    screen.listen()
    screen.onkeypress(go_up, "w")
    screen.onkeypress(go_down, "s")
    screen.onkeypress(go_left, "a")
    screen.onkeypress(go_right, "d")
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")
    screen.onkeypress(go_right, "Right")

    place_food(food, occupied_positions(include_food=False, include_bonus=False))
    draw_score(score_turtle, score, high_score, mode)

    try:
        while True:
            screen.update()

            # Handle borders (wrap or wall)
            x, y = head.position()
            max_x = SCREEN_WIDTH // 2 - STEP
            max_y = SCREEN_HEIGHT // 2 - STEP
            if wrap_walls:
                if x > max_x:
                    head.setx(-max_x)  # Wrap to opposite side.
                elif x < -max_x:
                    head.setx(max_x)
                if y > max_y:
                    head.sety(-max_y)
                elif y < -max_y:
                    head.sety(max_y)
            else:
                if x > max_x or x < -max_x or y > max_y or y < -max_y:
                    handle_game_over()
                    continue

            # Check collision with maze walls
            if maze_enabled and position_key(head.position()) in wall_positions:
                handle_game_over()
                continue

            update_bonus_bar()

            # Check collision with food
            if head.distance(food) < STEP:
                place_food(food, occupied_positions(include_food=False, include_bonus=True))
                new_segment = make_segment(color="green")
                segments.append(new_segment)
                score += POINTS_PER_FOOD
                if score > high_score:
                    high_score = score
                delay = max(0.05, delay - 0.003)
                if not bonus_active:
                    normal_eats += 1
                    if normal_eats >= BONUS_EATS_TRIGGER:
                        normal_eats = 0
                        spawn_bonus()
                draw_score(score_turtle, score, high_score, mode)

            if bonus_active and head.distance(bonus_food) < STEP:
                bonus_points = POINTS_PER_FOOD * BONUS_MULTIPLIER
                bonus_segment = make_segment(color="green")
                segments.append(bonus_segment)
                score += bonus_points
                if score > high_score:
                    high_score = score
                deactivate_bonus()
                draw_score(score_turtle, score, high_score, mode)

            # Move the body segments
            for idx in range(len(segments) - 1, 0, -1):
                x, y = segments[idx - 1].position()
                segments[idx].goto(x, y)
            if segments:
                x, y = head.position()
                segments[0].goto(x, y)

            move()

            # Check collision with self
            game_over = False
            for segment in segments:
                if segment.distance(head) < STEP / 2:
                    handle_game_over()
                    game_over = True
                    break
            if game_over:
                continue

            time.sleep(delay)
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
