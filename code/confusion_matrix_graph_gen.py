from sklearn.metrics import confusion_matrix
def confusion_matrix_graph_gen(y_true,y_pred,label_list = [0,1,2,3],
                          class_labels = ['Class 1','Class 2','Class 3','Class 4'],
                          method = 'true',save_path = None):
    """
    This function generate and store (optional) confusion matrix 
    params:
    The shape of y_ture and y_pred should be 1-d 
    y_true: a list of ground truth
    y_pred: a list of predictions
    label_list: a list of digits which contains all numbers appeared in the prediction
    class_labels: a list of names with respect to the digitinside class_labels
    method: how the percentage displayed in the graph block will be calculated
        'pred': the percentage in prediction column
        'true': the percentage in ground truth row
    save_path: default doesn't save the confusion matrix, if you want to save it, input with the
        path in string
    """
    y_true = y_true.cpu()
    y_pred = y_pred.cpu()
    cm_num = confusion_matrix(y_true,y_pred, labels = label_list, normalize = None)
    cm_prob = confusion_matrix(y_true,y_pred, labels = label_list, normalize = method)
    print(cm_num)
    H,W = cm_num.shape
    
    plt.figure(figsize = (25,25))  #the size of the graph
    plt.xticks(np.arange(len(class_labels)), class_labels)
    plt.yticks(np.arange(len(class_labels)), class_labels)
    matplotlib.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams.update({'font.size': 56})
    plt.imshow(cm_num, interpolation='nearest', cmap=plt.cm.Blues)  # Use a blue color map
    for i,cm_value_row in enumerate(cm_num): 
        for j,cm_value in enumerate(cm_value_row):
            cm = str(cm_value) + '\n ' + str(round(cm_prob[i][j]*100,2))+'%'
            if i == j:
                plt.text(j,i,cm,ha= 'center',va= 'center',fontstyle = 'normal',color = 'orange',weight = 'bold',fontsize = 48)
            else:
                plt.text(j,i,cm,ha = 'center',va = 'center',fontstyle = 'normal',color = 'black',weight = 'bold',fontsize = 48)
    #plt.title('Confusion Matrix')
    plt.xlabel('Prediction',color = 'black',weight = 'bold')
    plt.ylabel('Ground Truth',color = 'black',weight = 'bold')
    
    plt.colorbar()
    
    if save_path != None:
        plt.savefig(os.path.join(save_path + '/confusion_matrix.png'))
    plt.show()
