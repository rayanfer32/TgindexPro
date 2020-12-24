# Telegram Index Pro
###### Get your media streaming right from your telegram chat into VLC player and web player. No Downloads to wait for!! Easy to Share !!

[![Open Source Love](https://img.shields.io/github/issues/Rayanfer32/TgindexPro?style=for-the-badge)](.) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-orange.svg?style=for-the-badge)](LICENSE) [![GitHub forks](https://img.shields.io/github/forks/Rayanfer32/TgindexPro?style=for-the-badge)]() [![GitHub Stars](https://img.shields.io/github/stars/Rayanfer32/TgindexPro?style=for-the-badge)]() [![Twitter](https://img.shields.io/twitter/url?style=social)](https://twitter.com/intent/tweet?text=Wow:http://github.com/Rayanfer32/TgindexPro)

## Deploy Now!
[<img height=100 src="https://repl.it/badge/github/Rayanfer32/TgindexPro">](https://repl.it/github/Rayanfer32/TgindexPro)

## Highlights

* Create permanent/Static links for your telegram index (No interruptions if deployed on repl.it )
* Index of a selected channel/chat.
* Stream/Play media directly in VLC player
* View messages and media files on the browser.
* Search through the channel/chat.
* Download media files through browser/download managers.

## Demo

![website index](img/tgindex_site.PNG "website index")

## Bonus content

![playlist creator](img/playlist_site.PNG "playlist site")

## Deploy Guide
#### Easy Way:
[![Run on repl.it](https://repl.it/badge/github/Rayanfer32/TgindexPro)](https://repl.it/github/Rayanfer32/TgindexPro)


#### Preventing repl from going offline:
**Open** [Uptimerobot.com](https://uptimerobot.com) **and add your index site under HTTP(s) (this will ping the site every 5 minutes to keep the site alive)**

* **Environment Variables.**
`Edit the .env file inside`

| Variable Name | Value
|------------- | -------------
| `API_ID` (required) | Telegram api_id obtained from https://my.telegram.org/apps.
| `API_HASH` (required) | Telegram api_hash obtained from https://my.telegram.org/apps.
| `INDEXING_CHAT` (required) | Chat_ID of the chat you are using for index (add `chat id echo bot` to ur group or channel and make it admin to show chat id) 
| `SESSION_STRING` (required) | String obtained by running `$ python3 app/generate_session_string.py`. (Login with the telegram account which is a participant of the given channel (or chat).

#### Manual Deployment:
* **Install dependencies.**
```bash
 pip3 install -U -r requirements.txt
```

* **Environment Variables.**
`PORT` (optional) | Port on which app should listen to, defaults to 8080.
`HOST` (optional) | Host name on which app should listen to, defaults to 0.0.0.0. 
`DEBUG` (optional) | Give some value to set logging level to debug, info by default.

* **Run app.**
```bash
$ python3 -m app
```

## API

Here's the api description. [API](https://github.com/odysseusmax/tg-index/wiki/API)

## Contributions

Contributions are welcome.

## Credits

Orignal Tgindex Developer [@odysseusmax](https://tx.me/odysseusmax).

## License
Code released under [The GNU General Public License](LICENSE).
