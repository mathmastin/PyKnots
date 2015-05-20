import classdefs
import copy



for i in C:
    try:
        S.append((i.symmetry_group()).isometries())
    except ValueError:
        S.append(0)

Gens=[]

for i in S:
    if i != 0:
        gens=[]
        for j in i:
            if j.extends_to_link():
                m=1
                r=[]
                gen=[]                 
                for l in range(0,len(j.cusp_maps()[0].data)):
                    m=m*j.cusp_maps()[0].data[l][l]
                for k in j.cusp_maps():
                    r.append(k.data[0][0]) #this assumes the meridian corresponds to [0][0]
                                                    #but this seems to be correct... -m

                    
                gen.append(m)
                gen.append(r)
                gen.append(j.cusp_images())
                for k in range(0,len(gen[2])):
                    gen[2][k]=gen[2][k]+1
                if gens.count(list_to_gamma(gen))==0:
                    gens.append(list_to_gamma(gen))
        Gens.append(gens)
    else:
        Gens.append(0)

Groups=[]


for i in Gens:
    if i != 0:
        Groups.append(sub_gamma(i))
    else:
        Groups.append(0)

##the following code will print the groups to file
outfile = open(str(N)+".txt",'w')
print >>outfile, "Intrinsic symmetry groups as calculated by SnapPea"
print >>outfile, ""
print >>outfile, ""
print >>outfile, "Out of", len(C), "links SnapPea could not calcuate the groups",
print >>outfile, "for the following", S.count(0), "links:"
for i in range(0,len(C)):
    if S[i] == 0:
        print >>outfile, C[i]
print >>outfile, "----------------------------------------"
print >>outfile, ""
print >>outfile, ""

for i in range(0,len(C)):
    print >>outfile, C[i]
    print >>outfile, ""
    if Groups[i] == 0:
        print >>outfile,"SnapPea was not able to compute the symmetry group for this link."
        print >>outfile, "It is likely that ",C[i]," is not hyperbolic."
        print >>outfile, ""
    else:
        print >>outfile, "Group is order ",len(Groups[i]),"."
        for k in Groups[i]:
            print >>outfile, k
    print >>outfile, "----------------------------------------"

outfile.close()

























