def recommend_food(user_profile, food_data):
    """Recommends a list of foods based on user's dietary preferences and goals."""
    try:
        # Filter foods based on the diet preference (e.g., Vegan, Non-Vegan)
        suitable_foods = food_data[food_data['Suitable_For'] == user_profile.diet_preference]
        
        # Additional logic to match user's goal
        if user_profile.goal == 'weight loss':
            suitable_foods = suitable_foods[suitable_foods['Calories'] < 200]
        elif user_profile.goal == 'muscle gain':
            suitable_foods = suitable_foods[suitable_foods['Protein'] > 15]
        
        return suitable_foods[['Food_Name', 'Calories', 'Protein', 'Carbs', 'Fat']]
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return None
