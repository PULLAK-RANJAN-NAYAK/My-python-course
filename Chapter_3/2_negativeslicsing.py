# So basically this is for interview slicing but in the vice versa way
#    P U L L A K                           P  U  L  L  A  K 
#    0 1 2 3 4 5  (Normal slicing)        -6 -5 -4 -3 -2 -1  (This is negative slicing method)

A = "PULLAK"
print(A[-4:-1])    # This is the output "LLA"

B = "RANJAN"
print(B[-4:-1])   # This is the output NJA 
print(B[1:4])       # ANJ

C = "NAYAK"
print(C[0:4:2])
