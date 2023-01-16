| Function | Example | Output |
| --- | --- | --- |
| `pyautogui.moveTo(x, y)` | `pyautogui.moveTo(100, 200)` | Moves the mouse cursor to the coordinates (100, 200) |
| `pyautogui.click(x, y)` | `pyautogui.click(100, 200)` | Simulates a mouse click at the coordinates (100, 200) |
| `pyautogui.doubleClick(x, y)` | `pyautogui.doubleClick(100, 200)` | Simulates a double-click at the coordinates (100, 200) |
| `pyautogui.rightClick(x, y)` | `pyautogui.rightClick(100, 200)` | Simulates a right-click at the coordinates (100, 200) |
| `pyautogui.dragTo(x, y)` | `pyautogui.dragTo(100, 200)` | Simulates a mouse drag to the coordinates (100, 200) |
| `pyautogui.typewrite(string)` | `pyautogui.typewrite("Hello, World!")` | Types the string "Hello, World!" |
| `pyautogui.press(key)` | `pyautogui.press("a")` | Simulates pressing the "a" key |
| `pyautogui.hotkey(key1, key2, ...)` | `pyautogui.hotkey("ctrl", "alt", "delete")` | Simulates pressing the "ctrl", "alt", and "delete" keys at the same time |
| `pyautogui.moveRel(xOffset, yOffset)` | `pyautogui.moveRel(100, 200)` | moves the mouse cursor relative to its current position by 100 pixels to the right and 200 pixels down.
| `pyautogui.dragRel(xOffset, yOffset)` | `pyautogui.dragRel(100, 200)` | simulates a mouse drag relative to the current position by 100 pixels to the right and 200 pixels down.
| `pyautogui.scroll(clicks)` | `pyautogui.scroll(10)` | simulates a mouse scroll wheel movement of 10 clicks
| `pyautogui.typewrite(string, interval)` | `pyautogui.typewrite("Hello, World!", 0.1)` | types the string "Hello, World!" with a delay of 0.1 seconds between each key press.
| `pyautogui.press(key, presses=1, interval=0.0)` | `pyautogui.press("a", presses=3, interval=0.5)` | simulates pressing the "a" key 3 times with a delay of 0.5 seconds between each press.
| `pyautogui.hotkey(*keys, interval=0.0)` | `pyautogui.hotkey("ctrl", "alt", "delete", interval=1)` | simulates pressing the "ctrl", "alt", and "delete" keys at the same time with a delay of 1 second between each press.
| `pyautogui.screenshot(region=None)` | `pyautogui.screenshot()` | takes a screenshot of the entire screen
| `pyautogui.pixelMatchesColor(x, y, color)` | `pyautogui.pixelMatchesColor(100, 200, (255, 255, 255))` | returns True if the pixel at the coordinates (100, 200) is white.
| `pyautogui.locateOnScreen(image)` | `pyautogui.locateOnScreen("image.png")` | returns the coordinates of the image "image.png" on the screen
| `pyautogui.locateCenterOnScreen(image)` | `pyautogui.locateCenterOnScreen("image.png")` | returns the center coordinates of the image "image.png" on the screen
