from googletrans import Translator

translator = Translator()
text = "Hello, how are you?"
result = translator.translate(text, dest='fr')
print(f"Original: {text}")
print(f"French: {result.text}")