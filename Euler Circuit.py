#Panos30fyllou  April 2020
def circuitexists(Kn):
    for i in range (n):
        for j in range (n):
            if (Kn[i][j]): return False
    return True
inp = "Yes"
while True:
    if (inp == "Yes"):
        n = int(input("Enter a natural number: "))
        if n >= 0:
            if n % 2 == 1:
                Kn = [[]]
                Kn = [[True for x in range(n)] for y in range (n)]
                for i in range (n):
                    for j in range(n):
                        if(i == j): Kn[i][j] = False;
                l = list()
                l.append(0)
                while (not circuitexists(Kn)):      
                    z = 1
                    for i in range(n - 1, -1, -1):
                        if (Kn[l[len(l) - 1]][i]):
                            Kn[l[len(l) - 1]][i] = False
                            Kn[i][l[len(l) - 1]] = False
                            l.append(i)
                            break
                        z = i
                    if (z == 0):    break
                if (circuitexists(Kn)):
                    print("The Eulerian circuit for the graph K" + str(n) + " exists and is:")
                    for i in range(0, len(l), 2):
                        if (i > 0):             print("\t->\t", end="")
                        print("v" + str(l[i] + 1), end="")
                        if (i < len(l) - 1):    print("\t->\tv" + str(l[i + 1] + 1), end="")
                else:
                    print("The Eulerian circuit for the graph K" + str(n) + " doesn't exist.", end="")
            else:
                print("The Eulerian circuit for the graph K" + str(n) + " doesn't exist.", end="")
        else:
            print("The number given is not a natural")
    inp = input("\n\nDo you want to enter another graph?(Yes/No)")
    if inp == "No": break
    print("")