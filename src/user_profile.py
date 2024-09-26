class UserProfile:
    """Stores user profile data for diet recommendations."""
    
    def _init_(self, name, age, weight, height, activity_level, diet_preference, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level  # sedentary, moderate, active
        self.diet_preference = diet_preference  # vegan, non-vegan
        self.goal = goal  # weight loss, maintenance, muscle gain

    def calculate_bmr(self):
        """Calculates Basal Metabolic Rate (BMR) based on user info."""
        try:
            if self.diet_preference == 'male':
                bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
            else:
                bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
            return bmr
        except Exception as e:
            print(f"Error calculating BMR: {e}")
            return 0

    def calculate_daily_calories(self):
        """Calculates daily calorie requirements based on BMR and activity level."""
        try:
            bmr = self.calculate_bmr()
            if self.activity_level == 'sedentary':
                return bmr * 1.2
            elif self.activity_level == 'moderate':
                return bmr * 1.55
            elif self.activity_level == 'active':
                return bmr * 1.725
            else:
                return bmr
        except Exception as e:
            print(f"Error calculating daily calories: {e}")
            return 0