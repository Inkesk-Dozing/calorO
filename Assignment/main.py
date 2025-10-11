

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
        calories=float(input("Enter the number of calories consumed: "))  
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

def spaces(word, tab):
    """Calculate proper spacing for table alignment"""
    l = len(word)
    t = "\t"
    n = tab - l//8  # total tabs - tabs occupied by current word
    return t*n

print("\n====== DAILY CALORIE REPORT ======")
print("Meal Name\t\tCalories")
print("--------------------------------")
for i in range(len(meal_list)):
    print(f"{meal_list[i]}{spaces(meal_list[i], 3)}{calorie_list[i]:.2f}")
print("--------------------------------")
print(f"Total:{spaces('Total:', 3)}{total_calories:.2f}")
print(f"Average:{spaces('Average:', 3)}{avg_calories:.2f}")
print("--------------------------------")

# -------Task 6------
# Bonus Task

save_choice = input("\nDo you want to save this report to a file? (y/n): ").lower().strip()
if save_choice == 'y' or save_choice == 'yes':
    from datetime import datetime
    
    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"calorie_report_{timestamp}.txt"
    
    # Determine goal status
    if total_calories < daily_goal:
        goal_stat = f"Within goal - {daily_goal - total_calories} calories remaining"
    elif total_calories == daily_goal:
        goal_stat = "Met goal exactly"
    else:
        goal_stat = f"Exceeded goal by {total_calories - daily_goal} calories"
    
    # Write to file
    with open(filename, "w") as file:
        file.write("CALORIE TRACKER SESSION REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        file.write("MEAL DETAILS:\n")
        file.write("Meal Name\t\tCalories\n")
        file.write("-" * 32 + "\n")
        for i in range(len(meal_list)):
            file.write(f"{meal_list[i]}{spaces(meal_list[i], 3)}{calorie_list[i]:.2f}\n")
        file.write("-" * 32 + "\n")
        file.write(f"Total:{spaces('Total:', 3)}{total_calories:.2f}\n")
        file.write(f"Average:{spaces('Average:', 3)}{avg_calories:.2f}\n")
        file.write("-" * 32 + "\n\n")
        
        file.write("GOAL STATUS:\n")
        file.write(f"Daily Goal: {daily_goal} calories\n")
        file.write(f"Status: {goal_stat}\n")
    
    print(f"Report saved successfully to: {filename}")
else:
    print("Report not saved.")
