from brltrans import BrailleTranslator

translator = BrailleTranslator("en")
braille = translator.to_braille("Hello world!")
print(braille)  # Outputs: ⠓⠑⠇⠇⠕⠀⠺⠕⠗⠇⠙⠖