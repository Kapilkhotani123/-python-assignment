number = [1,2,3,4,5,6,7,8,9,10]

print("Original list: ",end="")
org = number[0:9:1]
print(org,end="")

print("\nExtracted first five elements: ",end="")
first = number[0:5:1]
print(first,end="")
print("\nReversed extracted elements: ",end="")
rev = first[::-1]
print(rev)

