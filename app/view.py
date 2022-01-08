from tkinter import Tk, StringVar, Label, Button

from app.interfaces import IObserver, IModelReading, IController


class View(IObserver):
    __model: IModelReading
    __controller: IController
    __number: int

    __window: Tk
    __labelText: StringVar

    def __init__(self, model: IModelReading, controller: IController):
        self.__model = model
        self.__controller = controller

        self.__window = Tk()
        self.__labelText = StringVar()

        self.__model.attach(self)
        self.__updateRandNumber()

        self.__drawWindow()

    def __del__(self):
        self.__model.detach(self)

    def __drawWindow(self):
        self.__window.title("SIMPLE MVC")
        self.__window.geometry("200x170")

        label = Label(textvariable=self.__labelText, font=("Arial Bold", 50))
        updateBtn = Button(text="Update", command=self.__updateRandNumber)
        closeBtn = Button(text="Close", command=self.__window.destroy)

        label.grid(row=1, columnspan=4, padx=10)
        updateBtn.grid(row=2, column=1, padx=10, pady=10)
        closeBtn.grid(row=2, column=2, pady=10)

        self.__window.mainloop()

    def __updateRandNumber(self):
        self.__controller.update()

    def modelIsChanged(self):
        self.__number = self.__model.randomNumber
        self.__labelText.set(self.__number)
