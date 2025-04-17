# -*- coding: cp1254 -*-
def buildParseTree(fpexp):
 fplist = fpexp.split()
 s = Stack()
 eTree = BinaryTree(’’)
 s.push(eTree)
 currentTree = eTree
 for i in fplist:
 if i == ’(’:
 currentTree.insertLeft(’’)
 s.push(currentTree)
 currentTree = currentTree.getLeftChild()
 elif i not in ’+-*/)’:
 currentTree.setRootVal(eval(i))
 parent = s.pop()
 currentTree = parent
 elif i in ’+-*/’:
 currentTree.setRootVal(i)
 currentTree.insertRight(’’)
 s.push(currentTree)
 currentTree = currentTree.getRightChild()
 elif i == ’)’:
 currentTree = s.pop()
 else: print "error: I don’t recognize " + i
 return eTree

