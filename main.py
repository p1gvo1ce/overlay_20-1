import datetime
# Открываем файл для чтения
with open('ПРОЧИТАЙ МЕНЯ.txt', 'r', encoding='utf-8') as file:
    # Читаем содержание файла
    file_contents = file.read()
# Проверяем наличие строки с "прочитано" в содержании файла
readme_check = False
if 'Прочитано' in file_contents:
    readme_check = True
else:
    # Добавляем строку с "прочитано" в конец файла
    with open('ПРОЧИТАЙ МЕНЯ.txt', 'a', encoding='utf-8') as file:
        new_line = f"Прочитано {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        file.write("\n\n" + new_line)
    print(file_contents)
    input('''\n\nЭту инструкцию ты всегда можешь найти в ПРОЧТИ МЕНЯ.txt в папке с программой
    
    Нажми Enter для продолжения''')
# Выводим содержание файла на экран



# Импорт библиотек
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# импорт прочих библиотек
# импорт графических библиотек
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Путь к файлу JSON с секретами
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'PATCH',
    scopes=['https://www.googleapis.com/auth/spreadsheets'])
gc = gspread.authorize(credentials)

# Класс персонажа
class Survivor:
    def __init__(
            self, name, current_player="", is_alive=True,
            prestige_level_player1=0, prestige_level_player2=0, prestige_level_player3=0, prestige_level_player4=0
    ):
        self.name = name        # Имя персонажа
        self.current_player = current_player        # Актуальный/последний игрок
        self.is_alive = is_alive        # Статус жив/убит
        self.prestige_level_player1 = prestige_level_player1    # Уровень престижа игрока 1
        self.prestige_level_player2 = prestige_level_player2    # Уровень престижа игрока 2
        self.prestige_level_player3 = prestige_level_player3    # Уровень престижа игрока 3
        self.prestige_level_player4 = prestige_level_player4    # Уровень престижа игрока 4

# Класс стримеров
class Streamer:
    def __init__(
            self, name, rank=20, drops=0):
        self.name = name        # Имя стримера
        self.rank = rank       # Актуальный ранг стримера
        self.drops = drops        # Количество капель стримера

# Создание экземпляров стримеров
Hydrodiction = Streamer("Hydrodictyon")
Milka_Evil = Streamer("Milka_Evil")
SakL0n = Streamer("SakL0n")
LuckyT1ger = Streamer("LuckyT1ger")

# Список стримеров
streamers = [Hydrodiction, Milka_Evil, SakL0n, LuckyT1ger]

#создание экземпляров классов персонажей.
Dwight_Fairfield = Survivor("Дуайт Фэйрфилд")
Meg_Thomas = Survivor("Мэг Томас")
Claudette_Morel = Survivor("Клодетт Морель")
Jake_Park = Survivor("Джейк Парк")
Nea_Karlsson = Survivor("Нея Карлссон")
Laurie_Strode = Survivor("Лори Строуд")
Ace_Visconti = Survivor("Эйс Висконти")
William_Overback = Survivor("Уильям Билл Овербек")
Feng_Min = Survivor("Фенг Мин")
David_King = Survivor("Дэвид Кинг")
Quentin_Smith = Survivor("Квентин Смит")
David_Tapp = Survivor("Детектив Тэпп")
Kate_Dansom = Survivor("Кейт Денсон")
Adam_Francis = Survivor("Адам Фрэнсис")
Jeffrey_Johansen = Survivor("Джефф Йохансен")
Jane_Romero = Survivor("Джейн Ромеро")
Ashlley_Williams = Survivor("Эшли Джей Уильямс")
Nancy_Wheeler = Survivor("Стив Харрингтон")
Steve_Harrington = Survivor("Нэнси Уиллер")
Yui_Kimura = Survivor("Юи Кимура")
Zarina_Kassir = Survivor("Зарина Кассир")
Cheryl_Mason = Survivor("Шерил Мейсон")
Felix_Richter = Survivor("Феликс Рихтер")
Elodie_Rakoto = Survivor("Элоди Ракото")
Yun_Jun_Lee = Survivor("Ли Юнчин")
Jull_Valentine = Survivor("Джилл Валентайн")
Leon_Kennedy = Survivor("Леон С. Кеннеди")
Mikaela_Reid = Survivor("Микаэла Рид")
Jonah_Vasques = Survivor("Хонас Васкес")
Yoshi_Asakawa = Survivor("Ёити Асакава")
Haddie_Kapur = Survivor("Хэдди Каур")
Ada_Wong = Survivor("Ада Вонг")
Rebecca_Chambers = Survivor("Ребекка Чемберс")
Vittorio_Toscano = Survivor("Витторио Тоскано")
Thalita_Lyra = Survivor("Талита Лира")
Renato_Lyra = Survivor("Ренато Лира")
Gabriel_Soma = Survivor("Габриэль Сома")
Nicolas_Cage = Survivor("Николас Кейдж")
Ellen_Ripley = Survivor("Эллен Рипли")

