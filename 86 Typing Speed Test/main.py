import random
import datetime
import json
from tkinter import *


words = None

window = Tk()
window.title("Type Speed Test")
window.geometry("1200x1000")

### GUI ###

def get_words(lang, lenght, type):
    lenght = int(lenght)
    if type == "Words":
        num_of_words = lenght
    elif type == "Seconds":
        num_of_words = 4.5 * lenght
    elif type == "Minutes":
        num_of_words =  250 * lenght
    num_of_words = int(num_of_words)
    lang = lang.lower()

    dict = open(f"static/{lang}.json")
    data = json.load(dict)
    all_words = data["words"]
    words = [random.choice(all_words) for _ in range(num_of_words)]

    return words

# Language
language_label = Label(window, text="Select Language:")
language_label.grid(row=0, column=0)

variable_lang = StringVar(window)
variable_lang.set("English")

language_menu = OptionMenu(window, variable_lang, "English", "Polish", "German")
language_menu.grid(row=1, column=0)

# Words/Minutes
type_label = Label(text="Words or Time:")
type_label.grid(row=0, column=1)

variable_type = StringVar(window)
variable_type.set("Words")

test_type = OptionMenu(window, variable_type, "Minutes", "Seconds", "Words")
test_type.grid(row=1, column=1)

# Number of Words / Time
lenght_label = Label(text="How many words/how long do you want to type:")
lenght_label.grid(row=0, column=2)

lenght_of_test = Entry()
lenght_of_test.grid(row=1, column=2)
lenght_of_test.insert(END, "1")   #!Add 15

# Submit Settings
def ok():
    global words
    lang = variable_lang.get()
    type_of_test = variable_type.get()
    lenght = lenght_of_test.get()
    words = get_words(lang, lenght, type_of_test)
    
    words_to_type.config(state=NORMAL)
    words_to_type.delete("1.0", END)
    words_to_type.insert(END, words)
    words_to_type.config(state=DISABLED)

button = Button(window, text="OK", command=ok)
button.grid(row=1, column=3)

# WPM and ACC labels


wpm_label = Label(text="WPM=0", pady=30)
wpm_label.grid(row=2, column=0, columnspan=2)

acc_label = Label(text="ACC=0", pady=30)
acc_label.grid(row=2, column=2, columnspan=2)

# Words to type area

words_to_type = Text(width=80)
words_to_type.insert(END, "Words to type")
words_to_type.config(state=DISABLED, wrap=WORD)
words_to_type.grid(row=3, column=0, columnspan=4)

# Type Area

type_area = Text(width=130)
type_area.grid(row=4, column=0, columnspan=4, pady=60, padx=20)


def start_typing(time_start):
    global words
    button.config(state=DISABLED)
    if words == None:
        ok()
    typed_words = type_area.get("1.0", END)
    typed_words_as_list = typed_words.split()
    if len(words) == len(typed_words_as_list) and words[-1] == typed_words_as_list[-1]:
        time_end = datetime.datetime.now()
        time = time_end - time_start
        time = time.total_seconds()
        time = round(time, 1)


        char_in_words = len(typed_words) - 1
        wpm = char_in_words * 60 / 5 / time
        wpm = round(wpm, 2)
        wpm_label.config(text=f"WPM={wpm}")

        number_of_letters = 0
        good_letters = []
        for word_id in range(len(words)):
            for letter_id in range(len(words[word_id])):
                number_of_letters += 1
                try:
                    if words[word_id][letter_id] == typed_words_as_list[word_id][letter_id]:
                        good_letters.append(words[word_id][letter_id])
                except:
                    pass
        number_of_good_letters = len(good_letters)
        print(number_of_letters)
        print(number_of_good_letters)
        acc = round(100 - (((number_of_letters-number_of_good_letters)/number_of_letters) * 100), 2)
        acc_label.config(text=f"ACC={acc}%")

    else:
        window.after(50, start_typing, time_start)


started = False
def check_time(event):
    global started
    if not started:
        started = True
        time_start = datetime.datetime.now()
        window.after(200, start_typing, time_start)
        

type_area.bind("<Any-KeyPress>", check_time)


window.mainloop()