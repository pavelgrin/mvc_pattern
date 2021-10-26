from app.interfaces import IController, IModelWriting


class Controller(IController):
    __model: IModelWriting

    def __init__(self, model: IModelWriting):
        self.model = model

    def update(self):
        self.model.updateRandom()
