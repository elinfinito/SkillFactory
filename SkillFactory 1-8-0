if __name__ == "__main__":

    queries = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"
    words = ['сериалы', 'курс']
    queries = queries.replace(",", " ")

    result = ""

    for i in words:
        if queries.find(i) >= 0:
            result = result + " " + i
    result = result.strip(" ")
    print(result)
