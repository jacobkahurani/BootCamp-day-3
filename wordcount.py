def words(s): #Define function called words that takes in one argument "s"
    w = s.split() # perform split operation on argument passed and assign to variable w
    a = [] # initiate empty list and assign to variable a
    for i in w:# perform iteration over contents of list w
        a.append((i,w.count(i))) # add to list a output of iteration
    b = [i for i in set(a)] # create a set from list a, initiate a list b via comprehension from contents of set
    return dict(b)#initialize a dictionary from list b
    