from transformers import pipeline

# Function for sentiment analysis (existing functionality)
def analyze_sentiment(text: str) -> dict:
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    return result

# Text Summarization
def analyze_summary(text: str) -> str:
    # Using Hugging Face's summarization pipeline
    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

# Named Entity Recognition (NER)
def analyze_ner(text: str) -> list:
    # Using Hugging Face's NER pipeline with grouped_entities for cleaner output
    ner_pipeline = pipeline("ner", grouped_entities=True)
    ner_results = ner_pipeline(text)
    return ner_results

if __name__ == "__main__":
    sample_text = (
        "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in April 1976. "
        "The company is known for its innovative products like the iPhone and Mac computers. "
        "Many tech enthusiasts love its sleek designs and powerful performance. "
        "Recently, the launch of the new iPhone has generated a lot of buzz in the market."
    )

    print("Sentiment Analysis:")
    print(analyze_sentiment(sample_text))
    print("\nText Summary:")
    print(analyze_summary(sample_text))
    print("\nNamed Entity Recognition:")
    print(analyze_ner(sample_text))

