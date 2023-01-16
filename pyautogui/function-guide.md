| Function                               | Description                                                                                                                                                                                                                    |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pyautogui.size()`                     | Returns the current screen resolution as a tuple (width, height).                                                                                                                                                            |
| `pyautogui.position()`                 | Returns the current mouse position as a tuple (x, y).                                                                                                                                                                         |
| `pyautogui.moveTo(x, y, duration=...)` | Moves the mouse to the specified position over the given duration.                                                                                                                                                             |
| `pyautogui.moveRel(x_offset, y_offset, duration=...)` | Moves the mouse relative to its current position over the given duration.                                                                                                                                                    |
| `pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left')` | Performs a mouse click at the specified position (or the current position if none is given) with the given number of clicks and interval between clicks. The default button is the left mouse button.                         |
| `pyautogui.doubleClick(x=None, y=None, interval=0.0, button='left')` | Performs a double click at the specified position (or the current position if none is given) with the given interval between clicks. The default button is the left mouse button.                                              |
| `pyautogui.tripleClick(x=None, y=None, interval=0.0, button='left')` | Performs a triple click at the specified position (or the current position if none is given) with the given interval between clicks. The default button is the left mouse button.                                              |
| `pyautogui.rightClick(x=None, y=None)` | Performs a right mouse click at the specified position (or the current position if none is given).                                                                                                                             |
| `pyautogui.middleClick(x=None, y=None)` | Performs a middle mouse click at the specified position (or the current position if none is given).                                                                                                                           |
| `pyautogui.scroll(clicks, x=None, y=None)` | Performs a mouse scroll at the current position (or the specified position if given) by the given number of clicks.                                                                                                           |
| `pyautogui.typewrite(message, interval=0.0)` | Types the given message as if it were being typed on a keyboard. The interval argument specifies the delay between each key press.                                                                                            |
| `pyautogui.press(keys, presses=1, interval=0.0)` | Presses and releases the given keys (which can be a string of characters or a list of key names) the specified number of times with the given interval between presses.                                                       |
| `pyautogui.hotkey(keys, interval=0.0)` | Presses and releases the given keys simultaneously (which can be a string of characters or a list of key names) with the given interval between press and release.                                                             |
``