import numpy as nm

rlist=[[1,2,3,4,5],[6,7,8,9,0]]

#convert to 2D array

rarray=nm.asarray(rlist)
print("rlist={}\nrarray=\n{}".format(rlist,rarray))

print("Slicing\n{}------list {}".format(rarray[1,-1],rlist[1][-1]))
