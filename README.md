# CBA-Gantt-Chart-Generator
  
Team 13: CBA to Program

Team Members:

Full Name: Charles Dineen

EID: cad3735

Full Name: Brandt Glidewell

EID: bbg439

Full Name: Alison Stutzmann

EID: acs4599

Project: Python Gantt Chart Application

Objective: Create a gantt chart application that is able to accept user input to plot a gantt chart, provide additinal information on
the tasks, and export the chart to a usable format

Notes:
Chart x axis represents days of the month.

Program does not yet have capability to merge contributions under the same name on the pie chart. If you input the same name for 
separate tasks the pie chart will dispay the same name as if they were separate contributors.

Program still requires updates for robustness. It will crash if you input incorrect data into the entry input boxes:

A task cost can be a float/int or N/A. Defaults to N/A if none provided

A task contributer can be a name or N/A. Defaults to N/A if none provided

The task start date should be the day of the month that the project will be started. Requires and int or float or it will crash.

The task duration is how many days the project will take to complete. Requires and int or float or it will crash.

A color is required for the chart entry or it will crash.

Selecting the cancel option on the entry windows will cause the program to crash.
