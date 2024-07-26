# Code:
# import libraries
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("savasy/bert-turkish-text-classification")

# build and load model, it take time depending on your internet connection
model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-turkish-text-classification")

# make pipeline
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# apply model
nlp("bla bla")
# [{'label': 'LABEL_2', 'score': 0.4753005802631378}]

code_to_label = {
    'LABEL_0': 'dunya ',
    'LABEL_1': 'ekonomi ',
    'LABEL_2': 'kultur ',
    'LABEL_3': 'saglik ',
    'LABEL_4': 'siyaset ',
    'LABEL_5': 'spor ',
    'LABEL_6': 'teknoloji '}

code_to_label[nlp("bla bla")[0]['label']]
# > 'kultur '
