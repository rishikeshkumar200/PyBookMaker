
def banao(name):
    l1=0
    with open("output/" + str(name) + ".txt") as f:
        with open("final/" + str(name) +".txt", "w") as f1:
            for line in f:
                l1=len(line)+l1
                f1.write("(" + str(l1) + ")" + "\t" +"")
                f1.write(line)


            

        

    

            