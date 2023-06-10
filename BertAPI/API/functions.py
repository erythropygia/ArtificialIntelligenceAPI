from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig, pipeline

import os
import json
nlpmodels_dir = os.path.join("NLPModels")

config_sentiment = AutoConfig.from_pretrained(nlpmodels_dir+r"/SENTIMENT-MODEL/config.json")
model_sentiment = AutoModelForSequenceClassification.from_pretrained(nlpmodels_dir+r"/SENTIMENT-MODEL/sentiment_model.bin", config=config_sentiment)
tokenizer_sentiment = AutoTokenizer.from_pretrained(nlpmodels_dir+r"/SENTIMENT-MODEL")

def create_pipeline():
    sentiment_pipeline = pipeline(
        task='text-classification',
        model=model_sentiment,
        tokenizer=tokenizer_sentiment,
        framework='pt',
        #device=device # GPU kullanmak isterseniz 0 yerine -1 yazın
    )

    return sentiment_pipeline

def predict(text):

    text = text.replace('\n', ' ')

    sentiment_pipeline= create_pipeline() 

    sentiment_result = sentiment_pipeline(text)
    sentiment = {
    "sentiment" : sentiment_result[0]['label'],
    "score": sentiment_result[0]['score']
    }


    ensemble_result = {
        'sentiment': sentiment
    }

    return ensemble_result
