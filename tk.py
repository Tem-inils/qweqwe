import tkinter as tk

root = tk.Tk()
root.title("Бегущий человек")

canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()

person = canvas.create_oval(10, 50, 50, 100, fill="blue")  # Тело
head = canvas.create_oval(20, 10, 40, 30, fill="yellow")  # Голова
leg1 = canvas.create_line(25, 100, 20, 120, fill="blue", width=5)  # Левая нога
leg2 = canvas.create_line(35, 100, 40, 120, fill="blue", width=5)  # Правая нога
arm1 = canvas.create_line(20, 60, 10, 80, fill="blue", width=5)  # Левая рука
arm2 = canvas.create_line(40, 60, 50, 80, fill="blue", width=5)  # Правая рука

# Функция для движения человечка
def move_person():
    canvas.move(person, 5, 0)
    canvas.move(head, 5, 0)
    canvas.move(leg1, 5, 0)
    canvas.move(leg2, 5, 0)
    canvas.move(arm1, 5, 0)
    canvas.move(arm2, 5, 0)
    root.after(100, move_person)

# Начать движение
move_person()

root.mainloop()