#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" A Simple Node Class """

# class for linked list #

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