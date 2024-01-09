import os
from torch import tensor
from Loss_Acc_graph import *
from bar_graph_gen import *
from confusion_matrix_graph_gen import *
from metrics_eval import *
root_path = ''
csv_models_path = os.path.join(root_path,'')
bar_graph_gen(csv_models_path)
gtrue = [0,1,2,2,1,0,3]
prediction = [1,1,2,0,2,0,3]
gtrue = tensor(gtrue)
prediction = tensor(prediction)
calculate_recall_precision(gtrue, prediction)
draw_confusion_matrix(gtrue,prediction)
test_txt  = '1 valid_acc 0.5\n valid_loss 1.2\n train_loss 0.55\n train 1.3'
string_extraction(test_txt)
