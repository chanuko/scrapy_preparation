# scrapy_preparation
scrapyを始めるときのやつ


```sh
pipenv install --python=$(which python)
```

```sh
pipenv shell
```

```sh
scrapy startproject samplesite
cd samplesite
scrapy genspider example example.com
```