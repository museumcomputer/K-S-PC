import keyboard
import time

def simulate_key_press():
    print("Enter the key or combination of keys you want to simulate (e.g., 'a', 'ctrl+c', 'shift+alt+f'): ")
    user_input = input("Input: ").strip()

    try:
        print(f"Simulating key press for: {user_input}")
        
        keyboard.press_and_release(user_input)
        print(f"Key(s) '{user_input}' pressed successfully.")
    except Exception as e:
        print(f"Error: Unable to simulate key press. Details: {e}")

if __name__ == "__main__":
    while True:
        simulate_key_press()
        time.sleep(1)