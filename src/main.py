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

news1 = [
    {
        "Date": "2023/6/15",
        "Title": "【重要】新曲リリース＆生放送決定！",
        "Description": "皆様への感謝の気持ちを込めて、新曲のCD発売が決定しました！さらに、リリース記念として生放送も行います。お楽しみに！",
        "Url": "http://localhost/news1"
    },
    {
        "Date": "2023/6/18",
        "Title": "🎵 サマーフェス開催決定！",
        "Description": "熱い夏を盛り上げるため、サマーフェスを開催します！多彩なバンドが出演予定です。お見逃しなく！",
        "Url": "http://localhost/news2"
    },
    {
        "Date": "2023/6/22",
        "Title": "【ライブ情報】全国ツアー開催中！",
        "Description": "全国各地をまわるツアーを開催中です！新曲も披露しますので、ぜひ会場にお越しください！",
        "Url": "http://localhost/news3"
    },
    {
        "Date": "2023/6/25",
        "Title": "🎉 ファン感謝イベント開催のお知らせ",
        "Description": "ファンの皆様への感謝を込めたイベントを開催します！特典やサプライズが満載です。お楽しみに！",
        "Url": "http://localhost/news4"
    },
    {
        "Date": "2023/6/28",
        "Title": "【重要】メンバーサプライズ生誕祭開催！",
        "Description": "メンバーの誕生日をお祝いするスペシャルイベントを行います！お誕生日サプライズも要チェックです。",
        "Url": "http://localhost/news5"
    },
    {
        "Date": "2023/7/2",
        "Title": "🎶 新アルバム制作進行中！",
        "Description": "新しいアルバムの制作が進行中です！新たな音楽で皆様を魅了します。",
        "Url": "http://localhost/news6"
    },
    {
        "Date": "2023/7/5",
        "Title": "【チケット発売情報】次回ライブ開催決定！",
        "Description": "次回のライブ開催が決定しました！チケットの発売は近日中に開始します。",
        "Url": "http://localhost/news7"
    },
    {
        "Date": "2023/7/9",
        "Title": "✨ 10周年記念ライブ開催！",
        "Description": "バンド結成10周年を記念してスペシャルライブを開催します！これまでの感謝を込めて、特別な演出も予定しています。",
        "Url": "http://localhost/news8"
    },
    {
        "Date": "2023/7/12",
        "Title": "【お知らせ】メンバーグッズ新発売！",
        "Description": "新しいメンバーグッズの発売が決定しました！限定アイテムもありますのでお見逃しなく。",
        "Url": "http://localhost/news9"
    },
    {
        "Date": "2023/7/15",
        "Title": "🎤 ソロコンサート開催決定！",
        "Description": "メンバーのソロコンサートを開催します！それぞれの個性が輝くスペシャルなステージになること間違いなし。",
        "Url": "http://localhost/news10"
    }
]
news2 = [
    {
        "Date":"2023/6/15", "Title":"【重要】新曲リリース＆生放送決定！",
        "Description":"""皆様への感謝の気持ちを込めて、新曲のCD発売が決定しました！さらに、リリース記念として生放送も行います。お楽しみに！""",
        "Url":"http://localhost/news1"
    },
    {
        "Date":"2023/7/2", "Title":"ライブイベント開催のお知らせ",
        "Description":"""今年もやってきました！私たちのライブイベントが7月15日に開催されます。新曲の披露や特別なパフォーマンスをお見逃しなく！""",
        "Url":"http://localhost/news2"},
    {
        "Date":"2022/8/10", "Title":"新アルバム『夢幻の旅』発売決定！",
        "Description":""""待望の新アルバム『夢幻の旅』が9月1日に発売されます。全曲ライブで披露する予定ですので、ぜひお楽しみに！""",
        "Url":"http://localhost/news3"
    },
    {
        "Date":"2022/9/5", "Title":"生放送のお知らせ！",
        "Description":"""9月20日に特別な生放送があります。新曲の初披露やメンバーとのトークが盛りだくさん！お見逃しなく！""",
        "Url":"http://localhost/news4"
    },
    {
        "Date":"2022/10/1", "Title":"ライブツアー開催決定！",
        "Description":"""全国ツアーの開催が決定しました！各地で熱いパフォーマンスをお届けします。日程とチケット情報は公式サイトをご確認ください。""",
        "Url":"http://localhost/news5"
    },
    {
        "Date":"2022/10/20", "Title":"CDリリース記念イベントのお知らせ",
        "Description":"""新アルバムのリリースを記念して、11月5日にイベントを開催します！メンバーとの握手会や特典付きのCD購入が可能です。""",
        "Url":"http://localhost/news6"
    },
    {
        "Date":"2022/11/15", "Title":"新曲「夢の翼」のCD発売が決定しました！",
        "Description":"""待望の新曲「夢の翼」のCDが12月1日に発売されます。心躍るメロディと感動の歌詞をお楽しみください！""",
        "Url":"http://localhost/news7"
    },
    {
        "Date":"2022/1/5", "Title":"生放送スペシャルイベント開催決定！",
        "Description":"""新年を迎え、1月20日に生放送スペシャルイベントを行います。新曲のステージパフォーマンスやメンバーの生トークをお届けします。""",
        "Url":"http://localhost/news8"
    },
    {
        "Date":"2023/2/10", "Title": "ライブツアー追加公演のお知らせ",
        "Description":"""大好評につき、ライブツアーの追加公演が決定しました！追加公演の詳細やチケットの販売情報は公式サイトでご確認ください。""",
        "Url":"http://localhost/news9"
    },
    {
        "Date":"2023/3/15", "Title": "新曲MV公開＆CD発売情報",
        "Description":"""新曲「未来への一歩」のMVが完成しました！さらに、CDの発売も同時に決定しましたので、ぜひチェックしてください。""",
        "Url":"http://localhost/news10"
    }
]


