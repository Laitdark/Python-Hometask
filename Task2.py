def showuserinfo(**userinfo):
    print("Информация о пользователе:" , userinfo)


username = input("Введите ваше имя: ")
usersurname = input("Введите вашу фамилию: ")
useryear = input("Введите год вашего рождения: ")
usercity = input("Введите ваш город проживания: ")
userphone = input("Введите ваш номер телефона: ")
useremail = input("Введите ваш Email: ")

showuserinfo(name=username, surname=usersurname, year=useryear, city=usercity, phone=userphone, email=useremail)
