from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BG       = RGBColor(0x0D, 0x11, 0x17)
BLUE     = RGBColor(0x58, 0xA6, 0xFF)
LTBLUE   = RGBColor(0x79, 0xC0, 0xFF)
ORANGE   = RGBColor(0xF0, 0x88, 0x3E)
WHITE    = RGBColor(0xC9, 0xD1, 0xD9)
DIM      = RGBColor(0x8B, 0x94, 0x9E)
CARDBG   = RGBColor(0x16, 0x1B, 0x22)
BORDER   = RGBColor(0x30, 0x36, 0x3D)
BLACK    = RGBColor(0x00, 0x00, 0x00)

FONT_TITLE = "Helvetica Neue"
FONT_BODY  = "Menlo"
FONT_HEAD  = "Helvetica Neue"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

def set_bg(slide, color=BG):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, left, top, width, height):
    return slide.shapes.add_textbox(left, top, width, height)

def set_text(tf, text, size=18, color=WHITE, bold=False, font=FONT_BODY, align=PP_ALIGN.LEFT):
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font
    p.alignment = align
    return p

def add_para(tf, text, size=18, color=WHITE, bold=False, font=FONT_BODY, align=PP_ALIGN.LEFT, space_before=Pt(6)):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font
    p.alignment = align
    if space_before:
        p.space_before = space_before
    return p

def add_bullet(tf, text, size=18, color=WHITE, level=0, font=FONT_BODY, space=Pt(4)):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.name = font
    p.level = level
    p.space_before = space
    return p

def add_card(slide, left, top, width, height, fill_color=CARDBG):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = BORDER
    shape.line.width = Pt(1)
    shape.shadow.inherit = False
    return shape

def title_line(slide, text, y=Inches(0.5)):
    tb = add_textbox(slide, Inches(0.8), y, Inches(11.5), Inches(0.8))
    set_text(tb.text_frame, text, size=36, color=BLUE, bold=True, font=FONT_HEAD, align=PP_ALIGN.LEFT)
    return tb

def step_title(slide, num, text, y=Inches(0.4)):
    tb = add_textbox(slide, Inches(0.8), y, Inches(11.5), Inches(0.8))
    tf = tb.text_frame
    set_text(tf, f"Step {num}:  {text}", size=34, color=BLUE, bold=True, font=FONT_HEAD)
    return tb

def code_block(slide, left, top, width, height, code_text):
    card = add_card(slide, left, top, width, height, fill_color=RGBColor(0x0D, 0x11, 0x17))
    card.line.color.rgb = BORDER
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(12)
    tf.margin_top = Pt(8)
    tf.margin_right = Pt(12)
    tf.margin_bottom = Pt(8)
    lines = code_text.strip().split("\n")
    for i, line in enumerate(lines):
        if i == 0:
            set_text(tf, line, size=14, color=RGBColor(0xC9, 0xD1, 0xD9), font=FONT_BODY)
        else:
            add_para(tf, line, size=14, color=RGBColor(0xC9, 0xD1, 0xD9), font=FONT_BODY, space_before=Pt(1))
    return card

# ========== SLIDE 1: TITLE ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
tb = add_textbox(slide, Inches(1), Inches(2.0), Inches(11), Inches(1.2))
set_text(tb.text_frame, "jsh", size=72, color=BLUE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER)
tb2 = add_textbox(slide, Inches(1), Inches(3.3), Inches(11), Inches(0.7))
set_text(tb2.text_frame, "A Unix Shell Written in C", size=32, color=LTBLUE, font=FONT_HEAD, align=PP_ALIGN.CENTER)
tb3 = add_textbox(slide, Inches(1), Inches(4.4), Inches(11), Inches(0.5))
set_text(tb3.text_frame, "Advanced C Project  —  EPITA MSc SE", size=20, color=DIM, font=FONT_HEAD, align=PP_ALIGN.CENTER)
tb4 = add_textbox(slide, Inches(1), Inches(5.0), Inches(11), Inches(0.5))
set_text(tb4.text_frame, "Joshua Musa", size=22, color=WHITE, font=FONT_HEAD, align=PP_ALIGN.CENTER)