# создание списка со всеми экземплярами персонажей
all_survivors = [
    Dwight_Fairfield,
    Meg_Thomas,
    Claudette_Morel,
    Jake_Park,
    Nea_Karlsson,
    Laurie_Strode,
    Ace_Visconti,
    William_Overback,
    Feng_Min,
    David_King,
    Quentin_Smith,
    David_Tapp,
    Kate_Dansom,
    Adam_Francis,
    Jeffrey_Johansen,
    Jane_Romero,
    Ashlley_Williams,
    Nancy_Wheeler,
    Steve_Harrington,
    Yui_Kimura,
    Zarina_Kassir,
    Cheryl_Mason,
    Felix_Richter,
    Elodie_Rakoto,
    Yun_Jun_Lee,
    Jull_Valentine,
    Leon_Kennedy,
    Mikaela_Reid,
    Jonah_Vasques,
    Yoshi_Asakawa,
    Haddie_Kapur,
    Ada_Wong,
    Rebecca_Chambers,
    Vittorio_Toscano,
    Thalita_Lyra,
    Renato_Lyra,
    Gabriel_Soma,
    Nicolas_Cage,
    Ellen_Ripley
    ]

# Заполнение всех экземпляров персонажей и стримеров из гугл таблицы
def vars_update():
    print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\tданные таблицы обновляются')
    # Открываем таблицу по URL
    spreadsheet = gc.open_by_url('LINK')

    # Выбираем лист по имени
    worksheet = spreadsheet.worksheet('Таблица')

    # Получаем все значения из листа
    data = worksheet.get_all_values()

    # Выводим данные
    # Пройдемся по каждой строке данных, начиная с третьей строки (индекс 2)
    for row in data[2:]:
        name = row[0]  # Значение в колонке A (имя персонажа)
        # Ищем соответствующий экземпляр класса в списке all_survivors
        for survivor in all_survivors:
            if survivor.name == name:

                # Обновляем данные экземпляра класса на основе значений в таблице
                survivor.current_player = row[1]  # Значение в колонке B (current_player)
                survivor.is_alive = row[2]  # Значение в колонке C (is_alive)
                try:
                    survivor.prestige_level_player1 = int(row[3])  # Значение в колонке D (prestige_level_player1)
                except:
                    print(f'Ошибка обновления престижей персонажа\n{survivor.name.upper()}\nЗначение "{row[3]}" не является целым числом')
                try:
                    survivor.prestige_level_player2 = int(row[4])  # Значение в колонке E (prestige_level_player2)
                except:
                    print(f'Ошибка обновления престижей персонажа\n{survivor.name.upper()}\nЗначение "{row[4]}" не является целым числом')
                try:
                    survivor.prestige_level_player3 = int(row[5])  # Значение в колонке F (prestige_level_player3)
                except:
                    print(f'Ошибка обновления престижей персонажа\n{survivor.name.upper()}\nЗначение "{row[5]}" не является целым числом')
                try:
                    survivor.prestige_level_player4 = int(row[6])  # Значение в колонке G (prestige_level_player4)
                except:
                    print(f'Ошибка обновления престижей персонажа\n{survivor.name.upper()}\nЗначение "{row[6]}" не является целым числом')

    # Теперь данные экземпляров класса в списке all_survivors обновлены на основе таблицы

    # Пройдемся по каждой строке данных, начиная с третьей строки (индекс 2)
    for row in data[2:6]:
        name = row[8]  # Значение в колонке I (name)
        # Ищем соответствующий экземпляр класса в списке streamers
        for streamer in streamers:
            if streamer.name == name:
                # Обновляем данные экземпляра класса на основе значений в таблице
                try:
                    if int(row[9])<=20 and int(row[9])>0:
                        streamer.rank = int(row[9])  # Значение в колонке J (rank)
                    else:
                        print(f'\n////////\n\nОшибка обновления ранга {streamer.name}\nЗначение "{row[9]}" не соответствует требованиям 1-20\n\n')
                except:
                    print(f'\n////////\n\nОшибка обновления ранга {streamer.name}\nЗначение "{row[9]}" не соответствует требованиям 1-20\n\n')
                try:
                    if int(row[10]) >= 0 and int(row[10]) <=5:
                        streamer.drops = int(row[10])  # Значение в колонке K (drops)
                    else:
                        print(f'\n////////\n\nОшибка пипок ранга {streamer.name}\nЗначение "{row[10]}" не соответствует требованиям 0-5\n\n')
                except:
                    print(f'\n////////\n\nОшибка пипок ранга {streamer.name}\nЗначение "{row[10]}" не соответствует требованиям 0-5\n\n')
    # Теперь данные экземпляров класса в списке streamers обновлены на основе таблицы

    print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\tданные таблицы обновлены')

