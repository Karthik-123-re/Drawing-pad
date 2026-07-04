import tkinter as tk

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=2, capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

def clear_canvas(event=None):
    canvas.delete("all")

root = tk.Tk()
root.title("Draw using Mouse")

canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()

button = tk.Button(root, text="Clear", command=clear_canvas)
button.pack()

last_x, last_y = 0, 0

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()
