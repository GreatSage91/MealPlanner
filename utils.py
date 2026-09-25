import os
import logging

# Set up logging to file
LOG_FILE = os.path.join(os.path.dirname(__file__), 'app.log')
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_string(prompt, required=True):
    """Ask the user for a text input. Keeps asking if required and empty."""
    while True:
        val = input(prompt).strip()
        if not val and required:
            print("Error: This field is required.")
        else:
            return val

def prompt_list(prompt):
    """Ask user to enter items one by one. Blank line finishes input."""
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

def prompt_comma_separated_list(prompt):
    """Ask user for comma-separated items. Keeps asking until valid."""
    while True:
        val = input(f"{prompt} (comma-separated): ").strip()
        items = [i.strip() for i in val.split(',') if i.strip()] if val else []
        if items:
            return items
        print("Error: Please enter at least one item.")

def print_error(msg):
    print(f"[ERROR] {msg}")

def print_success(msg):
    print(f"[SUCCESS] {msg}")
