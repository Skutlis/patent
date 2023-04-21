# Analyzing patent applications using NLP

The objective of this project was to produce a sentiment analysis on patents. There are many ways to produce such an analysis, but this particular project 
focuses on extracting key-words from patents. 

## The project in short
My approach to this project was to extract context from the patents by identifying relevant keywords. To begin, the available data from Zenodo was analyzed, and the "patent_txt_raw.csv" and "keywords.txt" files were selected as suitable for the model.

With data for over 6 million patents, the files were too large to be analyzed in any file editor, so python was utilized for analysis of the content. To reduce the size of the dataset, 50.000 patents were extracted and matched with relevant keywords. The initial approach followed a Kaggle notebook on natural language processing by Jeremy Howard, which used a pre-trained transformer model. However, due the model's memory requirements needed for such a big dataset, the model could not be trained on a laptop. A lot of time was spent trying to minimize the memory consumtion, with no luck. Luckily, there was another approach to this problem.

The Universal Language Model Fine-tuning (ULMFiT) approach by fastai containes models pre-trained on large datasets which can be fine-tuned for specific datasets. The architecture of the models are smaller than the ones in transformers(from huggingface) and require therefor less memory consumption. Training a model in the with the fastai library required a lot of doc reading since it (like most libraries) has a very spesific way of implementation. It was not so straight forwad to train a multi-labeled dataset, but after many attempts the model finally trained! The first model had a fixed input size (fixed amount of words) and a list of indexes as labels, where element at index i in the label list corresponded to word at index i in the input. The elements was either 1, if corresponding word was a keyword, or 0 otherwise. This model did not perform well, which is why it was so great to discover that the labels could be fed to the trainer as a string given that they contained the same amount of words! This gave a significantly better result. After fine-tuning the parameters, the model ended up with a great accuracy(accuracu_multi from fastai library): 0.999 on the validation set.

## Challanges
There were a lot of challanges during this project. Many of them were related to formatting the labels. A big problem throughout this project was labels (or classes) not included in the training dataset. A lot of thought went into how to format the labels in such a way that we can expose the model for new words and still get a result. The final model cannot predict new words, but it is exposed to a dataset of 50.000 patents, so it covers a lot of words. This could be a very robust model if the right resources were available(in the form of more memory and cpu). 

Another challange was memory consumption. The pre-trained transformers models from huggingface require vast amounts of memory for large datasets. The initial approach was to reduce the data by reducing the input columns and reducing rows. It was obvius that Transformers was not the way to go when even 50 patents lead to a Memory error when training the model. Luckily the ULMFiT library in fastai provides text classifiers uses significantly less memory, and was absolutly the right approach for this project. 

## Pitfalls
A definitiv pitfall with keyword extraction is that it could never capture the whole sentiment of a patent. The information extracted is more contextual then sentimental. The model is also very spesific, meaning that it cannot extract words which was not included in the training dataset. This pitfall could be minimized by training the model on a bigger dataset, but more resources is needed for that. 


## Larger context
Keyword extraction using NLP is a powerful technique in text mining that aims to extract significant insights and information data. It can be applied in various domains such as customer support, social media analysis, document clustering, and obtaining business intelligence. With the help of keyword extraction, businesses can analyze customer feedback, identify trending topics, and analyze sentiment towards a particular brand or product. Overall, this technique is incredibly valuable because it allows us to easily understand and analyze the content of large volumes of text data, leading to more efficient and effective decision-making.



## Reproducing the results
1. Download the files: "patent_txt_raw.zip" and "keywords.zip" from https://zenodo.org/record/3515985
2. Unpack the zipped files and put them in a subfolder of the project named "extraData"
3. Run the scripts: 
    3.(a) "grab50000.py" 
    3.(b) "matchKeywords.py" 
    3.(c) "trainModel.py" 
4. The model can be testet by running the script "predKeys.py" and following the instruction in the terminal


## Resources
https://zenodo.org/record/3515985
https://www.bytesview.com/blog/what-is-keyword-extraction/