import cv2
from PIL import Image
 
image_path = "c:/Users/Asus/Desktop/git/urok1/cat2.jpg"
cascade_path = 'c:/Users/Asus/Desktop/git/urok1/haarcascade_frontalcatface_extended.xml'
glasses_path = 'c:/Users/Asus/Desktop/git/urok1/glasses.png'
 
image = cv2.imread(image_path)
if image is None:
    print("ПОМИЛКА: Зображення не завантажено! Перевірте шлях до файлу.")
    exit()
else:
    print(f"Зображення завантажено. Розмір: {image.shape}")
 
cat_face_cascade = cv2.CascadeClassifier(cascade_path)
if cat_face_cascade.empty():
    print("ПОМИЛКА: XML-файл каскаду не завантажено! Перевірте шлях.")
    exit()
else:
    print("Каскад завантажено успішно")
 
cat_face = cat_face_cascade.detectMultiScale(image)
 
print(f"Знайдено мордочок котів: {len(cat_face)}")
print(f"Координати: {cat_face}")
 
cat = Image.open(image_path)
glasses = Image.open(glasses_path)
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
 
for (x, y, w, h) in cat_face:
    glasses_resized = glasses.resize((w, int(h/3)))
    cat.paste(glasses_resized, (x, int(y + h/4)), glasses_resized)
 
output_path = 'c:/Users/Asus/Desktop/git/urok1/cat_with_glasses2.png'
cat.save(output_path)
 
cat_with_glasses = cv2.imread(output_path)
cv2.imshow("Cat_with_glasses", cat_with_glasses)
cv2.waitKey()
cv2.destroyAllWindows()