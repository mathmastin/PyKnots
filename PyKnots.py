############################################################
# This file contains the class definitions for working
#   with the augemented whitten group and the
#   associated set of composite links.
#
#
#   Matt Mastin
#   University of Georgia
#   Mathematics Department
############################################################

# we import the copy methods and use them in place
#   of copy constructors when possible
import copy
import pickle


##################################################
# class definition for an element of the whitten
#   group:
#   \gamma_k = \Z^2 \times ((\Z^2)^k \rtimes \S_k)
#
#   m represents the mirror operation, intialized
#       0 to indicate an "empty" gamma_element
#
#   the array r holds the orientation information
#       for each component
#
#   p is an array representing an element in \S_k.
#       the element is stored as the array whose
#       ith coordinate is the image of i under p

class gamma_element():
    def __init__(self, m=None, r=None, p=None):
        self.m = m
        self.r = r
        self.p = p

# this is for string formatting
    def __str__(self):
##        gstr = "["
##        gstr+=(str(self.m)+","+str(self.r)+",")
##        gstr+=(str(con_perm(self.p)))+"]"

        p=con_perm(self.p)

        gstr = "("
        gstr+=(str(self.m))
        for i in self.r:
            gstr+=(","+str(i))
        gstr+=(",")
        if p==[]:
            gstr+=("e")
        else:
            gstr+=("(")
            for i in p:
                gstr+=(str(i))
            gstr+=(")")
        gstr+=(")")

        
        return gstr

# this is for string formatting
    def __repr__(self):
        gstr = "["
        gstr+=(str(self.m)+","+str(self.r)+",")
        gstr+=(str(self.p))+"]"
        return gstr

# here we define the comparison method
    def __cmp__(self, other):

        sp=con_perm(self.p)
        op=con_perm(other.p)
        
        if self.m==other.m and self.r==other.r and self.p==other.p:
            return 0
        if self.m < other.m:
            return 1
        if self.m > other.m:
            return -1
        if self.r < other.r:
            return 1
        if self.r > other.r:
            return -1
        if sp < op:
            return -1
        if sp > op:
            return 1
# now we define a hash
    def __hash__(self):
        hsh=0
        for x in r:
            hsh+=x
        return hsh
    
#
##################################################


##################################################
# class definition for an element of the
#   augmented whitten group
#
#   g is a list of n elements in \Gamma_k for
#    some k
#
#   p is an array representing an element in \S_n.
#       the element is stored as the array whose
#       ith coordinate is the image of i under p

class G_element:
    def __init__(self, n=0, k=0, g=None, p=None):
        self.n = n
        self.k = k
        self.g = g
        self.p = p

# this is for string formatting
    def __str__(self):
        gstr = "["
        gstr+=(str(self.g)+","+str(self.p))+"]"
        return gstr

# this is for string formatting
    def __repr__(self):
        gstr = "["
        gstr+=(str(self.g)+","+str(self.p))+"]\n"
        return gstr    

# here we define the comparison method
    def __cmp__(self, other):
        if self.n==other.n and self.k==other.k and self.g==other.g and self.p==other.p:
            return 0
        if self.n<=other.n:
            return -1
        else:
            return 1

# now we define a hash
    def __hash__(self):
        hsh=0
        for x in g:
            for y in g.r:
                hsh+=y
        return hsh
        
#
##################################################

##################################################
# class definition for an element of /Omega_{n,k}
#
#
#   cell is a collection of partitions of the set
#    (1,...,n) \times (1,...,k) into
#    \mu = nk-n+1 cells. This is stored as a list
#    of lists of 2-tuples.

class omega_element:
    def __init__(self, cell=None):
        self.cell = cell

# this is for string formatting
    def __str__(self):
        gstr=(str(self.cell))
        return gstr

# this is for string formatting
    def __repr__(self):
        gstr=(str(self.cell))
        return gstr

