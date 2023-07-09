import googletrans

def translate(text, source_lang, target_lang):
  """Translates text from one language to another."""
  translator = googletrans.Translator()
  translated_text = translator.translate(text, src=source_lang, dest=target_lang)
  return translated_text

if __name__ == "__main__":
  text = "I love you."
  source_lang = "en"
  target_lang = "fr"
  translated_text = translate(text, source_lang, target_lang)
  print(translated_text)
