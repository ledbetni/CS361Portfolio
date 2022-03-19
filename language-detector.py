from langdetect import detect
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class DetectorHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    def get_language(self, lang):

        languages_dict = {
            'af': 'Afrikaans',
            'ar': 'Arabic',
            'bn': 'Bengali',
            'bg': 'Bulgarian',
            'ca': 'Catalan',
            'cs': 'Czech',
            'cy': 'Welsh',
            'da': 'Danish',
            'de': 'German',
            'el': 'Greek',
            'en': 'English',
            'es': 'Spanish',
            'et': 'Estonian',
            'fa': 'Persian',
            'fi': 'Finnish',
            'fr': 'French',
            'gu': 'Gujarati',
            'he': 'Hemodern',
            'hi': 'Hindi',
            'hr': 'Croatian',
            'hu': 'Hungarian',
            'id': 'Indonesian',
            'it': 'Italian',
            'ja': 'Japanese',
            'kn': 'Kannada',
            'ko': 'Korean',
            'lt': 'Lithuanian',
            'lv': 'Latvian',
            'mk': 'Macedonian',
            'ml': 'Malayalam',
            'mr': 'MarMarāṭhī',
            'ne': 'Nepali',
            'nl': 'Dutch',
            'no': 'Norwegian',
            'pa': 'Punjabi',
            'pl': 'Polish',
            'pt': 'Portuguese',
            'ro': 'Romanian',
            'ru': 'Russian',
            'sk': 'Slovak',
            'sl': 'Slovene',
            'so': 'Somali',
            'sq': 'Albanian',
            'sv': 'Swedish',
            'sw': 'Swahili',
            'ta': 'Tamil',
            'te': 'Telugu',
            'th': 'Thai',
            'tl': 'Tagalog',
            'tr': 'Turkish',
            'uk': 'Ukrainian',
            'ur': 'Urdu',
            'vi': 'Vietnamese'
        }

        if lang in languages_dict:
            return languages_dict[lang]

    def get(self):
        self.write({'message': 'Welcome to AnyLanguage - send a POST request to localhost:3000'})

    def post(self):
        value = self.get_argument('text')
        langDetect = detect(value)
        pretty_lang = self.get_language(langDetect)
        self.write(pretty_lang)


def make_app():
    urls = [("/", DetectorHandler)]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    print("Language Detector microservice listening at 'http://localhost:3000' make a POST request to continue")
    IOLoop.instance().start()
