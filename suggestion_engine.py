"""
suggestion_engine.py - Suggest recipes based on available ingredients.
"""

def calculate_match(recipe_ingredients, available):
    """Calculate how well a recipe matches the user's available ingredients."""
    recipe_set = {i.lower().strip() for i in recipe_ingredients if i.strip()}
    available_set = {i.lower().strip() for i in available if i.strip()}
    if not recipe_set:
        return {"match_percent": 0.0, "matched": [], "missing": [],
                "matched_count": 0, "total_ingredients": 0}
    matched = recipe_set & available_set
    missing = recipe_set - available_set
    percent = round((len(matched) / len(recipe_set)) * 100, 1)
    return {"match_percent": percent, "matched": sorted(matched),
            "missing": sorted(missing), "matched_count": len(matched),
            "total_ingredients": len(recipe_set)}

def suggest_recipes(available_ingredients, recipes, top_n=8):
    """Return top_n recipes sorted by best ingredient match."""
    if not available_ingredients:
        return []
    results = []
    for r in recipes:
        info = calculate_match(r['ingredients'], available_ingredients)
        info['recipe'] = r
        results.append(info)
    results.sort(key=lambda x: (-x["match_percent"], len(x["missing"])))
    return results[:top_n]

def display_suggestions(suggestions):
    """Pretty-print the suggestion results."""
    if not suggestions:
        print("\nNo matching recipes found. Try adding more ingredients.")
        return
    print("\n" + "=" * 60)
    print("           TOP RECIPE SUGGESTIONS FOR YOU")
    print("=" * 60)
    for idx, item in enumerate(suggestions, 1):
        r = item['recipe']
        print(f"\n{idx}. {r['name']}  ({r['cuisine']})")
        print(f"   Match      : {item['match_percent']}% "
              f"({item['matched_count']}/{item['total_ingredients']} ingredients)")
        print(f"   Prep Time  : {r['prep_time']}")
        if item["matched"]:
            print(f"   You have   : {', '.join(item['matched'])}")
        if item["missing"]:
            print(f"   You need   : {', '.join(item['missing'])}")
        else:
            print("   You need   : None (You can cook this now!)")
    print("\n" + "=" * 60)
