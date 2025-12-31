# sales_lead_tracker
Simple CRM tool for tracking sales leads and pipeline value
# Sales Lead Tracker (Python) 🧑‍💼

A simple but powerful command-line CRM tool for tracking sales leads, updating status, and calculating pipeline value.

Perfect for sales professionals or small teams — add leads, update progress, and see total potential revenue at a glance.

## Features
- View all leads in clean table format
- Add new leads with name, company, email, and deal value
- Update lead status (New → Contacted → Proposal → Won/Lost)
- Automatic pipeline calculation (sum of open deals)
- Won revenue and conversion rate stats
- Easy to extend (add dates, notes, export to CSV later)

## Demo Example
🧑‍💼 SALES LEAD TRACKER - Welcome to the bag 🧑‍💼
Options:

View all leads
Add new lead
Update lead status
View pipeline summary
Quit

Choose (1-5): 4
================================================================================
SALES LEAD TRACKER
Name            Company              Email                     Status       Value ($)
John Smith      Acme Corp            john@acme.com             New             50000
Sarah Lee       TechStart            sarah@techstart.com       Contacted       75000
Mike Chen       Global Inc           mike@global.com           Proposal       100000
Emma Wilson     StartupX             emma@startupx.com         Won             30000
David Brown     Enterprise Co        david@enterprise.com      Lost            60000
Total Pipeline Value: $225,000
Won Revenue: $30,000
Conversion Rate: 20.0%
text## How to Run
1. Save as `sales_lead_tracker.py`
2. Run `python sales_lead_tracker.py`
3. Use the menu to manage leads

## Built With
- Python 3
- Lists (2D structure for data storage)
- Loops, functions, conditionals
- String formatting for clean output

Completed during self-taught Python journey (Codecademy Learn Python 3 – December 2025).  
Inspired by real sales/CRM experience — built to solve actual business problems.

Fork it and add:
- CSV import/export
- Sorting/filtering
- GUI version
Author: Travis Willis | Sydney, Australia | Former sales professional 
