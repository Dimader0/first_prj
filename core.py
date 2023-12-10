from main import*
import json

notes = dict()

try:
    with open("data.json", "r", encoding= "utf-8") as file:
        notes = json.load(file)
    listnotes.addItems(notes)
except:
    print("Такого файлу не існує!")

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
        print(notes)

def save_note():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text() # отримуємо назву замітки, яку ми обрали
        notes[key]["текст"] = textEdit.toPlainText() # отримуємо текст замітки
        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку!")

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

def del_tag():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        tag = listtags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        listtags.clear()
        listtags.addItems(notes[key]["теги"])
        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку для видалення тегу!")

def search_tag():
    tag = lineEdit.text()
    if btn_searchtag.text() == "Шукати замітки по тегу" and tag:
        note_filtered = dict()
        for note in notes:
            if tag in notes[note]["теги"]:
                note_filtered[note] = notes[note]
        btn_searchtag.setText("Скинути пошук")
        listnotes.clear()
        listtags.clear()
        listnotes.addItems(note_filtered)

    elif btn_searchtag.text() == "Скинути пошук":
        lineEdit.clear()
        listnotes.clear()
        listtags.clear()
        listnotes.addItems(notes)
        btn_searchtag.setText("Шукати замітки по тегу")
        

btn_searchtag.clicked.connect(search_tag)
btn_createnote.clicked.connect(add_note)
btn_savenote.clicked.connect(save_note)
btn_delitenote.clicked.connect(del_note)
listnotes.itemClicked.connect(show_note)
btn_addtonote.clicked.connect(add_tag)
btn_unpickfromnote.clicked.connect(del_tag)

mv.show()
app.exec_()