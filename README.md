# はじめに
rinna株式会社さんのKoemotionを勉強するためのページ予定  
まとめたものを追記

---
# Koemotionとは

apiでやり取りできるLLM。以下の特徴がある
- テキストを返す
- 低レイテンシでやりとり可能
- 2D,3Dの画像をしゃべるようなモーションを生成する元を返す

---
# 環境構築
- windows11 + wsl(ubuntu22.04)
- python 3.10.12

#### linuxバージョン確認/wsl内ターミナル
```bash
$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.5 LTS"
```

#### 必要なパッケージインストール
```bash
$ apt install python3.10-venv
```

#### 仮想環境作成入場
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
#### 仮想環境内で必要なパッケージインストール
```
(venv)$ pip install -U pip
(venv)$ pip install python-dotenv
```



---
ここまでのディレクトリ構造
```
(venv) root@ayakashi:/home/bastet/work/ai/koemotion# tree -L 2
.
├── README.md
├── __pycache__
│   └── settings.cpython-310.pyc
├── main.py
├── settings.py
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg

6 directories, 5 files
```
---

# koemotion
まずはドキュメントから
[Koemotionの利用ガイド](https://koemotion.rinna.co.jp/guide)


