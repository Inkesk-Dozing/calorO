# calorO - Calorie Tracker (Flask Web App)

A modern web-based calorie tracking application built with Flask.

## Features

- ✅ **Add Meals**: Log your meals with calorie counts
- ✅ **Daily Goal Tracking**: Set and monitor your daily calorie goal
- ✅ **Progress Visualization**: See your progress with a beautiful progress bar
- ✅ **Meal Management**: View, edit, and delete logged meals
- ✅ **Daily Statistics**: Track total calories, remaining calories, and average per meal
- ✅ **Neatly Formatted Tables**: Professional table layout with proper alignment
- ✅ **Report Export**: Download comprehensive session reports as text files
- ✅ **Reset Functionality**: Clear all meals to start fresh
- ✅ **Responsive Design**: Works on desktop and mobile devices

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000`

## Usage

1. **Set Your Daily Goal**: Enter your target daily calorie intake
2. **Add Meals**: Log each meal with its name and calorie count
3. **Track Progress**: Monitor your progress throughout the day
4. **Manage Meals**: Delete individual meals or reset everything
5. **View Statistics**: See totals, averages, and remaining calories
6. **Export Reports**: Download detailed session reports as text files

## Features Overview

- **Modern UI**: Clean, responsive design with Bootstrap 5
- **Real-time Updates**: See your progress update immediately
- **Session Storage**: Your data persists during your browsing session
- **Mobile Friendly**: Fully responsive design for all devices
- **Visual Progress**: Beautiful progress bar showing goal completion
- **Professional Tables**: Neatly formatted tables with proper alignment
- **Report Export**: Download comprehensive session reports with timestamps

## New Features (Task 5 & 6)

### 📊 Neatly Formatted Output
- **Professional Table Layout**: Clean, aligned tables with proper spacing
- **Right-aligned Numbers**: Calorie values are right-aligned for better readability
- **Consistent Formatting**: Uses f-strings and proper tab alignment throughout

### 📁 Report Export
- **One-Click Download**: Download comprehensive session reports instantly
- **Timestamped Files**: Automatic filename generation with date/time stamps
- **Complete Data**: Includes all meal details, totals, averages, and goal status
- **Professional Format**: Clean, readable text format perfect for sharing

### Sample Report Format
```
CALORIE TRACKER SESSION REPORT
========================================
Generated on: 2024-01-15 14:30:25

MEAL DETAILS:
Meal Name		Calories
--------------------------------
Breakfast		350
Lunch			600
Snack			150
--------------------------------
Total:			1100
Average:		366.67
--------------------------------

GOAL STATUS:
Daily Goal: 2000 calories
Status: Within goal - 900 calories remaining
```

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome 6
- **Data Storage**: Flask sessions (in-memory)
- **File Export**: Automatic text file generation with timestamps

## Original Command Line Version

The original command-line version is still available in `main.py` for reference.

