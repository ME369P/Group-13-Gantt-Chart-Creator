import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
      
class TopPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.SetBackgroundColour("white")
        self.TaskNames = []
        self.TaskCosts =[]
        self.TaskContributors = []
        self.TaskStarts = []
        self.TaskEnds = []
        self.TaskColors = []
        self.ChartTitle = 0
        
    def draw(self):
        self.figure = Figure(figsize = (8,5.5))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self,-1,self.figure)
        self.axes.set_xlabel('Days of the Month') 
        self.axes.set_ylabel('Tasks')
        self.axes.grid(True) 
        self.axes.set_xlim(0,31)
        self.axes.set_ylim(0,10)
        self.axes.yaxis.tick_right()
        self.axes.set_yticks([])
        self.axes.set_title("Gantt Chart")
        
        if len(self.TaskNames) > 0:
            
            self.figure = Figure(figsize = (8,5.5))
            self.axes = self.figure.add_subplot(111)
            self.canvas = FigureCanvas(self,-1,self.figure)
            self.axes.set_xlabel('Days of the Month') 
            self.axes.set_ylabel('Tasks')
            self.axes.grid(True) 
            graphpositionindex = 1
            listindex = 0
            self.yTickMarkers = []
            for item in self.TaskNames:
                self.axes.broken_barh([(float(self.TaskStarts[listindex]), float(self.TaskEnds[listindex]))], (graphpositionindex*10, 10), facecolors =self.TaskColors[listindex])
                tickmarker = (graphpositionindex*10)+5
                self.yTickMarkers.append(tickmarker)
                graphpositionindex += 1
                listindex += 1
            self.axes.set_yticks(self.yTickMarkers)    
            self.axes.set_yticklabels(self.TaskNames)
            self.axes.yaxis.tick_right()
            self.axes.set_title("Gantt Chart")
            
    def AddEntry(self,name,cost,contributor,start,end,color):
        self.TaskNames.append(name)
        self.TaskCosts.append(cost)
        self.TaskContributors.append(contributor)
        self.TaskStarts.append(start)
        self.TaskEnds.append(end)
        self.TaskColors.append(color)
        self.draw()