# ========== SLIDE 2: AGENDA ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Agenda")
tb = add_textbox(slide, Inches(1.2), Inches(1.5), Inches(10), Inches(5.5))
tf = tb.text_frame
items = [
    "Project Scope & Motivation",
    "Features Overview",
    "Architecture & Source Files",
    "Development Steps (1–8)",
    "Key System Calls",
    "Difficulties & Design Choices",
    "Code Quality",
    "Live Demo",
]
for i, item in enumerate(items):
    if i == 0:
        set_text(tf, f"{i+1}.  {item}", size=24, color=WHITE, font=FONT_HEAD)
    else:
        add_para(tf, f"{i+1}.  {item}", size=24, color=WHITE, font=FONT_HEAD, space_before=Pt(14))

# ========== SLIDE 3: PROJECT SCOPE ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Project Scope")

tb = add_textbox(slide, Inches(1.0), Inches(1.5), Inches(11), Inches(0.6))
set_text(tb.text_frame, "Goal:  Build a functional Unix shell from scratch in C99", size=22, color=WHITE, bold=True, font=FONT_HEAD)

tb = add_textbox(slide, Inches(1.0), Inches(2.3), Inches(11), Inches(0.5))
set_text(tb.text_frame, "Why a shell?", size=24, color=ORANGE, bold=True, font=FONT_HEAD)

tb = add_textbox(slide, Inches(1.2), Inches(2.9), Inches(10), Inches(3.5))
tf = tb.text_frame
bullets = [
    "Touches nearly every core C concept: memory, pointers, strings, arrays",
    "Deep dive into POSIX system calls: fork, exec, pipe, dup2",
    "Process management, signals, file descriptors",
    "Terminal I/O at the lowest level (raw mode, escape sequences)",
]
for i, b in enumerate(bullets):
    if i == 0:
        set_text(tf, f"•  {b}", size=20, color=WHITE, font=FONT_HEAD)
    else:
        add_para(tf, f"•  {b}", size=20, color=WHITE, font=FONT_HEAD, space_before=Pt(10))

tb = add_textbox(slide, Inches(1.0), Inches(5.8), Inches(11), Inches(0.5))
set_text(tb.text_frame, "~900 lines of C  ·  9 source files  ·  No external libraries — only libc + POSIX", size=16, color=DIM, font=FONT_HEAD, align=PP_ALIGN.LEFT)

# ========== SLIDE 4: FEATURES ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Features")

features = [
    ("REPL", "Interactive prompt with\nread-eval-print loop"),
    ("External Commands", "Run any program in $PATH\nvia fork + execvp"),
    ("Built-in Commands", "cd, pwd, exit run directly\nin the parent process"),
    ("I/O Redirection", "> (overwrite), >> (append),\n< (read from file)"),
    ("Pipes", "Arbitrary-length pipelines:\ncmd1 | cmd2 | cmd3"),
    ("Operators", "&& (and), || (or),\n; (sequential)"),
    ("Glob Expansion", "*.c and ? wildcards\nexpanded by the shell"),
    ("Line Editor + History", "Raw-mode input with\narrow keys and history"),
]

for i, (title, desc) in enumerate(features):
    col = i % 4
    row = i // 4
    left = Inches(0.6 + col * 3.1)
    top  = Inches(1.5 + row * 2.6)
    card = add_card(slide, left, top, Inches(2.8), Inches(2.2))
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(14)
    tf.margin_right = Pt(14)
    set_text(tf, title, size=18, color=BLUE, bold=True, font=FONT_HEAD)
    for line in desc.split("\n"):
        add_para(tf, line, size=15, color=WHITE, font=FONT_HEAD, space_before=Pt(4))

# ========== SLIDE 5: ARCHITECTURE ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Architecture")

code = """include/
  shell.h           — Shared function declarations

src/
  main.c            — REPL loop (entry point)
  terminal.c        — Raw-mode line editor + history
  tokenizer.c       — Splits input into token array
  operators.c       — ;  &&  ||  dispatch + glob
  globbing.c        — Wildcard expansion
  executor.c        — fork + execvp single commands
  pipes.c           — Multi-command pipelines
  redirections.c    — >  >>  <  via open + dup2
  builtins.c        — cd, exit, pwd"""

