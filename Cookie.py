#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/9/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

#derived class from DessertItem class

from DessertItem import DessertItem
class Cookie(DessertItem):
  """derived DessertItem class:
  specialized for Cookie dessert items.

  Calculates cost based on given quantity, and price per dozen
  
  Please give PRICE in DOLLARS and CENTS, not just in cents:
      CORRECT: 1.89
      INCORRECT: 189"""

  def __init__(self,n='Cookie',q=0,price=0.0):
    """initialize cookie object with name, quantity, and price per dozen"""
    DessertItem.__init__(self,n)
    self.quantity=float(q)
    self.priceDozen=float(price)

  def getQuantity(self):
    """returns the quantity of cookies"""
    return self.quantity

  def getPriceDozen(self):
    """returns the price per dozen cookies"""
    return self.priceDozen

  def setQuantity(self,qt):
    """assigns formal parameter to cookie's quantity"""
    self.quantity=floatt(qt)

  def setPriceDozen(self,price):
    """assigns the formal parameter to cookie's price"""
    self.priceDozen=float(price)

  def calculateCost(self):
    """calculates cost of cookie item based off given quantity and price"""
    cost=float(round(self.getQuantity()*(self.getPriceDozen()/12)))
    self.setCost(cost)
    return

  def __str__(self):
    """returns a string containing the cookie's info"""
    display=DessertItem.__str__(self)
    display+='\nQuantity: '+str(self.quantity)
    display+='\nPrice per Dozen: '+str(self.priceDozen)
    return display

#end of class build

#unit testing

if __name__=='__main__':
  des1=Cookie('Oatmeal Cookies',4,3.99)
  des1.calculateCost()
  print des1.getName()
  print des1.getCost()
  print des1.getQuantity()
  print des1.getPriceDozen()
  print des1

  des1.setQuantity(1)
  des1.setPriceDozen(10)
  des1.calculateCost()
  print des1
