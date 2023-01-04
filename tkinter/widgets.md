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

## Label
### example of how to use a Tkinter label to display text in a window:
```python
import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a label and place it in the window
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Run the Tkinter event loop
window.mainloop()
```
This program creates a window with a single label that displays the text "Hello, Tkinter!". You can customize the appearance and behavior of the label using various options and settings, such as the font, color, and alignment.

## Entry
#### example of how to use a Tkinter entry field to get input from the user:
```python
import tkinter as tk

def on_button_click():
    # Get the text from the entry field
    text = entry.get()
    print("You entered:", text)

# Create the main window
window = tk.Tk()

# Create an entry field and a button
entry = tk.Entry(window)
button = tk.Button(window, text="Get Text", command=on_button_click)

# Place the widgets in the window
entry.pack()
button.pack()

# Run the Tkinter event loop
window.mainloop()
```
This program creates a window with an entry field and a button. When the button is clicked, it will call the on_button_click function, which will get the text from the entry field and print it to the console. You can use the get method of the entry field to get the current text, and you can use the insert method to insert text into the entry field.
