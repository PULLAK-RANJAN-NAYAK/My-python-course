# Break stops the loop immediately while Continue skips the current iteration 

for i in range(100):
    if(i == 35):
        print("Found 35")
        break     # Foget everything and exit the loop
    print(i)      # It stops at 35 

    
                                     # Run both the programs and you will understand
    
    
for i in range(100):
    if(i == 35):
        print(i == 35) # If this print statement is not present it will skip "35" 
        continue    # skips the iterations
    print(i)        # It will skip 35 and move on to the next iteration(36)
    