# here we define the comparison method
    def __cmp__(self, other):
        if self.cell == other.cell:
            return 0
        if self.cell<other.cell:
            return -1
        else:
            return 1

# now we define a hash
    def __hash__(self):
        return 0
        

#
##################################################

##################################################
# class definition for an element of X
#
#
#   g is an element of \Gamma_k for some k
#
#   w is list of omega_elements

class X_element:
    def __init__(self,n=0, k=0, g=None,w=None):
        self.n = n
        self.k = k
        self.g = g
        self.w = w

# this is for string formatting
    def __str__(self):
        gstr=(str(self.g)+","+str(self.w))
        return gstr

# this is for string formatting
    def __repr__(self):
        gstr=(str(self.g)+","+str(self.w)+"\n")
        return gstr

# here we define the comparison method
    def __cmp__(self, other):
        if self.n==other.n and self.k==other.k and self.g==other.g and self.w==other.w:
            return 0
        if self.n<=other.n:
            return -1
        else:
            return 1

# now we define a hash
    def __hash__(self):
##        hsh=0
##        for x in g.r:
##            hsh+=x
        return 0

#
##################################################

############################################################
# This file contains the method implimentations for working
#   with the augemented whitten group and the
#   associated set of composite links.
#
#
#   Matt Mastin
#   University of Georgia
#   Mathematics Department
############################################################


##################################################
# Method to compute the Cartesian cross product
#   on the lists passed in
#
# From -> http://code.activestate.com/recipes/159975/
# Thanks Raymond Hettinger!!
def cross(*args):
    ans = [[]]
    for arg in args[0]:
        ans = [x+[y] for x in ans for y in arg]
    return ans
#
##################################################


##################################################
# Method to build the group \S_n
#   we build \S_n inductively
#
#   
#####################
##OLD CODE!!!!!!!!!!!
##def build_S_n(n):
##
##    S_1 = [[1]]
##    S_2 = [[1],[1,2]]
##
##    if n==1:
##        return S_1
##    if n==2:
##        return S_2
##
##    elts=[1,2]
##
##    S_n=[[1],[2],[1,2]]
##
##    for i in range(3,n+1):
##        for x in S_n:
##            for j in range(1,len(x)):
##                temp=copy.deepcopy(x)
##                temp.insert(len(x)-j,i)
##                S_n.append(copy.deepcopy(temp))
##
##    return S_n
#####################
def build_S_n(n):

    S_1 = [[1]]
    S_2 = [[1,2],[2,1]]

    if n==1:
        return S_1
    if n==2:
        return S_2

    S_n=S_2
    S_n1=list()

    for k in range(3,n+1):
        S_n1=[]
        for i in range(1,k+1):
            for z in S_n:
                x=copy.deepcopy(z)
                for j in range(0,len(x)):
                    if x[j]==i:
                        x[j]=k
                x.append(i)
                S_n1.append(x)
        S_n=copy.deepcopy(S_n1)
                
    S_n1.sort()
    return S_n1
#
##################################################


##################################################
# Method to build \Omega_{n,k}
#
#   !!!This currently only works for n=2,k=2
#       and n=2,k=1

def build_omega(n,k):

    if n==2 and k==2:

        omega1=omega_element([[(1,1),(2,1)],[(1,2)],[(2,2)]])
        omega2=omega_element([[(1,1),(1,2)],[(1,2)],[(2,1)]])
        omega3=omega_element([[(1,2),(2,1)],[(1,1)],[(2,2)]])
        omega4=omega_element([[(1,2),(2,2)],[(1,1)],[(2,1)]])

        omega=[omega1,omega2,omega3,omega4]
    else:
        omega=[[[(1,1),(2,1)]]]


    return omega

#
##################################################


##################################################
# Method to build the group \Gamma_n
#

