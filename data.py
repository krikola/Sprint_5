
class Urls:

    #Базовый URL
    BASE_URL = 'https://stellarburgers.education-services.ru'

    #URL используемые в тестах
    main_url = BASE_URL + '/'                                  #Главная страница
    login_url = BASE_URL + '/login'                            #Страница авторизации
    register_url = BASE_URL + '/register'                      #Страница регистрации
    profile_url = BASE_URL + '/account/profile'                #Страница профиля
    forgot_url = BASE_URL + '/forgot-password'                 #Страница восстановления пароля

class Test_User:
#данные тестового пользователя
    test_user_name = 'Nicl_Val'
    test_user_email = 'Valishin_Nickolai_41_666@yandex.ru'
    test_user_password = 'ValNick41'
