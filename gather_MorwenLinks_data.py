import classdefs

Sigs_infile=open("MorwenLinksSigmas.txt",'r')
Sigs=read_list(Sigs_infile)

DT_infile=open("MorwenLinksDT.txt",'r')

DTin=DT_infile.read()

DT=DTin.splitlines()

DATA=[]
temp_list=[]

for i in range(0,len(DT)):
    temp_list.append(convertDT(DT[i],2))
    temp_list.append(Sigs[i])
    DATA.append(temp_list)
    temp_list=[]

outfile=open("MorwenLinks_DT_Sigmas.txt",'w')

print >>outfile, DATA

outfile.close()

DT_infile.close()

Sigs_infile.close()
