import json
import os
import utils

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
RECIPES_FILE = os.path.join(DATA_DIR, 'recipes.json')
INGREDIENTS_FILE = os.path.join(DATA_DIR, 'ingredients.json')
MEAL_PLAN_FILE = os.path.join(DATA_DIR, 'meal_plan.json')

def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_recipes() -> list:
    _ensure_data_dir()
    if not os.path.exists(RECIPES_FILE):
        return []
    try:
        with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        utils.log_error(f"Failed to load recipes: {e}")
        return []

def save_recipes(recipes: list):
    _ensure_data_dir()
    with open(RECIPES_FILE, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, indent=4)
    utils.log_info(f"Saved {len(recipes)} recipes to {RECIPES_FILE}")

def load_ingredients() -> list:
    _ensure_data_dir()
    if not os.path.exists(INGREDIENTS_FILE):
        return []
    try:
        with open(INGREDIENTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        utils.log_error(f"Failed to load ingredients: {e}")
        return []

def load_meal_plan() -> dict:
    _ensure_data_dir()
    if not os.path.exists(MEAL_PLAN_FILE):
        return {}
    try:
        with open(MEAL_PLAN_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        utils.log_error(f"Failed to load meal plan: {e}")
        return {}

def save_meal_plan(meal_plan: dict):
    _ensure_data_dir()
    with open(MEAL_PLAN_FILE, 'w', encoding='utf-8') as f:
        json.dump(meal_plan, f, indent=4)
    utils.log_info(f"Saved meal plan to {MEAL_PLAN_FILE}")
