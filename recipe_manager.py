from models import Recipe
import storage
import utils

def add_recipe():
    utils.clear_screen()
    print("=== Add New Recipe ===")
    name = utils.prompt_string("Recipe Name: ")
    cuisine = utils.prompt_string("Cuisine (e.g., Italian, Mexican): ")
    prep_time = utils.prompt_string("Prep Time (e.g., 30 mins): ")
    
    ingredients = utils.prompt_list("Enter Ingredients")
    steps = utils.prompt_list("Enter Steps")
    
    recipe = Recipe(name, ingredients, steps, cuisine, prep_time)
    recipes = storage.load_recipes()
    recipes.append(recipe.to_dict())
    storage.save_recipes(recipes)
    
    utils.print_success(f"Recipe '{name}' added successfully!")

def list_recipes():
    utils.clear_screen()
    print("=== All Recipes ===")
    recipes = storage.load_recipes()
    if not recipes:
        print("No recipes found.")
        return
    
    for idx, r_data in enumerate(recipes, 1):
        r = Recipe.from_dict(r_data)
        print(f"{idx}. {r.name} ({r.cuisine}) - {r.prep_time}")

def search_recipes():
    utils.clear_screen()
    print("=== Search Recipes ===")
    query = utils.prompt_string("Search by name or ingredient: ").lower()
    
    recipes = storage.load_recipes()
    results = []
    for r_data in recipes:
        r = Recipe.from_dict(r_data)
        # Check name
        if query in r.name.lower():
            results.append(r)
            continue
        # Check ingredients
        for ing in r.ingredients:
            if query in ing.lower():
                results.append(r)
                break
                
    if not results:
        print("No matching recipes found.")
        return
        
    print(f"\nFound {len(results)} matching recipe(s):")
    for idx, r in enumerate(results, 1):
        print(f"{idx}. {r.name} ({r.cuisine}) - {r.prep_time}")

def view_full_recipe():
    list_recipes()
    recipes = storage.load_recipes()
    if not recipes:
        return
        
    try:
        choice = int(utils.prompt_string("\nEnter recipe number to view (or 0 to cancel): ", required=False) or 0)
        if choice == 0:
            return
        if 1 <= choice <= len(recipes):
            r = Recipe.from_dict(recipes[choice - 1])
            utils.clear_screen()
            print(f"=== {r.name} ===")
            print(f"Cuisine: {r.cuisine} | Prep Time: {r.prep_time}")
            print("\nIngredients:")
            for ing in r.ingredients:
                print(f"  - {ing}")
            print("\nSteps:")
            for i, step in enumerate(r.steps, 1):
                print(f"  {i}. {step}")
            print()
        else:
            utils.print_error("Invalid recipe number.")
    except ValueError:
        utils.print_error("Please enter a valid number.")

def suggest_recipes_from_ingredients():
    import suggestion_engine
    utils.clear_screen()
    print("=== Suggest Recipes from Available Ingredients ===")
    
    ingredients = utils.prompt_comma_separated_list("Enter available ingredients")
    recipes_data = storage.load_recipes()
    
    if not recipes_data:
        utils.print_error("No recipes in database.")
        return
        
    all_recipes = [Recipe.from_dict(r) for r in recipes_data]
    suggestions = suggestion_engine.suggest_recipes(ingredients, all_recipes)
    
    suggestion_engine.display_suggestions(suggestions)
    
    try:
        choice = int(utils.prompt_string("\nEnter recipe number to view full details (or 0 to cancel): ", required=False) or 0)
        if choice == 0:
            return
        if 1 <= choice <= len(suggestions):
            r = suggestions[choice - 1]['recipe']
            utils.clear_screen()
            print(f"=== {r.name} ===")
            print(f"Cuisine: {r.cuisine} | Prep Time: {r.prep_time} minutes")
            if r.difficulty:
                print(f"Difficulty: {r.difficulty}")
            if r.servings:
                print(f"Servings: {r.servings}")
            print("\nIngredients:")
            for ing in r.ingredients:
                print(f"  - {ing}")
            print("\nSteps:")
            for i, step in enumerate(r.steps, 1):
                print(f"  {i}. {step}")
            print()
        else:
            utils.print_error("Invalid recipe number.")
    except ValueError:
        utils.print_error("Please enter a valid number.")
