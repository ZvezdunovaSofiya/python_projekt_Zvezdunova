# дано двузначное число.Найдите сумму и произвидение его цифр
while True:
    try:
        num = int(input("Введите двузначное число: "))
        # Проверяем диапазон
        if 10 <= num <= 99:
            break
        else:
            print("Ошибка: число должно быть двузначным.")
    except ValueError:
        print("Ошибка: введите целое число!")

# Вычисления
summa = (num // 10) + (num % 10)
proizvedenie = (num // 10) * (num % 10)
print("Сумма цифр:", summa)
print("Произведение:", proizvedenie)