code_block(slide, Inches(1.0), Inches(1.5), Inches(7.5), Inches(5.0), code)

tb = add_textbox(slide, Inches(9.0), Inches(1.5), Inches(3.8), Inches(5.0))
tf = tb.text_frame
set_text(tf, "Design principles", size=20, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=10, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  Each file has one job", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  One shared header: shell.h", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  No global state (except history)", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  Clean separation of concerns", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  Compiles with -Wall -Wextra -Werror: zero warnings", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(10))

# ========== SLIDE 6: STEP 1 — REPL ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 1, "The REPL Skeleton")

code = """while (1) {
    ensure_newline()     // fix cursor if mid-line
    print "jsh $ "       // prompt
    line = read_line()   // raw-mode input
    if line == NULL      // Ctrl+D → EOF
        break
    if line is empty     // just pressed Enter
        continue
    tokens = tokenize(line)
    run_command_line(tokens)
    free tokens
}
return 0"""
code_block(slide, Inches(0.8), Inches(1.3), Inches(5.5), Inches(5.2), code)

tb = add_textbox(slide, Inches(7.0), Inches(1.3), Inches(5.5), Inches(5.2))
tf = tb.text_frame
set_text(tf, "How it works", size=22, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "•  Ctrl+D returns NULL from read_line() → breaks the loop and exits cleanly", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  Empty lines (just Enter) are skipped — no crash, no noise", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  ensure_newline() queries the terminal cursor position; if the cursor is mid-line (from a command like printf without \\n), it prints a newline first", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  Every iteration: allocate → use → free. No memory leaks.", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  Parent ignores SIGINT so Ctrl+C doesn't kill the shell itself", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))

# ========== SLIDE 7: STEP 2 — TOKENIZER ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 2, "Tokenizer")

tb = add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, "Splits a raw input string into an array of word tokens:", size=20, color=WHITE, font=FONT_HEAD)

code = """"ls -la /tmp"  →  ["ls", "-la", "/tmp", NULL]"""
code_block(slide, Inches(0.8), Inches(2.0), Inches(7.5), Inches(0.7), code)

tb = add_textbox(slide, Inches(0.8), Inches(3.0), Inches(11.5), Inches(4.0))
tf = tb.text_frame
set_text(tf, "Algorithm:", size=20, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "1.  Walk the string character by character", size=19, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "2.  Skip over whitespace between words", size=19, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "3.  For each word: malloc a copy (strdup) and store the pointer", size=19, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "4.  The array grows dynamically — doubles capacity when full (realloc)", size=19, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "5.  NULL-terminate the array — this is what execvp expects", size=19, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "6.  Return the array + count to the caller", size=19, color=WHITE, font=FONT_HEAD, space_before=Pt(10))

# ========== SLIDE 8: STEP 3 — EXECUTOR ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 3, "Command Execution — fork + execvp + waitpid")

left_items = [
    ("fork()", "Creates an exact copy of the shell.\nReturns 0 in child, child PID in parent."),
    ("execvp()", "Replaces the child process with the\nactual command (e.g. /bin/ls).\nThe child becomes the command."),
    ("waitpid()", "Parent blocks until the child exits.\nThen collects the exit code and\nprints the prompt again."),
]
y = Inches(1.3)
for title, desc in left_items:
    card = add_card(slide, Inches(0.8), y, Inches(5.5), Inches(1.6))
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(10)
    set_text(tf, title, size=18, color=ORANGE, bold=True, font=FONT_BODY)
    for line in desc.split("\n"):
        add_para(tf, line, size=15, color=WHITE, font=FONT_HEAD, space_before=Pt(2))
    y += Inches(1.75)

code = """JSH (parent, pid 100)
       |
    fork()
       |              \\
  PARENT (100)     CHILD (101)
       |              |
  waitpid(101)    execvp("ls")
  (blocks)            |
       |          child is now /bin/ls
       |          runs, prints, exits
       |              |
  waitpid returns  <-- child dead
       |
  print prompt"""
code_block(slide, Inches(6.8), Inches(1.3), Inches(5.8), Inches(5.5), code)

