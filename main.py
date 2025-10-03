

# ------------Task 1 ----------
#Harsh Dev Jha  , Date- 3/10/25
#calorO - Is a calorie tracker app
# Create a simple calorie tracker app that allows users to log their meals and
# the corresponding calorie intake. The app should provide the following features:
# 1. Log a meal with its calorie count.
# 2. View the total calorie intake for the day.
# 3. Set a daily calorie goal and track progress towards that goal.
# 4. View a summary of meals logged for the day.
# 5. Option to reset the daily log.
print("Hello! This is A Calorie Tracker App \n" \
"and You can use this app to track your daily calorie intake and expenditure.\n" \
"Let's get started!")

#------- Task 2------

meal_list=[]
calorie_list=[]
meal_no=input("How many meals do you want to log today? (Enter a number or 'q' to quit): ")
if meal_no=='q':
    print("Thank you for using the Calorie Tracker App.")
    exit()
else: 
    for i in range(int(meal_no)):
        meal=input(str("Enter your meal (e.g., breakfast, lunch, dinner, snack): "))
        calories=int(input("Enter the number of calories consumed: "))  
        meal_list.append(meal)
        calorie_list.append(calories)


#------Task 3------
total_calories=sum(calorie_list)
avg_calories=total_calories/len(calorie_list)
print(f"\nTotal calorie intake for the day: {total_calories} calories")
print(f"Average calorie intake per meal: {avg_calories:.3f} calories")

# .3f in formatting is used to display the float deimals up to 3 places only

daily_goal=float(input("Set your daily calorie goal: "))

#------Task 4------
if total_calories<daily_goal:
    print(f"You are within your daily calorie goal of {daily_goal} calories.")
    print(f"You have {daily_goal - total_calories} calories remaining for the day.")
elif total_calories==daily_goal:
    print("You have met your daily calorie goal exactly!")
elif total_calories>daily_goal:
    print(f"You have exceeded your daily calorie goal by {total_calories - daily_goal} calories.")
else:
    print("Error in calculating calorie goal.")
print("\nSummary of meals logged for the day:")

# -------Task 5------
print("\n========== DAILY CALORIE REPORT ==========")
print("Meal Name\tCalories")
print("------------------------------------------")
for i in range(len(meal_list)):
    print(f"{meal_list[i]}\t\t{calorie_list[i]}")
print("------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{avg_calories:.3f}")
print("------------------------------------------")
