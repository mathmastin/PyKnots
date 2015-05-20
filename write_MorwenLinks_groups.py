C=MorwenLinks(2)

groups=[]

S=[]

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
        Groups.append("Not Hyperbolic")

outfile=open("C:\Users\Mastin\Documents\compositelinks\symmetrypaper\snappea_calcs\MorwenLinksSigmas.txt",'w')

print >>outfile, Groups

outfile.close()

