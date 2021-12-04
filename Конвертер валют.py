def checkint():
    try:
        int(ent_int.get())
        return True
    except ValueError:
        messagebox.showinfo('Fatal ERROR', 'Число?')
        btn_restart.pack(expand=True, fill=BOTH)

def ok():
    frm_entry.pack_forget()
    if combo.get() == "RUB":
        checkint()
        calc = int(ent_int.get()) * 0.014
        string = str(ent_int.get()) + " RUB = " + str(calc) + " USD"
        lbl = Label(window, bg="black", fg="white", text=string)
        lbl.pack()
        fail = open('История конвертера валют.txt', 'a')
        fail.write("\n" + now.strftime("%d.%m.%Y %H:%M") + " : " + string)
        fail.close()

    elif combo.get() == "USD":
        checkint()
        calc = int(ent_int.get()) / 0.014
        string = str(ent_int.get()) + " USD = " + str(calc) + " RUB"
        lbl = Label(window, bg="black", fg="white", text=string)
        lbl.pack()
        fail = open('История конвертера валют.txt', 'a')
        fail.write("\n" + now.strftime("%d.%m.%Y %H:%M") + " : " + string)
        fail.close()

    else:
        messagebox.showinfo('Fatal ERROR', 'А валюту выбрать?')
    btn_restart.pack(expand=True, fill=BOTH)

def eade():
    btn_restart.pack_forget()
    frm_entry.pack()

def start():
    btn_start.destroy()
    eade()

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

lbl_close = Label(window, bg="black", fg="white", text="Чтобы закрыть окно нажите Alt+F4.")
lbl_close.pack()
lbl_nst = Label(window, bg="black", fg="white", text="Текущая дата и время:\n" + now.strftime("%d-%m-%Y %H:%M"))
lbl_nst.pack()

btn_start = Button(master=window, bg="black", fg="white", text="Начать", command=start)
btn_start.pack(expand=True, fill=BOTH)

frm_entry = Frame(relief=SUNKEN, bg="black", borderwidth=3)
frm_entry.pack_forget()
lbl_annotation = Label(master=frm_entry, bg="black", fg="white", text="Введите необходиое число,\nвыберите валюту и нажмите ОК.")
lbl_annotation.grid(column=0, row=1)
ent_int = Entry(master=frm_entry, bg="grey", fg="white", width=8)
ent_int.grid(column=0, row=2)
combo = Combobox(master=frm_entry, background="grey", foreground="white", width=7)
combo['values'] = ("RUB", "USD")
combo.grid(column=1, row=2)
btn_next = Button(master=frm_entry, bg="black", fg="white", text="ОК", command=ok)
btn_next.grid(column=0, row=3)

btn_restart = Button(master=window, bg="black", fg="white", text="Ещё раз", command=eade)
btn_restart.pack_forget()

window.mainloop()
