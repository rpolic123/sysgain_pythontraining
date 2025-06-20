from langdetect import detect

text1 = "Bonjour tout le monde"
text2 = "Hello everyone"
print(f"Text1 Language: {detect(text1)}")
print(f"Text2 Language: {detect(text2)}")