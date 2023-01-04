# `keyboard` Library Reference

## Functions

### `keyboard.add_hotkey(hotkey, callback, args=(), suppress=False, trigger_on_release=False)`

Adds a hotkey that calls the `callback` function when the hotkey is pressed.

#### Parameters
- `hotkey`: A string that describes the hotkey. The string should consist of one or more modifier keys (`alt`, `ctrl`, `shift`, `win`, and `cmd`), the `+` symbol, and a key name (e.g. `"ctrl+shift+a"`).
- `callback`: A function that will be called when the hotkey is pressed. The function should take no arguments.
- `args`: An optional tuple of arguments to pass to the `callback` function when it is called.
- `suppress`: An optional boolean indicating whether the hotkey press should be suppressed. If `True`, the hotkey press will not be passed on to the operating system.
- `trigger_on_release`: An optional boolean indicating whether the `callback` function should be called when the hotkey is released rather than when it is pressed.

#### Returns
None

### `keyboard.remove_hotkey(hotkey)`

Removes a hotkey that was previously added with `add_hotkey`.

#### Parameters
- `hotkey`: The hotkey to remove. This should be the same string that was used to add the hotkey.

#### Returns
None

### `keyboard.write(text, delay=0.0)`

Simulates typing the `text` string.

#### Parameters
- `text`: The text to type.
- `delay`: An optional delay (in seconds) between each key press. The default value is 0.0.

#### Returns
None

### `keyboard.press_and_release(keys, delay=None, speed=None)`

Simulates pressing and releasing the specified `keys`.

#### Parameters
- `keys`: A string or list of strings representing the keys to press and release.
- `delay`: An optional delay (in seconds) between pressing and releasing each key. The default value is `None`, which means that the delay will be determined by the `speed` parameter.
- `speed`: An optional typing speed (in words per minute) to use when determining the delay between pressing and releasing each key. The default value is `None`, which means that the delay will be determined by the `delay` parameter.

#### Returns
None

### `keyboard.wait(hotkey=None, suppress=False)`

Blocks execution of the script until a hotkey is pressed.

#### Parameters
- `hotkey`: An optional hotkey to wait for. If specified, the function will only return when the hotkey is pressed.
- `suppress`: An optional boolean indicating whether the hotkey press should be suppressed. If `True`, the hotkey press will not be passed on to the operating system.

#### Returns
None

### `keyboard.send(event, scan_code=0, flags=0)`

Sends a keyboard event to the operating system.

#### Parameters
- `event`: The event to send. This should be a string representing the key to press or release.
``
