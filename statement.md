# Project: CLI Recipe Manager & Meal Planner

## 1. Problem Statement
Many individuals struggle to organize their weekly meals and create accurate shopping lists without relying on overly complex, ad-heavy apps. The goal of this project is to build a lightweight, fast, terminal-based Recipe Manager and Meal Planner. It will allow users to store their favorite recipes, assign them to a 7-day meal plan, and automatically generate a clean, deduplicated shopping list.

## 2. Target Users
- Students living on a budget.
- Busy professionals who want quick terminal-based meal planning.
- Anyone looking for a simple offline tool without the clutter of web interfaces or accounts.

## 3. Minimum Viable Product (MVP) Features
- **Add Recipe**: Name, ingredients list, steps list, cuisine, prep time.
- **View & Search**: View all recipes or search by name/ingredient.
- **Suggestion Engine**: Intelligently suggest recipes based on a provided list of available ingredients.
- **Meal Planning**: Assign recipes to a Mon–Sun 7-day plan.
- **Shopping List**: Generate a combined, deduplicated shopping list to a text file.
- **Persistent Storage**: Save data using standard JSON files so nothing is lost upon exit.
- **Error Handling**: Graceful error management for invalid inputs or missing data.

## 4. Out of Scope (for MVP)
- Nutrition calculation (calories, macros).
- User accounts / logins.
- Images or GUI/Web interfaces.
- Recurring multi-week meal plans.

## 5. Non-Functional Requirements
| Requirement | Description |
|---|---|
| **Usability** | The terminal interface must have clear, numbered menus, easy-to-read prompts, and give feedback on success/failure. |
| **Reliability** | The program must handle invalid user inputs gracefully without throwing uncaught exceptions or crashing. |
| **Maintainability** | Code must be divided into modular files (models, storage, views) for easy updates and readable logic. |
| **Data Persistence** | All recipe and meal plan data must be persisted to the disk (JSON) immediately upon creation/modification. |
| **Resource Efficiency** | The application must remain lightweight and avoid using unnecessary third-party libraries; Python Standard Library is sufficient. |
