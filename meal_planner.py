import storage
import utils
from models import Recipe
import os

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def view_meal_plan():
    utils.clear_screen()
    print("=== 7-Day Meal Plan ===")
    plan = storage.load_meal_plan()
    for day in DAYS:
        meal = plan.get(day, "No meal planned")
        print(f"{day}: {meal}")
    print()

def create_meal_plan():
    utils.clear_screen()
    print("=== Create/Edit Meal Plan ===")
    recipes = storage.load_recipes()
    if not recipes:
        utils.print_error("No recipes available. Please add recipes first.")
        return

    print("Available Recipes:")
    for idx, r_data in enumerate(recipes, 1):
        print(f"{idx}. {r_data['name']}")
    print()

    plan = storage.load_meal_plan()
    for day in DAYS:
        current = plan.get(day, 'None')
        choice = utils.prompt_string(f"Select recipe number for {day} (leave blank to keep '{current}', 'c' to clear): ", required=False)
        if choice.lower() == 'c':
            plan[day] = ""
        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(recipes):
                plan[day] = recipes[idx-1]['name']
            else:
                utils.print_error("Invalid number, skipping...")
        # If blank, do nothing (keep existing)
        
    storage.save_meal_plan(plan)
    utils.print_success("Meal plan updated successfully!")

def generate_shopping_list():
    utils.clear_screen()
    print("=== Generate Shopping List ===")
    plan = storage.load_meal_plan()
    recipes_data = storage.load_recipes()
    
    # Build dictionary of recipes by name for easy lookup
    recipe_dict = {r['name']: Recipe.from_dict(r) for r in recipes_data}
    
    planned_recipe_names = {name for name in plan.values() if name}
    if not planned_recipe_names:
        utils.print_error("Meal plan is empty. Please create a meal plan first.")
        return

    all_ingredients = []
    for name in planned_recipe_names:
        if name in recipe_dict:
            all_ingredients.extend(recipe_dict[name].ingredients)
        else:
            print(f"[Warning] Recipe '{name}' from meal plan not found in database.")

    # Deduplicate and sort (case-insensitive deduplication)
    unique_ingredients = sorted({
        ing.strip().capitalize()
        for ing in all_ingredients
        if ing.strip()
    })

    if not unique_ingredients:
        utils.print_error("No ingredients found for the planned meals.")
        return

    print("Shopping List:")
    for ing in unique_ingredients:
        print(f"- {ing}")

    # Save to file
    output_file = os.path.join(storage.DATA_DIR, 'shopping_list.txt')
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=== Shopping List ===\n")
            for ing in unique_ingredients:
                f.write(f"- {ing}\n")
        utils.print_success(f"\nShopping list exported to {output_file}")
    except IOError as e:
        utils.print_error(f"Failed to export shopping list: {e}")
