# DAppRank


[![GitHub license](https://img.shields.io/github/license/Bit03/gluon.svg)](https://github.com/Bit03/gluon/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/Bit03/gluon.svg)](https://github.com/Bit03/gluon/network)
[![GitHub stars](https://img.shields.io/github/stars/Bit03/gluon.svg)](https://github.com/Bit03/gluon/stargazers)
[![Build Status](https://travis-ci.org/Bit03/gluon.svg?branch=master)](https://travis-ci.org/Bit03/gluon)
[![Coverage Status](https://coveralls.io/repos/github/Bit03/gluon/badge.svg?branch=master)](https://coveralls.io/github/Bit03/gluon?branch=master)
[![Updates](https://pyup.io/repos/github/Bit03/gluon/shield.svg)](https://pyup.io/repos/github/Bit03/gluon/)
[![Python 3](https://pyup.io/repos/github/Bit03/gluon/python-3-shield.svg)](https://pyup.io/repos/github/Bit03/gluon/)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/Bit03/gluon.svg?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FBit03%2Fgluon)


[![Dapprank](https://cdn.dribbble.com/users/2123695/screenshots/4787505/dapprank.png)](https://dribbble.com/shots/4787505-DApp-Rank)

## 准备工作

```.bash
git clone --recursive -j8 https://github.com/Bit03/gluon.git

cd gluon/
mkvirtualenv -p `which python3.6` -r requirements/local.txt


cd path/to/gluon/frontend/
npm i
npm run build

```

## 启动 Django server
```.bash
mv .env.example .env

python manage.py runserver
```