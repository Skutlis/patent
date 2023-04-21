
c = 0
newFile = ""
with open("extraData\\patent_txt_raw.csv", "r") as f:
    for line in f:
        c += 1
        if c == 50000:
            break
        newFile += line


fl = open("extraData\\50000_patents.csv", "x")
fl.write(newFile)
fl.close()



