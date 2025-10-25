# Advanced BMI Calculator
def bmi_calculator():
    print("="*40)
    print("💪 Welcome to the Advanced BMI Calculator 💪")
    print("="*40)

    while True:
        # Take User's name
        name = input("What's your name? ").strip().title()
        
        # Take user's weight
        weight_kg = float(input("What's your weight in Kg? "))
        
        # Take User's height in cm
        height_cm = float(input("What's your height in cm? "))
        
        # Convert height to meters
        height_m = height_cm / 100
        
        # Calculate BMI
        bmi = round(weight_kg / (height_m ** 2), 1)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            advice = "You should eat more nutritious food and possibly see a nutritionist."
        elif 18.5 <= bmi <= 24.9:
            category = "Normal Weight"
            advice = "Great job! Keep maintaining a balanced diet and regular exercise."
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
            advice = "Consider adopting a healthier diet and more physical activity."
        else:
            category = "Obese"
            advice = "You should consult a doctor or dietitian for a personalized plan."

        # Display results
        print("\n" + "-"*40)
        print(f"👤 Name: {name}")
        print(f"📏 BMI: {bmi}")
        print(f"🏷️ Category: {category}")
        print("-"*40)
        print(f"💡 Advice: {advice}")
        print("-"*40)

        # Show BMI reference
        print("\n📘 BMI Classification (WHO Standards):")
        print("Underweight: < 18.5")
        print("Normal weight: 18.5 – 24.9")
        print("Overweight: 25 – 29.9")
        print("Obesity: ≥ 30")

        # Ask if the user wants to continue
        try_again = input("\nWould you like to calculate again? (y/n): ").strip().lower()
        if try_again != 'y':
            print("\nThank you for using the BMI Calculator! Stay healthy 🌱")
            break


# Run the Program
bmi_calculator()
