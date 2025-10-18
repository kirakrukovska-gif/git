import logging 
logging.basicConfig(
    filename="trace.log",
    filemode="w",
    level=logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def login(username, password):
    correct_username = "Kira"
    correct_password = "1414"

    try:
        logging.debug(f"Спроба входу користувача {username}")
        assert username == correct_username and password == correct_password, "Невірна назва або пароль користувача" 
        print("Вхід виконано успішно!")
        logging.info(f"Успішний вхід користувача {username}")
    except Exception as e:
        print(e)
        logging.exception(f"Помилка при вході користувача {username}: {e}")

login("Kira", "1414")
login("Olya", "1030")