# Создаем черное изображение для фона
background_image = Image.new('RGBA', (150, 150), (0, 0, 0, 255))

# Обновление портретов выживших
def load_survivor_image(survivor):
    # Подгружаем портрет в зависимости от статуса персонажа жив/убит
    if survivor.is_alive == "TRUE":
        image_path = f"survivors/alive/{survivor.name}.webp"
    else:
        image_path = f"survivors/dead/{survivor.name}.png"
    image = Image.open(image_path)
    image.thumbnail((150, 150))

    # Создаем черное изображение для фона
    background = Image.new('RGBA', (150, 150), (0, 0, 0, 255))

    # Объединяем изображение с черным фоном
    image = Image.alpha_composite(background, image)

    # Создаем изображение для престижей
    prestige_image = Image.new('RGBA', (150, 150))

    # Вставляем изображения престижей
    prestige_levels = [
        survivor.prestige_level_player1,
        survivor.prestige_level_player2,
        survivor.prestige_level_player3,
        survivor.prestige_level_player4
    ]

    for i, prestige_level in enumerate(prestige_levels):
        if prestige_level > 0:
            prestige_image_path = f'streamers_pitures/{i+1}.png'
            prestige_img = Image.open(prestige_image_path)
            prestige_img.thumbnail((25, 25))
            # Устанавливаем точные координаты для вставки изображения престижа
            prestige_image.paste(prestige_img, (20 + 28 * i, 115))

    # Наложение изображения престижей на портрет
    image.paste(prestige_image, (0, 0), prestige_image)

    if survivor.current_player:
        # Масштабирование изображения choise.PNG по ширине
        if survivor.is_alive == 'TRUE':
            text_image = Image.open('other_pictures/choise.PNG')
        else:
            text_image = Image.open('other_pictures/choise_dead.PNG')
        width, height = text_image.size
        new_width = 150  # Ширина, как у портретов
        new_height = int(height * (new_width / width))
        text_image.thumbnail((new_width, new_height))

        # Создаем маску из альфа-канала изображения choise.PNG
        text_mask = text_image.convert('L')  # Преобразуем в оттенки серого
        text_mask = text_mask.point(lambda p: p > 0 and 255)  # Создаем маску

        # Добавление текста с учетом прозрачности
        image.paste(text_image, (1, 1), text_mask)

        # Добавление текста
        draw = ImageDraw.Draw(image)
        # Создаем объект шрифта с указанным шрифтом и размером
        font = ImageFont.truetype("resourses/ofont.ru_Bebas Neue.ttf", 20)  # Выберите шрифт и размер
        text = survivor.current_player
        if survivor.is_alive == 'TRUE':
            text_color = (0, 0, 0)  # Выберите цвет текста (белый в RGB)
        else:

            text_color = (255, 255, 255)  # Выберите цвет текста (белый в RGB)
        text_position = (20, 10)  # Выберите координаты для текста
        draw.text(text_position, text, fill=text_color, font=font)

    photo = ImageTk.PhotoImage(image)
    return photo

