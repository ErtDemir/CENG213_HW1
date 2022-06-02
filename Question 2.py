import itertools as it

def giveRelationSet():
    #Assumed Perfect User
    relationSet = set() 
    line = input("Enter the relation list one by one:\n ") 
    while(line != ""): 
	    relationSet.add(tuple(line.split(","))) 
	    line = input("Enter the other one or if you want finish just push the enter:    ")
    return(relationSet)

def giveAssociateSet():
    #Assumed Perfect User
    associateSet = set(input("Please enter your associate of relation! (Ex : 'a,b,c,d,e'):    ").split(","))
    return(associateSet)

def addingReflexivity(relationSet,associateSet):
    for i in associateSet:
        relationSet.add((i,i))


def takeTuple(index,associateList):
    setOfTuple = set()
    for i in it.product(associateList, repeat=index):
        setOfTuple.add(i)
    return sorted(list(setOfTuple))

def firstAlgorithm(relationSet,associateSet):
    fullSet = set()
    associateList = list(associateSet)
    tupleLen = 1
    while tupleLen <= len(associateList):
        for i in takeTuple(tupleLen,associateList):
            if tupleLen == 1:     # Adding Reflexivity
                fullSet.add((i[0],i[0]))
            elif tupleLen == 2:     # Adding Pairs
                if (i[0],i[1]) in relationSet: 
                    fullSet.add((i[0],i[1]))
            else:
                follower = 1
                complete = 0
                while follower != tupleLen:
                    if (i[follower-1], i[follower]) in fullSet:
                        if follower == tupleLen - 1:
                            complete = 1
                            break
                        else:
                            follower += 1
                    else:
                        break
                if complete ==1:
                    fullSet.add((i[0] , i[tupleLen-1]))
        tupleLen += 1
    return fullSet

def secondAlgorithm(relationSet,associateSet):
    addingReflexivity(relationSet,associateSet)
    associateList = list(associateSet)
    i,j,k = 0,0,0
    while (i < len(associateList)):
        j = 0
        while (j < len(associateList)):
            k = 0
            while (k < len(associateList)):
                if ((associateList[i],associateList[j])) in relationSet and ((associateList[j],associateList[k])) in relationSet and ((associateList[i],associateList[k])) not in relationSet:
                    relationSet.add((associateList[i],associateList[k]))
                    i,j,k = 0,0,0
                else:
                    k += 1
            j += 1
        i += 1
    return relationSet

def thirdAlgorithm(relationSet , associateSet):
    addingReflexivity(relationSet,associateSet)
    for j in associateSet:
        for i in associateSet:
            for k in associateSet:
                if ((i,j)) in relationSet and ((j,k)) in relationSet:
                    relationSet.add((i,k))
    return relationSet

def main():
    relationSet = giveRelationSet()
    associateSet = giveAssociateSet()
    a = firstAlgorithm(relationSet,associateSet)
    print(sorted(a))

main()