def build_gamma(n):
    
    Z_2 = [1,-1]
    S_n = build_S_n(n)
    gamma = []
    base_set = []

    base_set.append(Z_2)

    for i in range(0,n):
        base_set.append(Z_2)

    base_set.append(S_n)
 
    cross_set = cross(base_set)

    for j in range(0, len(cross_set)):
        gamma.append(gamma_element(
            cross_set[j][0],cross_set[j][1:n+1],
                cross_set[j][n+1]))

    return gamma

#
##################################################


##################################################
# Method to perform the Whitten operation on two
#   elements of \Gamma_n
#
#   x and y are whitten elements in \Gamma_k,
#       stored as gamma_element()
#
#   returns the whitten product of x and y

def whit_mult(x, y):

    r = [0] * len(x.r)
    p = [0] * len(x.p)

    for i in range(0, len(x.r)):
        r[i]=x.r[i] * y.r[(x.p[i])-1]

    for i in range(0, len(x.p)):
        p[i]=y.p[(x.p[i])-1]

    return gamma_element(x.m*y.m,r,p)
                   
#
##################################################


##################################################
# Method to build the group \G_{n,k}
#

def build_G(n,k):
    Gamma_k = build_gamma(k)
    S_n = build_S_n(n)
    G = []

    base_set = [0] * int(n+1)

    for i in range(0, n):
        base_set[i] = Gamma_k

    base_set[n] = S_n

    cross_set = cross(base_set)
    
    for x in cross_set:
        G.append(G_element(n,k,x[0:n],x[n]))
        
    return G

#
##################################################


##################################################
# Method to build the set X
#

def build_X(n,k):
    Gamma_k = build_gamma(k)
    omega=build_omega(n,k)
    X = []

    base_set = [0] * int(n+1)

    for i in range(0, n):
        base_set[i] = Gamma_k

    base_set[n] = omega
    
    cross_set = cross(base_set)

    for x in cross_set:
        X.append(X_element(n,k,x[0:n],
                           omega_element(x[n])))

    return X

#
##################################################


##################################################
# Method to perform the action of G on
#   \Omega_{n,k}
#

def g_on_omega(g, w):

    # there should be a nice way to do this
    #   without having to deepcopy...
    gw = copy.deepcopy(w)

    for x in gw.cell:
        for z in x:
            z = (g.p[z[0]-1],g.g[z[0]-1].p[z[1]-1])
        
    return gw

#
##################################################


##################################################
# Method to perform the action of G on X
#

def g_on_X(g, x):

    gx = X_element(x.n,x.k,[],[])

    for i in range(0,x.n):
        gx.g.append(whit_mult(g.g[i],x.g[g.p[i]-1]))
        
    gx.w = g_on_omega(g,x.w) 

    return gx

#
##################################################


##################################################
# Method to generate subgroups of G
#
# This method will take an array of G_elements
#   and generate the smallest subgroup of G
#   containing all elements in the array




#
##################################################

##################################################
# Method to generate subgroups of Gamma_k
#
# This method will take an array of gamma_elements
#   and generate the smallest subgroup of Gamma_k
#   containing all elements in the array

def sub_gamma(elements):
    
    for i in elements:
        while(elements.count(i) > 1):
            elements.remove(i)
        
    subgroup=copy.deepcopy(elements)
    flag=1
    while(flag):
        size=len(subgroup)
        for i in subgroup:
            for j in subgroup:
                x=whit_mult(i,j)
                if subgroup.count(x)==0:
                    subgroup.append(x)
            if size==len(subgroup):
                flag=0
    subgroup.sort()
    return subgroup
#
##################################################

##################################################
# Method to generate cosets of a subgroup of
#   Gamma_k
#
# This method will take in a subgroup of Gamma_k
#   as a list of Gamma_elements and the group
#   Gamma_k and return a list of the cosets as
#   lists

