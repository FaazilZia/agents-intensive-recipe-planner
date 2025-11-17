# formatter.py: organizes a raw ingredient list
def format_ingredients(recipe_results, gemini_model=None):
    # For demo, use this dummy list
    raw_ingredients = ["chicken breast", "carrot", "onion", "rice", "milk", "egg"]
    categories = {
        "Produce": ["carrot", "onion"],
        "Dairy": ["milk"],
        "Pantry": ["rice"],
        "Meat": ["chicken breast"],
        "Eggs": ["egg"]
    }
    markdown = "# Shopping List\n"
    for category, items in categories.items():
        markdown += f"## {category}\n"
        for item in items:
            markdown += f"- {item}\n"
    return markdown
