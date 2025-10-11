# Enter the value or replace your name and the date with the entered date in the letter

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''
                          
print(letter.replace("<|Name|>","Ranjan").replace("<|Date|>","09-10-2025")) # This is an wise way 
                                                                            # You can do chaining of .replace