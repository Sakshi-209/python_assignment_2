element={"apple","orange","banana","pineapple","guava"};
element1={"bus","car","train","orange","guava"};
#BY USING symmetric_differnce()
#this method will return a new set that contains only the items that are not present in both the sets
z = element.symmetric_difference(element1);
print(z);