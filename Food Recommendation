# List of common Indian food dishes (can be customized)
common_foods = [
    'biryani', 'dosa', 'idli', 'samosa', 'pani puri', 'paneer', 'butter chicken', 'naan',
    'tandoori chicken', 'chole', 'poha', 'paratha', 'dal', 'jalebi', 'gulab jamun',
    'masala', 'chaat', 'kebab', 'pulao', 'uttapam', 'vada', 'ladoo'
]

def filter_food_items(review):
    words = review.split()
    foods = [word for word in words if word in common_foods]
    return ' '.join(foods)

df['FoodItems'] = df[review_column].apply(filter_food_items)
# Get positive reviews
positive_reviews = df[df['Liked'] == 1]['FoodItems']

# Count frequencies of food items
food_counter = Counter(common_foods)
for review in positive_reviews:
    food_counter.update(review.split())

# Print top 10 food dish recommendations
print("Top 10 food recommendations based on positive reviews:")
for dish, freq in food_counter.most_common(10):
    print(f"{dish}: {freq}")
