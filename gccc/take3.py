from z3 import *

flag=[70,76,65,71,123,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125]

the_xor=[164,189,185,59,69,219,128,71,234,22,249,118,224,27,101,66,42,66,208,0,249,240,43,251,158,40,22,74,76,87,82,124]

X=BitVec('x',39)
Z=[Extract(i+7,i,X)for i in range(32)]
XAX=[Z[i] ^ the_xor[i]for i in range(32)]

ng_cc = [And(65<=XAX[i],XAX[i]<=90)for i in range(0,32)]
ng2_c = [Or(ng_cc[i],XAX[i]==32,XAX[i]==123,XAX[i]==125)for i in range(32)]

flag_c = [If( flag[i]==0 ,ng2_c[i] , XAX[i] == flag[i] )for i in range (32)]
s=Solver()
print flag_c
s.add(flag_c)
print s.check()
print s.model()
