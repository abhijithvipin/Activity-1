from data_loader import load_data
from user_profile import UserProfile
from recommender import recommend_food

def main():
    # Load the dataset
    file_path = 'food_items.csv'
    food_data = load_data(file_path)
    
    if food_data is None:
        print("Failed to load food data. Exiting.")
        return
    
    # Get user input
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        activity_level = input("Enter your activity level (sedentary, moderate, active): ")
        diet_preference = input("Enter your diet preference (Vegan, Non-Vegan): ")
        goal = input("Enter your fitness goal (weight loss, maintenance, muscle gain): ")
        
        # Create user profile
        user_profile = UserProfile(name, age, weight, height, activity_level, diet_preference, goal)
        
        # Get recommendations
        recommended_foods = recommend_food(user_profile, food_data)
        
        if recommended_foods is not None:
            print("\nRecommended Foods for You:")
            print(recommended_foods)
        else:
            print("No suitable foods found.")
    except Exception as e:
        print(f"Error in user input: {e}")

if __name__ == "__main__":
    main()
