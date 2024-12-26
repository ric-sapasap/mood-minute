import keyboard


def on_key_event(event):
    print(event)


print("Press any key (Ctrl+C to exit)...")
# Listen for key press events
keyboard.hook(on_key_event)

# Keep the program running
keyboard.wait("esc")
