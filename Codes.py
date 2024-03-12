from googletrans import Translator

# function that translates the entered text using google translate
def translateText(text, targetLang):
  translator = Translator()
  Translation = translator.translate(text, dest = targetLang)
  return Translation.text

# text to translate
text = input("text to translate: ")

# target language choice
targetLang = input('''
1) Turkish 
2) English
3) German
4) Spanish
5) Japanese
6) French
7) Russian

Enter the code for a language in: ''')

if targetLang == '1':
    targetLang = "tr"
elif targetLang == '2':
    targetLang = "en"
elif targetLang == '3':
    targetLang = "de"
elif targetLang == '4':
    targetLang = "es"
elif targetLang == '5':
    targetLang = "ja"
elif targetLang == '6':
    targetLang = "fr"
elif targetLang == '7':
    targetLang = "ru"
else: # To prevent possible errors
    print("An incorrect selection code please correct.")

# text translation
TranslatedText = translateText(text, targetLang)

# Çevrilen metni ekrana yazdır
print(f"({text}) when translated into the desired language --> {TranslatedText}")