# Обновление табличек стримеров
def load_streamer_image(streamer):
    # Загрузить фоновое изображение
    background = Image.open("ranks/bg.png")
    background.thumbnail((200, 200))
    load_ok = False
    # Создайте изображение с иконкой ранга + обработка ошибок ввода
    try:
        rank_icon = Image.open(f"ranks/{streamer.rank}.png")
        rank_icon.thumbnail((90, 90))
        if streamer.drops > 0:
            pips_icon = Image.open(f"ranks/pip{streamer.drops}.png")
            pips_icon.thumbnail((90, 90))
        load_ok = True
    except:
        print(f'Ошибка загрузки ранга {streamer.name}\nРанг {streamer.rank}\nКапли {streamer.drops}')


    # Создём изображение с именем стримера
    name_image = Image.new('RGBA', (200, 50))
    draw = ImageDraw.Draw(name_image)
    font = ImageFont.truetype("resourses/ofont.ru_Bebas Neue.ttf", 25)
    # Задаём цвет текста в зависимости от ранга
    if streamer.rank > 16:
        text_color = (63, 64, 63)
    if streamer.rank <17:
        text_color = (167, 71, 52)
    if streamer.rank <13:
        text_color = (181, 175, 171)
    if streamer.rank <9:
        text_color = (255, 168, 2)
    if streamer.rank < 5:
        text_color = (255, 6, 12)
    text_position = (5, 5)
    draw.text(text_position, streamer.name, fill=text_color, font=font)

    # Наложение иконки ранга на фон
    if load_ok:
        background.paste(rank_icon, (10, 10))
    # Наложение иконки капель на фон
    if streamer.drops > 0 and load_ok:
        background.paste(pips_icon, (100, 55))

    # Наложение изображения с именем
    background.paste(name_image, (10, 95))

    photo = ImageTk.PhotoImage(background)
    return photo

# Вывод таблицы на экран и обновление данных
def display_survivors():
    def update_images():
        # Обновляем данные
        vars_update()

        # Очищаем предыдущие изображения
        for widget in frame.winfo_children():
            widget.destroy()

        row = 0
        col = 0

        for survivor in all_survivors:
            photo = load_survivor_image(survivor)
            label = tk.Label(frame, image=photo, bg="black")  # Установите черный фон
            label.photo = photo
            label.grid(row=row, column=col)

            col += 1
            if col == 8:
                col = 0
                row += 1
        col = 0
        row += 1
        for streamer in streamers:
            photo = load_streamer_image(streamer)
            label = tk.Label(frame, image=photo, bg="black")
            label.photo = photo
            label.grid(row=row, column=col)

            col += 2
            if col == 8:
                col = 0
                row += 1
        # Запустить таймер снова через 5 секунд
        root.after(5000, update_images)

    root = tk.Tk()
    root.title("Survivors")
    root.geometry("1920x1920")  # Установливаем разрешение окна
    frame = tk.Frame(root, bg="black")  # Установите черный фон для frame
    frame.pack()
    update_images()  # Первоначальное обновление изображений

    root.mainloop()

# Запуск отрисовки таблицы
display_survivors()