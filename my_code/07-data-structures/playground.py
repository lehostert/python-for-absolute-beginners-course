
# Data structures
# 1. Dictionaries
# 2. Lists / arrays [1,1,7,11]
# 3. Sets

# List:
# Getting items in order, keeping them in order, and selecting specific elements of that list
print("List Example")
lst =[1,1,11,17]
print(lst[3])
print(lst)
lst.append(11)
print(lst)

lst.sort()
print(lst)

# Set:
# distinct items only
print("Set Example")
st = {1, 1, 11, 7}
st.add(1)
st.add(11)
print(st)
print()

# Dictionaries
# Given a Name/Key define a value
d = {
     'bob': 0,
     'sarah': 0
}
print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)