# ========== SLIDE 9: STEP 4 — BUILTINS + SIGNALS ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 4, "Built-in Commands & Signals")

# Left column: builtins
tb = add_textbox(slide, Inches(0.8), Inches(1.3), Inches(6.0), Inches(0.5))
set_text(tb.text_frame, "Why must some commands be built-in?", size=20, color=ORANGE, bold=True, font=FONT_HEAD)

tb = add_textbox(slide, Inches(0.8), Inches(1.9), Inches(6.0), Inches(2.0))
tf = tb.text_frame
set_text(tf, "cd must run in the parent process.", size=18, color=WHITE, font=FONT_HEAD)
add_para(tf, "If cd ran in a forked child, it would change the child's directory — then the child exits and the parent's directory is unchanged.", size=17, color=DIM, font=FONT_HEAD, space_before=Pt(6))

# Builtin table as cards
builtins = [("cd [dir]", "chdir() in parent"), ("pwd", "getcwd() + print"), ("exit", "exit(0)")]
y = Inches(3.5)
for cmd, desc in builtins:
    card = add_card(slide, Inches(0.8), y, Inches(5.5), Inches(0.7))
    tf = card.text_frame
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(6)
    tf.word_wrap = True
    set_text(tf, f"{cmd}   →   {desc}", size=16, color=WHITE, font=FONT_BODY)
    y += Inches(0.85)

# Right column: signals
card = add_card(slide, Inches(7.0), Inches(1.3), Inches(5.5), Inches(2.2))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Signal Handling", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "Parent:  signal(SIGINT, SIG_IGN)", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(6))
add_para(tf, "Ignores Ctrl+C → shell stays alive", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(4))
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "Child:   signal(SIGINT, SIG_DFL)", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(6))
add_para(tf, "Restores default → Ctrl+C kills commands", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(4))

card2 = add_card(slide, Inches(7.0), Inches(3.8), Inches(5.5), Inches(1.8))
tf2 = card2.text_frame
tf2.word_wrap = True
tf2.margin_left = Pt(14)
tf2.margin_top = Pt(14)
set_text(tf2, "handle_builtin() return values:", size=18, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf2, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf2, "-1 = not a builtin → try execvp", size=16, color=WHITE, font=FONT_BODY, space_before=Pt(6))
add_para(tf2, " 0 = builtin succeeded", size=16, color=WHITE, font=FONT_BODY, space_before=Pt(4))
add_para(tf2, " 1 = builtin failed (e.g. cd bad dir)", size=16, color=WHITE, font=FONT_BODY, space_before=Pt(4))

# ========== SLIDE 10: STEP 5 — REDIRECTIONS ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 5, "I/O Redirection  (>  >>  <)")

tb = add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, 'File descriptors are like TV channels — we retune where they point:', size=20, color=WHITE, font=FONT_HEAD)

# FD table
fds = [("fd 0  (stdin)", "Keyboard", "Where input comes from"),
       ("fd 1  (stdout)", "Screen", "Where output goes"),
       ("fd 2  (stderr)", "Screen", "Where errors go")]
y = Inches(2.0)
for fd, default, purpose in fds:
    card = add_card(slide, Inches(0.8), y, Inches(5.5), Inches(0.65))
    tf = card.text_frame
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(6)
    tf.word_wrap = True
    set_text(tf, f"{fd}   default: {default}  —  {purpose}", size=15, color=WHITE, font=FONT_BODY)
    y += Inches(0.75)

# Right side: example
code = """echo hello > out.txt

Step 1: open("out.txt") → returns fd 3
Step 2: dup2(3, 1) — retune fd 1
        fd 1 (stdout) now → out.txt
Step 3: close(fd 3) — no longer needed
Step 4: echo writes to fd 1 as usual
        but it goes to the file now

Runs in the CHILD only (after fork,
before execvp) so parent fds are safe."""
code_block(slide, Inches(6.8), Inches(1.6), Inches(5.8), Inches(4.5), code)

# Operators
tb = add_textbox(slide, Inches(0.8), Inches(4.5), Inches(5.5), Inches(2.0))
tf = tb.text_frame
set_text(tf, ">    open with O_TRUNC (overwrite)", size=16, color=ORANGE, font=FONT_BODY)
add_para(tf, ">>   open with O_APPEND (add to end)", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(8))
add_para(tf, "<    open with O_RDONLY (read input)", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(8))

