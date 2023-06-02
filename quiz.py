Game=input("you play to quiz game! :")
if Game !="yes":
    quit()
print("let's start")
corret=0
wrong=0
user=input("what is india capital :")
if user.lower()=="new delhi":
    print("corret ans")
    corret +=1
    print("")
else:
    print("wrong ans")
    wrong +=1

user=input("who is the pm of india :")
if user.lower()=="narendra modi":
    print("corret ans")
    corret +=1
    print("")
else:
    print("wrong ans")
    wrong +=1
user=input("2011 cricket world cup winners :")
if user.lower()=="india":
    print("corret ans")
    corret +=1
    print("")
else:
    print("wrong ans")
    wrong +=1
user=input("OOP menines !:")
if user.lower()=="obeject oretend programing":
    print("corret ans")
    corret +=1
    print("")
else:
    print("wrong ans")
    wrong +=1

print("corret ans :"+str(corret))
print("wrong ans :"+str(wrong))























