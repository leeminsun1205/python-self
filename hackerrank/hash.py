n = int(input())
elements = tuple(map(int, input().split()))

# Step 2: Create a tuple
t = tuple(elements)

# Step 3: Compute the hash value
hash_value = hash(t)

# Step 4: Print the result
print(hash_value)