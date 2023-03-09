from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def open_file():
    file_path = filedialog.askopenfilename()
    data = pd.read_csv(file_path, sep=',', encoding='utf-8')
    label_file.config(text="Выбранный файл: " + file_path)
    # Преобразование даты из строки в объект datetime
    # Удаление столбца "Объём", так как он не используется для прогнозирования
    data.drop('Объём', axis=1, inplace=True)

    # Замена запятых на точки и преобразование данных из строкового в числовой формат
    data['Цена'] = data['Цена'].str.replace(',', '.').astype(float)
    data['Откр.'] = data['Откр.'].str.replace(',', '.').astype(float)
    data['Макс.'] = data['Макс.'].str.replace(',', '.').astype(float)
    data['Мин.'] = data['Мин.'].str.replace(',', '.').astype(float)
    data['Изм. %'] = data['Изм. %'].str.replace(',', '.').str.replace('%', '').astype(float)

    # Удаление строк с отсутствующими значениями
    data.dropna(inplace=True)

    # Нормализация данных
    scaler = MinMaxScaler()
    data[['Цена', 'Откр.', 'Макс.', 'Мин.', 'Изм. %']] = scaler.fit_transform(data[['Цена', 'Откр.', 'Макс.', 'Мин.', 'Изм. %']])

    # Очистка таблицы от старых данных (если такие есть)
    for i in tree.get_children():
        tree.delete(i)

    # Добавление новых данных в таблицу
    for index, row in data.iterrows():
        tree.insert('', 'end', values=(row['Дата'], row['Цена'], row['Откр.'], row['Макс.'], row['Мин.'], row['Изм. %']))

root = Tk()

# Создание таблицы
tree = ttk.Treeview(root, columns=('date', 'price', 'open', 'high', 'low', 'change'), show='headings')

# Настройка заголовков столбцов
tree.column('date', width=120, anchor='center')
tree.column('price', width=100, anchor='center')
tree.column('open', width=100, anchor='center')
tree.column('high', width=100, anchor='center')
tree.column('low', width=100, anchor='center')
tree.column('change', width=100, anchor='center')

tree.heading('date', text='Дата')
tree.heading('price', text='Цена')
tree.heading('open', text='Открытие')
tree.heading('high', text='Максимум')
tree.heading('low', text='Минимум')
tree.heading('change', text='Изменение')

# Создание кнопки для выбора файла
button_file = Button(root, text="Выбрать файл", command=open_file)
button_file.pack(pady=10)

label_file = Label(root, text="")
label_file.pack()


label_result = Label(root, text="")
label_result.pack()

root.mainloop()
