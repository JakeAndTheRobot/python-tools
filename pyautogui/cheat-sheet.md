## Mouse Functions

```python
# Move the mouse to the specified position
pyautogui.moveTo(x, y, duration=num_seconds)

# Move the mouse relative to its current position
pyautogui.moveRel(x_offset, y_offset, duration=num_seconds)

# Get the current mouse position
pyautogui.position()

# Perform a mouse click at the current position
pyautogui.click()

# Perform a mouse click at the specified position
pyautogui.click(x=100, y=200)

# Perform a double click at the current position
pyautogui.doubleClick()

# Perform a triple click at the current position
pyautogui.tripleClick()

# Perform a right mouse click at the current position
pyautogui.rightClick()

# Perform a middle mouse click at the current position
pyautogui.middleClick()

# Perform a mouse scroll at the current position
pyautogui.scroll(clicks)

# Perform a mouse scroll at the specified position
pyautogui.scroll(clicks, x=100, y=200)

```

## Keyboard Funtions

```python
# Type the given message
pyautogui.typewrite(message, interval=0.0)

# Press and release the given keys
pyautogui.press(keys, presses=1, interval=0.0)

# Press and release the given keys simultaneously
pyautogui.hotkey(keys, interval=0.0)

```

## Screen Functions

```python
# Get the size of the screen
pyautogui.size()

# Take a screenshot and save it to the specified file
pyautogui.screenshot(file_name)

# Take a screenshot and return it as an Image object
screenshot = pyautogui.screenshot()

# Find the top-left corner of the first instance of the image on the screen
position = pyautogui.locateOnScreen(image)

# Find the top-left corner and size of the first instance of the image on the screen
position, size = pyautogui.locateOnScreen(image)

# Find the top-left corner of the first instance of the image on the screen within the given region
position = pyautogui.locateOnScreen(image, region=(0, 0, 800, 600))

# Find the top-left corner and size of the first instance of the image on the screen within the given region
position, size = pyautogui.locateOnScreen(image, region=(0, 0, 800, 600))

# Find the center of the first instance of the image on the screen
center = pyautogui.center(image)

# Find the center of the first instance of the image on the screen within the given region
center = pyautogui.center(image, region=(0, 0, 800, 600))

# Wait until the image appears on the screen
pyautogui.wait(image)

# Wait until the image disappears from the screen
```