app = FastAPI()


@app.get("/News")
def news():

    #ランダムな記事を3つ選択してそれを閲覧した記事とする
    #閲覧した記事の名詞表現をデータベースから取り出す(ユーザの単語リストとする)


    my_rds = rds.Redis()
    random_news = [hl.md5(news2[randint(0,len(news2)-1)]['Description'].encode()).hexdigest() for i in range(3)]

    random_title_noun = [(my_rds.hget(v,'Title').decode(), my_rds.hget(v,'Noun').decode()) for v in random_news]
    random_mrp = [v[1] for v in random_title_noun]
    random_title = [v[0] for v in random_title_noun]
    print(random_title)
    mrp_serialize = ''
    for word in random_mrp:
        mrp_serialize += word
    
    #ここから類似度を計算する
    
    tfidf = TfidfVectorizer()

    #見ていないものだけを抽出する
    all_news = [v.decode() for v in my_rds.scan_iter(match='*') if not(v.decode() in random_news)]
    all_description = [{'Title':my_rds.hget(v,'Title').decode(), 'Noun':my_rds.hget(v,'Noun').decode(), 'Date':my_rds.hget(v,'Date').decode(), 'URL':my_rds.hget(v,'URL')} for v in all_news]



    dt_now = datetime.datetime.now()
    doc_dict_list = [{'Title':'-', 'Noun':mrp_serialize, 'Date':dt_now.strftime('%Y/%m/%d'), 'URL':'-'}] + all_description
    doc_list = [v['Noun'] for v in doc_dict_list]

    res_list = [{'Title':v['Title'], 'level':0, 'URL':v['URL']} for v in doc_dict_list[1:]]

    X = tfidf.fit_transform(doc_list)

    Xarray = X.toarray()

    ruijido = cosine_similarity(Xarray)
    time_passed = [(datetime.datetime.now()-datetime.datetime.strptime(t['Date'], '%Y/%m/%d')).days for t in doc_dict_list[1:]]
    time_weighted = [v*time_weight(365,t) for v, t in zip(ruijido[0][1:], time_passed)]

    max_ruijido = max(time_weighted)
    max_ruijido_quartor = max_ruijido/4

    for i, v in enumerate(time_weighted):
        level = 0
        if (max_ruijido_quartor*4) <= v:
            level = 1
        elif (max_ruijido_quartor*3) <= v < (max_ruijido_quartor*4):
            level = 2
        elif (max_ruijido_quartor*2) <= v < (max_ruijido_quartor*3):
            level = 3
        elif (max_ruijido_quartor) <= v < (max_ruijido_quartor*2):
            level = 4
        else:
            level = 5
        res_list[i]['level'] = level
    
    return res_list

def time_weight(max_day, x):
    if max_day <= x:
        return 0
    return (1/(x+1)) - (1/(max_day+1))
    
def main():
    """ my_register1 = Register.Register(news1)
    my_register1.register_noun()
    my_register2 = Register.Register(news2)
    my_register2.register_noun() """
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
