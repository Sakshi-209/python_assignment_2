element={"apple","orange","banana","pineapple","guava"};

#bY USING remove()
#if ur removing item is not present in the set then remove give us a error
element.remove("guava");
print(element);

#we use repeat use remove item as guava then they give us error
#element.remove("guava");
#print(element);

#BY USING discard()
#if ur removing item is not present in the set then discard doesn't give us a error
element.discard("banana");
print(element);

#we use repeat use remove item as banana then they doesn't give us error
element.discard("banana");
print(element);