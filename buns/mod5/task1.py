class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end == None:
        	pass
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        pass

    def print(self):
        """
        вывод на печать содержимого стека
        """
        
        pass
