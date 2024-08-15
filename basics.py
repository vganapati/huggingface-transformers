from transformers import pipeline

# Sentiment Analysis

classifier = pipeline("sentiment-analysis")
print(classifier(["I've been waiting for a HuggingFace course my whole life!", 
                  "I love learning!",
                  "I hate learning!"]))

# Zero-shot classification

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
print(classifier("This is a course about the Transformers library",
                 candidate_labels=["education", "politics", "business"]))

print(classifier("This is a course about how to knit",
                 candidate_labels=["education", "crafts", "business"]))

# Text generation

generator = pipeline("text-generation")
print(generator("In this course, we will tech you how to", num_return_sequences=2))

# Mask filling

unmasker = pipeline("fill-mask")
print(unmasker("This course will teach you about <mask> models.", top_k=2))

# Named entity recognition

ner = pipeline("ner", grouped_entities=True)
print(ner("I am a clown named Joker in San Francisco"))

# Question answering

question_answerer = pipeline("question-answering")
print(question_answerer(question="Where do I work?", 
                        context="My name is Jane and I work in Berkeley."))

