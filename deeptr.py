from PackageLaba3.deep_translator import TransLate, LangDetect, CodeLang, LanguageList

text = "Створити віртуальне оточення (ім'я оточення - прізвище студента). В цьому оточенні створити проект Python"
code_of_dest_lang = "pl"

detected_lang = LangDetect(text, set="lang")
translation = TransLate(text, detected_lang, code_of_dest_lang)

dest_lang = CodeLang(code_of_dest_lang)

print("Оригінальний текст: " + text)
print("Мова оригінального тексту: " + detected_lang)
print("Переклад:" + translation)
print("Мова перекладу: " + dest_lang)
print("Код мови перекладу: " + code_of_dest_lang)

LanguageList("screen", text)
