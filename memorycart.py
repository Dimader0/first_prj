from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox


app = QApplication([])

def win():
    ms_win = QMessageBox()
    ms_win.setText("правильно")
    ms_win.exec_()

def lose():
    ms_lose = QMessageBox()
    ms_lose.setText("неправильно")
    ms_lose.exec_()

mw = QWidget()
mw.resize(500, 400)
mw.setWindowTitle('Memorycard')

question = QLabel("Quest ???")
rb1 = QRadioButton("ans1")
rb2 = QRadioButton("ans2")
rb3 = QRadioButton("ans3")
rb4 = QRadioButton("ans4")

main_layout = QVBoxLayout()
h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()

h2_layout.addWidget(rb1, alignment=Qt.AlignCenter)
h2_layout.addWidget(rb2, alignment=Qt.AlignCenter)
h1_layout.addWidget(rb3, alignment=Qt.AlignCenter)
h1_layout.addWidget(rb4, alignment=Qt.AlignCenter)

main_layout.addWidget(question, alignment=Qt.AlignCenter)
main_layout.addLayout(h2_layout)
main_layout.addLayout(h1_layout)

mw.setLayout(main_layout)

rb1.clicked.connect(win)
rb2.clicked.connect(lose)
rb3.clicked.connect(lose)
rb3.clicked.connect(lose)

mw.show()
app.exec_()