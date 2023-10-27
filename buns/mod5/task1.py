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
        if self.end is None:
        	pass
				 val = self.end.pref
				 self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
				newNode = Node(val)
				newNode.pref = self.end
       self.end = newNode

    def print(self):
        """
        вывод на печать содержимого стека
        """
        node = self.end
				 while node is note None:
						print(node.data)
						node = node.pref
