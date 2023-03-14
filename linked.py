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
            # There is no root node yet, so create it and return it
            self.root = self.nodetype(value)
            return self.root
        
        while tracked.child:
            # Iterate to the end of the linked list
            tracked = tracked.child
        
        # Create new end node
        tracked.child = self.nodetype(value)

        if self.nodetype is DoubleLink:
            # Handle double-linked lists by setting the new node's parent
            tracked.child.parent = tracked

        # Return the new node
        return tracked.child

    def search(self, value):
        tracked = self.root
        while tracked:
            # Iterate through the linked list, returning a node when value matches
            if tracked.value == value:
                return tracked

            tracked = tracked.child
        
        # The value is not in the list if we have not returned yet
        return None
    
    def delete(self, value):
        tracked = self.root

        if tracked.value == value:
            # If the node to be deleted is the list's root, reset the root
            self.root = tracked.child
            del tracked
            return

        # Iterate through the list until the node to be deleted is found
        while tracked:
            # We check the node's child, as we can't access the node's parent
            # in a single-linked list
            if tracked.child.value == value:
                # Store a reference to the node to be deleted
                old_child = tracked.child

                # We set the parent's new child reference to the node after the deleted node
                tracked.child = old_child.child

                # Delete the node
                del old_child
                return

            tracked = tracked.child

    def __init__(self, nodetype, *values):
        self.root = None
        # We store the type of node used to facilitate OOP
        self.nodetype = nodetype

        # Construct the linked list from supplied values
        for value in values:
            self.insert(value)

class DictLinkedList(LinkedList):
    def insert(self, key, value=None):
        # Overrides the insert method to account for two pieces of information being stored

        # Calls the LinkedList insert method to insert a new node
        node = super().insert(key)
        # Sets the value of the new node
        node.value = value

    def search(self, key):
        # In Dictionaries, we search by key. Therefore we need to override search
        tracked = self.root
        while tracked:
            if tracked.key == key:
                return tracked
            tracked = tracked.child
        return None

    def __init__(self, key, value):
        # Uses LinkedList's initialisation method, and sets the value of the root node
        super().__init__(DictNode, key)
        self.root.value = value

class SingleLinkedList(LinkedList):
    def __init__(self, *values):
        # Constructs a LinkedList using single link nodes
        super().__init__(SingleLink, *values)

class DoubleLinkedList(LinkedList):

    def delete(self, value):
        # In a double linked list, we need to change a node's parent too
        node = self.search(value)
        if node:
            if node is self.root:
                # If the node is the root, we need to reset the root
                self.root = node.child
                node.child.parent = None
            else:
                # Remove the node from the linked list
                node.child.parent = node.parent
                node.parent.child = node.child
            del node

    def __init__(self, *values):
        # Constructs a LinkedList using double link nodes
        super().__init__(DoubleLink, *values)
