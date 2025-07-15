q=int(input("from year:-"))
r=int(input("To year:-"))
count=0
if q<r:
  for i in range(q,r+1):
    if i%4==0:
      print("\t\t\t\t\t{}:-is a leap year".format(i))
      i+=1
      count+=1
    else :
        print(i,":-not a leap year")
        i+=1

else :
  print("not calculatble as TO<FOR")

print("\t\t\t\t\tTotal leap year:-",count)
