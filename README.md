# calorO
> <p align="center">The Echo Is Never Silent,<br>
> Genesis Hums With Memory.</p>

<p align="center">
Created by Inkesk<br>
Powered by OSKA<br>
Under ØSKA<br></p>
<div align="center"><strong>.</strong></div>
<br>

Calorie Tracker CLI with UI

<h1 align="center" style="color: #e3833a;">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fantasque+Sans+Mono&weight=700&size=33&pause=1000&color=0e75b6&center=true&width=702&lines=🥗+calarO+-+Calorie+Tracker+App+%F0%9F%91%8D&color=6F42C1	)](https://git.io/typing-svg)

 <!-- 🥗 calorO - Calorie Tracker App-->


</h1>


 [🌐 **Live Demo**](https://caloro.onrender.com) - Deployment
---

## 🚀 Introduction

**calorO** is a simple, interactive calorie tracker app designed to help users log their meals and calorie intake throughout the day. Track your daily progress, set goals, and receive instant feedback on your dietary habits—all from an easy-to-use Python interface!

---

## 🎯 Features

- Log meals with corresponding calorie counts.
- View total calorie intake for the day.
- Set and monitor progress towards a daily calorie goal.
- Get a detailed summary of all meals logged each day.
- **Neatly formatted output** with proper table alignment and f-strings.
- **Save session reports** to timestamped text files.
- Reset your daily log with ease.

---

## 🏗️ How It Works

> Begin your calorie tracking journey with an inviting welcome message to guide you step-by-step!
- Input the number of meals you want to log.
- For each meal, specify its name and calorie count.
- After logging, see total and average calories consumed.
- Set a daily calorie goal—get notified if you're under, on, or over your target.
- View a **neatly formatted table** with proper alignment showing all your meals and statistics.
- **Save your session** to a timestamped text file for future reference.

---

## 📊 Reporting

The app generates formatted reports with:

### Console Output

<h2>Sample</h2>

```
========== DAILY CALORIE REPORT ==========
Meal Name		Calories
--------------------------------
Breakfast		350
Lunch			600
Snack			150
--------------------------------
Total:			1100
Average:		366.67
--------------------------------
```

<h2>Output from the Project Code (maine.py)</h2>
<img width="1191" height="836" alt="Screenshot 2025-10-11 181908" src="https://github.com/user-attachments/assets/f0cf9bac-4866-4a20-b21f-0c043817f112" />

### File Export
- **Automatic timestamping**: Files named `calorie_report_YYYYMMDD_HHMMSS.txt`
- **Comprehensive data**: Includes timestamp, meal details, totals, averages, and goal status
- **Professional formatting**: Clean, readable text format for easy sharing

### Sample Report File
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
Click for Sample txt Report file on Creation
<a href="https://github.com/Inkesk-Dozing/calorO/blob/main/.docs/calorie_report_20251011_181845.txt" target="_blank">
  <img src="https://img.shields.io/badge/View%20File-Calorie_Report-blue?logo=github" alt="Calorie Report Badge">
</a>


# 📱For Flask Built App

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
- **Visual Progress**: Progress bar showing goal completion
- **Professional Tables**: Neatly formatted tables with proper alignment
- **Report Export**: Download comprehensive session reports with timestamps

## New Features 

### 📁 Report Export
- **One-Click Download**: Download comprehensive session reports instantly
- **Timestamped Files**: Automatic filename generation with date/time stamps
- **Complete Data**: Includes all meal details, totals, averages, and goal status
- **Professional Format**: Clean, readable text format perfect for sharing


## 🧠 CRISP-DM Framework

**Business Understanding**  
Calorie tracking helps users make informed dietary choices. This app simplifies that process by allowing users to log food items and view calorie summaries.

**Data Understanding**  
User inputs include food name and quantity. These are mapped to calorie values using internal logic or external databases, and also are
added to a report file for future reference if needed.

**Data Preparation**  
Inputs are cleaned (e.g., lowercased, stripped), validated, and stored in structured format (CSV or JSON).

**Modeling**  
No ML model yet, but logic could be extended to suggest healthier alternatives or predict intake trends.
Considering in Future implementations.

**Evaluation**  
Success is measured by accuracy of calorie estimates and ease of use. Future metrics may include user retention or feedback, if scaled as such.

**Deployment**  
Live on Render: [https://caloro.onrender.com](https://caloro.onrender.com)


## General Importance

### Future Implementations
-**Importing Data**: Import Prev log file to add data in it.
-**Styling UI**: UI could be made more attractive and user friendly for longer run.
-**Model**: Add and ML model for data referring and analyzing.


### Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome 6
- **Data Storage**: Flask sessions (in-memory)
- **File Export**: Automatic text file generation with timestamps

## Original Command Line Version

The original command-line version is still available in `main.py` for Assignment reference purposes.

##Disclaimer
This is Extra to what was assigned but the assigned task can still be refered to at 'main.py.'