class BottomPanel(wx.Panel):
    def __init__(self,parent,toppanel):
        wx.Panel.__init__(self,parent=parent)
        self.SetBackgroundColour("white")
        
        self.chart = toppanel
        
        self.addinfobutton = wx.Button(self,label="Insert Task",size=(150,170),pos=(225,10))
        self.addinfobutton.Bind(wx.EVT_BUTTON,self.AddButtonOnClick)
    
    def GetContributionChart(self):
        self.piefigure = Figure(figsize = (3,3))
        self.pieaxes = self.piefigure.add_subplot(111)
        self.piecanvas = FigureCanvas(self,-1,self.piefigure)
        if len(self.chart.TaskContributors) > 0:
            index = 0
            self.percentages = []
            totalworkdays = 0
            for item in self.chart.TaskContributors:
                if item != "N/A":
                    totalworkdays += float(self.chart.TaskEnds[index])
                    index += 1
            index = 0
            self.labels = []
            for item in self.chart.TaskContributors:
                if item != "N/A":
                    percent = (float(self.chart.TaskEnds[index])/totalworkdays)*100
                    self.percentages.append(percent)
                    index += 1
                    self.labels.append(item)

            self.pieaxes.pie(self.percentages,labels=self.labels)
            self.pieaxes.set_title("Contribution Chart")
        else:
             empty = [100]
             self.pieaxes.pie(empty)
             self.pieaxes.set_title("Contribution Chart")

    def GetBudgetList(self):
        budgetboxlabel = wx.StaticText(self,-1,"Budget",pos=(406,6))
        self.BudgetBox = wx.ListCtrl(self,-1,size=(500,170),pos=(400,25),style=wx.LC_REPORT)
        self.BudgetBox.InsertColumn(0, 'Task',width = 100)
        self.BudgetBox.InsertColumn(1, "Cost (USD)",width=100)
        self.BudgetBox.InsertColumn(2, "Total Cost (USD)",width=100)
        if len(self.chart.TaskCosts) > 0:
            index = 0
            index2 = 0
            for item in self.chart.TaskCosts:
                if item != "N/A":
                    self.BudgetBox.InsertItem(index,self.chart.TaskNames[index2])
                    self.BudgetBox.SetItem(index,1,self.chart.TaskCosts[index2])
                    index += 1
                index2 +=1
            totalcost = 0
            for item in self.chart.TaskCosts:
                if item != "N/A":
                    totalcost += float(item)
            self.BudgetBox.SetItem(0,2,str(totalcost))  
            
    def AddButtonOnClick(self,event):

        TaskNameBox = wx.TextEntryDialog(None, "Enter Task Name","Task Name Entry")
        if TaskNameBox.ShowModal() == wx.ID_OK:
            TaskName = TaskNameBox.GetValue()
        TaskNameBox.Show()
        TaskNameBox.Destroy()
            
        TaskCostBox = wx.TextEntryDialog(None,"Enter Task Cost (USD)", "Task Cost Entry")
        if TaskCostBox.ShowModal() == wx.ID_OK:
            if TaskCostBox.GetValue() != "N/A"or "":
                TaskCost = TaskCostBox.GetValue()
            else:
                TaskCost = "N/A"
        TaskCostBox.Show()
        TaskCostBox.Destroy()
            
        TaskContributorBox = wx.TextEntryDialog(None,"Enter Contributor Name", "Task Contributor Entry")
        if TaskContributorBox.ShowModal() == wx.ID_OK:
            if TaskContributorBox.GetValue() != "N/A" or "":
                TaskContributor = TaskContributorBox.GetValue()
            else:
                TaskContributor = "N/A"
        TaskContributorBox.Show()
        TaskContributorBox.Destroy()
            
        TaskStartBox = wx.TextEntryDialog(None, "Enter Task Start Date","Task Start Date Entry")
        if TaskStartBox.ShowModal() == wx.ID_OK:
            TaskStart = TaskStartBox.GetValue()
        TaskStartBox.Show()
        TaskStartBox.Destroy()
            
        TaskEndBox = wx.TextEntryDialog(None, "Enter Task Duration","How many days will it take to complete this task?")
        if TaskEndBox.ShowModal() == wx.ID_OK:
            TaskEnd = TaskEndBox.GetValue()
        TaskEndBox.Show()
        TaskEndBox.Destroy()
        
        TaskColorBox = wx.TextEntryDialog(None, "Enter Task Color","Task Color Selection")
        if TaskColorBox.ShowModal() == wx.ID_OK:
            TaskColor = TaskColorBox.GetValue()
        TaskColorBox.Show()
        TaskColorBox.Destroy()
 
        self.chart.AddEntry(TaskName,TaskCost,TaskContributor,TaskStart,TaskEnd,TaskColor)
        self.GetContributionChart()
        self.GetBudgetList()
        
class myFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None, title="CBA Gantt Chart Generator",
            size=(800, 650))
        
        self.splitter = wx.SplitterWindow(self)
        self.toppanel = TopPanel(self.splitter)
        self.bottompanel = BottomPanel(self.splitter,self.toppanel)
        self.splitter.SplitHorizontally(self.toppanel,self.bottompanel)
        self.splitter.SetMinimumPaneSize(400)
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem1 = fileMenu.Append(wx.ID_EXIT, 'Insert New Chart from CSV')
        fileItem2 = fileMenu.Append(wx.ID_EXIT, 'Save Tasks to CSV')
        fileItem3 = fileMenu.Append(wx.ID_ANY, 'Export Chart to Image')
        fileItem4 = fileMenu.Append(wx.ID_ANY, 'Exit')
        menubar.Append(fileMenu, 'File')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU,self.SaveChart,fileItem3)
        self.Bind(wx.EVT_MENU,self.Quit,fileItem4)
        self.toppanel.draw()
        self.bottompanel.GetContributionChart()
        self.bottompanel.GetBudgetList()
        
        
    def Quit(self,e):
        self.Destroy()

    def SaveChart(self,e):
        self.toppanel.figure.savefig("Gantt Chart.png")

def main():
    app = wx.App()
    MainFrame = myFrame()
    MainFrame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

