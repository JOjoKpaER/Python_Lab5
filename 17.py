def check_password(func):
    def wrapper():
        if input() == 'password':
            func()
            return True
        else:
            print('Access denied')
            return None
    return wrapper


@check_password
def access():
    print("Access granted")


print(access())
