import random
import time
import turtle

# Snake game using Turtle graphics.
# This file is heavily annotated so you can explain each line and choice.


SCREEN_WIDTH = 600  # Playable grid width in pixels.
SCREEN_HEIGHT = 600  # Playable grid height in pixels.
HUD_HEIGHT = 120  # Extra space above the grid for score + timer.
WINDOW_HEIGHT = SCREEN_HEIGHT + HUD_HEIGHT  # Total window height.
STEP = 20  # Size of one grid cell (snake moves in this step).
START_DELAY = 0.12  # Starting frame delay (seconds); lower is faster.
POINTS_PER_FOOD = 10  # Points for a normal food.
BONUS_MULTIPLIER = 2  # Bonus food = normal points * this multiplier.
BONUS_EATS_TRIGGER = 5  # Spawn bonus after this many normal foods.
BONUS_DURATION = 10  # Bonus food stays on screen for this many seconds.
BAR_WIDTH = 220  # Width of the bonus timer bar.
BAR_HEIGHT = 12  # Height of the bonus timer bar.
BAR_TOP_Y = WINDOW_HEIGHT // 2 - 50  # Y-position of the bar in the HUD.
BUTTON_WIDTH = 160  # Menu button width.
BUTTON_HEIGHT = 50  # Menu button height.
BUTTON_CLICK_PADDING = 8  # Clickable padding around each button.
BORDER_COLOR = "gray"  # Border color (subtle but visible on black).


def setup_screen():
    """Create and configure the Turtle window."""
    screen = turtle.Screen()  # Main drawing window for Turtle.
    screen.title("Snake - Intro to Python Project")  # Window title bar text.
    screen.bgcolor("black")  # Set background to black for contrast.
    screen.setup(width=SCREEN_WIDTH, height=WINDOW_HEIGHT)  # Window size.
    screen.tracer(0)  # Turn off auto redraw; we call screen.update() manually.
    return screen  # Return the configured screen object.


def make_segment(color="green", shape="square"):
    """Create a snake segment turtle with a given color and shape."""
    segment = turtle.Turtle()  # A Turtle object is a drawable shape.
    segment.speed(0)  # 0 = fastest animation (no delays).
    segment.shape(shape)  # Square by default, triangle for head, etc.
    segment.color(color)  # Fill/outline color of the segment.
    segment.penup()  # Lift pen so moving does not draw lines.
    return segment  # Return the prepared segment.


def make_food():
    """Create the normal food turtle."""
    food = turtle.Turtle()  # Turtle used as the food marker.
    food.speed(0)  # Fastest animation for instant moves.
    food.shape("circle")  # Circle looks like a pellet.
    food.color("red")  # Red stands out against black.
    food.penup()  # Prevent drawing lines when moved.
    food.goto(0, 100)  # Initial position before random placement.
    return food


def make_bonus_food():
    """Create the bonus food turtle (hidden until activated)."""
    food = turtle.Turtle()  # Separate turtle for bonus food.
    food.speed(0)  # Fast rendering for reposition.
    food.shape("circle")  # Circle so it looks like food.
    food.color("gold")  # Gold to signal "special" reward.
    food.penup()  # No drawing lines while moving.
    food.hideturtle()  # Start hidden until bonus is spawned.
    return food