# ========== SLIDE 11: STEP 6 — PIPES ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 6, "Pipes")

tb = add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, "pipe(fd) creates a one-way data channel:  fd[0] = read end,  fd[1] = write end", size=20, color=WHITE, font=FONT_HEAD)

code = """ls | grep .c

1. Create pipe → fd[0]=read, fd[1]=write
2. fork() child 1 (ls):
     dup2(fd[1], stdout) → ls output goes into pipe
     close(fd[0], fd[1]) → already duplicated
     execvp("ls")
3. fork() child 2 (grep):
     dup2(fd[0], stdin)  → grep reads from pipe
     close(fd[0], fd[1])
     execvp("grep", [".c"])
4. Parent closes both pipe ends
5. waitpid() for both children"""
code_block(slide, Inches(0.8), Inches(2.0), Inches(6.5), Inches(4.8), code)

tb = add_textbox(slide, Inches(7.8), Inches(2.0), Inches(5.0), Inches(4.8))
tf = tb.text_frame
set_text(tf, "Key insight", size=20, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "•  ls writes to stdout as usual", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  grep reads from stdin as usual", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "•  Neither knows about the other — the pipe connects them through the kernel", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "", size=10, font=FONT_HEAD, color=WHITE, space_before=Pt(10))
add_para(tf, "Critical rule:", size=20, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "Must close unused pipe ends! If the write end stays open anywhere, the reader never sees EOF and hangs forever.", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))

# ========== SLIDE 12: MULTI-PIPE ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 6, "Multi-Pipe Chaining  (ls | grep .c | wc -l)")

code = """Iteration 1:
  pipe() → fd[3]=read, fd[4]=write
  fork child 1 (ls):
    stdout → fd[4] (pipe write end)
    execvp("ls")
  Parent: close fd[4], save fd[3] as prev_fd

Iteration 2:
  pipe() → fd[5]=read, fd[6]=write
  fork child 2 (grep):
    stdin  ← prev_fd (fd[3], reads ls output)
    stdout → fd[6] (new pipe write end)
    execvp("grep", [".c"])
  Parent: close prev_fd, close fd[6]
          prev_fd = fd[5]

Iteration 3 (last command, no new pipe):
  fork child 3 (wc):
    stdin ← prev_fd (fd[5], reads grep output)
    execvp("wc", ["-l"])
  Parent: close prev_fd

waitpid() for all 3 children
Return last child's exit code"""
code_block(slide, Inches(0.8), Inches(1.3), Inches(7.5), Inches(5.8), code)

tb = add_textbox(slide, Inches(8.8), Inches(1.5), Inches(4.0), Inches(4.0))
tf = tb.text_frame
set_text(tf, "The prev_fd trick:", size=20, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "Each iteration saves the read end of the current pipe as prev_fd.", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "The next command reads from prev_fd and writes to a brand new pipe.", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))
add_para(tf, "This chains any number of commands together.", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(10))

# ========== SLIDE 13: STEP 7 — OPERATORS ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 7, "Operators  ( ;  &&  || )")

# Operator table
ops = [
    (";", "Always run the next command"),
    ("&&", "Run next only if previous succeeded (exit 0)"),
    ("||", "Run next only if previous failed (exit ≠ 0)"),
]
y = Inches(1.3)
for op, desc in ops:
    card = add_card(slide, Inches(0.8), y, Inches(5.5), Inches(0.65))
    tf = card.text_frame
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(6)
    tf.word_wrap = True
    set_text(tf, f"  {op}    {desc}", size=16, color=WHITE, font=FONT_BODY)
    y += Inches(0.75)

code = """gcc main.c && ./a.out
→ runs a.out only if gcc succeeded

gcc main.c || echo FAIL
→ echoes FAIL only if gcc failed

echo hi ; ls ; pwd
→ all three run no matter what"""
code_block(slide, Inches(7.0), Inches(1.3), Inches(5.5), Inches(3.0), code)

