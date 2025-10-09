import re

# Load movie list
pattern = r"\[(.*?)\]"
with open("README.md", "r") as f:
    content = f.read()

all_movies = re.findall(pattern, content)

# Normalize function to make search robust
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())  # lowercase, remove non-alphanumerics

# Build a normalized movie lookup
normalized_movies = {normalize(m): m for m in all_movies}

# Search function
def search_movie(query):
    query_norm = normalize(query)
    results = [title for norm, title in normalized_movies.items() if query_norm in norm]
    return results

# Example usage
user_input = "nun"
found_movies = search_movie(user_input)

print("Movies found:")
for movie in found_movies:
    print(movie)
