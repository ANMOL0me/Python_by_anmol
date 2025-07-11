#BILLING COUNTER
print("\t\t\tMENU")
print("JUICE's\nAPPLE:-30\tMANGO:-40\tBANANA:-50")
print("\t#Type none if no order")
order1=str(input("ORDER_1:-"))
if order1=="none":
  print("NO ORDER")
  price1=0
  ordquan1=0
  print("price:-0")
elif order1=="apple":
  price1=30
  print("price:-{}".format(price1))
  ordquan1=int(input("Quantity:-"))

elif order1=="mango":
  price1=40
  print("price:-{}".format(price1))
  ordquan1=int(input("Quantity:-"))

elif order1=="banana":
  price1=50
  print("price:-{}".format(price1))
  ordquan1=int(input("Quantity:-"))

else:
  print("dont use your brain")
  price1=0
  ordquan1=0

price1
ordquan1
total1=ordquan1*price1
order2=str(input("ORDER_2:-"))

if order2=="none":
  print("NO ORDER")
  price2=0
  ordquan2=0
  print("price:-0")

elif order2=="apple":
  price2=30
  print("price:-{}".format(price2))
  ordquan2=int(input("Quantity:-"))

elif order2=="mango":
  price2=40
  print("price:-{}".format(price2))
  ordquan2=int(input("Quantity:-"))

elif order2=="banana":
  price2=50
  print("price:-{}".format(price2))
  ordquan2=int(input("Quantity:-"))

else:
  print("dont use your brain")
  price2=0
  ordquan2=0
  #total

total2=ordquan2*price2

alltot=total1+total2
print("\t\t\tBILLING")
print("Item\t\tQnt\t\tPrice\t\tTotal")
print("{}\t\t{}\t\t{}\t\t{}".format(order1,ordquan1,price1,total1))
print("{}\t\t{}\t\t{}\t\t{}".format(order2,ordquan2,price2,total2))
print("Total\t\t\t\t\t{}".format(alltot))
if alltot >=200:
  print("20% off on order of above 200")
  totaldis=total1*0.2+total2*0.2
  print("Total\t\t\t\t\t{}/-".format(alltot-totaldis))
else:
  print("No discount")
  print("Total\t\t\t\t\t{}/-".format(alltot))