tb = add_textbox(slide, Inches(0.8), Inches(3.8), Inches(11.5), Inches(3.0))
tf = tb.text_frame
set_text(tf, "How it works in run_command_line():", size=20, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "1.  Walk tokens left to right, scanning for operators", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "2.  Each operator marks the end of a segment", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "3.  Before running a segment, check: should we skip?", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "     •  Previous was &&  but last command failed  →  skip", size=17, color=DIM, font=FONT_HEAD, space_before=Pt(4))
add_para(tf, "     •  Previous was ||  but last command succeeded  →  skip", size=17, color=DIM, font=FONT_HEAD, space_before=Pt(4))
add_para(tf, "4.  Otherwise: expand globs → check for pipes → check builtins → execute", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))

# ========== SLIDE 14: STEP 7 cont — GLOB ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 7, "Glob Expansion  ( *.c  and  ? )")

tb = add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.5))
set_text(tb.text_frame, "The shell expands wildcards before the command ever sees them:", size=20, color=WHITE, font=FONT_HEAD)

code = """ls *.c
→ the shell expands this to:
ls main.c pipes.c executor.c tokenizer.c ..."""
code_block(slide, Inches(0.8), Inches(2.0), Inches(6.5), Inches(1.5), code)

tb = add_textbox(slide, Inches(0.8), Inches(3.8), Inches(11.5), Inches(3.5))
tf = tb.text_frame
set_text(tf, "Algorithm:", size=20, color=ORANGE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "1.  For each token, check:  does it contain * or ?     (strchr)", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "2.  If yes → call glob() to find all matching filenames", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "3.  Splice the matches into a new token array, replacing the wildcard token", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "4.  If no matches → keep the original token as-is (same as bash)", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "5.  Free the old array, use the expanded one", size=18, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "", size=10, font=FONT_HEAD, color=WHITE, space_before=Pt(8))
add_para(tf, "Called in operators.c before dispatching each segment. Each token is checked independently.", size=17, color=DIM, font=FONT_HEAD, space_before=Pt(4))

# ========== SLIDE 15: STEP 8 — RAW MODE ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 8, "Raw-Mode Line Editor")

tb = add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.6))
tf = tb.text_frame
set_text(tf, 'Problem:  getline() uses "cooked mode" — no control over arrow keys, history, or display.', size=20, color=WHITE, font=FONT_HEAD)
add_para(tf, 'Solution:  Switch to raw mode using the termios API.', size=20, color=WHITE, font=FONT_HEAD, space_before=Pt(6))

# Left: termios
card = add_card(slide, Inches(0.8), Inches(2.4), Inches(5.5), Inches(4.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "termios settings", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "tcgetattr() — save current settings", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(8))
add_para(tf, "tcsetattr() — apply raw mode", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(4))
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(6))
add_para(tf, "Disable ECHO:", size=17, color=WHITE, bold=True, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "Typed characters are NOT auto-printed. We manually write() each one to the screen.", size=16, color=DIM, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(6))
add_para(tf, "Disable ICANON:", size=17, color=WHITE, bold=True, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "Input is delivered one character at a time, instead of waiting for Enter.", size=16, color=DIM, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(6))
add_para(tf, "VMIN=1, VTIME=0:", size=17, color=WHITE, bold=True, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "read() blocks until at least 1 byte arrives.", size=16, color=DIM, font=FONT_HEAD, space_before=Pt(2))

