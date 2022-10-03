import math


def mainLogic():
    phi_list = list(map(float, input("Введите вероятности появления символов в сообщении (через пробел):\n").split()))
    i = int(input("Введите длину элементарного сообщения:\n"))
    m = int(input("Введите мощность алфавита:\n"))
    n_i = int(input("Введите ni (количество символов):\n"))

    entropy = 0

    for phi in phi_list:
        entropy += - phi * math.log(phi, 2)

    n_min = entropy / math.log(m, 2)

    print("\nЭнтропия сообщения равна: {0} [биты]".format(entropy))
    print("Средняя длина кодовой комбинации равна: {0} [буквы]".format(n_min))

    if n_min == n_i:
        print("Используемый способ кодирования наиболее эффективен.")
    else:
        print("Используемый способ кодирования избыточен.")
        print("Избыточность используемого алфавита равна: {:0.2f} %".format((n_i - n_min) * 100 / n_i))
        print("Длина сообщения при эффективном кодировании равна: {0} [буквы]".format(i * n_min))

    print("Длина сообщения при выбранном способе кодирования равна: {0} [буквы]".format(i * n_i))


if __name__ == '__main__':
    mainLogic()
