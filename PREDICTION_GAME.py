print("SNAKE WATER GUN GAME \nMAKE FIRST 3 POINTS TO WIN FROM COMPUTER")
import random
c=['snake','water','gun']
name=str(input("ENTER YOUR NAME:-"))

score=0
computer=0
n=0
while score<3 and computer<3:
  n+=1
  user=str(input(f"\nChoose:-SNAKE or WATER or GUN\n\n{n}:-{name}:-"))
  if user=='snake' or user=='water' or user=='gun':
        random_c = random.choice(c)
        x=random_c
        print("COMPUTER:-",x)
        if user==x:
            score+=1
            print(f"good +1\n\t\t\tcomputer={computer}\n\t\t\t{name}={score}")
            continue
        else :
                computer+=1
                print(f"hahaha\t\t\t\n\t\t\tcomputer={computer}\n\t\t\t{name}={score}")
                continue
  else:
                    print(f"wrong\nCheck your input {name}")
                    print(f"\t\t\t{name}={score}\n")
                    continue
else :
                        print(f"\t\t\tGAME COMPLETED")
                        if computer==3:
                            print(f"\nCOMPUTER WINS")
                        elif score==3:
                                print(f"{name} WINS")
                        else :
                                    print("DRAW")
