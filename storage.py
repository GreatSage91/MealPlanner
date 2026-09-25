import json
import os
import utils

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
RECIPES_FILE = os.path.join(DATA_DIR, 'recipes.json')
INGREDIENTS_FILE = os.path.join(DATA_DIR, 'ingredients.json')
MEAL_PLAN_FILE = os.path.join(DATA_DIR, 'meal_plan.json')

def _load_json(path, default):
    """Load JSON from a file. Returns default if file missing or corrupt."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        return default
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        utils.log_error(f"Failed to load {path}: {e}")
        return default

def _save_json(path, data, message):
    """Save data as JSON to a file and log the action."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    utils.log_info(message)

def load_recipes():
    return _load_json(RECIPES_FILE, [])

def save_recipes(recipes):
    _save_json(RECIPES_FILE, recipes, f"Saved {len(recipes)} recipes")

def load_ingredients():
    return _load_json(INGREDIENTS_FILE, [])

def load_meal_plan():
    return _load_json(MEAL_PLAN_FILE, {})

def save_meal_plan(plan):
    _save_json(MEAL_PLAN_FILE, plan, "Saved meal plan")
