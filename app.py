from flask import Flask, render_template, request, redirect, url_for, session

"""
Simple Flask app (assignment-style) for a calorie tracker.
Features:
- Add meals with calories
- Set a daily calorie goal
- View totals and reset the daily log

Note: Data is stored in the Flask session (per browser session).
"""

app = Flask(__name__)
app.secret_key = 'dev-secret-key'

# Initialize session data if not exists
def init_session():
    """Ensure default session keys exist."""
    if 'meals' not in session:
        session['meals'] = []
    if 'daily_goal' not in session:
        session['daily_goal'] = 2000

@app.route('/')
def index():
    init_session()
    meals = session.get('meals', [])
    daily_goal = session.get('daily_goal', 2000)
    # Basic calculations for display
    total_calories = sum(meal['calories'] for meal in meals)
    avg_calories = total_calories / len(meals) if meals else 0
    remaining_calories = daily_goal - total_calories

    return render_template(
        'index.html',
        meals=meals,
        total_calories=total_calories,
        avg_calories=avg_calories,
        daily_goal=daily_goal,
        remaining_calories=remaining_calories,
    )

@app.route('/add_meal', methods=['POST'])
def add_meal():
    meal_name = request.form.get('meal_name', '').strip()
    calories = request.form.get('calories', '').strip()

    # Parse and validate inputs simply
    try:
        calories = int(calories)
    except ValueError:
        return redirect(url_for('index'))

    if not meal_name or calories < 0:
        return redirect(url_for('index'))

    init_session()
    meals = session.get('meals', [])
    meals.append({'name': meal_name, 'calories': calories})
    session['meals'] = meals

    return redirect(url_for('index'))

@app.route('/set_goal', methods=['POST'])
def set_goal():
    goal = request.form.get('daily_goal', '').strip()

    # Parse and validate goal simply
    try:
        goal = int(goal)
    except ValueError:
        return redirect(url_for('index'))

    if goal > 0:
        session['daily_goal'] = goal
    return redirect(url_for('index'))

@app.route('/delete_meal/<int:index>')
def delete_meal(index):
    init_session()
    meals = session.get('meals', [])
    if 0 <= index < len(meals):
        meals.pop(index)
        session['meals'] = meals
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['meals'] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
