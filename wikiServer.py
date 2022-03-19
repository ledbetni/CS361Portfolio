import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.ioloop import IOLoop
import json
import urllib

class MainHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')


    def wikiScraper(self,item):
        import wikipedia
        import warnings
        warnings.catch_warnings()
        warnings.simplefilter("ignore")
        #CHANGE LANGUAGE SETTING
        #wikipedia.set_lang("fr")
        try:
            itemPage = wikipedia.page(item)
            print(itemPage.summary)
            print("----------------------")
            return itemPage.summary
        except wikipedia.exceptions.DisambiguationError as e:
            print(e)
            return(e)
        except wikipedia.exceptions.PageError as p:
            print(p)
            return(p)
           


    def get(self):
            self.write({'message':'Welcome to wiki scraper - send a POST request to localhost:1400'})

    async def post(self):
        value =  self.get_argument('item')
        wikiValue =  self.wikiScraper(value)
        postRes =  json.dumps({'item': str(wikiValue)})
        self.write(postRes)
        


def make_app():
    return tornado.web.Application({
        (r"/", MainHandler),
        
    })

if __name__ == "__main__":
    app = make_app()
    app.listen(1400)
    print("Server listening on port 1400, make a POST request to use the Wiki Scraper")
    IOLoop.instance().start()