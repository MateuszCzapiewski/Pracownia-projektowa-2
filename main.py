import tkinter as tk
import random

okno = tk.Tk()
okno.title("Ping Pong")

canvas = tk.Canvas(okno, width=600, height=400, bg="skyblue")
canvas.pack()

gracz_paletka = canvas.create_rectangle(250, 380, 350, 390, fill="goldenrod")
przeciwnik_paletka = canvas.create_rectangle(0, 0, 600, 10, fill="goldenrod")
ball = canvas.create_oval(290, 190, 310, 210, fill="yellow")

ball_speed_x = -2
ball_speed_y = 2

game_over = True
paddle_speed = 20

def start_game():
    global game_over, paddle_speed
    game_over = False
    paddle_speed = 20
    canvas.delete("game_over_text")
    okno.after(5, move_ball)

start_button = tk.Button(okno, text="Start", command=start_game)
start_button.pack()


speed_label = tk.Label(okno, text="Prędkość paletki: " + str(paddle_speed))
speed_label.pack(side=tk.RIGHT)

def ruch_paletka(event):
    global paddle_speed

    key = event.keysym
    if key == "Left":
        canvas.move(gracz_paletka, -paddle_speed, 0)
    elif key == "Right":
        canvas.move(gracz_paletka, paddle_speed, 0)
    elif key == "Up":
        paddle_speed += 5
    elif key == "Down":
        if paddle_speed > 5:
            paddle_speed -= 5

    update_speed_label()

okno.bind("<KeyPress>", ruch_paletka)

def move_ball():
    global ball_speed_x, ball_speed_y, game_over

    ball_coords = canvas.coords(ball)
    przeciwnik_coords = canvas.coords(przeciwnik_paletka)

    if ball_coords[0] <= 0 or ball_coords[2] >= 600:
        ball_speed_x = -ball_speed_x

    if ball_coords[1] <= 0:
        ball_speed_y = -ball_speed_y

    if ball_coords[3] >= 400:
        ball_speed_y = -ball_speed_y


    if (
        ball_coords[3] >= canvas.coords(gracz_paletka)[1]
        and ball_coords[1] <= canvas.coords(gracz_paletka)[3]
        and ball_coords[2] >= canvas.coords(gracz_paletka)[0]
        and ball_coords[0] <= canvas.coords(gracz_paletka)[2]
    ):
        ball_speed_y = -ball_speed_y

    canvas.move(ball, ball_speed_x, ball_speed_y)

    ball_coords = canvas.coords(ball)
    if ball_coords[0] < 0:
        canvas.move(ball, -ball_coords[0], 0)
    elif ball_coords[2] > 600:
        canvas.move(ball, 600 - ball_coords[2], 0)


    if ball_coords[3] >= 400 and not game_over:
        game_over = True
        canvas.create_text(
            300,
            200,
            text="Game Over",
            font=("Helvetica", 30),
            fill="red",
            tags="game_over_text",
        )
        start_button.config(text="Restart")

    if not game_over:
        okno.after(10, move_ball)

def update_speed_label():
    speed_label.config(text="Prędkość paletki: " + str(paddle_speed))
    okno.after(1000, update_speed_label)

update_speed_label()

okno.mainloop()
