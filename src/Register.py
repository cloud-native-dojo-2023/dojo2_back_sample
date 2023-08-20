import redis as rd
import tango_kaiseki as tk
import hashlib as hl
import datetime

class Register:
    def __init__(self, News_list, host, port) -> None:
        self.News_list = News_list
        self.host = host
        self.port = port

    def register_noun(self):

        rhandler = rd.Redis(host=self.host, port=self.port)
        rpipe = rhandler.pipeline()

        for i, news in enumerate(self.News_list):

            my_datetime = datetime.datetime.strptime(news['Date'],'%Y/%m/%d')
            my_unixtime = my_datetime.timestamp()

            myword = ''
            for word in [v[0] for v in tk.split_noun(tk.cleanning(news["Description"]))]:
                myword += word + ' '

            """ rhandler.hmset(myhash, {'Title':news['Title'], 'Date':news['Date'], 'URL':news['Url'], 'Noun':myword}) """
            desctiption_unixtime_hash = hl.md5((news['Description']+'-'+str(my_unixtime)).encode()).hexdigest()

            rpipe.zadd('NewsRank',{desctiption_unixtime_hash:my_unixtime})
            rpipe.hset(desctiption_unixtime_hash,'Title',news['Title'])
            rpipe.hset(desctiption_unixtime_hash,'Url',news['Url'])
            rpipe.hset(desctiption_unixtime_hash,'Noun',myword)
        rpipe.execute()

