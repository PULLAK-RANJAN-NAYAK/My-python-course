# WAP to remove and strip the word from the list and even the list

def remove(l,word):
    n = []
    for item in l:
        if(item!=word):
            n.append(item.strip(word))
    return n 
    
l = ["Ranjan","Pullak","Nayak","an"]
print(remove(l,"an"))
        
    