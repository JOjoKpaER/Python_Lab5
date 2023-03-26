def ask_password(login, password, success, failure):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_n = 0
    consonant_in_lgn = True
    for i in password:
        if i in vowels:
            vowels_n += 1
        else:
            if i not in login:
                consonant_in_lgn = False
    for i in login:
        if i not in vowels:
            if i not in password:
                consonant_in_lgn = False
    if vowels_n == 3 and consonant_in_lgn:
        success(login)
        return
    if vowels_n != 3 and not consonant_in_lgn:
        failure(login, "Everything is wrong")
        return
    if vowels_n != 3:
        failure(login, "Wrong number of vowels")
        return
    if not consonant_in_lgn:
        failure(login, "Wrong consonants")
        return


def main(login, password):
    ask_password(login, password,
                 lambda log: print("Привет,", log),
                 lambda log, err:
                 print("Кто-то пытался притвориться пользователем",
                       log,
                       "но в пароле допустил ошибку:",
                       err.upper()))


main("anastasia", "nsyatos")
main("eugene", "anig")
main("eugene", "amig")
main("eugene", "amigo")
ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))
