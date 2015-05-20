gam=build_gamma(2)

subgroups=[]

for i in gens:
    subgroups.append(sub_gamma(i))

conj_lists=[]
temp_list1=[]
temp_list2=[]
count=0

outfile1=open("conj_numbers.txt",'w')

for i in subgroups:
    for g in gam:
        temp_group=conj_group(i,g)
        temp_group.sort()
        if temp_list1.count(temp_group)==0:
            temp_list1.append(temp_group)
    print >>outfile1, sgnames[count], " has ",len(temp_list1)," conjugate subgroups."
    temp_list2.append(sgnames[count])
    temp_list2.append(temp_list1)
    count=count+1
    conj_lists.append(temp_list2)
    temp_list1=[]
    temp_list2=[]

outfile1.close()


outfile = open("gamma2_conj_classes.txt",'w')
print >>outfile, conj_lists

outfile.close()
        
