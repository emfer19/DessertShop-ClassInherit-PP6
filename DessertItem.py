#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/9/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

#main class

class DessertItem:
  """Main class to obtain dessert name and cost"""

  def __init__(self,n='none',c=0.0):
    """Initializes DessertItem object with dessert name"""
    self.name=n
    self.cost=c

  def getName(self):
    """Returns the dessert item name"""
    return self.name

  def getCost(self):
    """Returns the dessert item cost"""
    return self.cost

  def setName(self, na):
    """Assigns the formal parameter to the dessert item"""
    self.name=str(na)

  def setCost(self, co):
    """Assigns the formal parameter to the dessert item"""
    self.cost=float(co)

  def __str__(self):
    """Returns a string containing the information of the dessert item"""
    display="\nItem: "+str(self.name)
    display+="\nCost: "+str(round(self.cost,2))
    return display

#end of class build

#unit test

if __name__=='__main__':
  des1=DessertItem()
  print des1

  des1.setName('candy')
  print des1.getName()

  des1.setCost(45)
  print des1.getCost()

  print des1

  des2=DessertItem('cookie',6)
  print des2
