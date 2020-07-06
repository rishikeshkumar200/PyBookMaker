l1=0
with open("sample.txt") as f:
    with open("out2.txt", "w") as f1:
        for line in f:
            f1.write(line)
            l1=len(line)+l1
            f1.write("(" + str(l1) + ")")
            