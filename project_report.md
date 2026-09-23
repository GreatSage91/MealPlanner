# CLI Recipe Manager & Meal Planner: Project Report

## 1. Introduction
The **CLI Recipe Manager & Meal Planner** is a terminal-based application designed to help users efficiently manage their recipes, organize weekly meal plans, and generate consolidated shopping lists. Developed strictly with the Python Standard Library, this lightweight tool offers high performance, reliability, and persistent data storage via JSON without any external dependencies.

## 2. Requirements & MVP Scope
### Must-Have Features (MVP)
- **Recipe Management:** Add, view, search, and view detailed information for recipes.
- **Suggestion Engine:** Intelligently suggest recipes based on available ingredients, showing match percentages.
- **Meal Planning:** Assign recipes to a 7-day meal plan.
- **Shopping List Generation:** Combine and deduplicate ingredients based on the selected meal plan.
- **Persistent Data Storage:** Save state locally using JSON files.

### Non-Functional Requirements
1. **Usability:** A clear, numbered menu system guiding user interactions with feedback on success/failure.
2. **Reliability:** Comprehensive input validation to prevent crashes due to invalid input types or logic errors.
3. **Maintainability:** Modular architecture dividing responsibilities across various files (e.g., `models.py`, `storage.py`, `utils.py`).
4. **Data Persistence:** Automatic data syncing to disk upon state changes ensuring data isn't lost.
5. **Error Handling:** Graceful recovery during events like missing files or incorrectly formatted data.

## 3. Diagrams & Architecture

### 3.1 System Architecture Diagram
The system is divided into functional modules keeping concerns separated.

```mermaid
graph TD
    A[main.py] --> B(recipe_manager.py)
    A --> C(meal_planner.py)
    B --> D[models.py]
    C --> D
    B --> E[(storage.py)]
    C --> E
    B --> F[utils.py]
    C --> F
    B --> H[suggestion_engine.py]
    E -.-> G((JSON Files))
    E --> F
```

### 3.2 Use Case Diagram
User interactions with the core functionalities.

```mermaid
flowchart LR
    User([User])
    User --> A([Add Recipe])
    User --> B([View All Recipes])
    User --> C([Search Recipe])
    User --> F([Suggest Recipes])
    User --> D([Create Meal Plan])
    User --> E([Generate Shopping List])
```

### 3.3 Sequence Diagram
Sequence covering "Add Recipe" and "Generate Shopping List".

```mermaid
sequenceDiagram
    participant U as User
    participant M as main
    participant RM as recipe_manager
    participant MP as meal_planner
    participant S as storage
    
    U->>M: Select "Add Recipe"
    M->>RM: add_recipe()
    RM->>U: Prompt details (name, ingredients, etc.)
    U-->>RM: Enter details
    RM->>S: load_recipes()
    S-->>RM: List of Recipes
    RM->>S: save_recipes(new_list)
    RM-->>U: Success Message
    
    U->>M: Select "Generate Shopping List"
    M->>MP: generate_shopping_list()
    MP->>S: load_meal_plan()
    S-->>MP: Meal Plan Dict
    MP->>S: load_recipes()
    S-->>MP: List of Recipes
    MP->>MP: Deduplicate Ingredients
    MP->>S: Save to shopping_list.txt
    MP-->>U: Show Shopping List & Success
```

### 3.4 Workflow / Process Diagram
Flowchart detailing the overall logic.

```mermaid
flowchart TD
    Start([Start]) --> MainMenu{Main Menu}
    MainMenu -->|1. Add Recipe| AddR[Input Recipe Data]
    AddR --> SaveR[Save to JSON] --> MainMenu
    
    MainMenu -->|2. View Recipes| ViewR[Display All Recipes] --> MainMenu
    
    MainMenu -->|5. Create Plan| CreateP[Assign Recipes to Days]
    CreateP --> SaveP[Save Plan to JSON] --> MainMenu
    
    MainMenu -->|6. Suggest Recipes| Suggest[Match Ingredients]
    Suggest --> ShowSuggest[Display Matches] --> MainMenu
    
    MainMenu -->|8. Gen Shopping List| GenS[Extract & Deduplicate Ingredients]
    GenS --> PrintS[Print & Save to File] --> MainMenu
    
    MainMenu -->|9. Exit| Stop([Exit Program])
```

## 4. Technical Implementation details
- **Language:** Python 3.8+
- **Database/Storage:** Flat JSON files (`data/recipes.json`, `data/meal_plan.json`).
- **Data Classes:** Leveraging Python `dataclasses` for representing `Recipe` models elegantly.
- **Logging:** Implemented via standard `logging` library mapping outputs to `app.log`.

## 5. Conclusion
The CLI Recipe Manager successfully acts as a streamlined and resilient tool covering all requested MVP constraints without introducing unnecessary software bloat.
