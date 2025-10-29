import logging
import cv2 
import random


print("------------Привіт! Вас вітає приватна вікторина------------------")
print("        Зараз ти спробуєш свої знання в програмуванні")
print("  ")
print("    Але перед цим звісно ж пройди перевірку на скан обличчя")
print("  ")

logging.basicConfig(
    level=logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
  
class FacePhoto:
    def __init__(self,image_path= "c:/Users/Asus/Desktop/git/urok1/face.jpg"):
        self.image_path = image_path

    def detect_user(self):
        import os
        if not os.path.exists(self.image_path):
            print("ПОМИЛКА: Файл не знайдено!")
            return False
        
        image = cv2.imread(self.image_path)
        if image is None:
            print("ПОМИЛКА: Неможливо завантажити зображення!")
            return False
        print("Ваше обличчя знайдено в базі.")
        return True
    

def quiz_questions():
    questions = [
        ('1. Яка мова програмування використовується у цьому коді?' , 'Python'),
        ('2. Яка бібліотека використовується з фото?' , 'cv2'),
        ('3. Як називається функція, яка створює послідовність у Python?' , 'range'),
        ('4. Як називається цикл, який виконується, поки умова істинна?', 'while'),
        ('5. Яке ключове слово використовується для створення функції?', 'def')
        ]
    for q,a in questions:
        yield q, a

def main():
    allowed_users = ["Alice", "Kira", "Bob", "Andrew"]
    user_name = input("Як тебе звати? ")

    if user_name in allowed_users:
        print(f"Перевірка, {user_name}")
    else:
        print(f"Вибач {user_name}! Такого імені немає в списку( ")
        print("Перевіримо фото або виберемо випадкове ім'я")

    photo = FacePhoto("c:/Users/Asus/Desktop/git/urok1/face.jpg")
    detected = photo.detect_user()

    if not detected:
        fallback_users = ["Alice", "Kira", "Bob", "Andrew"]
        user_name = random.choice(fallback_users)
        print(f"Використовуємо запасне ім'я: {user_name}")

    print(f"Вітаю, {user_name}! ")
    print("Починаємо через 3... 2... 1... ")

    score = 0
    for q, a in quiz_questions():
        print(q)
        user_answer=input("Твоя відповідь: ")

        if user_answer.lower() == a.lower():
            print("Молодець. Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильна відповідь: {a}")
    print(f"Твій результат: {score}/5 балів")
    logging.info(f"Користувач {user_name} завершив вікторину з результатом {score}/5 балів")
                  

if __name__ == "__main__":
    try:
        main()
    except NameError as e:
        print("Виникла помилка", e)
    except Exception as e:
        print("Непередбаченна помилка", e)





