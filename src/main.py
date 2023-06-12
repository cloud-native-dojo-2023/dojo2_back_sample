from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

News_list = [
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
        "Date":"2023/8/10", "Title":"新アルバム『夢幻の旅』発売決定！",
        "Description":""""待望の新アルバム『夢幻の旅』が9月1日に発売されます。全曲ライブで披露する予定ですので、ぜひお楽しみに！""",
        "Url":"http://localhost/news3"
    },
    {
        "Date":"2023/9/5", "Title":"生放送のお知らせ！",
        "Description":"""9月20日に特別な生放送があります。新曲の初披露やメンバーとのトークが盛りだくさん！お見逃しなく！""",
        "Url":"http://localhost/news4"
    },
    {
        "Date":"2023/10/1", "Title":"ライブツアー開催決定！",
        "Description":"""全国ツアーの開催が決定しました！各地で熱いパフォーマンスをお届けします。日程とチケット情報は公式サイトをご確認ください。""",
        "Url":"http://localhost/news5"
    },
    {
        "Date":"2023/10/20", "Title":"CDリリース記念イベントのお知らせ",
        "Description":"""新アルバムのリリースを記念して、11月5日にイベントを開催します！メンバーとの握手会や特典付きのCD購入が可能です。""",
        "Url":"http://localhost/news6"
    },
    {
        "Date":"2023/11/15", "Title":"新曲「夢の翼」のCD発売が決定しました！",
        "Description":"""待望の新曲「夢の翼」のCDが12月1日に発売されます。心躍るメロディと感動の歌詞をお楽しみください！""",
        "Url":"http://localhost/news7"
    },
    {
        "Date":"2024/1/5", "Title":"生放送スペシャルイベント開催決定！",
        "Description":"""新年を迎え、1月20日に生放送スペシャルイベントを行います。新曲のステージパフォーマンスやメンバーの生トークをお届けします。""",
        "Url":"http://localhost/news8"
    },
    {
        "Date":"2024/2/10", "Title": "ライブツアー追加公演のお知らせ",
        "Description":"""大好評につき、ライブツアーの追加公演が決定しました！追加公演の詳細やチケットの販売情報は公式サイトでご確認ください。""",
        "Url":"http://localhost/news9"
    },
    {
        "Date":"2024/3/15", "Title": "新曲MV公開＆CD発売情報",
        "Description":"""新曲「未来への一歩」のMVが完成しました！さらに、CDの発売も同時に決定しましたので、ぜひチェックしてください。""",
        "Url":"http://localhost/news10"
    }
]

@app.get("/News")
async def news():
    return sorted(News_list, reverse=True)