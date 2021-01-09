#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" A Doubly LinkedList Class """

############ Node Class ###################
class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None 
        self.data = data

    def get_data(self):
        return self.data
    
    def get_next(self):
        next = self.next
        return next.data
    
    def get_prev(self):
        prev = self.previous
        return prev.data
    
    def __str__(self):
        return self.get_data()

################## Class for LinkedList ###################

class LinkedList:
    def __init__(self):
        self.head = None
    
    #method to add to beginning of list
    def push(self, newHead):

        #Base Case: If list is empty, make input head
        if(self.head == None):
            self.head = newHead
        
        #reassign new head to list 
        else:
            #link to head Node
            newHead.next = self.head
            #link reference to new head
            self.head.previous = newHead

            #assign head value to new node
            self.head = newHead
    
    #method to add to end of list  
    def append(self, newTail):

        #Base Case: If list is empty, make input the head. 
        if(self.head == None): 
            self.head = newTail

        else: 
            #grab first element
            tail = self.head 

            #traverse through the list until you have tail
            while(tail):
                if tail.next == None:
                    newTail.previous = tail
                    tail.next = newTail
                    break 
                else:
                    tail = tail.next

    #Method to find a node given it's data. 
    def findNode(self, node_Data):

        #start at the beginning of the list
        search = self.head

        #traverse through the list
        while(search):
            if(search.data == node_Data):
                #return Node if data matches query
                return search
            else:
                search = search.next
            

    #method to add a Node after a given Node
    def insertAfter(self, currentNode, newNode):

        #Base Case: Make sure data is valid, node exists in list
        if currentNode == None:
            print("Please provide a valid Node to insert after.")
            return

        #grab current 'next' 
        nextNode = currentNode.next

        #insert node
        currentNode.next = newNode
        newNode.previous = currentNode

        #assign value after
        newNode.next = nextNode
        nextNode.previous = newNode
    

    #Method to remove Node, given the object as a parameter
    def remove(self, deleteNode):

        #Base Case 1: Make sure data is valid, node exists in list
        if deleteNode == None:
            print("Please provide a valid Node to delete. Node not found in list.")
            return
        
        #Base Case 2: If deletion is the head Node
        if deleteNode == self.head:
            self.head = self.head.next
            self.head.previous = None
            return
        
        #Base Case 3: If deletion is the tail Node
        if deleteNode.next == None:
            prev = deleteNode.previous
            prev.next = None
            return

        #Else: grab current links 
        previous = deleteNode.previous
        nextNode = deleteNode.next

        #assign new links
        previous.next = nextNode
        nextNode.previous = previous

    #Method to loop through list and print
    def print_list(self):
        #grab first element
        nodeIndex = self.head

        #print data while the tail isn't reached
        while(nodeIndex):
            print(" %s" % (nodeIndex.data))
            nodeIndex = nodeIndex.next
    
    def print_backwards(self):
        #grab first element
        nodeIndex = self.head

        #Traverse to tail
        while(nodeIndex.next is not None):
            nodeIndex = nodeIndex.next

        #print data while the head isn't reached
        while(nodeIndex):
            print(" %s" % (nodeIndex.data))
            nodeIndex = nodeIndex.previous

############### Functions ################
def print_Pretty(phrase, pList):
    print("*" * 40)
    print("")
    print(str(phrase))
    pList.print_list()
    print("")
    print("_" * 40)

def print_Pretty_Back(phrase, pList):
    print("*" * 40)
    print("")
    print(str(phrase))
    pList.print_backwards()
    print("")
    print("_" * 40)

################ Main ####################

if __name__ == "__main__":

    #initial List object
    list = LinkedList()

    #initiate Nodes to place into list
    n1 = Node('Node 1')
    n2 = Node('Node 2')
    n3 = Node('Node 3')
    n4 = Node('Node 4')
    n5 = Node('Node 5')

    #Add Nodes to list
    list.push(n1)
    list.push(n2)
    list.push(n3)
    list.push(n4)
    list.push(n5)
    
    ########### Simple Tests #############
    #print Nodes in list
    print_Pretty("Printed Initial Doubly LinkedList: ", list)

    #add Nodes to end & middle of list
    n6 = Node('Node 6')
    n7 = Node('Delete Me')
    list.append(n6)
    list.insertAfter(n2,n7)

    print_Pretty("Doubly LinkedList After Additions: ", list)

    #remove node
    list.remove(n7)
    print_Pretty("Doubly LinkedList After Deletion: ", list)

    #backwards printing of list
    print_Pretty_Back("Backwards List Print-Out: ", list)
