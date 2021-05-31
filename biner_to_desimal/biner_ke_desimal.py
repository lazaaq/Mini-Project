input_1 = input("masukkan angka biner : ")
input_2 = input_1.split()

biner = []
desimal = []

panjang_list = len(input_2)
for i in range (0, panjang_list):
    input_ = int(input_2[i])
    biner.append(input_)

print(biner)
for i in range(0, panjang_list):
    decimal = biner[i]*(2**(panjang_list-i-1))
    desimal.append(decimal)
    
for i in range(0, len(biner)):
    print(biner[i], end="")

print("\n")
print(sum(desimal))
