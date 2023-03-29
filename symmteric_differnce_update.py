element={"apple","orange","banana","pineapple","guava"};
element1={"bus","car","train","orange","guava"};

#BY USING symmetric_difference_update()
#this method will keep only the items that not present in both the sets
element.symmetric_difference_update(element1);
print(element);