def gamma_cosets(subgroup,gam):
    cosets=list()
    ctemp=list()
    for i in gam:
        for j in subgroup:
            gtemp=whit_mult(i,j)
            if ctemp.count(gtemp)==0:
                ctemp.append(gtemp)
        ctemp.sort()        
        if cosets.count(ctemp)==0:
            cosets.append(ctemp)
        ctemp=[]        

    return cosets

#
##################################################



##################################################
# Method to read G generators from a file
#
# This method will read a list of G elements from
#   <infile> and store them as a list of G_elements.

def read_G(infile):




    return None

#
##################################################

##################################################
# Method to convert a string into a gamma_element
#

def str_to_gamma(s):

    k=((s.count(",")-1)/2)+1

    r=[0]*k
    p=[0]*k

    s=s.replace("["," ")
    s=s.replace(","," ")
    s=s.replace("]"," ")
    s=s.replace("\n"," ")

    g = s.split()

    print g
    
##    m=int(g[0])

    for i in range(0,k):
        r[i]=int(g[i+1])

    for i in range(0,k):
        p[i]=int(g[k+1+i])

    return gamma_element(m,r,p)
#
##################################################

##################################################
# Method to convert a string into a G_element
#

def read_gens(infile, n):

    gens = [[]]*n
    i=0

    s=infile.readlines()

    s=str(s).split("*")

    print str(s[0])

##    for i in range(0,n):
##        for x in s:
##            #gens[i].append(str_to_gamma(x))
##            print str(x)

##    for j in range(0,n):
##        while(s[i]!="*"):
##            gens[i].append(str_to_gamma(s[i]))
##            i+=1
##        i+=1

    return gens
#
##################################################

##################################################
# Method to generate tex code for tables of
#   coset representatives
#

def gen_coset_table(G,subgs,sgnames,f):

    cos=[]

    #for i in subgs:
    #    cos.append(gamma_cosets(i,G))
    dubslash = "\\\\"

    print >>f, "%code to generate tables"
    print >>f, "\\begin{center}"
    print >>f, "\\begin{longtable}{|l|l|}"
    print >>f, "\hline"
    print >>f, "\multicolumn{2}{|c|}{List of Groups} ",dubslash
    print >>f, "\hline"

    k=0
    for i in subgs:
        print >>f, "\multirow{",len(i),"}{*}{",sgnames[k],"}"
        for j in i: 
            print >>f, "&","$", j,"$", dubslash
        print >>f, "\hline"
        k=k+1

    print >>f, "\end{longtable}"
    print >>f, "\end{center}"

    return None
#
##################################################

##################################################
# Method to output groups to a text file
#   link is a the name of the link as a strink and
#   gens is a list of the generators of the group
#

def print_group(link,gens):

    outf=open(link+".txt",'w')
    
    subg=sub_gamma(gens)
    subg.sort()
    
    print >>outf, "The following is the symmetry subgroup for ", link
    
    print >>outf, "Size of group: ", len(subg)
    
    print >>outf, "Generators (probably too many here):"
    for j in gens:
        print >>outf, j
        
    print >>outf, "Group Elements:"
    for i in subg:
        print >>outf, i
        
    outf.close()

    return None

#
##################################################

##################################################
# Method to convert a permutation to cycle
#   notation
#
#   !!!!!!!!CURENTLY ONLY WORKS FOR N<=3!!!!!!!!!

def con_perm(p):

    cycle=[]

    for i in range(0,len(p)):
        if (p[i]!=i+1):
            break

    if (i==len(p)-1):
        return cycle
    
    cycle.append(i+1);

    j=i
    
    while(p[j]!=i+1):
        cycle.append(p[j])
        j=p[j]-1
    
    return cycle


#
##################################################

##################################################
# Method to convert a permutation from cycle to
#   vector notation

def cycle_to_vect(p):

    vect = []
    
    

    return vect

#
##################################################

##################################################
#

def new_tex_file(outfile):

    print >>outfile, "%This file was created by Matt Mastin"

    infile = open("open_tex.dat",'r')

    for line in infile:
        print >>outfile, line

    infile.close()

    return None

