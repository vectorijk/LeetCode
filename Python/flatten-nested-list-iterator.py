# Time:  O(n), n is the number of the integers.
# Space: O(h), h is the depth of the nested lists.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#iterator
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]
        
    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        # if stack top is List, push every element in list
        while self.stack and not self.stack[-1].isInteger():
            top = self.stack.pop()
            for nestedInt in top.getList()[::-1]:
                self.stack.append(nestedInt)
        
        return len(self.stack) > 0

### dfs 
class NestedIterator(object):
    def __init__(self, nestedList):
        result = []
        self.dfs(nestedList, result)
        self.lst = result[::-1]
    
    def dfs(self, nestedList, res):
        for item in nestedList:
            if item.isInteger():
                res.append(item.getInteger())
            else:
                self.dfs(item.getList(), res)

    def next(self):
        return self.lst.pop()

    def hasNext(self):
        return len(self.lst) > 0


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.__depth = [[nestedList, 0]]


    def next(self):
        """
        :rtype: int
        """
        nestedList, i = self.__depth[-1]
        self.__depth[-1][1] += 1
        return nestedList[i].getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.__depth:
            nestedList, i = self.__depth[-1]
            if i == len(nestedList):
                self.__depth.pop()
            elif nestedList[i].isInteger():
                    return True
            else:
                self.__depth[-1][1] += 1
                self.__depth.append([nestedList[i].getList(), 0])
        return False
 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
