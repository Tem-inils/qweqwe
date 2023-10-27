import tkinter as tk


# Функция для обработки нажатия кнопок
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


# Создание главного окна
root = tk.Tk()
root.geometry("400x600")
root.title("Калькулятор")

# Создание поле ввода
entry = tk.Entry(root, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Создание кнопок
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

i = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font='lucida 20 bold')
    btn.grid(row=i // 4, column=i % 4, padx=10, pady=10)
    btn.bind("<Button-1>", button_click)
    i += 1

root.mainloop()
