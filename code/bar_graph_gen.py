import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

def bar_graph_gen(csv_path = './test_results/Accuracy_models.csv',
                  colors = ['red', 'green', 'blue', 'yellow','purple','gray', 'orange','brown'],
                  model_names = ['model_1','model_2','model_3','model_4','model_5','modle_6','model_7','model_8']
                  display_range = (92,96)):
  """
  csv_path: where the accuracy/output stores
  colors: the color of bar with respect to each model (from bottom to top), default 8 model types
  model_names： the name of bar with respect to each model (from bottom to top), default 8 model types
  display_range: limit the display range of accuracy (default from 92 to 96)
  """
  plt.figure(figsize = (15,15))  #define the size of  the ourput graph
                    
  df = pd.read_csv(csv_path)  #the csv should contain one column 'Accuracy', if this code does not change.
  bar_idx = np.arange(len(colors))  #the y axis values, range from 0 to number of models -1
  
  plt.barh(bar_idx,df['Accuracy']*100, color = colors)  #plot the bar in horizontal direction
  
  plt.yticks(np.arange(len(model_names)),model_names)  #change the displayed ticks along y axis to model_names
  range_l, range_h = display_range
  plt.xlim(range_l,range_h)  
  
  plt.ylabel('Model type')
  plt.xlabel('Accuracy (%)')
  #plt.title('Accuracy comparison between models')
  matplotlib.rcParams['font.family'] = 'Times New Roman'
  
  plt.show()
