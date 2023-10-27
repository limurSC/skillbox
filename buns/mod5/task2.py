
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
        
				 newNode = Node(val)
        if n == 0:
            newNode.nref = self.start
            if self.start is not None:
                self.start.pref = newNode
            self.start = newNode
            if self.end is None:
                self.end = newNode
        else:
            node = self.start
            count = 0
            while node is not None and count < n:
                node = node.nref
                count += 1
            if node is None:
                self.end.nref = newNode
                newNode.pref = self.end
                self.end = newNode
            else:
                newNode.nref = node
                newNode.pref = node.pref
                node.pref.nref = newNode
                node.pref = newNode

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        node = self.start
        while node is not None:
            print(node.data)
            node = node.nref



