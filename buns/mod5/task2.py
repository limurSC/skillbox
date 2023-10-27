
#task2
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
				 if self.start is None:
        	pass
				 val = self.start.data
				 self.start = self.start.nref
				 if self.start is None:
				 		self.end = None
				 else:
						self.start.pref = None
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        newNode = Node(val)
				 if self.start is None:
						self.start = newNode
						self.end = newNode
				 else:
						newNode.pref = self.pref
						self.end.nref = newNode
						self.end = newNode

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        pass

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        pass
