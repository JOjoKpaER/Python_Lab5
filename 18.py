def check_password(password):



@check_password('123')
def func1():
    print('Grant access to 123')


@check_password('password')
def func2():
    print('Grant access to password')


func1()
func2()
