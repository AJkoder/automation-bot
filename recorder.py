import json
import time
from pynput import mouse, keyboard

actions = []
start_time = time.time()

def on_click(x, y, button, pressed):
    if pressed:
        actions.append({
            'type': 'click',
            'x': x,
            'y': y,
            'time': time.time() - start_time
        })
        print(f"Recorded click at ({x}, {y})")

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            # Stop listener
            print("ESC pressed, stopping recording...")
            return False  # This stops the listener and exits .join()
        actions.append({
            'type': 'key',
            'key': key.char,
            'time': time.time() - start_time
        })
        print(f"Recorded key press: {key.char}")
    except AttributeError:
        actions.append({
            'type': 'key',
            'key': str(key),
            'time': time.time() - start_time
        })
        print(f"Recorded special key press: {key}")

with mouse.Listener(on_click=on_click) as mouse_listener, \
     keyboard.Listener(on_press=on_press) as keyboard_listener:

    print("🎥 Recording... Press ESC to stop.")
    keyboard_listener.join()  # Waits here until on_press returns False (ESC)

# After listener stops, save actions:
if actions:
    with open("actions.json", "w") as f:
        json.dump(actions, f, indent=4)
    print(f"✅ Saved {len(actions)} actions to actions.json")
else:
    print("⚠️ No actions recorded!")
