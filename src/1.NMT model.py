## English to German
from transformers import pipeline
translation = pipeline(“translation_en_to_de”)
text = "I like to study Data Science and Machine Learning"

translated_text = translation(text, max_length=40)[0]['translation_text']
print(translated_text)


## Custom Language Translation Example - English to Chinese
from transformers import AutoModelWithLMHead, AutoTokenizer
model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")

translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)
text = "I like to study Data Science and Machine Learning"
translated_text = translation(text, max_length=40)[0]['translation_text']
print(translated_text)