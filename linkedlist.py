#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" A Simple LinkedList Class """

############ Node Class ###################
class Node:
    def __init__(self, data):
        self.next = None 
        self.data = data

    def get_data(self):
        return self.data
    
    def get_next(self):
        next = self.next
        return next.data
    
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

        #assign value after
        newNode.next = nextNode
    

    #method to remove Node, given the object as a parameter
    def remove(self, deleteNode):

        #Base Case 1: Make sure data is valid, node exists in list
        if deleteNode == None:
            print("Please provide a valid Node to delete. Node not found in list.")
            return
        
        #Base Case 2: If deletion is the head Node
        if deleteNode == self.head:
            self.head = self.head.next
            return


        #Else: start at head. Also grab pointer to be linked
            #  If deletion is tail, nextNode will still be pointing to None
        previous = self.head
        nextNode = deleteNode.next

        #find the node that is previous to deletion, link to next node after deletion
        while(previous):
            if previous.next == deleteNode:
                previous.next = nextNode
            
            previous = previous.next

    #Method to loop through list and print
    def print_list(self):
        #grab first element
        nodeIndex = self.head

        #print data while the tail isn't reached
        while(nodeIndex):
            print(" %s" % (nodeIndex.data))
            nodeIndex = nodeIndex.next

############### Functions ################
def print_Pretty(phrase, pList):
    print("*" * 40)
    print("")
    print(str(phrase))
    pList.print_list()
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

    #Add Nodes to list
    list.push(n1)
    list.push(n2)
    list.push(n3)
    
    ########### Tests #############
    #print Nodes in list
    print_Pretty("Printed Initial LinkedList: ", list)


    #add Nodes to end & middle of list
    n4 = Node('Node 4')
    n5 = Node('Delete Me')
    list.append(n4)
    list.insertAfter(n2,n5)

    print_Pretty("LinkedList After Additions: ", list)

    #remove node
    list.remove(n5)
    print_Pretty("LinkedList After Deletion: ", list)

    #get next node data
    testNode = Node('Test')
    testNode = list.findNode('Node 2')
    print("Node Query Found: " + str(testNode.data))
    print("Next Node In List: " + str(testNode.get_next()))



    






