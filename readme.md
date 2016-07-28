# Skeleton of tornado project
## Softs
* debian
* tornado
* postgresql
* momoko
* yoyo
* vagrant

## Migrations
* конфиг - configs/yoyo.ini
* старт из папки project: yoyo -c ../configs/yoyo.ini <apply/rollback/reapply/mark/unmark/new>

## Start
* vagrant up

## Start tests with covarage
py.test --cov=postman --cov-report term-missing tests/