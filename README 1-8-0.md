ДОМАШНЕЕ ЗАДАНИЕ
Теперь мы можем перейти к решению реальной задачи.

Дана строчка из CSV-файла, которая содержит набор поисковых запросов, разделенных запятой:

queries = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"
Также дан список слов, по которому необходимо отфильтровать исходную строку с поисковыми запросами:

words = ['сериалы', 'курс']
Вам необходимо написать скрипт, который выводит на экран строчку queries, в которой оставлены только те запросы, которые содержат слова из листа words.

При проверке решения проверьте, пожалуйста, три пункта:

1. Итоговый ответ содержится в переменной result. Т. е. если в самом конце кода написать print(result), то на экран будет выведен верный ответ.

2. Переменная result имеет тот же строковый тип, что и исходная строка queries.

3. Порядок фраз в ответе должен сохраниться.

И  обратите внимание на пробелы и запятые!
