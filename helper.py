#1 Загрузка данных из CSV-файла с помощью библиотеки Pandas:

import pandas as pd

data = pd.read_csv('prices.csv')

# Вывод первых 5 строк данных для проверки
print(data.head())

#2 Создание нейронной сети с помощью библиотеки TensorFlow

import tensorflow as tf

model = tf.keras.Sequential([
  tf.keras.layers.Dense(256, activation='relu'),
  tf.keras.layers.Dense(256, activation='relu'),
  tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])
#3 Разделение данных на обучающую и тестовую выборки с помощью функции train_test_split из библиотеки sklearn

from sklearn.model_selection import train_test_split

train_data, test_data, train_targets, test_targets = train_test_split(
    data.drop(columns=['target']), 
    data['target'], 
    test_size=0.2, 
    random_state=42
)

#4 Обучение нейронной сети

history = model.fit(
    train_data, train_targets,
    batch_size=100,
    epochs=100,
    validation_data=(test_data, test_targets)
)

#5 Использование нейронной сети для прогнозирования цен активов

predictions = model.predict(test_data)

#6 Определение момента выставления ордеров на покупку и продажу активов на основе прогноза цен
#7 Закрытие сделок для получения максимальной прибыли
#8 Создание графического интерфейса с помощью библиотеки PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Прогнозирование цен активов")
        self.resize(400, 200)

        self.label = QLabel("Введите параметры нейронной сети:")
        self.input1_label = QLabel("Количество эпох обучения:")
        self.input1 = QLineEdit()
        self.input2_label = QLabel("Размер обучающего набора данных:")
        self.input2 = QLineEdit()
        self.input3_label = QLabel("Размер проверочного набора данных:")
        self.input3 = QLineEdit()
        self.input4_label = QLabel("Размер тестового набора данных:")
        self.input4 = QLineEdit()
        self.button = QPushButton("Обучить")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input
