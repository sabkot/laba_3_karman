from deep_translator import GoogleTranslator
import langdetect

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translation = GoogleTranslator(source=src, target=dest).translate(text)
        return translation
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang_info = langdetect.detect_langs(text)
        if set == "lang":
            return lang_info[0].lang
        elif set == "confidence":
            return str(lang_info[0].prob)
        else:
            return f"Мова: {lang_info[0].lang}, Коефіцієнт довіри: {lang_info[0].prob}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    try:
        languages = GoogleTranslator()._languages

        if lang in languages.values():
            for code, name in languages.items():
                if name == lang:
                    return code

        elif lang in languages:
            return languages[lang]
        else:
            return "Мова не знайдена"
    except Exception as e:
        return str(e)

def LanguageList(out: str = "screen", text: str = None):
    try:
        if out == "file":
            if text is None:
                return "Відсутній параметр тексту"
            with open("languageList.txt", "w", encoding="utf-8") as file:
                file.write("N\tМова\tISO-639 код\tТекст\n")
                file.write("-" * 80 + "\n")
                for i, (code, name) in enumerate(GoogleTranslator()._languages.items(), start=1):
                    translation = TransLate(text, "auto", code)
                    file.write(f"{str(i).ljust(5)}{name.ljust(20)}{code.ljust(15)}{translation}\n")
            print("Ok")
            return "Ok"
        else:
            if text is None:
                return "Відсутній параметр тексту"
            print("N\tМова\tISO-639 код\tТекст")
            print("-" * 80)
            for i, (code, name) in enumerate(GoogleTranslator()._languages.items(), start=1):
                translation = TransLate(text, "auto", code)
                print(f"{str(i).ljust(5)}{name.ljust(20)}{code.ljust(15)}{translation}")
            print("Ok")
            return "Ok"
    except Exception as e:
        return str(e)
