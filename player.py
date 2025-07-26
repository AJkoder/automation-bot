import json
import pyautogui
import time
import keyboard as kb

with open("actions.json", "r") as f:
    actions = json.load(f)

print("▶️ Playback starting in 3 seconds... (Press ESC to stop)")
time.sleep(3)

start_time = time.time()

try:
    for action in actions:
        while time.time() - start_time < action['time']:
            time.sleep(0.01)

        if action['type'] == 'click':
            pyautogui.click(action['x'], action['y'])

        elif action['type'] == 'key':
            key = action['key']
            if 'Key.' in key:
                pyautogui.press(key.replace('Key.', ''))
            else:
                pyautogui.typewrite(key)

        if kb.is_pressed('esc'):
            print("⛔ Playback stopped by user.")
            break

    print("✅ Playback completed.")

except KeyboardInterrupt:
    print("⛔ Stopped manually.")
