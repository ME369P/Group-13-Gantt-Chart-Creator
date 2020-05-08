# CBA-Gantt-Chart-Generator
  
Team 13: CBA to Program

Team Members:

Full Name: Charles Dineen

EID: cad3735

Full Name: Brandt Glidewell

EID: bbg439

Full Name: Alison Stutzmann

EID: acs4599

# Project: 
Python Gantt Chart Application

# Objective: 
Create a gantt chart application that is able to accept user input to plot a gantt chart, provide additional information on
the tasks, and export the chart to a usable format.

# Notes:
+ The CBA Gantt Chart Generator file is intended as the finished code that includes all capabilities intended for the scope of the project. 

+ The CBA Gantt Chart Further Capabilities file was created while exploring ways to expand the function of the chart generator via searching for and reading csv files from a directory as well as saving csv files back to a directory. It has been included in this repository for reference but is not operational as the "finished code".

+ The plotly code and proj_data files are included as a reference to compare the implementation of plotly versus matplotlib in creating a front-end Gantt chart. Overall, the implementation of a gantt chart is much simpler and requires less lines of code in plotly than matplotlib, and the chart created by plotly is generally more aesthetically pleasing. However, matplotlib allows for simpler integration with wxPython and the plotly code uploaded simply reads from a csv file for user input instead of allowing the user to edit the chart in real time.

# Additional Notes for CBA Gantt Chart Generator Code:

+ Chart x axis represents days of the month.

+ Program does not yet have capability to merge contributions under the same name on the pie chart. If you input the same name for 
separate tasks the pie chart will dispay the same name as if they were separate contributors.

+ Program still requires updates for robustness. It will return an error if incorrect data is input into the entry input boxes:

    - A task cost can be a float/int or N/A. Defaults to N/A if none provided

    - A task contributer can be a name(string) or N/A. Defaults to N/A if none provided

    - The task start date should be the day of the month that the project will be started. Requires an int or float input.

    - The task duration is how many days the project will take to complete. Requires an int or float input.

    - A color is required for the chart entry or it will return an error.

    - Selecting the cancel option on the entry windows will cause the program to crash.
