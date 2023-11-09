from fastapi import FastAPI
from random import randint
import datetime
import redis as rds
import hashlib as hl
import Register
import uvicorn
from pydantic import BaseModel
from tango_kaiseki import split_noun
from tango_kaiseki import mrp_analisys
from tango_kaiseki import cleanning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import UserRegister
import os

redis_endpoint = (os.getenv("REDISIPADDR"), int(os.getenv("REDISPORT")))
print(redis_endpoint)
IPADDR = (os.getenv("IPADDR"))
news1 = [
    {
        "Date": "2023/6/15",
        "Title": "【重要】クジラが水族館にやってきました！",
        "Description": "この度，クジラが水族館の仲間に加わります。大迫力なクジラの展覧をお楽しみに！",
        "Url": IPADDR + "/news/news1"
    },
    {
        "Date": "2023/7/15",
        "Title": "「珊瑚」展示公開のお知らせ",
        "Description": "珊瑚を展示公開します！珊瑚の魅力が分かっちゃう！！",
        "Url": IPADDR + "/news/news10"
    },
    {
        "Date": "2023/6/15",
        "Title": "夜間の生物展示 (アシカ・ケープペンギン・モモイロペリカン)に関するお知らせ",
        "Description": "この度夜間の生物展示が好評であるため期間を延長します．お楽しみください！",
        "Url": IPADDR + "/news/news11"
    },
    {
        "Date": "2023/7/2",
        "Title": "サカバンバスピスの新グッズ限定発売決定！",
        "Description": "今年もやってきました！新グッズ限定販売が今年も開催されます．今年はサカバンバスピスをグッズ化します．お楽しみに！",
        "Url": IPADDR + "/news/news12"
    },
    {
        "Date": "2023/8/10",
        "Title": "ペンギンの赤ちゃんが生まれました！",
        "Description": "今年は元気なペンギンの赤ちゃんが生まれました！後日名前募集いたします．奮ってご応募ください．",
        "Url": IPADDR + "/news/news13"
    },
    {
        "Date": "2023/9/5",
        "Title": "イルカショーのご案内",
        "Description": "4月から7月までのイルカショーの予定をお知らせします．イルカスタジアムでの入場制限は行っておりませんのでご自由にご観覧ください．",
        "Url": IPADDR + "/news/news14"
    },
    {
        "Date": "2023/10/1",
        "Title": "アシカショーのお知らせ",
        "Description": "アシカショーの4月から6月の予定をお知らせします．ぜひ遊びに来てくださいね！",
        "Url": IPADDR + "/news/news15"
    },
    {
        "Date": "2023/10/20",
        "Title": "コツメカワウソの赤ちゃんが生まれました！",
        "Description": "コツメカワウソの赤ちゃんが4頭生まれました．男の子1頭と女の子3頭です．後日名前募集いたします．奮ってご応募ください．",
        "Url": IPADDR + "/news/news16"
    },
    {
        "Date": "2023/11/15",
        "Title": "年間パスポート利用規約改定のお知らせ",
        "Description": "2023年3月31日をもって年間パスポート利用規約が改定されます．2023年4月1日から新しくなるためご注意ください．",
        "Url": IPADDR + "/news/news17"
    },
    {
        "Date": "2023/1/5",
        "Title": "新エリア増設決定！",
        "Description": "この度皆様の熱いご要望により深海魚エリアを増設することとなりました．2022年2月3日から工事が始まりますのでご理解とご協力をよろしくお願いいたします．",
        "Url": IPADDR + "/news/news18"
    }
]
news2 = [
    {
        "Date":"2023/4/10", 
        "Title":"新エリアの深海魚エリアにシーラカンスを展示決定！",
        "Description":"""新しく増設された深海魚エリアにシーラカンスのはく製を展示することが決定いたしました！深海魚エリアをお楽しみに！""",
        "Url":IPADDR + "/news/news19"
    },
    {
        "Date":"2023/4/20", 
        "Title":"新エリアの深海魚エリアが来月オープン！",
        "Description":"""ついに！！2023年5月7日から深海魚エリアがオープンします！まだ見たことのない魚と出会えるかもしれません！お見逃しなく！""",
        "Url":IPADDR + "/news/news2"},
    {
        "Date":"2023/7/15", 
        "Title":"深海魚エリアにダイオウグソクムシがやってくる！",
        "Description":""""5月にオープンした深海魚エリアにダイオウグソクムシが追加されます！お楽しみに！""",
        "Url":IPADDR + "/news/news20"
    },
    {
        "Date":"2023/6/22", 
        "Title":"ドクターフィッシュ体験イベント開催！",
        "Description":"""角質を食べてくれるというドクターフィッシュを体験できるイベントを開催します！水槽に入れることができるのは手のみとなります．""",
        "Url":IPADDR + "/news/news3"
    },
    {
        "Date":"2023/6/25", 
        "Title":"セイウチショーのご案内",
        "Description":"""4月から7月までのセイウチショーの予定をお知らせします．ショーのあとはセイウチに触れることができますのでお楽しみに！""",
        "Url":IPADDR + "/news/news4"
    },
    {
        "Date":"2023/6/28", 
        "Title":"イベントチケット発売のお知らせについて",
        "Description":"""ペンギンふれあいイベントのチケットは午前10時からチケット売り場で販売いたします．皆様のご理解とご協力の程よろしくお願いいたします．""",
        "Url":IPADDR + "/news/news5"
    },
    {
        "Date":"2023/7/2",
        "Title":"展示・ショーについてのお知らせ",
        "Description":"""アシカの体調管理を優先するため一部内容を変更しショーを実施します．ご理解とご協力の程、宜しくお願い申し上げます。""",
        "Url":IPADDR + "/news/news6"
    },
    {
        "Date":"2023/7/5", 
        "Title":"イルカの「さくら」永眠のお知らせ",
        "Description":"""本日，イルカの「さくら」が永眠いたしました．「さくら」を応援してくださったみなさまに，感謝とお礼を申しあげます．""",
        "Url":IPADDR + "/news/news7"
    },
    {
        "Date":"2023/9/10", 
        "Title": "【期間限定】ハロウィンイベント開催！",
        "Description":"""ハロウィンイベントを開催します．館内にお化けやパンプキンなどの装飾が施され，いつもと違う体験ができます．""",
        "Url":IPADDR + "/news/news8"
    },
    {
        "Date":"2023/6/30", 
        "Title": "期間限定イベント「水族館夏祭り」開催のお知らせ",
        "Description":"""水族館と夏祭りが融合した期間限定イベントを開催します．7月10日から8月31日まで開催され，夜の水族館ではプロジェクションマッピングが投影されます．また，期間限定グッズの販売も行っております．""",
        "Url":IPADDR + "/news/news9"
    }
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserModel(BaseModel):
    UID:str

class RegisterModel(BaseModel):
    UID:str
    HASH:str


@app.post("/News")
def news(user:UserModel):

    my_rds = rds.Redis(host=redis_endpoint[0], port=redis_endpoint[1])

    #ランダムな記事を3つ選択してそれを閲覧した記事とする
    #閲覧した記事の名詞表現をデータベースから取り出す(ユーザの単語リストとする)



    # random_number = [randint(0,len(news2)-1) for i in range(3)]
    # random_news_hash = [hl.md5((news2[i]['Description']+'-'+str(datetime.datetime.strptime(news2[i]['Date'],'%Y/%m/%d').timestamp())).encode()).hexdigest() for i in random_number]

    # random_title_noun = [(my_rds.hget(v,'Title').decode(), my_rds.hget(v,'Noun').decode()) for v in random_news_hash]
    # random_mrp = [v[1] for v in random_title_noun]
    # random_title = [v[0] for v in random_title_noun]
    # print(random_title)
    # mrp_serialize = ''
    # for word in random_mrp:
    #     mrp_serialize += word

    #redisからuserの単語リストを取得する
    # username = user.UID
    username = user.UID
    print(username)
    user_words = [word.decode() for word in my_rds.lrange(username, 0, -1)]

    mrp_serialize = ''
    for word in user_words:
        mrp_serialize += word
    
    #ここから類似度を計算する
    
    tfidf = TfidfVectorizer()

    
    #ハッシュをランキングにしたもので日時でソートする
    all_news_ranked = my_rds.zrevrange('NewsRank',0,11, withscores=True)
    all_description = [{'Title':my_rds.hget(v,'Title').decode(), 'Noun':my_rds.hget(v,'Noun').decode(), 'URL':my_rds.hget(v,'Url').decode(), 'Date':datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d"), 'Hash': v.decode()} for v,t in all_news_ranked]

    doc_dict_list = [{'Title':None, 'Noun':mrp_serialize, 'URL':None, 'Date':datetime.datetime.now(), 'Hash':None}] + all_description
    doc_list = [v['Noun'] for v in doc_dict_list]

    res_list = [{'Title':v['Title'], 'level':0, 'URL':v['URL'], 'Hash':v['Hash'], 'Date':v['Date'], 'ruijido':'0.0000'} for v in doc_dict_list[1:]]

    X = tfidf.fit_transform(doc_list)

    Xarray = X.toarray()

    ruijido = [v for v in cosine_similarity(Xarray)[0][1:]]
    if abs(max(ruijido) - min(ruijido)) <= 0:
        ruijido = [1 for v in ruijido]
    time_passed = [(datetime.datetime.now()-datetime.datetime.strptime(t['Date'],"%Y-%m-%d")).days for t in doc_dict_list[1:]]
    time_weighted = [v*time_weight(365,t) for v, t in zip(ruijido, time_passed)]

    print(time_weighted)

    max_ruijido = max(time_weighted)
    min_ruijido = min(time_weighted)

    #分割数おかしい

    for i, _v in enumerate(time_weighted):
        level = 0
        v = (_v - min_ruijido)/(max_ruijido - min_ruijido)
        if 0.8 <= v <= 1:
            level = 1
        elif 0.6 <= v < 0.8:
            level = 2
        elif 0.4 <= v < 0.6:
            level = 3
        elif 0.2 <= v < 0.4:
            level = 4
        else:
            level = 5
        res_list[i]['Date'] = res_list[i]['Date']
        res_list[i]['level'] = level
        res_list[i]['ruijido'] = format(v*100, '.2f')
        print(level)
    
    return res_list

@app.get("/Noun")
async def get_noun(uid: str="yamasita"):
    my_rds = rds.Redis(host=redis_endpoint[0], port=redis_endpoint[1])
    user_words = [word.decode() for word in my_rds.lrange(uid, 0, -1)]
    return user_words

@app.post("/Register")
def register(data:RegisterModel):
    my_rds = rds.Redis(host=redis_endpoint[0], port=redis_endpoint[1])
    news_hash = data.HASH
    uid = data.UID

    worddata = my_rds.hget(news_hash,'Noun').decode()
    my_rds.rpush(uid,worddata)

    print([v.decode() for v in my_rds.lrange(uid,0,-1)])

    return data

def time_weight(max_day, x):
    if max_day <= x:
        return 0
    return (1/(x+1)) - (1/(max_day+1))
    
def main():
    print(redis_endpoint)
    my_rds = rds.Redis(host=redis_endpoint[0], port=redis_endpoint[1])
    # username = "test_user3"
    # user_words = [word.decode() for word in my_rds.lrange(username, 0, -1)]
    # print(user_words)
    # random_number = [randint(0,len(news2)-1) for i in range(3)]
    # random_news_hash = [hl.md5((news2[i]['Description']+'-'+str(datetime.datetime.strptime(news2[i]['Date'],'%Y/%m/%d').timestamp())).encode()).hexdigest() for i in [randint(0,len(news2)-1) for i in range(3)]]

    # random_title_noun = [(my_rds.hget(v,'Title').decode(), my_rds.hget(v,'Noun').decode()) for v in [hl.md5((news2[i]['Description']+'-'+str(datetime.datetime.strptime(news2[i]['Date'],'%Y/%m/%d').timestamp())).encode()).hexdigest() for i in [randint(0,len(news2)-1) for i in range(3)]]]
    # random_mrp = [v[1] for v in [(my_rds.hget(v,'Title').decode(), my_rds.hget(v,'Noun').decode()) for v in [hl.md5((news2[i]['Description']+'-'+str(datetime.datetime.strptime(news2[i]['Date'],'%Y/%m/%d').timestamp())).encode()).hexdigest() for i in [randint(0,len(news2)-1) for i in range(3)]]]]
    #random_mrpの名詞をredisに入れる
    
    # random_title = [v[0] for v in random_title_noun]
    # print(random_title)
    # mrp_serialize = ''
    # for word in random_mrp:
    #     mrp_serialize += word


    # DB初期化用コード
    # my_register1 = Register.Register(news1)
    # my_register1.register_noun()
    # my_register2 = Register.Register(news2)
    # my_register2.register_noun()
    # ur = UserRegister.UserRegister(["test_user_null"],[[v[1] for v in [(my_rds.hget(v,'Title').decode(), my_rds.hget(v,'Noun').decode()) for v in [hl.md5((news2[i]['Description']+'-'+str(datetime.datetime.strptime(news2[i]['Date'],'%Y/%m/%d').timestamp())).encode()).hexdigest() for i in [randint(0,len(news2)-1) for i in range(3)]]]] for i in range(3)])

    my_rds.flushdb()
    redis_initialize()
    ur = UserRegister.UserRegister(redis_endpoint[0],redis_endpoint[1],["yamasita", "tarou", "hanako"])
    ur.register_user()

    # my_rds = rds.Redis(host=redis_endpoint[0], port=redis_endpoint[1])
    # test = my_rds.zrevrange('NewsRank',0,-1,withscores=True)
    # print(test)
    # for v,t in test:
    #     print(datetime.datetime.fromtimestamp(t), my_rds.hget(v.decode(),'Title').decode())

    uvicorn.run(app, host="0.0.0.0", port=8000)

def redis_initialize():
    my_rds = rds.Redis(host=redis_endpoint[0], port=redis_endpoint[1])
    # DB初期化用コード
    my_register1 = Register.Register(news1, redis_endpoint[0],redis_endpoint[1])
    my_register1.register_noun()
    my_register2 = Register.Register(news2, redis_endpoint[0], redis_endpoint[1])
    my_register2.register_noun()
    ur = UserRegister.UserRegister(redis_endpoint[0],redis_endpoint[1],["test_user_null"],[[v[1] for v in [(my_rds.hget(v,'Title').decode(), my_rds.hget(v,'Noun').decode()) for v in [hl.md5((news2[i]['Description']+'-'+str(datetime.datetime.strptime(news2[i]['Date'],'%Y/%m/%d').timestamp())).encode()).hexdigest() for i in [randint(0,len(news2)-1) for i in range(3)]]]] for i in range(3)])

if __name__ == "__main__":
    main()
