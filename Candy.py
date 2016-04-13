#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/9/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

#derived class from DessertItem class

from DessertItem import DessertItem
class Candy(DessertItem):
  """derived DessertItem class:
  specialized for Candy dessert items.

  Calculates cost based on given weight, and price per pound
  
  Please give PRICE in DOLLARS and CENTS, not just in cents:
      CORRECT: 1.89
      INCORRECT: 189"""

  def __init__(self,n='Candy',w=0.0,price=0.0):
    """initialize candy object with name, cost, weight, and price per pound"""
    DessertItem.__init__(self,n)
    self.weight=float(w)
    self.pricePound=float(price)

  def getWeight(self):
    """returns the weight of candy"""
    return self.weight

  def getPricePound(self):
    """returns the price per pound of candy"""
    return self.pricePound

  def setWeight(self,lb):
    """assigns formal parameter to candy's weight"""
    self.weight=float(lb)

  def setPricePound(self,price):
    """assigns the formal parameter to candy's price"""
    self.pricePound=float(price)

  def calculateCost(self):
    """calculates cost of candy item based off given weight and price"""
    cost=(round(self.getWeight()*(self.getPricePound()*100))/100)
    self.setCost(cost)
    return

  def __str__(self):
    """returns a string containing the candy's info"""
    display=DessertItem.__str__(self)
    display+='\nWeight in lbs: '+str(self.weight)
    display+='\nPrice per Pound: '+str(self.pricePound)
    return display

#end of class build

#unit testing

if __name__=='__main__':
  des1=Candy('fudge',2.3,.89)
  des1.calculateCost()
  print des1.getName()
  print des1.getCost()
  print des1.getWeight()
  print des1.getPricePound()
  print des1

  des1.setWeight(1)
  des1.setPricePound(10)
  des1.calculateCost()
  print des1
