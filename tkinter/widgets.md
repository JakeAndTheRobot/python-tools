# Widgets

| Widget             | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `Button`           | A button widget that can be clicked to trigger an action                                         |
| `Label`            | A widget that displays text or an image                                                          |
| `Entry`            | A single-line text field for entering input                                                      |
| `Text`             | A multi-line text field for entering and displaying large amounts of text                        |
| `Checkbutton`      | A widget that displays a checkbox that can be checked or unchecked                              |
| `Radiobutton`      | A widget that displays a radio button that can be selected as part of a group                   |
| `Listbox`          | A widget that displays a list of items that can be selected                                     |
| `Menu`             | A widget that displays a menu of options                                                        |
| `Scale`            | A widget that displays a sliding scale for selecting a value                                     |
| `Canvas`           | A widget that provides a drawing surface for displaying graphics and images                     |
| `Frame`            | A container widget that can be used to group other widgets together                             |

## Button
#### example of how to use a Tkinter button to print a message when it is clicked:
```python
import tkinter as tk

def on_button_click():
    print("Button was clicked!")

# Create the main window
window = tk.Tk()

# Create a button and place it in the window
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Run the Tkinter event loop
window.mainloop()
```
This program creates a window with a single button. When the button is clicked, it will call the on_button_click function, which will print the message "Button was clicked!".
