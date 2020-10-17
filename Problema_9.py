a=int(input("Introduceti numarul de bile mici:",a))
b=int(input("Introduceti numarul de bile mari:",b))
a1a=int(input("Introduceti numarul de bile mici albe:",a1a))
a1r=int(input("Introduceti numarul de bile mici rosii:",a1r))
a1v=int(input("Introduceti numarul de bile mici verzi:",a1v))
b1a=int(input("Introduceti numarul de bile mari albe:",b1a))
b1r=int(input("Introduceti numarul de bile mari rosii:",b1r))
b1v=int(input("Introduceti numarul de bile mari verzi:",b1v))
mari=b1a+b1v+b1r
mici=a1a+a1v+a1r
if mari>mici
   print("mari=",mari)
else print("mici=",mici)
a=a1a+b1a
r=a1r+b1r
v=a1v+b1v
if((a>r) and (a>v))
   print("Bile albe=",a)
if((r>a) and (r>v))
   print("Bile rosii=",r)
else print("Bile verzi=",v)