# Generate the tables from 2 to 20 in all the seperate text files 

def generate(n):
    for i in range(n):
        table = ""
        for i in range(1,11):
            table += f"{n} x {i} = {n*i}\n"
    
    with open(f"Tables/table_{n}.txt","w") as f: #Creating table.txt in Tables folder
        f.write(table)
        
for i in range(2, 21):
    generate(i)
    
    # This probllem is kind of hassle and consists many txt file in a folder Tables