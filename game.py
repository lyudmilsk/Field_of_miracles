import random

mylist = ["apple", "banana", "cherry"]


def game(m_list: list):
    sl = random.choice(m_list)
    k = len(sl)
    p1 = list('*' * k)
    print('Розпочинаємо гру. У вас  5 спроб ')
    print('відгадайте слово: ', p1)
    for i in range(5):
        if '*' in p1:
            b = input('введіть букву або слово: ')
            if len(b) == k:
                if b == sl:
                    print('Вітаю, ви відгадали слово')
                    break
                else:
                   print('не вірно - спробуй ще!')
            elif len(b) != 1:
                print(f'або слово {k} букв, або 1 букву')
            else:
                if b in sl:
                    x = 0
                    while x in range(k):
                        m = sl.find(b, x, k)
                        if m == -1:
                            break
                        x = m + 1

                        p1[m] = b
                    print(f'є така буква, у вас  ще спроб {4 - i} ')
                    print(p1)

                    continue
                else:
                    print(f'такої букви немає, спроб залишилося {4-i} ')
                    print(p1)
                    continue
        else:
            print('Вітаю, ви відгадали слово!')
            print(p1)
        break

print('Нажаль, спроби закінчилися. Невдача - наступним, разам повезе ')


game(mylist)