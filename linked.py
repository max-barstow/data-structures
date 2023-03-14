class SingleLink:
    def __init__(self, value):
        self.child = None
        self.value = value

class DictNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.child = None

class DoubleLink:
    def __init__(self, value):
        self.parent = None
        self.child = None
        self.value = value

class LinkedList:
    def insert(self, value):
        tracked = self.root
        if tracked is None:
            self.root = self.nodetype(value)
            return self.root
        while tracked.child:
            tracked = tracked.child
        tracked.child = self.nodetype(value)
        if self.nodetype is DoubleLink:
            tracked.child.parent = tracked
        return tracked.child

    def search(self, value):
        tracked = self.root
        while tracked:
            if tracked.value == value:
                return tracked
            tracked = tracked.child
        return None
    
    def delete(self, value):
        tracked = self.root
        if tracked.value == value:
            self.root = tracked.child
            del self
            return

        while tracked and tracked.child:
            if tracked.child.value == value:
                tracked.child = tracked.child.child
                del tracked.child
                return

    def __init__(self, nodetype, *values):
        self.root = None
        self.nodetype = nodetype
        for value in values:
            self.insert(value)

class DictLinkedList(LinkedList):
    def insert(self, key, value=None):
        node = super().insert(key)
        node.value = value

    def search(self, key):
        tracked = self.root
        while tracked:
            if tracked.key == key:
                return tracked
            tracked = tracked.child
        return None

    def __init__(self, key, value):
        super().__init__(DictNode, key)
        self.root.value = value

class SingleLinkedList(LinkedList):
    def __init__(self, *values):
        super().__init__(SingleLink, *values)

class DoubleLinkedList(LinkedList):
    def delete(self, value):
        node = self.search(value)
        if node:
            if node is self.root:
                self.root = node.child
                node.child.parent = None
            else:
                node.child.parent = node.parent
                node.parent.child = node.child
            del self

    def __init__(self, *values):
        super().__init__(DoubleLink, *values)
