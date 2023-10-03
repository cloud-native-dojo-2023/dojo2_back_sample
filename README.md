# クラウドネイティブ道場2023

## 使い方

Redisを使っているのでこれをインストールする
https://redis.io/docs/getting-started/installation/

```
pip3 install fastapi
pip3 install uvicorn[standard]
```  

```uvicorn main:app --reload```  

このコマンドで, ローカルでfastapiサーバーが起動する.

http://127.0.0.1:8000/News

にアクセスすることでニュース一覧を取得する.

## 追記
上記のインストールはしなくても良いです.
コンテナ化してあります.
