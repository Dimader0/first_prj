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
    key = listnotes.selectedItems()[0].text() # отримати назву замітки, текст якої треба відобразити
    textEdit.setText(notes[key]["текст"]) # за ключами отримати текст замітки і вставити її у віджет

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

btn_createnote.clicked.connect(add_note)
btn_savenote.clicked.connect(save_note)
btn_delitenote.clicked.connect(del_note)
listnotes.itemClicked.connect(show_note)
btn_addtonote.clicked.connect(add_tag)

mv.show()
app.exec_()