# Right: character handling
card = add_card(slide, Inches(6.8), Inches(2.4), Inches(5.8), Inches(4.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Character handling loop", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "Printable (32–126):", size=17, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "Append to buffer + echo to screen", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "Enter:", size=17, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "Null-terminate, save to history, return", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "Backspace (127):", size=17, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "Erase last char from buffer + screen", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "Arrow keys (escape sequences):", size=17, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "Up/Down: cycle through history", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "Left/Right: move cursor position", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(2))
add_para(tf, "Ctrl+D (byte 4):", size=17, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "Free buffer, return NULL (EOF signal)", size=16, color=WHITE, font=FONT_HEAD, space_before=Pt(2))

# ========== SLIDE 16: STEP 8 cont — HISTORY ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
step_title(slide, 8, "Command History")

card = add_card(slide, Inches(0.8), Inches(1.3), Inches(5.5), Inches(5.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "History implementation", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "•  Static array of strdup'd strings", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "•  Up to 100 entries", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  add_to_history() saves non-empty lines", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  When full: free oldest, memmove all down", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  Up/Down arrows adjust history_index", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "", size=10, font=FONT_HEAD, color=WHITE, space_before=Pt(10))
add_para(tf, "Redrawing on navigation:", size=18, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "write(\"\\r\")     → cursor to column 0", size=15, color=WHITE, font=FONT_BODY, space_before=Pt(6))
add_para(tf, "write(\"\\033[K\") → erase to end of line", size=15, color=WHITE, font=FONT_BODY, space_before=Pt(4))
add_para(tf, "write(\"jsh $ \") → reprint prompt", size=15, color=WHITE, font=FONT_BODY, space_before=Pt(4))
add_para(tf, "write(buffer)   → print history entry", size=15, color=WHITE, font=FONT_BODY, space_before=Pt(4))

# Right: escape sequences
card = add_card(slide, Inches(6.8), Inches(1.3), Inches(5.8), Inches(3.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Arrow key escape sequences", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "Arrow keys send 3 bytes each:", size=17, color=DIM, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "\\033 [ A  =  Up arrow", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(6))
add_para(tf, "\\033 [ B  =  Down arrow", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(4))
add_para(tf, "\\033 [ C  =  Right arrow", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(4))
add_para(tf, "\\033 [ D  =  Left arrow", size=16, color=ORANGE, font=FONT_BODY, space_before=Pt(4))
add_para(tf, "", size=6, font=FONT_HEAD, color=WHITE, space_before=Pt(4))
add_para(tf, "When \\033 is detected, read 2 more bytes to identify which arrow key was pressed.", size=16, color=DIM, font=FONT_HEAD, space_before=Pt(4))

# ensure_newline
card = add_card(slide, Inches(6.8), Inches(5.1), Inches(5.8), Inches(1.7))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "ensure_newline()", size=18, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "Queries cursor column via \\033[6n (Device Status Report). If cursor is not at column 1, prints a newline so the prompt starts on a fresh line.", size=15, color=DIM, font=FONT_HEAD, space_before=Pt(6))

# ========== SLIDE 17: SYSTEM CALLS SUMMARY ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Key System Calls Summary")

syscalls = [
    ("fork()", "Clone the current process", "executor, pipes"),
    ("execvp()", "Replace process with a command", "executor, pipes"),
    ("waitpid()", "Wait for a child to finish", "executor, pipes"),
    ("pipe()", "Create a one-way data channel", "pipes"),
    ("dup2()", "Retune a file descriptor", "redirections, pipes"),
    ("open()", "Open a file, get an fd", "redirections"),
    ("signal()", "Set signal handler (IGN/DFL)", "main, executor"),
    ("tcgetattr / tcsetattr", "Get / set terminal mode", "terminal"),
    ("glob()", "Expand wildcard patterns", "globbing"),
    ("chdir() / getcwd()", "Change / get working dir", "builtins"),
]

# Header
y = Inches(1.4)
card = add_card(slide, Inches(0.8), y, Inches(11.5), Inches(0.55), fill_color=RGBColor(0x21, 0x26, 0x2D))
tf = card.text_frame
tf.margin_left = Pt(14)
tf.margin_top = Pt(6)
tf.word_wrap = True
run = set_text(tf, "", size=15, color=BLUE, bold=True, font=FONT_BODY)
# We'll just do text
set_text(tf, "System Call                      What It Does                              Used In", size=15, color=BLUE, bold=True, font=FONT_BODY)
y += Inches(0.6)

for call, desc, used_in in syscalls:
    card = add_card(slide, Inches(0.8), y, Inches(11.5), Inches(0.48))
    tf = card.text_frame
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(4)
    tf.word_wrap = True
    line = f"{call:<32s}{desc:<42s}{used_in}"
    set_text(tf, line, size=14, color=WHITE, font=FONT_BODY)
    y += Inches(0.52)

# ========== SLIDE 18: DIFFICULTIES ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Difficulties & Design Choices")

difficulties = [
    ("Pipe fd leaks", "Forgetting to close unused pipe ends caused children to hang forever waiting for EOF. Every fd must be closed in every process that doesn't use it."),
    ("cd must be a builtin", "Running cd in a forked child changes the child's directory — which is useless because the child exits immediately. cd must call chdir() in the parent."),
    ("Redirections in the child", "Redirections must run after fork() but before execvp(), so the parent's file descriptors stay untouched for the next command."),
    ("Raw mode complexity", "Had to handle every character manually: printable chars, backspace, escape sequences (3-byte arrow keys), Ctrl+D. Plus restore terminal settings on every exit path."),
    ("Memory discipline", "Every malloc has a matching free. Token arrays, line buffers, glob results, history entries — all freed after use. No leaks in normal flow."),
]

y = Inches(1.3)
for title, desc in difficulties:
    card = add_card(slide, Inches(0.8), y, Inches(11.5), Inches(1.05))
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(14)
    tf.margin_top = Pt(8)
    set_text(tf, title, size=17, color=ORANGE, bold=True, font=FONT_HEAD)
    add_para(tf, desc, size=15, color=DIM, font=FONT_HEAD, space_before=Pt(2))
    y += Inches(1.15)

# ========== SLIDE 19: CODE QUALITY ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Code Quality")

# Left: structure + build
card = add_card(slide, Inches(0.8), Inches(1.4), Inches(5.5), Inches(2.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Structure", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "•  9 source files, each with one job", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "•  One shared header: shell.h", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  Clean separation of concerns", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  No global state (except history)", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))

card = add_card(slide, Inches(0.8), Inches(4.2), Inches(5.5), Inches(2.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Build", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "•  Makefile with all, clean, re targets", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "•  Compiles with -Wall -Wextra -Werror", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  Zero warnings", size=17, color=ORANGE, bold=True, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  C99 standard", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))

# Right: style + safety
card = add_card(slide, Inches(6.8), Inches(1.4), Inches(5.8), Inches(2.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Style", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "•  Consistent brace style throughout", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "•  Every function has a doc comment", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  Inline comments explain the \"why\"", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  ~900 lines total — no bloat", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))

card = add_card(slide, Inches(6.8), Inches(4.2), Inches(5.8), Inches(2.5))
tf = card.text_frame
tf.word_wrap = True
tf.margin_left = Pt(14)
tf.margin_top = Pt(14)
set_text(tf, "Safety", size=20, color=BLUE, bold=True, font=FONT_HEAD)
add_para(tf, "•  All malloc/realloc checked for NULL", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(8))
add_para(tf, "•  All fork/pipe/open errors handled", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  perror() on every failure path", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))
add_para(tf, "•  No memory leaks in normal flow", size=17, color=WHITE, font=FONT_HEAD, space_before=Pt(6))

# ========== SLIDE 20: DEMO ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
title_line(slide, "Demo")

code = """$ make && ./jsh

jsh $ echo hello world
jsh $ ls -la | grep .c | wc -l
jsh $ echo hi > out.txt && cat out.txt
jsh $ gcc main.c || echo "compilation failed"
jsh $ cd /tmp ; pwd
jsh $ ls *.c
jsh $ ↑ ↓  (arrow keys for history)
jsh $ Ctrl+C  (kills running command, not the shell)
jsh $ Ctrl+D  (exits)"""
code_block(slide, Inches(1.5), Inches(1.5), Inches(10), Inches(5.0), code)

# ========== SLIDE 21: THANK YOU ==========
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide)
tb = add_textbox(slide, Inches(1), Inches(2.5), Inches(11), Inches(1.2))
set_text(tb.text_frame, "Thank You", size=64, color=BLUE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER)
tb2 = add_textbox(slide, Inches(1), Inches(4.0), Inches(11), Inches(0.7))
set_text(tb2.text_frame, "Questions?", size=36, color=LTBLUE, font=FONT_HEAD, align=PP_ALIGN.CENTER)

# ========== SAVE ==========
output = "/Users/joshuamusa/Desktop/EPITA/MSC-SE/S2/Advanced_C/Project/shell/jsh_presentation.pptx"
prs.save(output)
print(f"Saved to {output}")
