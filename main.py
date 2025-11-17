from agents.planner import plan_recipes
from agents.researcher import research
from agents.formatter import format_ingredients

def google_search(query):
    # This just returns example data; in real use, connect Google Search API
    return {"title": query, "url": "example.com", "ingredients": ["chicken breast", "carrot"]}

def main():
    prompt = "Plan 3 dinners for a week for two people, focusing on chicken and vegetables."
    searches = plan_recipes(prompt)
    recipe_results = research(searches, google_search)
    shopping_list = format_ingredients(recipe_results)
    print(shopping_list)

if __name__ == '__main__':
    main()
