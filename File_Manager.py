import re

# Load movie list
pattern = r"\[(.*?)\]"
with open("Entertainment.md", "r+") as f:
    content = f.read()

all_movies = re.findall(pattern, content)

# Normalize function to make search robust
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())  # lowercase, remove non-alphanumerics

# Build a normalized movie lookup
key_value_pair = {normalize(m): m for m in all_movies}

# Search function
def search_movie(query):
    query_norm = normalize(query)
    results = [title for norm, title in key_value_pair.items() if query_norm in norm]
    print(results)
    return results

# Example usage
user_input = input("Enter movie/tv show name: ").lower().strip()
found_movies = search_movie(user_input)

if not found_movies:
    print("Not found!")
else:
    for movie in found_movies:
        print(movie)
