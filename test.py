kabise = [1, 5, 9, 13, 17, 22, 26, 30]
sal = []

j=0
num = input(" Enter a number: ")
check_kabise = ( int(num) % 33)
for i in range(1, int(num)+1):
    if (i % 33) in kabise:
        sal.append(i)
        j += 1

if check_kabise in kabise:
    print("kabise ast.")
else:
    print("mamooooooli ast.")

print(" ")
print(f"sal kabise from (j):{j}")
print("sal kabise:", sal)