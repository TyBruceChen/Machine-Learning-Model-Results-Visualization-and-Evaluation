from sklearn.metrics import recall_score, precision_score, f1_score
def calculate_recall_precision(y_true,y_pred,method = 'weighted'):
    """
    This function generate recall, precision and f1 score
    params:
    y_true and y_pred should be a 1-d array-like variable, the default type is torch.tensor
    y_true: a list of ground truth
    y_pred: a list of predictions
    method: how the recall, precision and F1 score will be calculated. default: None and weighted

    Output: return two sets of metrics. One set contains three lists, where each store the score for
    each class. The other set contains three variable with specified calculation method
    """
    if len(y_true) != len(y_pred):
      return f'The length of ground truth input ({len(y_true)}) is not equal to prediction\'s ({len(y_pred)})!'
    y_true = y_true.cpu()
    y_pred = y_pred.cpu()
    recall = recall_score(y_true,y_pred,average = None)  #the score for each class
    precision = precision_score(y_true,y_pred,average = None)
    f1 = f1_score(y_true,y_pred,average = None)
  
    recall_w = (recall_score(y_true,y_pred,average = method))
    precision_w = (precision_score(y_true,y_pred,average = method))
    f1_w = (f1_score(y_true,y_pred,average = method))
  
    return recall, precision,f1,recall_w,precision_w,f1_w
