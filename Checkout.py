#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/9/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

from FileUtilities import*
from DessertItem import DessertItem
from Candy import Candy
from Cookie import Cookie

class Checkout:
  """Reads a file containing a customer's items
     and creates the proper object, adds it to a list,
     and then calculates the total cost"""

  def __init__(self):
    """initializes with nothing"""
    self._itemList=[]
    self._file=openFileReadRobust()

  def createItems(self):
    """Read file and create a list of all the objects,
       will create a polymorphic list.
       In the data file, a 0 should precede a cookie data line
                     and a 1 should precede a candy data line"""

    line=self._file.readline()
    while line:
      data=line.split(',')
      if data[0]=='0': #shows this is a cookie
        cookieObj=Cookie(data[1],data[2],data[3]) #create cookie object using data in line
        self._itemList.append(cookieObj) #append it to the list
      elif data[0]=='1': #shows this is a candy
        candyObj=Candy(data[1],data[2],data[3]) #creates the candy object using data in line
        self._itemList.append(candyObj) #append it to the list
      line=self._file.readline()
    self._file.close()

  def displayReceipt(self):
    """Calculates the cost of all the items in the list,
       displays all the items and overal total cost"""
    total=0
    for item in self._itemList:
      item.calculateCost()
      total+=item.getCost()
      print item
    
    print 'Total Cost: $'+str(total)
