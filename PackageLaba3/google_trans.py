from googletrans import Translator, LANGUAGES


def TransLate(text: str, src: str, dest: str) -> str:
    """
    Функція повертає текст перекладений на задану мову, або повідомлення про помилку.

    text - текст, який необхідно перекласти;
    src - назва або код мови заданого тексту, відповідно до стандарту ISO-639,
    або значення 'auto';
    dest - назва або код мови на яку необхідно перевести заданий текст,
    відповідно до стандарту ISO-639
    """
    translator = Translator()

    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return str(e)


def LangDetect(text: str, set: str = "all") -> str:
    """
    Функція визначає мову та коефіцієнт довіри для заданого тексту,
    або повертає повідомлення про помилку.

    text - текст для якого потрібно визначити мову та коефіцієнт довіри;
    set - 'lang' – функція повертає тільки мову тексту
          'confidence' – функція повертає тільки коефіцієнт довіри
          'all' (по замовченню) – функція повертає мову і коефіцієнт довіри
    """
    translator = Translator()

    try:
        detection = translator.detect(text)

        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Мова: {detection.lang}, Коефіцієнт довіри: {detection.confidence}"
    except Exception as e:
        return str(e)


def CodeLang(lang: str) -> str:
    """
    Функція повертає код мови (відповідно до таблиці), якщо в параметрі lang міститься назва
    мови, або повертає назву мови, якщо в параметрі lang міститься її код,
    або повідомлення про помилку.

    lang - назва або код мови
    """
    try:
        lang = lang.lower()

        if lang in LANGUAGES:
            return LANGUAGES[lang]
        elif lang in LANGUAGES.values():
            for code, name in LANGUAGES.items():
                if name == lang:
                    return code
        else:
            return "Мова не знайдена"
    except Exception as e:
        return str(e)


def LanguageList(out: str = "screen", text: str = None):
    """
    Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів,
    а також текст, перекладений на цю мову. Повертає 'Ok', якщо всі операції виконані,
    або повідомлення про помилку.
    out - 'screen' (по замовченню) – вивести таблицю на екран
    'file' – вивести таблицю в файл. (Тип файлу на розсуд студента)
    text - текст, який необхідно перекласти. Якщо параметр відсутній, то відповідна колонка
    в таблиці також повинна бути відсутня.
    """
    try:
        if out == "file":
            if text is None:
                return "Відсутній параметр тексту"

            with open("../languageList.txt", "w", encoding="utf-8") as file:
                file.write("N\tМова\tISO-639 код\tТекст\n")
                file.write("-" * 80 + "\n")
                for i, (code, name) in enumerate(LANGUAGES.items(), start=1):
                    translation = TransLate(text, "auto", code)
                    file.write(f"{str(i).ljust(5)}{name.ljust(20)}{code.ljust(15)}{translation}\n")
            print("Ok")
            return "Ok"
        else:
            if text is None:
                return "Відсутній параметр тексту"

            print("N\tМова\tISO-639 код\tТекст")
            print("-" * 80)
            for i, (code, name) in enumerate(LANGUAGES.items(), start=1):
                translation = TransLate(text, "auto", code)
                print(f"{str(i).ljust(5)}{name.ljust(20)}{code.ljust(15)}{translation}")
            print("Ok")
            return "Ok"
    except Exception as e:
        return str(e)