#
##################################################

##################################################
#
def close_tex_file(outfile):

    infile = open("close_tex.dat",'r')
    
    for line in infile:
        print >>outfile, line

    infile.close()

    return None

#
##################################################

##################################################
#

def make_gamma_ws(n):
    gamma = build_gamma(3)
    




    return None

#
##################################################

##################################################
#
def strip_list(L_orig):
    L=copy.deepcopy(L_orig)
    elt = list()
    parenStack=list()

    Delim=chr(L.popleft())
    if ord(Delim==40):
        Offset=1
    else:
        Offset=2
    
    
    parenStack.append(L[0])
    delim=chr(L[0])
    if ord(delim==40):
        offset=1
    else:
        offset=2

    while(len(parenStack!=0)):
        elt.append(L[0])
        if(L[0]==delim):
            parenStack.append(L[0])
        if(L[0]==chr(ord(delim)+offset)):
            parenStack.pop()
    
    



    return elt





#
##################################################


##################################################
# Definitions of subgroups

S_2_1=[0,6]
S_4_1=[0,1,6]
S_4_2=[0,6,2]
S_8_1=[0,1,6,2]
S_8_2=[0,6,1,10]

presubgs=[S_2_1,S_4_1,S_4_2,S_8_1,S_8_2]

sgnames=["$\Sigma_{2,1}$","$\Sigma_{4,1}$","$\Sigma_{4,2}$","$\Sigma_{8,1}$","$\Sigma_{8,2}$"]

#
##################################################

##################################################
# Read list from file
def read_list(infile):
    outfile=open("readlist.py",'w')
    l=infile.read()

    s="l=" + l

    s=s.replace("{","[")
    s=s.replace("}","]")
    s=s.replace('(','[')
    s=s.replace(')',']')

    print >>outfile, "import pickle"
    print >>outfile, s
    print >>outfile, "outfile=open(\"readlist.txt\",\'w\')"
    print >>outfile, "pickle.dump(l,outfile)"
    print >>outfile, "outfile.close()"

    outfile.close()

    #print s

    execfile("readlist.py")

    ifile=open("readlist.txt",'r')

    L=pickle.load(ifile)

    ifile.close()

    return L

#
##################################################

##################################################
# Convert list in the form {1,{1,1,1},{1,2,3}} =
#   (1,1,1,1,e) to gamma element

def list_to_gamma(L):

    g=gamma_element(L[0],L[1],L[2])

    return g

#
##################################################

##################################################
# 

def possible_subgroups(GRP, N):

    #get number of components
    n=len(GRP[0].r)

    #build appropriate \Gamma
    gamma=build_gamma(n)

    #this will be our list of possible
    #   subgroups
    GRPS=[]

    #this will be a list of elements
    #   which are not in the sbgrps
    OUT=copy.deepcopy(N)

    #Add group generated by GRP as the first
    #   element in our list of possible
    #   groups
    GRPS.append(sub_gamma(GRP))

    #we know that the product of an element
    #   in OUT with one in GRP is NOT in,
    #   so we remove them
    for i in N:
        for j in GRPS[0]:
            elt=whit_mult(i,j)
            if(OUT.count(elt)==0):
                OUT.append(elt)
                
    #left will be our list of elements which
    #   are still candidates, at this point
    #   we just remove from gamma the guys
    #   in OUT and any element accounted
    #   for in GRPS
    left=copy.deepcopy(gamma)
    for i in OUT:
        left.remove(i)
    for i in GRPS:
        for j in i:
            if left.count(j)!=0:
                left.remove(j)

    #if we have already accounted for all
    #   all elements in gamma... then we
    #   are done and we return GRPS
