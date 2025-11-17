# researcher.py: gets recipe data for each query
def research(searches, google_search):
    results = []
    for query in searches:
        recipe_data = google_search(query)  # This simulates a Google search
        results.append(recipe_data)         # Expect recipe_data: {title, url, ingredients}
    return results