def make_scoreboard():
    """Create the scoreboard turtle that writes HUD text."""
    score_turtle = turtle.Turtle()  # Turtle used only for text.
    score_turtle.speed(0)  # Fastest so text updates instantly.
    score_turtle.color("white")  # White text for visibility.
    score_turtle.penup()  # Do not draw lines.
    score_turtle.hideturtle()  # Hide cursor; only show text.
    score_turtle.goto(0, WINDOW_HEIGHT // 2 - 30)  # Top HUD position.
    return score_turtle


def draw_score(score_turtle, score, high_score, mode):
    """Render the score text in the HUD."""
    score_turtle.clear()  # Remove previous score text.
    score_turtle.write(
        f"Score: {score}  High Score: {high_score}  Mode: {mode.title()}",
        align="center",  # Center align text at current position.
        font=("Arial", 16, "normal"),  # Font family, size, and style.
    )


def make_bar_turtle(color):
    """Create a turtle used to draw the bonus timer bar."""
    bar = turtle.Turtle()  # Turtle used to draw rectangles.
    bar.speed(0)  # Fastest drawing.
    bar.hideturtle()  # Hide the cursor; show only shapes.
    bar.color(color)  # Color for the bar (frame or fill).
    bar.penup()  # Don't draw when moving to start point.
    return bar


def draw_bar_frame(frame_turtle, left_x, top_y, width, height):
    """Draw the outline (frame) of the bonus timer bar."""
    frame_turtle.clear()  # Remove previous frame.
    frame_turtle.goto(left_x, top_y)  # Top-left corner of the bar.
    frame_turtle.pendown()  # Start drawing the rectangle.
    for _ in range(2):
        frame_turtle.forward(width)  # Top/bottom edge.
        frame_turtle.right(90)  # Turn down.
        frame_turtle.forward(height)  # Side edge.
        frame_turtle.right(90)  # Turn to continue rectangle.
    frame_turtle.penup()  # Lift pen so it won't draw when moving.


def draw_bar_fill(fill_turtle, left_x, top_y, width, height, progress):
    """Draw the filled part of the bonus timer bar."""
    fill_turtle.clear()  # Clear the previous fill.
    fill_width = max(0, int(width * progress))  # Convert progress to pixels.
    if fill_width == 0:
        return  # Nothing to draw when time is up.
    fill_turtle.goto(left_x, top_y)  # Start at top-left.
    fill_turtle.begin_fill()  # Begin filled rectangle.
    fill_turtle.pendown()
    fill_turtle.forward(fill_width)  # Draw top edge of fill.
    fill_turtle.right(90)
    fill_turtle.forward(height)  # Right edge.
    fill_turtle.right(90)
    fill_turtle.forward(fill_width)  # Bottom edge.
    fill_turtle.right(90)
    fill_turtle.forward(height)  # Left edge.
    fill_turtle.right(90)
    fill_turtle.penup()
    fill_turtle.end_fill()  # Complete the fill.


def draw_button(button_turtle, center_x, center_y, text, fill_color):
    """Draw one rectangular button and return its clickable bounds."""
    button_turtle.setheading(0)  # Reset heading so rectangles are not rotated.
    half_w = BUTTON_WIDTH // 2  # Half width for centering math.
    half_h = BUTTON_HEIGHT // 2  # Half height for centering math.
    left = center_x - half_w  # Left edge X position.
    top = center_y + half_h  # Top edge Y position.
    button_turtle.color("white", fill_color)  # White border + filled color.
    button_turtle.goto(left, top)  # Move to top-left corner.
    button_turtle.pendown()  # Start drawing the button box.
    button_turtle.begin_fill()  # Fill the rectangle with fill_color.
    for _ in range(2):
        button_turtle.forward(BUTTON_WIDTH)  # Draw top/bottom edges.
        button_turtle.right(90)  # Turn down.
        button_turtle.forward(BUTTON_HEIGHT)  # Draw side edges.
        button_turtle.right(90)  # Turn to continue rectangle.
    button_turtle.end_fill()  # Stop filling.
    button_turtle.penup()  # Stop drawing.
    button_turtle.goto(center_x, center_y - 10)  # Position text slightly down.
    button_turtle.write(text, align="center", font=("Arial", 14, "bold"))
    return (left, left + BUTTON_WIDTH, center_y - half_h, center_y + half_h)


def draw_overlay():
    """Draw a full-screen overlay so menus appear above the game."""
    overlay = turtle.Turtle()  # Turtle used for the overlay rectangle.
    overlay.hideturtle()  # Hide cursor.
    overlay.speed(0)  # Fast drawing.
    overlay.penup()  # Move without drawing.
    overlay.setheading(0)  # Ensure orientation is 0 degrees.
    overlay.color("black", "black")  # Black outline and fill.
    overlay.goto(-SCREEN_WIDTH // 2, WINDOW_HEIGHT // 2)  # Top-left corner.
    overlay.begin_fill()  # Start filled rectangle.
    overlay.pendown()
    overlay.forward(SCREEN_WIDTH)  # Top edge.
    overlay.right(90)
    overlay.forward(WINDOW_HEIGHT)  # Right edge.
    overlay.right(90)
    overlay.forward(SCREEN_WIDTH)  # Bottom edge.
    overlay.right(90)
    overlay.forward(WINDOW_HEIGHT)  # Left edge.
    overlay.end_fill()  # Finish fill.
    overlay.penup()
    return overlay


def wait_for_button_choice(screen, buttons):
    """Block until the user clicks one of the given buttons."""
    selection = {"value": None}  # Mutable so nested function can set it.

    def on_click(x, y):
        # Handle mouse clicks and check if they fall within button bounds.
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
                selection["value"] = button["key"]  # Record chosen button.
                return

    screen.listen()  # Enable event listening.
    screen.onscreenclick(on_click)  # Bind click handler.
    screen.update()  # Draw any pending shapes before waiting.
    while selection["value"] is None:
        screen.update()  # Keep the window responsive.
        time.sleep(0.01)  # Small sleep to reduce CPU usage.
    screen.onscreenclick(None)  # Remove click handler.
    return selection["value"]  # Return the button key that was clicked.


def choose_mode(screen):
    """Show the start menu and return 'easy', 'normal', or 'hard'."""
    overlay = draw_overlay()  # Cover the game while the menu is visible.
    prompt = turtle.Turtle()  # Turtle to draw the title text.
    prompt.hideturtle()
    prompt.color("white")
    prompt.penup()
    prompt.goto(0, 120)
    prompt.write("Choose a mode", align="center", font=("Arial", 18, "bold"))

    buttons = []  # Store button metadata for click detection.
    labels = [("Easy", "easy"), ("Normal", "normal"), ("Hard", "hard")]
    xs = [-180, 0, 180]  # X positions for three evenly spaced buttons.
    for idx, (label, key) in enumerate(labels):
        btn = turtle.Turtle()
        btn.speed(0)
        btn.hideturtle()
        btn.penup()
        bounds = draw_button(btn, xs[idx], 20, label, "#2a2a2a")
        buttons.append({"key": key, "bounds": bounds, "turtle": btn})

    selection = wait_for_button_choice(screen, buttons)  # Block until clicked.
    prompt.clear()  # Clear prompt text.
    prompt.hideturtle()
    for button in buttons:
        button["turtle"].clear()  # Clear button drawing.
        button["turtle"].hideturtle()
    overlay.clear()  # Remove the overlay.
    overlay.hideturtle()

    return selection


def choose_post_game(screen, score, high_score):
    """Show the game-over screen and return 'replay' or 'menu'."""
    overlay = draw_overlay()  # Dim the game with a solid overlay.
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
    xs = [-120, 120]  # Two centered buttons.
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
    """Return a list of wall coordinates for hard mode."""
    walls = set()  # Use a set to avoid duplicate points.
    max_x = SCREEN_WIDTH // 2 - STEP * 2  # Keep walls inside the border.
    max_y = SCREEN_HEIGHT // 2 - STEP * 2

    # Left and right vertical wall sections with small openings.
    for y in range(-max_y, max_y + 1, STEP):
        if y not in (-40, -20, 0, 20, 40):
            walls.add((-200, y))  # Left column of wall blocks.
        if y not in (-120, -100, -80):
            walls.add((200, y))  # Right column of wall blocks.

    # Top and middle horizontal walls with gaps.
    for x in range(-max_x, max_x + 1, STEP):
        if x not in (-60, -40, -20, 0, 20):
            walls.add((x, 160))  # Upper horizontal line.
        if x not in (-20, 0, 20):
            walls.add((x, 0))  # Center horizontal line.

    # Bottom corners only (short arms so they don't reach the center).
    bottom_arm = 120  # Length of each bottom arm.
    for x in range(-max_x, -max_x + bottom_arm + STEP, STEP):
        walls.add((x, -160))  # Bottom-left arm.
    for x in range(max_x - bottom_arm, max_x + STEP, STEP):
        walls.add((x, -160))  # Bottom-right arm.

    # Extra small segments to break up the space.
    for x in range(-140, -60 + STEP, STEP):
        walls.add((x, 80))
    for x in range(60, 140 + STEP, STEP):
        walls.add((x, -80))

    walls.discard((0, 0))  # Keep the center open for the snake start.
    return list(walls)  # Convert to list for drawing order.


def draw_maze(wall_positions):
    """Draw the hard-mode walls using stamps."""
    wall_turtle = turtle.Turtle()  # Turtle used to stamp wall blocks.
    wall_turtle.speed(0)  # Fast draw.
    wall_turtle.shape("square")  # Walls are square blocks.
    wall_turtle.color("gray")  # Subtle gray color.
    wall_turtle.penup()  # Move without drawing lines.
    for x, y in wall_positions:
        wall_turtle.goto(x, y)  # Move to wall position.
        wall_turtle.stamp()  # Stamp the square at that position.
    wall_turtle.hideturtle()  # Hide cursor after drawing.
    return wall_turtle


def draw_border(wrap_walls):
    """Draw the grid border (dotted for wrap mode, solid otherwise)."""
    border = turtle.Turtle()
    border.hideturtle()
    border.speed(0)
    border.color(BORDER_COLOR)
    max_x = SCREEN_WIDTH // 2 - STEP  # Last valid grid center X.
    max_y = SCREEN_HEIGHT // 2 - STEP  # Last valid grid center Y.
    half_step = STEP // 2  # Shift to the outer edge of the cell.
    edge_x = max_x + half_step
    edge_y = max_y + half_step
    if wrap_walls:
        border.penup()
        for x in range(-max_x, max_x + 1, STEP):
            border.goto(x, edge_y)  # Top dotted edge.
            border.dot(6)
            border.goto(x, -edge_y)  # Bottom dotted edge.
            border.dot(6)
        for y in range(-max_y, max_y + 1, STEP):
            border.goto(-edge_x, y)  # Left dotted edge.
            border.dot(6)
            border.goto(edge_x, y)  # Right dotted edge.
            border.dot(6)
    else:
        border.penup()
        border.goto(-edge_x, edge_y)  # Start at top-left.
        border.pendown()
        border.goto(edge_x, edge_y)  # Top line.
        border.goto(edge_x, -edge_y)  # Right line.
        border.goto(-edge_x, -edge_y)  # Bottom line.
        border.goto(-edge_x, edge_y)  # Left line.
        border.penup()
    return border


def position_key(position):
    """Convert a turtle position into a clean integer grid key."""
    return (int(round(position[0])), int(round(position[1])))


def place_food(food, occupied_positions):
    """Place food on a random free grid cell."""
    max_x = SCREEN_WIDTH // 2 - STEP  # Max center coordinate inside border.
    max_y = SCREEN_HEIGHT // 2 - STEP
    while True:
        x = random.randrange(-max_x, max_x + 1, STEP)  # Snap to grid.
        y = random.randrange(-max_y, max_y + 1, STEP)
        if (x, y) not in occupied_positions:  # Avoid snake, walls, bonus.
            food.goto(x, y)
            return


def main():
    """Main entry point: set up the game and run the loop."""
    screen = setup_screen()  # Create the window and configure it.
    mode = choose_mode(screen)  # Ask the player to pick difficulty.
    wrap_walls = mode == "easy"  # Easy mode lets the snake wrap.
    maze_enabled = mode == "hard"  # Hard mode adds maze walls.
    head = make_segment(color="white", shape="triangle")  # Snake head.
    food = make_food()  # Normal red food.
    bonus_food = make_bonus_food()  # Bonus food (hidden initially).
    score_turtle = make_scoreboard()  # HUD score writer.
    bar_frame = make_bar_turtle("white")  # Bonus bar frame turtle.
    bar_fill = make_bar_turtle("yellow")  # Bonus bar fill turtle.

    direction = "stop"  # Start with no movement.
    score = 0  # Current score.
    high_score = 0  # Highest score for this run.
    delay = START_DELAY  # Current speed (lower is faster).

    segments = []  # List of body segments.
    normal_eats = 0  # Count normal foods eaten since last bonus spawn.
    bonus_active = False  # Whether bonus food is currently visible.
    bonus_expires_at = 0.0  # Time at which bonus expires.
    wall_positions = set()  # Coordinates of maze walls.
    wall_turtle = None  # Turtle used to draw maze walls.
    border_turtle = draw_border(wrap_walls)  # Dotted or solid border.
    if maze_enabled:
        wall_positions = set(build_maze())  # Build hard-mode maze.
        wall_turtle = draw_maze(wall_positions)  # Draw the maze once.

    def occupied_positions(include_food=True, include_bonus=True):
        """Return a set of grid cells currently occupied by something."""
        positions = {position_key(head.position())}  # Start with the head.
        for segment in segments:
            positions.add(position_key(segment.position()))  # Add each body.
        for wall in wall_positions:
            positions.add(wall)  # Add maze walls (already grid-aligned).
        if include_food:
            positions.add(position_key(food.position()))  # Add normal food.
        if include_bonus and bonus_active:
            positions.add(position_key(bonus_food.position()))  # Add bonus.
        return positions

    def deactivate_bonus():
        """Hide bonus food and clear its timer bar."""
        # nonlocal allows us to update the variable from the enclosing scope.
        nonlocal bonus_active
        bonus_active = False
        bonus_food.hideturtle()  # Make bonus food disappear.
        bar_frame.clear()  # Remove bar outline.
        bar_fill.clear()  # Remove bar fill.

    def spawn_bonus():
        """Activate bonus food and start its timer."""
        # nonlocal lets us update these state variables in main().
        nonlocal bonus_active, bonus_expires_at
        bonus_active = True
        bonus_expires_at = time.time() + BONUS_DURATION  # Expiry timestamp.
        bonus_food.showturtle()  # Make bonus visible.
        place_food(bonus_food, occupied_positions(include_food=True, include_bonus=False))
        left_x = -BAR_WIDTH // 2  # Center the bar horizontally.
        draw_bar_frame(bar_frame, left_x, BAR_TOP_Y, BAR_WIDTH, BAR_HEIGHT)

    def update_bonus_bar():
        """Update the bonus timer bar each frame."""
        if not bonus_active:
            return  # Nothing to update if bonus is not active.
        remaining = bonus_expires_at - time.time()  # Seconds left.
        if remaining <= 0:
            deactivate_bonus()  # Time expired, hide bonus.
            return
        progress = remaining / BONUS_DURATION  # Fraction of time left.
        left_x = -BAR_WIDTH // 2  # Align bar to center.
        draw_bar_fill(bar_fill, left_x, BAR_TOP_Y, BAR_WIDTH, BAR_HEIGHT, progress)

    def apply_mode(new_mode):
        """Apply a new mode (easy/normal/hard) and redraw borders/walls."""
        # nonlocal because we are reassigning state from the outer scope.
        nonlocal mode, wrap_walls, maze_enabled, wall_positions, wall_turtle, border_turtle
        mode = new_mode
        wrap_walls = mode == "easy"
        maze_enabled = mode == "hard"
        if border_turtle:
            border_turtle.clear()  # Clear old border.
            border_turtle.hideturtle()
        border_turtle = draw_border(wrap_walls)  # Draw border for mode.
        if wall_turtle:
            wall_turtle.clear()  # Remove old maze.
            wall_turtle.hideturtle()
            wall_turtle = None
        wall_positions = set(build_maze()) if maze_enabled else set()
        if maze_enabled:
            wall_turtle = draw_maze(wall_positions)  # Draw new maze.

    def reset_state():
        """Reset the snake and gameplay state after a game over."""
        # nonlocal because we are updating outer-scope variables.
        nonlocal score, delay, direction, normal_eats
        head.goto(0, 0)  # Move head back to center.
        direction = "stop"  # Stop movement until input.
        head.setheading(0)  # Face right (default heading).
        for segment in segments:
            segment.hideturtle()  # Hide old body segments.
        segments.clear()  # Clear body list.
        score = 0  # Reset score.
        delay = START_DELAY  # Reset speed.
        normal_eats = 0  # Reset bonus counter.
        deactivate_bonus()  # Hide bonus if active.
        place_food(food, occupied_positions(include_food=False, include_bonus=False))
        draw_score(score_turtle, score, high_score, mode)  # Update HUD.

    def handle_game_over():
        """Pause, show game-over menu, then replay or return to menu."""
        nonlocal direction
        direction = "stop"  # Stop movement immediately.
        deactivate_bonus()  # Clear bonus visuals.
        time.sleep(0.6)  # Small pause before showing menu.
        choice = choose_post_game(screen, score, high_score)  # Menu choice.
        if choice == "menu":
            apply_mode(choose_mode(screen))  # Allow mode change.
        reset_state()  # Reset gameplay state to restart.

    def set_head_heading(new_direction):
        """Rotate the head so the triangle points in the move direction."""
        headings = {"up": 90, "right": 0, "down": 270, "left": 180}
        head.setheading(headings[new_direction])  # Set turtle orientation.

    def go_up():
        """Change direction to up unless reversing."""
        nonlocal direction
        if direction != "down":  # Prevent 180-degree turn.
            direction = "up"
            set_head_heading(direction)

    def go_down():
        """Change direction to down unless reversing."""
        nonlocal direction
        if direction != "up":
            direction = "down"
            set_head_heading(direction)

    def go_left():
        """Change direction to left unless reversing."""
        nonlocal direction
        if direction != "right":
            direction = "left"
            set_head_heading(direction)

    def go_right():
        """Change direction to right unless reversing."""
        nonlocal direction
        if direction != "left":
            direction = "right"
            set_head_heading(direction)

    def move():
        """Move the snake head one grid cell in the current direction."""
        x, y = head.position()  # Current head position.
        if direction == "up":
            head.sety(y + STEP)  # Move up by one cell.
        elif direction == "down":
            head.sety(y - STEP)  # Move down by one cell.
        elif direction == "left":
            head.setx(x - STEP)  # Move left by one cell.
        elif direction == "right":
            head.setx(x + STEP)  # Move right by one cell.

    screen.listen()  # Enable keyboard input.
    screen.onkeypress(go_up, "w")  # WASD controls.
    screen.onkeypress(go_down, "s")
    screen.onkeypress(go_left, "a")
    screen.onkeypress(go_right, "d")
    screen.onkeypress(go_up, "Up")  # Arrow key controls.
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")
    screen.onkeypress(go_right, "Right")

    place_food(food, occupied_positions(include_food=False, include_bonus=False))
    draw_score(score_turtle, score, high_score, mode)  # Initial HUD render.

    try:
        while True:
            screen.update()  # Redraw all turtles for this frame.

            # Handle borders (wrap in easy mode, die in normal/hard).
            x, y = head.position()
            max_x = SCREEN_WIDTH // 2 - STEP
            max_y = SCREEN_HEIGHT // 2 - STEP
            if wrap_walls:
                if x > max_x:
                    head.setx(-max_x)  # Wrap from right to left.
                elif x < -max_x:
                    head.setx(max_x)  # Wrap from left to right.
                if y > max_y:
                    head.sety(-max_y)  # Wrap from top to bottom.
                elif y < -max_y:
                    head.sety(max_y)  # Wrap from bottom to top.
            else:
                if x > max_x or x < -max_x or y > max_y or y < -max_y:
                    handle_game_over()  # Hit wall.
                    continue

            # Check collision with maze walls (hard mode only).
            if maze_enabled and position_key(head.position()) in wall_positions:
                handle_game_over()
                continue

            update_bonus_bar()  # Update bonus timer each frame.

            # Check collision with normal food.
            if head.distance(food) < STEP:
                place_food(food, occupied_positions(include_food=False, include_bonus=True))
                new_segment = make_segment(color="green")  # Add one body segment.
                segments.append(new_segment)
                score += POINTS_PER_FOOD
                if score > high_score:
                    high_score = score
                delay = max(0.05, delay - 0.003)  # Gradually increase speed.
                if not bonus_active:
                    normal_eats += 1
                    if normal_eats >= BONUS_EATS_TRIGGER:
                        normal_eats = 0
                        spawn_bonus()  # Spawn bonus after N normal foods.
                draw_score(score_turtle, score, high_score, mode)

            # Check collision with bonus food.
            if bonus_active and head.distance(bonus_food) < STEP:
                bonus_points = POINTS_PER_FOOD * BONUS_MULTIPLIER
                bonus_segment = make_segment(color="green")  # Add a segment.
                segments.append(bonus_segment)
                score += bonus_points
                if score > high_score:
                    high_score = score
                deactivate_bonus()
                draw_score(score_turtle, score, high_score, mode)

            # Move the body segments from tail to head.
            for idx in range(len(segments) - 1, 0, -1):
                x, y = segments[idx - 1].position()
                segments[idx].goto(x, y)
            if segments:
                x, y = head.position()
                segments[0].goto(x, y)

            move()  # Move the head after the body follows.

            # Check collision with self.
            game_over = False
            for segment in segments:
                if segment.distance(head) < STEP / 2:
                    handle_game_over()
                    game_over = True
                    break
            if game_over:
                continue

            time.sleep(delay)  # Control the frame rate.
    except turtle.Terminator:
        # This exception happens if the user closes the Turtle window.
        pass


# if __name__ == "__main__":
main()  # Direct call so the game starts when this file is run.
