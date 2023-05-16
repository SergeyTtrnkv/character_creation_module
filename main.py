from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Возращает строку с посчетом урона нанесенным персонажем."""
    if char_class == 'warrior':
        return (f'{char_name} нанес противнику {5 + randint(3, 5)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} нанес противнику {5 + randint(5, 10)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} нанес '
                f'противнику {5 + randint(-3, -1)} ед. урона')
    return (f'{char_name} не нанес урона противнику')


def defence(char_name: str, char_class: str) -> str:
    """Возвращает строку с подсчетом блокированного урона."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')
    return (f'{char_name} не пришлось блокировать урон со стороны противника')


def special(char_name: str, char_class: str) -> str:
    """Возращает строку со специальным умением."""
    if char_class == 'warrior':
        return (f'{char_name} применил спецумение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил спецумение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил спецумение «Защита {10 + 30}»')
    return ('f{char_name} спецумений не применял')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи:'
          'attack — для атаки противника;'
          'defence — для блокировки атаки;'
          'special — для применения спецспособности.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Возвращает описание вида персонажа при выборе."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior,'
                           'Маг — mage, Лекарь — healer:')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.'
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.'
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.'
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


# main()
