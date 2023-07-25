import redis as rd
import tango_kaiseki as tk
import hashlib as hl

class Register:
    def __init__(self, News_list) -> None:
        self.News_list = News_list

    def register_noun(self):

        rhandler = rd.Redis()

        for i, news in enumerate(self.News_list):

            myword = ''
            myhash = hl.md5(news['Description'].encode()).hexdigest()

            for word in [v[0] for v in tk.split_noun(tk.cleanning(news["Description"]))]:
                myword += word + ' '

            rhandler.hmset(myhash, {'Title':news['Title'], 'Noun':myword, 'Date':news['Date']})

