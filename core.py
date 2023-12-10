from main import*
import json

notes = dict()
messange = QMessageBox()

try:
    with open("data.json", "r", encoding= "utf-8") as file:
        notes = json.load(file)
    listnotes.addItems(notes)
except:
    print("Такого файлу не існує!")
    messange.setWindowTitle("Назва файлу")
    messange.setText("Такого файлу не існує!")
    messange.exec_()

def show_note():
    textEdit.clear()
    listtags.clear()
    key = listnotes.selectedItems()[0].text() # отримати назву замітки, текст якої треба відобразити
    textEdit.setText(notes[key]["текст"]) # за ключами отримати текст замітки і вставити її у віджет
    listtags.addItems(notes[key]["теги"])

def add_note():
    note_name, ok = QInputDialog.getText(mv, "Додати замітку", "Назва замітки") # діалогове вікно створення нової замітки
    if ok and note_name != "": # чи ми ввели назву замітки і натистули ок
        notes[note_name] = {"текст": "", "теги": []} # створюється структура замітки з назвою
        listnotes.addItem(note_name) # назва замітки поміщається у віджет списку заміток
        listtags.addItems(notes[note_name]["теги"]) # теги замітки поміщаються у спимок тегів

def save_note():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text() # отримуємо назву замітки, яку ми обрали
        notes[key]["текст"] = textEdit.toPlainText() # отримуємо текст замітки
        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку!")
        messange.setWindowTitle("Назва замітки")
        messange.setText("Ви не вибрали замітку!")
        messange.exec_()

def del_note():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        del notes[key] # видаляємо елемент словника за ключем
        # чистимо віджети
        listnotes.clear()
        textEdit.clear()
        listtags.clear()
        # оновлюємо віджет новими даними
        listnotes.addItems(notes)
        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку!")
        messange.setWindowTitle("Назва замітки")
        messange.setText("Ви не вибрали замітку!")
        messange.exec_()

def add_tag():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        tag = lineEdit.text() # новий тег
        if not tag in notes[key]["теги"]: # перевірка наявності тегу в списку тегів
            notes[key]["теги"].append(tag) # Додаємо в кінець новий тег
            listtags.addItem(tag) # додаємо у віджет новий тег
            lineEdit.clear()
            with open("data.json", "w", encoding= "utf-8") as file:
                json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку для додавання тега!")
        messange.setWindowTitle("Назва замітки")
        messange.setText("Ви не вибрали замітку для додавання тега!")
        messange.exec_()

def del_tag():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text() # отримуємо назву замітки
        tag = listtags.selectedItems()[0].text() # отримуємо назву тегу
        notes[key]["теги"].remove(tag) # видаляємо тег з словника
        listtags.clear()
        listtags.addItems(notes[key]["теги"]) # додавання заміток у віджет з оновленими тегами
        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку для видалення тегу!")
        messange.setWindowTitle("Назва замітки")
        messange.setText("Ви не вибрали замітку для видалення тегу!")
        messange.exec_()

def search_tag():
    tag = lineEdit.text() # отримуємо назву тегу
    if btn_searchtag.text() == "Шукати замітки по тегу" and tag: # перевірка введення тегу
        note_filtered = dict() # словник відфільтрованих заміток
        for note in notes: # перебираємо всі замітки у словнику
            if tag in notes[note]["теги"]: # якщо знашли тег то записуємо записуємо замітку у новий словник 
                note_filtered[note] = notes[note]
        btn_searchtag.setText("Скинути пошук")
        listnotes.clear()
        listtags.clear()
        listnotes.addItems(note_filtered) # додаємо список відфільтрованих заміток
    elif btn_searchtag.text() == "Скинути пошук":
        lineEdit.clear()
        listnotes.clear()
        listtags.clear()
        listnotes.addItems(notes) # додаємо всі замітки до віджетів
        btn_searchtag.setText("Шукати замітки по тегу")
    elif tag == "":
        messange.setWindowTitle("Назва тега")
        messange.setText("Ви не ввели тег для пошуку")
        messange.exec_()

def save_in_txt():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        index = 1
        for note in notes:
            if note[0] == key:
                text = textEdit.toPlainText()
                with open(str(index)+".txt", "w", encoding= "utf-8") as file:
                    file.write(note[0]+"\n")
                    file.write(text+"\n")
                    for tag in notes[key]["теги"]:
                        file.write(tag+" ")
                    file.write("\n")
            index += 1
    else:
        print("Ви не вибрали замітку!")
        messange.setWindowTitle("Назва замітки")
        messange.setText("Ви не вибрали замітку для збереження!")
        messange.exec_()


btn_save_to_txt.clicked.connect(save_in_txt)
btn_searchtag.clicked.connect(search_tag)
btn_createnote.clicked.connect(add_note)
btn_savenote.clicked.connect(save_note)
btn_delitenote.clicked.connect(del_note)
listnotes.itemClicked.connect(show_note)
btn_addtonote.clicked.connect(add_tag)
btn_unpickfromnote.clicked.connect(del_tag)

mv.show()
app.exec_()