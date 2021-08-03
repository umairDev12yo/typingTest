import time

def search(thing,inThing):
    for i in range(len(thing)):
        for j in range(len(inThing)):
            if thing[i]==inThing[i]:
                return True
            else:
                return False


maxTime=600
timeZero=time.time()
theFirstTime=time.time()
# print(theFirstTime)
whatToType="The quick Brown Fox jumps over the lazy Dog"
print(f"Write This {whatToType}")
inputType=input(">>>")
theSecondTime=time.time()
# print(theSecondTime)

resultTime=theSecondTime-theFirstTime
intWhatToType=len(whatToType)
lastResult=resultTime/intWhatToType
print(f"You took a total time of:- {resultTime} ")
print(f"Your lpm:- {lastResult}")
firstListLoid=whatToType.split()
firstList=list(firstListLoid)
secondListLoid=whatToType
secondList=list(secondListLoid)

if whatToType==inputType:
    print("Your effieciency is sus")
else:
    print("About you'r effieciency, it is not calculated but it sucks, tbh or you did quite a little mistake, idk")

# if(search(firstList,secondList)):
#     print("Gud")
# else:
#     print("Your effieciency has not been calculated but it's kinda low, i guess, or i mean idk you did a mistake")