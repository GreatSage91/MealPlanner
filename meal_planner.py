import os
import storage
import utils

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def view_meal_plan():
    utils.clear_screen()
    print("=== 7-Day Meal Plan ===")
    plan = storage.load_meal_plan()
    for day in DAYS:
        print(f"{day}: {plan.get(day, 'No meal planned')}")
    print()

def create_meal_plan():
    utils.clear_screen()
    print("=== Create/Edit Meal Plan ===")
    recipes = storage.load_recipes()
    if not recipes:
        utils.print_error("No recipes available. Please add recipes first.")
        return
    print("Available Recipes:")
    for idx, r in enumerate(recipes, 1):
        print(f"{idx}. {r['name']}")
    print()
    plan = storage.load_meal_plan()
    for day in DAYS:
        current = plan.get(day, 'None')
        choice = utils.prompt_string(
            f"Select recipe # for {day} (blank=keep '{current}', c=clear): ",
            required=False)
        if choice.lower() == 'c':
            plan[day] = ""
        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(recipes):
                plan[day] = recipes[idx - 1]['name']
            else:
                utils.print_error("Invalid number, skipping...")
    storage.save_meal_plan(plan)
    utils.print_success("Meal plan updated successfully!")

def generate_shopping_list():
    utils.clear_screen()
    print("=== Generate Shopping List ===")
    plan = storage.load_meal_plan()
    recipes = storage.load_recipes()
    # Build name -> recipe lookup
    recipe_dict = {r['name']: r for r in recipes}
    planned_names = {name for name in plan.values() if name}
    if not planned_names:
        utils.print_error("Meal plan is empty. Please create a meal plan first.")
        return
    all_ingredients = []
    for name in planned_names:
        if name in recipe_dict:
            all_ingredients.extend(recipe_dict[name]['ingredients'])
        else:
            print(f"[Warning] Recipe '{name}' not found in database.")
    # Deduplicate and sort (case-insensitive)
    unique = sorted({ing.strip().capitalize() for ing in all_ingredients if ing.strip()})
    if not unique:
        utils.print_error("No ingredients found for the planned meals.")
        return
    print("Shopping List:")
    for ing in unique:
        print(f"- {ing}")
    # Save to file
    output_file = os.path.join(storage.DATA_DIR, 'shopping_list.txt')
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=== Shopping List ===\n")
            for ing in unique:
                f.write(f"- {ing}\n")
        utils.print_success(f"\nShopping list exported to {output_file}")
    except IOError as e:
        utils.print_error(f"Failed to export shopping list: {e}")
