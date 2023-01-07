import tkinter as tk
import pyautogui
import tkinter.filedialog

def take_screenshot():
  # Get the region coordinates from the Entry widgets
  x1 = int(entry1.get())
  y1 = int(entry2.get())
  x2 = int(entry3.get())
  y2 = int(entry4.get())

  # Open a Save As dialog box and get the image name
  image_name = tkinter.filedialog.asksaveasfilename()

  # Take a screenshot of the specified region and save it to an image file
  image = pyautogui.screenshot(image_name, region=(x1, y1, x2, y2))
  print(f'Screenshot "{image_name}" saved!')

# Create the main window
window = tk.Tk()
window.title('Screenshot App')

# Create Entry widgets for the region coordinates
entry1 = tk.Entry(window, width=5)
entry2 = tk.Entry(window, width=5)
entry3 = tk.Entry(window, width=5)
entry4 = tk.Entry(window, width=5)

# Create labels for the Entry widgets
label1 = tk.Label(window, text='x1')
label2 = tk.Label(window, text='y1')
label3 = tk.Label(window, text='x2')
label4 = tk.Label(window, text='y2')

# Use the grid() manager to place the widgets
label1.grid(row=0, column=0, sticky='e')
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0, sticky='e')
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0, sticky='e')
entry3.grid(row=2, column=1)
label4.grid(row=3, column=0, sticky='e')
entry4.grid(row=3, column=1)

# Create a Button widget
button = tk.Button(window, text='Take Screenshot', command=take_screenshot)
button.grid(row=4, column=1)

window.mainloop()
