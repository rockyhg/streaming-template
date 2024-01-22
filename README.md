# streaming-template

## はじめに
Streamlit上でリアルタイム画像処理を行うためのテンプレートです。

[streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc) というライブラリを使用し、リアルタイムのカメラ画像をウェブブラウザ上に表示することができます

**リアルタイム画像処理のメリット:**

- データ（カメラ画像）が生成される瞬間に分析と予測を行うことができます
- ユーザーエクスペリエンス: 即時にフィードバックがあるので楽しいです


## デモ用Webアプリ

このテンプレートをデプロイしたWebアプリです。

https://streaming-template.streamlit.app

1. 上記ページにアクセスし、[SELECT DEVICE] ボタンを押し、カメラを選択してください
2. [START] ボタンを押してください
3. カメラで映した映像とダミーのバウンディングボックスが表示されます


## セットアップ手順

1. GitHubからZipファイルをダウンロード、フォルダに展開

2. VS Codeで上記フォルダを開く

3. 仮想環境を作成する
    - VS Codeのターミナルを開き、下記のコマンドを実行
    - `$ python -V`（Pythonのバージョンを確認。念のため）
    - `$ python -m venv myenv`
      - `myenv` には好きな仮想環境名を入力してください

4. 仮想環境を有効化する
	- Windowsの場合: `$ myenv\Scripts\Activate.ps1`
	- Macの場合: `$ source myenv/bin/activate`
	- コマンドラインの冒頭に仮想環境名が表示される

5. ライブラリをインストール
	`$ pip install -r requirements.txt`

6. [Twilio（トゥイリオ）](https://www.twilio.com/ja-jp)の無料アカウントを作成

7. Twilioのアカウント情報を取得
   - Twilioにログインし、「Account Info」から下記2つをコピーする
     - Account SID
     - Auth Token

8. 環境変数ファイル作成
   - 同フォルダ内に、`.env`（拡張子のみ）というファイルを作成
   - ACCOUNT SID, AUTH TOKENを記入
   - Twilioのアカウント情報を環境変数に格納するため

```
TWILIO_ACCOUNT_SID="<自分のAccount SID>"
TWILIO_AUTH_TOKEN="<自分のAuth Token>"
```

9. ローカル動作確認
   - `$ streamlit run app.py`

10. [Streamlit Cloud](https://share.streamlit.io/) にデプロイ
    - [New app] ボタン
    - 必要事項を入力
    - [Advanced settings...] リンク
    - Python versionを選択
    - Secrets欄に上記環境変数情報を入力


## 補足

- WebRTC プロトコルを使用してブラウザ間のピアツーピア通信を確立し、ビデオやオーディオをリアルタイムに送受信します
- このテンプレートを Streamlit Cloud にデプロイして動かすには、TURNサーバーの設定が必要です
  - TURN サーバーは、直接通信が難しいネットワーク環境でも、データを中継することで通信を可能にするものです
- このテンプレートでは、Twilio というサービスのTURNサーバーを使用しています
- ローカル環境でも動作させたい場合は、python-dotenv というライブラリを使用し、`.env` ファイルに環境変数を記載します
- 【注意】`.env` ファイルにはアカウント情報が含まれているので、GitHubには公開しないようにします。このため、`.gitignore` ファイルに `.env` を記載しています


## References

- [whitphx/streamlit-webrtc: Real-time video and audio streams over the network, with Streamlit.](https://github.com/whitphx/streamlit-webrtc)
- [whitphx/streamlit-webrtc-example](https://github.com/whitphx/streamlit-webrtc-example/blob/main/app.py)
