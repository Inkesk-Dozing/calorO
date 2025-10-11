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

The app generates beautifully formatted reports with:

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
<a href="https://github.com/Inkesk-Dozing/calorO/blob/main/calorie_report_20251011_181845.txt" target="_blank">
  <img src="https://img.shields.io/badge/View%20File-Calorie_Report-blue?logo=github" alt="Calorie Report Badge">
</a>

## Notes
To check details on App by flask and installation refer to :
[![App by Flask](https://img.shields.io/badge/App_by-Flask-blue?logo=flask)](https://github.com/Inkesk-Dozing/calorO/blob/main/App.md)
