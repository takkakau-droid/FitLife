# Проект FitLife - MVP версия 1.0
print("Привет! Я FitLife-бот, твой помощник в заботе о здоровье!")
print("Давай познакомимся.\n")

# Константы
WATER_PER_KG = 30
ML_PER_LITER = 1000
SEPARATOR = "=" * 40

# 1. Знакомство
while True:
    user_name = input("Как тебя зовут? ")
    if user_name.strip():
        break
    print("Имя не может быть пустым. Попробуй ещё раз.")

while True:
    try:
        user_age = int(input("Сколько тебе лет? "))
        break
    except ValueError:
        print("Пожалуйста, введи число.")

# 2. Сбор данных
while True:
    try:
        user_weight = float(input("Введи свой вес (в кг, например 75.5): "))
        if user_weight > 0:
            break
        print("Вес должен быть положительным числом.")
    except ValueError:
        print("Пожалуйста, введи число.")

while True:
    try:
        user_height = float(
            input("Введи свой рост (в метрах, например 1.75): ")
        )
        if user_height > 0:
            break
        print("Рост должен быть положительным числом.")
    except ValueError:
        print("Пожалуйста, введи число.")

# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

# Выбор категории ИМТ
if bmi_rounded < 18.5:
    bmi_category = "недостаточная масса тела"
elif bmi_rounded < 25:
    bmi_category = "норма"
elif bmi_rounded < 30:
    bmi_category = "избыточная масса тела"
else:
    bmi_category = "ожирение"

water_ml = user_weight * WATER_PER_KG
water_needed = round(water_ml / ML_PER_LITER, 1)

# 4. Вывод красивого результата
print(SEPARATOR)
print("           ПЕРСОНАЛЬНЫЙ ОТЧЁТ")
print(SEPARATOR)
print(f"Имя: {user_name}")
print(f"Возраст: {user_age} лет")
print(f"Вес: {user_weight} кг")
print(f"Рост: {user_height} м")
print(SEPARATOR)
print(f"Индекс массы тела (ИМТ): {bmi_rounded} ({bmi_category})")
print(f"Рекомендуемая норма воды: {water_needed} л в день")
print(SEPARATOR)
print("Расчёт окончен. Будьте здоровы!")
