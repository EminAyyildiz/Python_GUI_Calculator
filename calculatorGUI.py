from tkinter import *

class CALCULATOR:

    def __init__(self, master):
        self.master = master
        master.title("***CALCULATOR*** Emin Ayyıldız")

        self.screen = Entry(master, width=40, borderwidth=5,bg ='#add8e6')
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


        self.buton_1 = Button(master, text="1", padx=40, pady=20, command=lambda: self.number_enter(1))
        self.buton_2 = Button(master, text="2", padx=40, pady=20, command=lambda: self.number_enter(2))
        self.buton_3 = Button(master, text="3", padx=40, pady=20, command=lambda: self.number_enter(3))
        self.buton_4 = Button(master, text="4", padx=40, pady=20, command=lambda: self.number_enter(4))
        self.buton_5 = Button(master, text="5", padx=40, pady=20, command=lambda: self.number_enter(5))
        self.buton_6 = Button(master, text="6", padx=40, pady=20, command=lambda: self.number_enter(6))
        self.buton_7 = Button(master, text="7", padx=40, pady=20, command=lambda: self.number_enter(7))
        self.buton_8 = Button(master, text="8", padx=40, pady=20, command=lambda: self.number_enter(8))
        self.buton_9 = Button(master, text="9", padx=40, pady=20, command=lambda: self.number_enter(9))
        self.buton_0 = Button(master, text="0", padx=40, pady=20, command=lambda: self.number_enter(0))

        self.buton_add = Button(master, text="+", padx=39, pady=20, command=self.add)
        self.buton_substract = Button(master, text="-", padx=41, pady=20, command=self.substract)
        self.buton_multply = Button(master, text="*", padx=40, pady=20, command=self.multiply)
        self.buton_divide = Button(master, text="/", padx=41, pady=20, command=self.divide)

        self.buton_equal = Button(master, text="=", padx=105, pady=20, command=self.equal)
        self.buton_del = Button(master, text="Sil", padx=102, pady=20, command=self.delete)


        self.buton_1.grid(row=3, column=0)
        self.buton_2.grid(row=3, column=1)
        self.buton_3.grid(row=3, column=2)

        self.buton_4.grid(row=2, column=0)
        self.buton_5.grid(row=2, column=1)
        self.buton_6.grid(row=2, column=2)

        self.buton_7.grid(row=1, column=0)
        self.buton_8.grid(row=1, column=1)
        self.buton_9.grid(row=1, column=2)
        self.buton_0.grid(row=4, column=0)

        self.buton_add.grid(row=5, column=0)
        self.buton_substract.grid(row=6, column=0)
        self.buton_multply.grid(row=6, column=1)
        self.buton_divide.grid(row=6, column=2)

        self.buton_equal.grid(row=5, column=1, columnspan=2)
        self.buton_del.grid(row=4, column=1, columnspan=2)

        self.num1 = None
        self.num2 = None
        self.operation = None
        self.result = None

    def number_enter(self, number):
        current = self.screen.get()
        self.screen.delete(0, END)
        self.screen.insert(0, str(current) + str(number))

    def add(self):
        self.num1 = float(self.screen.get())
        self.screen.delete(0, END)
        self.operation = "add"

    def substract(self):
        self.num1 = float(self.screen.get())
        self.screen.delete(0, END)
        self.operation = "subtract"

    def multiply(self):
        self.num1 = float(self.screen.get())
        self.screen.delete(0, END)
        self.operation = "multiply"

    def divide(self):
        self.num1 = float(self.screen.get())
        self.screen.delete(0, END)
        self.operation = "divide"

    def equal(self):
        self.num2 = float(self.screen.get())
        self.screen.delete(0, END)

        if self.operation == "add":
            self.result = self.num1 + self.num2
        elif self.operation == "subtract":
            self.result = self.num1 - self.num2
        elif self.operation == "multiply":
            self.result = self.num1 * self.num2
        elif self.operation == "divide":
            self.result = self.num1 / self.num2

        self.screen.insert(0, str(self.result))

    def delete(self):
        self.screen.delete(0, END)

root = Tk()
calculator = CALCULATOR(root)
root.mainloop()