import plotly.figure_factory as ff
import pandas as pd
import os


df_pd = pd.read_csv(os.path.join(os.getcwd(), 'proj_data.csv'))
df_pd.columns = ['Task', 'Start', 'Finish']
df = df_pd.to_dict('records')
print(df)

colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']

          
fig = ff.create_gantt(df, 
                      index_col = 'Start',
                      colors = colors, 
                      title = 'Gantt Chart Tool', 
                      bar_width = 0.2, 
                      showgrid_x = False, 
                      showgrid_y = False,
                      height = 600, 
                      width = 600, 
                      reverse_colors = False, 
                      show_colorbar = False)

fig.layout.xaxis.rangeselector={}


fig.show()


fig.write_image('proj_temp.png')
#fig.write_image('proj_temp.pdf')
