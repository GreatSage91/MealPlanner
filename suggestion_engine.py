"""
suggestion_engine.py
Intelligent recipe suggestion based on available ingredients.
"""

from typing import List, Dict, Any
from models import Recipe


def calculate_match(recipe_ingredients: List[str], available: List[str]) -> Dict[str, Any]:
    """
    Calculate match percentage between a recipe and available ingredients.
    Returns a dictionary with match details.
    """
    # Normalize to lowercase and strip spaces
    recipe_set = {ing.lower().strip() for ing in recipe_ingredients if ing.strip()}
    available_set = {ing.lower().strip() for ing in available if ing.strip()}

    if not recipe_set:
        return {
            "match_percent": 0.0,
            "matched": [],
            "missing": [],
            "matched_count": 0,
            "total_ingredients": 0
        }

    matched = recipe_set & available_set
    missing = recipe_set - available_set

    match_percent = (len(matched) / len(recipe_set)) * 100

    return {
        "match_percent": round(match_percent, 1),
        "matched": sorted(list(matched)),
        "missing": sorted(list(missing)),
        "matched_count": len(matched),
        "total_ingredients": len(recipe_set)
    }


def suggest_recipes(available_ingredients: List[str], recipes: List[Recipe], top_n: int = 8) -> List[Dict[str, Any]]:
    """
    Suggest best recipes based on available ingredients.
    
    Args:
        available_ingredients: List of ingredients the user has
        recipes: List of Recipe objects
        top_n: Number of top suggestions to return
    
    Returns:
        List of dictionaries containing recipe + match details, sorted by best match
    """
    if not available_ingredients:
        return []

    results = []

    for recipe in recipes:
        match_info = calculate_match(recipe.ingredients, available_ingredients)

        results.append({
            "recipe": recipe,
            "match_percent": match_info["match_percent"],
            "matched": match_info["matched"],
            "missing": match_info["missing"],
            "matched_count": match_info["matched_count"],
            "total_ingredients": match_info["total_ingredients"]
        })

    # Sort by match_percent (descending), then by fewer missing ingredients
    results.sort(key=lambda x: (-x["match_percent"], len(x["missing"])))

    return results[:top_n]


def display_suggestions(suggestions: List[Dict[str, Any]]) -> None:
    """
    Pretty print the suggestion results.
    """
    if not suggestions:
        print("\nNo matching recipes found. Try adding more ingredients.")
        return

    print("\n" + "="*60)
    print("           TOP RECIPE SUGGESTIONS FOR YOU")
    print("="*60)

    for idx, item in enumerate(suggestions, 1):
        recipe = item["recipe"]
        print(f"\n{idx}. {recipe.name}  ({recipe.cuisine})")
        print(f"   Match      : {item['match_percent']}% "
              f"({item['matched_count']}/{item['total_ingredients']} ingredients)")
        print(f"   Prep Time  : {recipe.prep_time} minutes")

        if item["matched"]:
            print(f"   You have   : {', '.join(item['matched'])}")
        if item["missing"]:
            print(f"   You need   : {', '.join(item['missing'])}")
        else:
            print("   You need   : None (You can cook this now!)")

    print("\n" + "="*60)
