class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is full"
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
        return "The value has been successfully inserted!"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"

    def preOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)

    def postOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index=1):
        if self.customList is None:
            return None
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "Binary Tree is empty"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

    def deleteBT(self):
        self.customList = None
        return "Binary Tree has been deleted successfully"

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.searchNode("Hot"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print("PreOrder Traversal")
newBT.preOrderTraversal()
print("InOrder Traversal")
newBT.inOrderTraversal()
print("PostOrder Traversal")
newBT.postOrderTraversal()
print("LevelOrder Traversal")
newBT.levelOrderTraversal()
print(newBT.deleteNode("Tea"))
print("LevelOrder Traversal")
newBT.levelOrderTraversal()
print(newBT.deleteBT())
print("LevelOrder Traversal")
print(newBT.levelOrderTraversal())