##    if(left==GRPS[0]):
##        return GRPS   
##    while(len(left)!=0):
##        print len(left)
##        GRPS=add_gens(GRPS, left, OUT)
##        for i in GRPS:
##            for j in i:
##                if left.count(j)!=0:
##                    left.remove(j)
##        print "size of left =", len(left)

##    for i in range(0,len(left)):
##        print len(GRPS)
##        GRPS = add_gens(GRPS, left, OUT)
##
##    for i in GRPS:
##        if(GRPS.count(i)!=1):
##            GRPS.remove(i)
##
##    flag = 1
##    #for i in range(0,2):
##    GRPS_len = len(GRPS)
##
##    print "length of groups = ", len(GRPS)
##    for k in GRPS:
##        TEMP=add_gens(k,left, OUT)
##        print "length of temp: ", len(TEMP)
##        
##        for j in TEMP:
##            if(GRPS.count(j) == 0):
##                GRPS.append(j)
                
##    if(len(GRPS) == GRPS_len):
##        flag = 0


    TEMPLIST=copy.deepcopy(GRPS)
    flag = 1
    while(flag == 1):
        size = len(GRPS)
        for i in TEMPLIST:
            NEWGRPS = add_gens(i,left,OUT)

            for j in NEWGRPS:
                if(GRPS.count(j)==0):
                    GRPS.append(j)
        TEMPLIST=copy.deepcopy(NEWGRPS)
        NEWGRPS=[]

        if(len(GRPS)==size):
            flag = 0
            

    return GRPS

#
##################################################

##################################################
#

def add_gens(grp, left, OUT):

    NEWGRPS=[]
    newgns=[]

    print "starting with group: "
    for i in grp:
        print i

    for i in left:
        for k in grp:
            newgns.append(k)
        newgns.append(i)

        print "gens:"
        for j in newgns:
            print j

        newgrp=sub_gamma(newgns)        

        print "group:"
        print len(newgrp)
        for j in newgrp:
            print j

        flag = 1

        for i in OUT:
            if(newgrp.count(i)!=0):
                flag=0

        if(NEWGRPS.count(newgrp)==0 and flag==1):
            NEWGRPS.append(newgrp)
        
        newgns=[]
        newgrp=[]
    
##    for i in left:
##        for j in GRPS:
##            newgens=copy.deepcopy(j)
##            newgens.append(i)
##            newgp=sub_gamma(newgens)
##            #print len(newgp)
##            if(NEWGRPS.count(newgp)==0):
##                flag = 1
##                for k in OUT:
##                    if(newgp.count(k)!=0):
##                        flag=0
##                if(flag==1):
##                    NEWGRPS.append(newgp)

    return NEWGRPS

#
##################################################

##################################################
# Read group from file
def read_group(infile):

    L=read_list(infile)

    grp=[]

    for i in L:
        grp.append(gamma_element(i[0],i[1],i[2]))

    return grp


#
##################################################

############################################################
# Test Code
############################################################

##ifile=open("s21.txt",'r')
##sg=read_list(ifile)
##
##subg=[]
##for i in sg:
##    subg.append(list_to_gamma(i))
##
##N=[gamma_element(-1,[1,1],[1,2])]
##
##POS=possible_subgroups(subg, N)
##
##outfile=open("results_from _POS.txt",'w')
##
##print >>outfile, POS
##
##outfile.close()
##
##ifile.close()





##Gamma2=build_gamma(2)
###for i in range(0,len(Gamma3)-1):
###    print i, " ", Gamma3[i]
##
#presgens=[0,19,16,2,35,42,27,44,17]
##presgens=[0,1]
##
##sgens=[]
##for i in presgens:
##    sgens.append(Gamma2[i])
##    print Gamma2[i]
##
##outfile=open("S21.txt",'w')
##
##sg=sub_gamma(sgens)
##
##print sg
##print >>outfile, sg
##outfile.close()
##
##print len(sg)
##for i in sg:
##    print i,"\n"

