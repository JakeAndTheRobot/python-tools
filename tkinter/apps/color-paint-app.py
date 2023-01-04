# This program creates a window with a canvas widget and a button. 
# The canvas widget allows the user to draw circles on it by dragging the mouse, and the button opens a color chooser dialog that allows the user to select a new color. 
# The current color is used to fill the circles as they are drawn on the canvas. You can use the create_oval method of the canvas widget

import tkinter as tk
import tkinter.colorchooser as colorchooser

def on_paint(event):
    # Draw a circle on the canvas at the current mouse position
    x, y = event.x, event.y
    r = 5
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)

def on_color_change():
    # Open a color chooser dialog and update the current color
    global color
    color = colorchooser.askcolor()[1]

# Create the main window
window = tk.Tk()

# Create a canvas and a button
canvas = tk.Canvas(window, width=200, height=100)
canvas.pack()
canvas.bind("<B1-Motion>", on_paint)
button = tk.Button(window, text="Change Color", command=on_color_change)
button.pack()

# Set the initial color
color = "black"

# Run the Tkinter event loop
window.mainloop()
