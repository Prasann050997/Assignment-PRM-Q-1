# Python Candidates - Question 1

def sort_string(l):
        n = len(l)
        for i in range(n-1):
            for j in range(i,n-1):
                if ord(l[j][-2])>ord(l[j+1][-2]):
                    l[j],l[j+1]=l[j+1],l[j]
        return l
n =int(input("Enter no. of elements : "))
lis=[]
for i in range(1,n+1):
    lis.append(input(f"Enter String {i} : "))

print("Sorted list of strings : ",sort_string(lis))
