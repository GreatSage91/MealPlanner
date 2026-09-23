import utils
import recipe_manager
import meal_planner
import sys

def display_menu():
    print("=== CLI Recipe Manager & Meal Planner ===")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Search Recipes")
    print("4. View Full Recipe Details")
    print("5. Create / Edit Meal Plan")
    print("6. Suggest Recipes from Available Ingredients")
    print("7. View Meal Plan")
    print("8. Generate Shopping List")
    print("9. Exit")

def main():
    while True:
        utils.clear_screen()
        display_menu()
        choice = utils.prompt_string("\nSelect an option (1-9): ")
        
        if choice == '1':
            recipe_manager.add_recipe()
        elif choice == '2':
            recipe_manager.list_recipes()
        elif choice == '3':
            recipe_manager.search_recipes()
        elif choice == '4':
            recipe_manager.view_full_recipe()
        elif choice == '5':
            meal_planner.create_meal_plan()
        elif choice == '6':
            recipe_manager.suggest_recipes_from_ingredients()
        elif choice == '7':
            meal_planner.view_meal_plan()
        elif choice == '8':
            meal_planner.generate_shopping_list()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            sys.exit(0)
        else:
            utils.print_error("Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()