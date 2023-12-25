import random
def Loss_Acc_graph_gen(log_path_list = ['/model_1_log_path'], log_name = ['keyword_to_identify_model_1_logs']
        , plot_selection = 'Both'
        , title_name = '', formal=False
        , label_list=[] ,save_fig = False, save_df = False
        , save_name = str(int(random.random()*1000))):
    """
    params:
    log_path: a list of path where you store the log files
    log_name: a list of keywords to identify the log files for each model you want to display
    plot_selection: 'Both' -> plot both Acc and Loss, 'Acc' -> only plot Acc, 'Loss' -> only plot Loss

    title_name: the graph title, it will only display when formal = False
    formal: True-> disable the title, False -> enable to draw the title
    label_list: legend (name) for each set of lines, when you want to plot multiple models'
      results in one graph.
    save_fig: whether to save the graph
    save_df: whether to save the epochs along with loss/acc ... into csv file
    save_name: specify the name of the saved file(s)
    """
    root_path = './' #the files will be saved under this dir path

    plt.figure(figsize=(10, 10)) #size of the figure

    for i, log_path in enumerate(log_path_list):
        dict_log = {}
        sets = log_name[i]
        log_path_list = []
        test_acc_list = []
        test_loss_list = []
        train_acc_list = []
        train_loss_list = []
        epoch_list = []
        result = []

        for log in os.listdir(log_path):
            if sets in log:  #find files that match with providing keywords
                log_path_list.append(os.path.join(log_path, log))

        for log in log_path_list:
            f = open(log, 'r')
            line = f.read()
            # when the content of the reading file changes, just change the string_extraction function
            epoch, valid_acc,valid_loss, train_loss, train_acc = string_extraction(line)
            result.append((int(epoch), float(valid_acc),float(valid_loss), float(train_loss), float(train_acc)))

        # sort the order according to epoch value
        result = sorted(result, key=get_epoch)
        print(result)
        for eval_item in result:  #read
            epoch_list.append(eval_item[0])
            test_acc_list.append(eval_item[1])
            test_loss_list.append(eval_item[2])
            train_loss_list.append(eval_item[3])
            train_acc_list.append(eval_item[4])

        max_acc = max(test_acc_list)
        max_acc_idx = test_acc_list.index(max_acc)
        max_acc_epoch = epoch_list[max_acc_idx]

        min_loss = min(test_loss_list)
        min_loss_idx = test_loss_list.index(min_loss)
        min_loss_epoch = epoch_list[min_loss_idx]

        plt.rcParams.update({'font.size': 35})
        #matplotlib.rcParams['font.family'] = 'Times New Roman'

        if plot_selection == 'Acc' or 'Both':
            if len(label_list) != 0:
                label = label_list[i]
            else: 
                label = ''
            if plot_selection == 'Both':
                plt.subplot(2,1,1)
            plt.plot(epoch_list, train_acc_list, label = label + ' Train Acc')
            plt.plot(epoch_list, test_acc_list, label = label + ' Validation Acc')
            best_acc = f'Best {str(max_acc_epoch)}: {str(round(max_acc, 2))}'
            plt.scatter(max_acc_epoch, max_acc, s=150, label=f'Max accuracy: {best_acc}')
            plt.xlabel('Epoch')
            plt.ylabel('Accuracy')
        if plot_selection == 'Loss' or 'Both':
            if len(label_list) != 0:
                label = label_list[i]
            else: 
                label = ''
            if plot_selection == 'Both':
                plt.subplot(2,1,2)
            plt.plot(epoch_list, train_loss_list, label = label + ' Train Loss')
            plt.plot(epoch_list, test_loss_list, label = label + ' Validation Loss')
            best_loss = f'Best {str(min_loss_epoch)}: {str(round(min_loss, 2))}'
            plt.scatter(min_loss_epoch, min_loss, s=150, label=f'Min loss: {round(min_loss, 4)}')
            plt.xlabel('Epoch')
            plt.ylabel('Loss')
        if save_df == True:
            dict_log['epoch'] = epoch_list
            dict_log['valid_acc'] = test_acc_list
            dict_log['train_acc'] = train_acc_list
            dict_log['valid_loss'] = test_loss_list
            dict_log['train_loss'] = train_loss_list
            df_log = pd.DataFrame(dict_log)
            if len(label_list) != 0:
              label = label_list[i]
            df_log.to_csv(root_path + save_name + '_'+ str(i) + '.csv')

    plt.legend()

    if formal == False:
      if plot_selection == 'Loss' or None:
        plt.title(title_name + 'ACC',fontsize = 25)

    plt.legend()
    if formal == False:
      if plot_selection == 'Acc' or None:
        plt.title(title_name + 'LOSS',fontsize = 25)

    #matplotlib.rcParams['font.family'] = 'Times New Roman'
    if save_fig == True:
            plt.savefig(root_path + save_name + '.png')
    plt.show()

def get_epoch(ls):  #return the first item in the list
    return ls[0]

def string_extraction(txt):
    """
    The function to extract information inside each log file
    input format:[epoch] valid_acc [valid_acc]\n valid_loss [valid_loss]\n train_loss [train_loss]\n train [train_acc]
    output format:[ep],[valid_acc],[valid_loss],[train_loss],[train_acc]
    """
    sub_string_list = txt.split('\n')
    ep,valid_acc = sub_string_list[0].split(' valid_acc ')
    _,valid_loss = sub_string_list[1].split(' valid_loss ')
    _,train_loss = sub_string_list[2].split(' train_loss ')
    _,train_acc = sub_string_list[3].split(' train ')
    return ep, valid_acc, valid_loss, train_loss, train_acc
