from transformers import pipeline

# 1. Create a sentiment-analysis pipeline using a model from Hugging Face
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# 2. Run the model on a sample text
result = classifier("Streamlit makes it easy to build amazing apps!")
print(result)