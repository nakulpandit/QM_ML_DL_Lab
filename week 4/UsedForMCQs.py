from IPython.display import display, clear_output
from ipywidgets import widgets
from random import shuffle

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)

    shuffle(options)
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        layout={'width': 'max-content'},
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Right." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Wrong. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])
    



Q1=create_multipleChoice_widget('What algorithm would you pick among the following options?', ['The one with the highest training scores', 'The one with the highest test scores', 'The one with the highest difference\n between test and training score'], 'The one with the lowest difference\n between test and training score')
Q2=create_multipleChoice_widget('Which of the following is the best proxy for the generalisation error of a model?',['Training score','Test score','Training error', 'Test Error'],'Test Error')
Q3=create_multipleChoice_widget('Why do we do k-fold validation rather than using a simple train/test split?', ['To select better features', 'To solve underfitting', 'To solve overfitting'], 'To avoid over/underestimating performance because of a peculiar split')
Q4=create_multipleChoice_widget('You are dealing with a binary classification problem in an imbalanced data set. Which one of the following should you probably NOT use as an evaluation metric?', ['Precision', 'Recall'], 'Accuracy')
Q5=create_multipleChoice_widget('Which of the following statements is FALSE about accuracy in machine learning classification?', 
['It represents the overall proportion of correct predictions made by the model.', 'It gives equal weight to both true positives and true negatives.', 'It can be misleading in imbalanced datasets where one class dominates.'], 'It is always the most important metric to consider when evaluating a model.')
Q6=create_multipleChoice_widget('A spam filter has high precision but low recall. What does this mean?', ['It correctly identifies most spam emails, but also flags some legitimate emails as spam.', 'It performs poorly overall, with both high false positives and false negatives.', 'It needs more training data to improve its accuracy.'], 'It misses many spam emails, but the ones it catches are truly spam.')
Q7=create_multipleChoice_widget('A medical test for a rare disease has high recall but low precision. What does this imply?', ['It accurately identifies healthy individuals, but misses many true positive cases.', 'It requires further refinement to improve its overall performance.', 'It is suitable for screening large populations due to its high sensitivity.'], 'It rarely misses a true positive case, but often misdiagnoses healthy individuals.')
Q8=create_multipleChoice_widget('When choosing between optimising for precision or recall, the deciding factor often depends on:', ['The size of the dataset used for training.', 'The computational resources available.', 'The complexity of the machine learning algorithm used.'], 'The cost of false positives and false negatives in the specific application.')

Q9=create_multipleChoice_widget('Your algorithm suffers from high bias if:', ['The model you are using is too complex.', 'The algorithm you are using takes too long.'], 'The model you are using is too simple.')
Q10=create_multipleChoice_widget('Your algorithm suffers from high variance if:', ['The model you are using is too simple.', 'The algorithm you are using takes too long.'], 'The model you are using is too complex.')
Q11=create_multipleChoice_widget('A telltale sign that your algorithm suffers from high bias is:', ['The training scores are much better than the test scores.', 'Both training and test scores are too good to be true.', 'The learning curve shows that the training scores have plateaued.' ], 'The training scores and the test scores are poor.')
Q12=create_multipleChoice_widget('A telltale sign that your algorithm suffers from high variance is:', ['Both training and test scores are too good to be true.', 'The learning curve shows that the training scores have plateaued.', 'The training scores and the test scores are poor.'], 'The training scores are much better than the test scores.')
Q13=create_multipleChoice_widget('Which strategy could help fix high bias?', ['Decreasing model complexity.', 'Using fewer features'], 'Increasing model complexity.')
Q14=create_multipleChoice_widget('Which strategy could help fix high variance?', ['Increasing model complexity.', 'Using more and different features'], 'Decreasing model complexity.')
Q15=create_multipleChoice_widget('What does the plateau on a learning curve typically indicate?', [
'The model is underfitting the data and needs more training data or complex architecture.', 'The model is overfitting the training data and might not generalise well to unseen data.', 'The chosen evaluation metric is not suitable for the task and needs to be replaced.'], 'The model has achieved optimal performance and further training will not improve it.')


