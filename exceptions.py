# -*- coding:utf-8 -*-


def process_user_notation(user_notation):
    """ Пользовательская нотация """
    result = 0

    notation = [item.strip() for item in user_notation.split()]

    try:
        notation = [notation[0]] + [float(i) for i in notation[1:]]
        try:
            assert notation[1] >= 0
            assert notation[2] >= 0

        except AssertionError:
            print("Нотация содержит отрицательное число!")
            return

        operations = {
            '?': notation[1] + notation[2],
            '+': notation[1] + notation[2],
            '-': notation[1] - notation[2],
            '*': notation[1] * notation[2]}

        if notation[0] == '/':
            try:
                result = notation[1] / notation[2]

            except ZeroDivisionError as e:
                print(e)
                return
        elif notation[0] in operations:
            result = operations[notation[0]]

    except(IndexError, ValueError) as e:
        print(e)
        return

    return result


def get_document_data(user_request, *docs_list):
    """ Поиск атрибутов документов по запросу """

    user_names = []
    for document in docs_list:

        try:
            try:
                user_names.append(document[user_request])

            except KeyError:
                print("Поля \"{0}\" в документе нет!".format(user_request))

        except AttributeError:
            print("Неверный формат документа!")
    return '\n'.join(user_names)

if __name__ == "__main__":

    notations = [
        "* 8 5",
        "- 8.2 7",
        "/ 8.345 3",
        "/ -8.345 4",
        "/ 8.345 -4 ", ]

    for n in notations:
        print(process_user_notation(n))

    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]

    print((get_document_data("name", *documents)))
    print((get_document_data("birth_date", *documents)))
