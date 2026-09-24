import json
import os
import utils

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
RECIPES_FILE = os.path.join(DATA_DIR, 'recipes.json')
INGREDIENTS_FILE = os.path.join(DATA_DIR, 'ingredients.json')
MEAL_PLAN_FILE = os.path.join(DATA_DIR, 'meal_plan.json')

def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def _load_json(path: str, default):
    _ensure_data_dir()
    if not os.path.exists(path):
        return default
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        utils.log_error(f"Failed to load {path}: {error}")
        return default

def _save_json(path: str, data, message: str):
    _ensure_data_dir()
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    utils.log_info(message)

def load_recipes() -> list:
    return _load_json(RECIPES_FILE, [])

def save_recipes(recipes: list):
    _save_json(RECIPES_FILE, recipes, f"Saved {len(recipes)} recipes to {RECIPES_FILE}")

def load_ingredients() -> list:
    return _load_json(INGREDIENTS_FILE, [])

def load_meal_plan() -> dict:
    return _load_json(MEAL_PLAN_FILE, {})

def save_meal_plan(meal_plan: dict):
    _save_json(MEAL_PLAN_FILE, meal_plan, f"Saved meal plan to {MEAL_PLAN_FILE}")
