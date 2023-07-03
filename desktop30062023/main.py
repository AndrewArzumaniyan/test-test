from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QMessageBox
from random import randint

app = QApplication([]) # создаем приложение
mw = QWidget() # создаем главное окно

mw.setWindowTitle('Quiz') # устанавливаем заголов для главного окна
mw.resize(500, 300) # изменяем размер главного окна
mw.move(600, 500) # перемещаем главное окно от центра на 600 вправо и 500 вверх

question = QLabel('В каком году появилась Алгоритмика?')
btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

main_layout = QVBoxLayout()
main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

def show_win():
  mes = QMessageBox()
  mes.setText('Правильно!')
  mes.exec_()

def show_lose():
  pass # пишем дома

btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)

mw.setLayout(main_layout)

mw.show() # отображаем окно
app.exec_() # позволяем закрыть приложение при нажатии на крестик