##outfile=open("group.txt",'w')
##
##print >>outfile, sg
##
##outfile.close()

##infile=open("group.txt",'r')
##
##L=read_list(infile)
##
##
##print "here"
##print list_to_gamma(L[0])
##
##SUBGP=[]
##
##for i in L:
##    SUBGP.append(list_to_gamma(i))
##

##
##N.append(list_to_gamma([1,[1,1,1],[1,3,2]]))

#TEST=possible_subgroups(sg, N)

#for i in TEST:
    #print len(i)

#outf=open("pos_text.txt",'w')

#print >>outf, TEST

#outf.close()
        
##ifile=open("pos_text.txt",'r')
##
##TEST=read_list(ifile)
##
##print TEST


##################################################
#Test code for generating tables


##outfile = open("mtex_test.tex",'w')
##
##new_tex_file(outfile)
##
##gam=build_gamma(2)
##gens=[]
##temp=[]
##subgs=[]
##
##for i in presubgs:
##    for j in i:
##        temp.append(gam[j])
##    gens.append(temp)
##    temp=[]
##                
##for i in gens:
##    subgs.append(sub_gamma(i))
##
##gen_coset_table(gam,subgs,sgnames, outfile)
##
##close_tex_file(outfile)
##
##outfile.close()
#
##################################################

##################################################
#Test code for con_perm

##s=build_S_n(3)
##
##for i in s:
##    print con_perm(i)
##    print ""
##
##g=build_gamma(3)
##print g[0]

#
##################################################


##################################################
##infile = open('infile.txt','r')
##
##gens = read_gens(infile, 3)
##
##print gens
##################################################


##################################################
# The following is test code to compute the symmetry
#   subgroups for 7^3_1 and 6^3_2

##gam=build_gamma(3)
##gens=[gam[42],gam[38],gam[16],gam[1]]
##
##gens.sort()
##
##print_group("7^3_1",gens)
##
##gen_nums=[0,18,36,30,25,17,44,48,61,55,74,62,77,59,33,22]
##
##gens2=[]
##
##for i in gen_nums:
##    gens2.append(gam[i])
##
##gens2.sort()
##
##print_group("6^3_2",gens2)

#
############################################################






##subg=sub_gamma(gens)
##
##subg.sort()
##
##outf=open("7^3_1.txt",'w')
##
##print >>outf, "The following is the symmetry subgroup for 7^3_1"
##print >>outf, "Size of group: ", len(subg)
##print >>outf, "Generators:"
##for j in gens:
##    print >>outf, j
##print >>outf, "Group Elements:"
##for i in subg:
##    print >>outf, i
##outf.close()

##gam=build_gamma(3)
##print len(gam)
####j=0
####for i in gam:
####    print j
####    print i
####    print "\n"
####    j=j+1
##
##test=sub_gamma([gam[0]])
##print len(test)
##
##cos=gamma_cosets(test,gam)
##
##print len(cos)
##
##for i in cos:
##    print i










############################################################
# Test Code for input from file to groups

##infile = open('infile.txt','r')
##outfile = open('outfile.txt','w')
##
##
##
##G = build_G(2,2)
##X = build_X(2,2)
##sigma = [0,1,2,3,8,9,10,11]
##
##gamma = build_gamma(2)
##
##print gamma
##
##orbit1 = set()
##orbit2 = set()
##
##for i in sigma:
##    outfile.write(str(G[i])+"\n")
##
##s = "[[[1,[1],[1]], [1,[1],[1]]],[1, 2]]"
##
##
##infile.close()
##outfile.close()

#
############################################################


##k=8
##print str(X[k])+"\n"
##for g in sigma:
##    print G[g]
##    orbit1.add(g_on_X(G[g],X[k]))
##
##print orbit1
##
##k=0
##print str(X[k])+"\n"
##for g in sigma:
##    orbit2.add(g_on_X(G[g],X[k]))
##
##print orbit2

