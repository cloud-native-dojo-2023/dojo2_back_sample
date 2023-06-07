from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

News_list = [
    {"Date":"2023/6/2", "Title":"【出演ステージ決定！】2023年7月29日(土)「FUJI ROCK FESTIVAL '23」出演決定！","Description":"""2023年7月28日(金)、29日(土)、30日(日)に湯沢町苗場スキー場にて開催される「FUJI ROCK FESTIVAL '23」にVaundyの出演が決定いたしました！


●日時：
2023年7月28日(金)、29日(土)、30日(日)
※Vaundyは7月29日(土) WHITE STAGEに出演いたします。

●会場：
湯沢町苗場スキー場（新潟県）

オフィシャルサイトはこちら""",
"Url":"https://vaundy.jp/news/detail/10211"},

{"Date":"2023/5/30", "Title":"雑誌「ROCKIN'ON JAPAN」にて「JAPAN JAM 2023」写真＆レポート掲載！","Description":"""音楽雑誌「ROCKIN’ON JAPAN」2023年7月号の別冊 JAPAN JAM 2023にて、「JAPAN JAM 2023」の写真とミニレポートが掲載されています。


「ROCKIN’ON JAPAN」2023年7月号
https://www.rockinon.co.jp/publication/magazine/178803""",
"Url":"https://vaundy.jp/news/detail/10276"},

{"Date":"2023/5/22", "Title":"「strobo」リリース3周年を記念し、2022年の「Vaundy Museum Live」をYouTubeにて生配信決定！","Description":"""1stアルバム「strobo」リリース3周年を記念し、2022年にWOWOWにて放送された貴重な「Vaundy Museum Live」を5月27日(土)21:00よりYouTubeにてライブ映像ノーカット特別生配信！

■生配信詳細
『WOWOW×Vaundy Museum Live on YouTube』
配信日：2023年5月27日(土) 21:00 START(予定)
https://www.youtube.com/@Vaundy""",
"Url":"https://vaundy.jp/news/detail/10275"},

{"Date":"2023/5/20", "Title":"雑誌「MUSICA」にて「VIVA LA ROCK 2023」写真＆コメント掲載！","Description":"""音楽雑誌「MUSICA」2023年6月号 Vol.194にて、「VIVA LA ROCK 2023」の写真とコメントが掲載されています。


「MUSICA」2023年6月号 Vol.194
http://www.musica-net.jp/detail/2023/6/""",
"Url":"https://vaundy.jp/news/detail/10274"},

{"Date":"2023/5/20", "Title":"2023年8月26日(土)「音楽と髭達2023-WA-」出演決定！ ","Description":"""2023年8月26日(土)にHARD OFF ECO スタジアム新潟にて開催される「音楽と髭達2023-WA-」にVaundyの出演が決定いたしました！


●日時：
2023年8月26日(土)
開場 8:30 / 開演 10:40
※Vaundyは19:10より出演いたします。

●会場：
HARD OFF ECO スタジアム新潟（新潟県）


オフィシャルサイトはこちら""",
"Url":"https://vaundy.jp/news/detail/10272"},

{"Date":"2023/5/19", "Title":"【配信タイムテーブル解禁！】「メトロック2023 独占生中継！Day2」出演決定！","Description":"""ABEMAにて5月21日(日)に無料独占配信される「メトロック2023 独占生中継！Day2」に出演いたします。


放送日時：
2023年5月21日(日) 11:00～

■放送チャンネル：ABEMA メトロックチャンネル
https://abe.ma/42dRP6W
※Vaundyの見逃し配信はございません。""",
"Url":"https://vaundy.jp/news/detail/10272"},

{"Date":"2023/5/19","Title":"【出演日解禁！】2023年8月12日(土)「RISING SUN ROCK FESTIVAL 2023 in EZO」出演決定！","Description":"""2023年8月11日(金・祝)、12日(土)に石狩湾新港樽川ふ頭横野外特設ステージにて開催される「RISING SUN ROCK FESTIVAL 2023 in EZO」にVaundyの出演が決定いたしました！


●日時：
2023年8月11日(金・祝)、12日(土)
11日：開場 10:00／開演 14:00
12日：開場 10:00／開演 12:30
※Vaundyは8月12日(土)に出演いたします。

●会場：
石狩湾新港樽川ふ頭横野外特設ステージ
（北海道石狩市新港中央1丁目 / 小樽市銭函5丁目）

オフィシャルサイトはこちら""",
"Url": "https://vaundy.jp/news/detail/10271"},

{"Date":"2023/5/15","Title":"【ステージサイドバック席先行受付開始！】Vaundy one man live ARENA tour チケット先行受付情報","Description":"""2023年11月より全国5ヶ所10公演を行うVaundy初のアリーナツアー"Vaundy one man live ARENA tour" のチケット先行受付が決定しました！

●ステージサイドバック席オフィシャル先行受付
https://w.pia.jp/t/vaundy-tour/
受付期間：2023/05/15(月) 12:00 ～ 2023/05/28(日) 23:59
抽選日：2023/06/06(火)

＝＝＝＝＝

2023年11月18日(土) Open 17:00 / Start 18:00
会場：宮城・ゼビオアリーナ仙台

2023年11月19日(日) Open 15:00 / Start 16:00
会場：宮城・ゼビオアリーナ仙台

2023年12月02日(土) Open 17:00 / Start 18:00
会場：神奈川・横浜アリーナ

2023年12月03日(日) Open 15:00 / Start 16:00
会場：神奈川・横浜アリーナ

2023年12月09日(土) Open 17:00 / Start 18:00
会場：福岡・マリンメッセ福岡 A館

2023年12月10日(日) Open 15:00 / Start 16:00
会場：福岡・マリンメッセ福岡 A館

2023年12月16日(土) Open 17:00 / Start 18:00
会場：大阪・大阪城ホール

2023年12月17日(日) Open 15:00 / Start 16:00
会場：大阪・大阪城ホール

2024年01月05日(金) Open 18:00 / Start 19:00
会場：愛知・日本ガイシホール

2024年01月06日(土) Open 15:00 / Start 16:00
会場：愛知・日本ガイシホール

2024年01月20日(土) Open 17:00 / Start 18:00
会場：東京・国立代々木競技場 第一体育館

2024年01月21日(日) Open 15:00 / Start 16:00
会場：東京・国立代々木競技場 第一体育館

〈全公演共通〉
チケット代 : ¥9,900-（税込)

主催・企画 : SDR/Vaundy_ART Work Studio
制作 : SDR・Intergroove Productions Inc.

＊注意事項＊
本公演の開催にあたり、ご来場されるお客様におかれましては、ご案内と注意事項を必ずよくお読み頂きますようお願い致します。
※本注意事項は予告なく変更する場合がありますので予めご了承下さい。


公演詳細はLIVEページをご覧ください。""",
"Url":"https://vaundy.jp/news/detail/10202"},

{"Date":"2023/5/12","Title":"【出演日解禁！】2023年8月19日(土)「MONSTER baSH 2023」出演決定！ ","Description":"""2023年8月19日(土)、20日(日)に香川県国営讃岐まんのう公園にて開催される「MONSTER baSH 2023」にVaundyの出演が決定いたしました！


●日時：
2023年8月19日(土)、20日(日)
開場 9:00／開演 11:00 (予定)
※Vaundyは8月19日(土)に出演いたします。

●会場：
国営讃岐まんのう公園（香川県）

オフィシャルサイトはこちら""",
"Url":"https://vaundy.jp/news/detail/10259"},

{"Date":"2023/5/10","Title":"Vaundyプロデュース楽曲「おもかげ (produced by Vaundy)」がストリーミング累計1億回再生を突破！","Description":"""Vaundyプロデュース楽曲「おもかげ (produced by Vaundy)」がストリーミング累計1億回再生を突破！

YouTubeチャンネル『THE FIRST TAKE』で実現したコラボレーションで、第73回NHK紅白歌合戦ではmilet×Aimer×幾田りら×Vaundyとして歌唱し大きな話題を呼んだ楽曲 milet×Aimer×幾田りら「おもかげ (produced by Vaundy)」がBillboard JAPANチャートにおけるストリーミング累計再生回数1億回を突破！
https://www.billboard-japan.com/d_news/detail/124943/2


Vaundyが他アーティストに提供した楽曲ではAdo「逆光 (ウタ from ONE PIECE FILM RED)」に続き2曲目の1億回突破となる。



「おもかげ (produced by Vaundy)」milet×Aimer×幾田りら""",
"Url":"https://vaundy.jp/news/detail/10265"}
]

@app.get("/News")
async def news():
    return News_list