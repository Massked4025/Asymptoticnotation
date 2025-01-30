def printn(n):
    iteration = 0
    print("The total number is", n)
    iteration += 1
    print("The total iteration is", iteration)

printn(10)
printn(25)
# Time complexety = O(1) best case scenario

def printa(n):
    iteration = 0
    print("The total number is", n)
    for i in range(1,n+1):
        iteration += 1
    print("The total iteration is", iteration)

printa(10)
printa(25)
# Time complexety = O(n) average case scenario

def printz(n):
    iteration = 0
    print("The total number is", n)
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
            iteration += 1
        print("")
    print("The total iteration is", iteration)

printz(5)
printz(6)