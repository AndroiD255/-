def проверка_числа():
    try:
        int(число.get())
        return True
    except ValueError:
        messagebox.showinfo('Fatal ERROR', 'Число?')
        кнопка_повтора.pack(expand=True, fill=BOTH)


def ок():
    пояснение.pack_forget()
    сбор_вводных_данных.pack_forget()
    кнопка_ок.pack_forget()
    if валюта.get() == "RUB":
        проверка_числа()
        преобразование = int(число.get()) * 0.014
        преобразование = str(число.get()) + " RUB = " + str(преобразование) + " USD"
        вывод = Label(window, bg="black", fg="white", text=преобразование)
        вывод.pack()
        fail = open('История конвертера валют.txt', 'a')
        fail.write("\n" + now.strftime("%d.%m.%Y %H:%M") + " : " + преобразование)
        fail.close()

    elif валюта.get() == "USD":
        проверка_числа()
        преобразование = int(число.get()) / 0.014
        преобразование = str(число.get()) + " USD = " + str(преобразование) + " RUB"
        вывод = Label(window, bg="black", fg="white", text=преобразование)
        вывод.pack()
        fail = open('История конвертера валют.txt', 'a')
        fail.write("\n" + now.strftime("%d.%m.%Y %H:%M") + " : " + преобразование)
        fail.close()

    else:
        messagebox.showinfo('Fatal ERROR', 'А валюту выбрать?')
    кнопка_повтора.pack(expand=True, fill=BOTH)


def пис():
    кнопка_повтора.pack_forget()
    пояснение.pack(fill=X)
    сбор_вводных_данных.pack()
    кнопка_ок.pack(fill=X)


def начать():
    первоначальная_кнопка.destroy()
    пис()


from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import *
now = datetime.now()
current_time = now.strftime("%d-%m-%Y %H:%M")

window = Tk()
window["bg"] = "black"
window.title("Конвентер рублей в доллары и назад.")
window.attributes('-fullscreen', True)

закрыть = Label(window, bg="black", fg="white", text="Чтобы закрыть окно нажите Alt+F4.")
закрыть.pack()
тд = Label(window, bg="black", fg="white", text="Текущая дата и время:")
тд.pack()
дмгчм = Label(window, bg="black", fg="white", text=now.strftime("%d-%m-%Y %H:%M"))
дмгчм.pack()

первоначальная_кнопка = Button(master=window, bg="black", fg="white", text="Начать", command=начать)
первоначальная_кнопка.pack(expand=True, fill=BOTH)

пояснение = Label(window, bg="black", fg="white", text="Введите необходиое число, выберите валюту и нажмите ОК.")
пояснение.pack_forget()
сбор_вводных_данных = Frame(relief=SUNKEN, bg="black", borderwidth=3)
сбор_вводных_данных.pack_forget()
число = Entry(master=сбор_вводных_данных, bg="grey", fg="white", width=8)
число.grid(column=0, row=1)
валюта = Combobox(master=сбор_вводных_данных, background="grey", foreground="white", width=7)
валюта['values'] = ("RUB", "USD")
валюта.grid(column=1, row=1)
кнопка_ок = Button(master=window, bg="black", fg="white", text="ОК", command=ок)
кнопка_ок.pack_forget()
кнопка_повтора = Button(master=window, bg="black", fg="white", text="Ещё раз", command=пис)
кнопка_повтора.pack_forget()

window.mainloop()
