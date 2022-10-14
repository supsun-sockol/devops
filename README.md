#  Инструкция
## Инструкция по запуску скрипта
Скрипт запускается с агрументами командной строки, например:
'''
script.py ./test.yaml -wd ./test_rep -f 1
'''

Обязательным аргументом является путь до yaml файла
Далее можно использовать ключи
1) -wd - work directory - папка, в которой лежат версии проекта
2) -f - ключ запроса подтверждения удаления
3) --help

## Инструкция по написанию yaml файла

Структур состоит из правил. Каждое правио выполняется с каждым проектом

role - отдельные павила выполняющиеся последовательно
if - блок условий, котороый относится к определенной
версии проекта, но не затрагивает файлы внутри

1) age - минимальный возраст проекта, если проекту меньше, то к нему не применятся действия
2) maj - версия проекта release или test

do - блок действий, которые выполнятся, если ВСЕ условия
из блока if будут выполнены

1) delrep: 1 - удалить данную версию проекта
2) delmask: mask удалить все файлы и папки, которые попадают под маску
3) delage - удаляет все файлы и папки, которые старше определенного возраста
в заданной папке

возраст указывается в формате 5d - означает 5 дней
программу можно легко расширить до дней, месятцев, лет и т.д
Пример:
'''
- rule:
    if:
        age: 5d
        maj: test
    do:
        delrep: 1
- rule:
    if:
        age: 3d
        maj: test
    do:
        delmask: "tests/*.tar.gz"

- rule:
    if:
        age: 5d
        maj: release
    do:
        delage:
            age: 70d
            path: debug
'''

## Пояснения к бонусу

Использовалась база данный MySQL
Пример базы данный прикреплен в качестве примера к проекту
Подключение осуществляется с помощью библиотеки python pymysql
Если она у вас не установлена, требуется установить

База данных была развернута в докере с пробросо на локальном хосте

Grafana-у я экспортировал в json файл. Для гарантии прикрепил скриншоты