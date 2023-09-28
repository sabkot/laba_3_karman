from PackageLaba3.deep_translator import GoogleTranslator
import langdetect


def get_language(text):
    try:
        return langdetect.detect(text)
    except Exception as e:
        return str(e)


def translate_text(config_file):
    try:

        with open(config_file, 'r') as f:
            config = {}
            for line in f:
                key, value = line.strip().split(': ')
                config[key] = value


        with open(config['file_name'], 'r', encoding='utf-8') as f:
            text = f.read()


        source_language = get_language(text)
        print("Мова тексту:", source_language)


        translated_text = GoogleTranslator(source=source_language, target=config['target_language']).translate(text)


        if config['output'] == 'file':
            output_file_name = config['file_name'].split('.')[0] + '_' + config['target_language'] + '.txt'
            with open(output_file_name, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print("Ok")
        elif config['output'] == 'screen':
            print("Мова перекладу:", config['target_language'])
            print(translated_text)
            print("Ok")
        else:
            print("Невірно вказано вивід (file або screen)")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    config_file = "config_file.txt"
    translate_text(config_file)
