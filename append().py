tup1=("apple","banana","orange","guava");
#append by converting to list
x=list(tup1);
x.append("sakshi");
tup1=tuple(x);
print(tup1);

#add tuple to tuple
tup2=("pineapple",);
tup1+=tup2;
print(tup1);