import pandas as pd
from fastai.text.all import *


if __name__ == "__main__":
 
    # Pad the labels to the same length
    def selectKeywords(label, word_amount):
        labelList = label.split()
        if len(labelList) < word_amount:
            labelList = labelList + ['NA'] * (word_amount - len(labelList))
        else:
            labelList = labelList[:word_amount]
        return ' '.join(labelList)

    # Load data and preprocess
    frame = pd.read_csv('extraData\\50000_patents_with_keywords.csv')
    frame = frame.drop(columns=['patent', 'claims'])
    frame = frame.dropna()
    
    # Create the input for the model
    frame['input'] ='ABSTRACT: ' + frame.abstract 
    
    # Create the labels for the model
    num_keywords = max(frame['keywords'].apply(lambda x: len(x.split(' '))))
    frame['labels'] = frame['keywords'].apply(lambda x: selectKeywords(x, num_keywords))
    frame = frame.drop(columns=['title', 'abstract', 'keywords'])

    # Define data block and dataloader
    all_labels = list(set(frame['labels'].str.split().explode()))
    datablock = DataBlock(blocks=(TextBlock.from_df('input', seq_len=72), MultiCategoryBlock(encoded=False, vocab=all_labels)),
                   splitter=RandomSplitter(valid_pct=0.1, seed=42),
                   get_x=ColReader('text'),
                   get_y=ColReader('labels', label_delim=' '),
                  )

    dataloader = datablock.dataloaders(frame)

    # Define and train the model
    learner = text_classifier_learner(dataloader, AWD_LSTM, drop_mult=0.5, metrics=accuracy_multi)
    learner.fit_one_cycle(2, 4e-4)

    # Save the trained model
    learner.export('keyWordExtracter.pkl')
