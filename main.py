from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget,
                             QTextEdit, QLineEdit, QMessageBox, QInputDialog)

app = QApplication([])
mv = QWidget()
mv.resize(900, 700)
mv.setWindowTitle("Замітки")

textEdit = QTextEdit()
listnotes = QListWidget()
listtags = QListWidget()
inputtag = QLineEdit()
labelnotes = QLabel("Список заміток")
labeltags = QLabel("Список тегів")

btn_save_to_txt = QPushButton("Зберегти в txt")
btn_createnote = QPushButton("Створити замітку")
btn_savenote = QPushButton("Зберегти замітку")
btn_delitenote = QPushButton("Видалити замітку")
btn_addtonote = QPushButton("Додати до замітки")
btn_unpickfromnote = QPushButton("Відкріпити від замітки")
btn_searchtag = QPushButton("Шукати замітки по тегу")

lineEdit = QLineEdit("")
lineEdit.setPlaceholderText("Введіть тег...")

layout_notes = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(textEdit)

col_2 = QVBoxLayout()
col_2.addWidget(labelnotes)
col_2.addWidget(listnotes)

row_1 = QHBoxLayout()
row_1.addWidget(btn_createnote)
row_1.addWidget(btn_delitenote)

row_2 = QHBoxLayout()
row_2.addWidget(btn_savenote)
row_2.addWidget(btn_save_to_txt)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(labeltags)
col_2.addWidget(listtags)
col_2.addWidget(lineEdit)

row_3 = QHBoxLayout()
row_3.addWidget(btn_addtonote)
row_3.addWidget(btn_unpickfromnote)

row_4 = QHBoxLayout()
row_4.addWidget(btn_searchtag)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch= 2)
layout_notes.addLayout(col_2, stretch= 1)

mv.setLayout(layout_notes)

