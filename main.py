#Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:


def neworder(lst):

    if s == "none":
        list1=lst,
        print(list1)
    elif s == "asc":
        list1=sorted(lst, reverse=False),
        print(list1)
    elif s == "des":
        list1=sorted(lst, reverse=True),
        print(list1)
    else:
        print("Whoops, I think you entered something other than asc, des, or none!")


lst1 = ([5,2,33,1,900,4,1234])
lst=lst1
s = (input("How would you like this list ordered? For ascending, enter asc, for descending enter des, otherwise enter "
           "none to retain the current order"))
#s=s.lower()
neworder(lst)


lst2 = ([1,2,9,7,55,43,2345,1000])
lst=lst2
s = (input("How would you like this list ordered? For ascending, enter asc, for descending enter des, otherwise enter "
           "none to retain the current order"))
#s=s.lower()
neworder(lst)
