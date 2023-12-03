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
    key = listnotes.selectedItems()[0].text()
    textEdit.setText(notes[key]["текст"])

def add_note():
    note_name, ok = QInputDialog.getText(mv, "Додати замітку", "Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        listnotes.addItem(note_name)
        listtags.addItems(notes[note_name]["теги"])
        print(notes)

def save_note():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        notes[key]["текст"] = textEdit.toPlainText()
        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(notes, file, sort_keys= True, ensure_ascii= False)
    else:
        print("Ви не вибрали замітку!")

def del_note():
    pass

btn_createnote.clicked.connect(add_note)
btn_savenote.clicked.connect(save_note)
listnotes.itemClicked.connect(show_note)

mv.show()
app.exec_()