import os
import logging

LOG_FILE = os.path.join(os.path.dirname(__file__), 'app.log')
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(msg: str):
    logging.info(msg)

def log_error(msg: str):
    logging.error(msg)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_string(prompt: str, required: bool = True) -> str:
    while True:
        val = input(prompt).strip()
        if not val and required:
            print("Error: This field is required.")
        else:
            return val

def prompt_list(prompt: str) -> list:
    print(f"{prompt} (enter a blank line to finish):")
    items = []
    while True:
        val = input("> ").strip()
        if not val:
            if not items:
                print("Error: List cannot be empty.")
                continue
            break
        items.append(val)
    return items

def prompt_comma_separated_list(prompt: str) -> list:
    while True:
        val = input(f"{prompt} (comma-separated): ").strip()
        if not val:
            print("Error: Please enter at least one item.")
            continue
        # Split by comma and strip whitespace
        items = [i.strip() for i in val.split(',') if i.strip()]
        if not items:
            print("Error: Please enter valid items.")
            continue
        return items

def print_error(msg: str):
    print(f"[ERROR] {msg}")

def print_success(msg: str):
    print(f"[SUCCESS] {msg}")
