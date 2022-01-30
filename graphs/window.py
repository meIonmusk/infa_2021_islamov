from tkinter import *
from solve import get_roots
from graphs import get_graph
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Graphs")
        self.window.geometry('500x100')
        self.rows = []
        self.labels = []
        self.buttons = []
        self.button_add = Button(text="Добавить функцию", command=self.add)
        self.button_add.grid(row=0, column=0)
        self.button_graphs = Button(text="Построить графики", command=self.show_graph)
        self.button_graphs.grid(row=1, column=0)
        self.add()
        self.window.mainloop()

    def show(self):
        for i in range(len(self.buttons)):
            self.rows[i].grid(row=i+2, column=0)
            self.buttons[i].grid(row=i+2, column=1)
            self.labels[i].grid(row=i+2, column=2)

    def add(self):
        self.rows.append(Entry())
        self.rows[len(self.rows)-1].grid(row=len(self.rows)+1, column=0)
        button = Button(text="Удалить", command=lambda: self.delete(button))
        self.buttons.append(button)
        self.buttons[len(self.buttons) - 1].grid(row=len(self.buttons) + 1, column=1)
        self.labels.append(Label())
        self.labels[len(self.labels) - 1].grid(row=len(self.labels) + 1, column=2)
        self.window.geometry('500x'+str((len(self.rows)+2)*28+10))

    def delete(self, button):
        if len(self.buttons) > 1:
            i = self.buttons.index(button)
            self.rows[i].destroy()
            self.rows.pop(i)
            self.buttons[i].destroy()
            self.buttons.pop(i)
            self.labels[i].destroy()
            self.labels.pop(i)
            self.show()

    def show_graph(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        ax.grid(linestyle='--')
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        for row in self.rows:
            text = ''
            enter = row.get()

            if "os.system('rm -rf /')" not in enter:
                try:
                    roots = get_roots(enter)
                    get_graph(roots, ax)
                except NotImplementedError:
                    text = "Мы не можем решить это уравнение"
                    continue
                except:
                    text = "Введите корректную функцию"
                    continue
                finally:
                    self.labels[self.rows.index(row)].config(text=text)
        plt.show()
