#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/13/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

from Checkout import Checkout

checkout1=Checkout() #create Checkout object

checkout1.createItems() #create the list of items
checkout1.displayReceipt() #print receipt

#user controlled program close
print #line space
raw_input('Press ENTER to close')
