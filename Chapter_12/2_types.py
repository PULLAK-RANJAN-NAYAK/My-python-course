from typing import list,tuple,Dict,Union

# List of integer 
number : list[int] = [1,2,3,4,5]

# Tuple of a str and interger
person : tuple[str , int] = ("Ranjan", 19)

# Dict with string keys and integer values 
persons : Dict[str,int] = {"Ranjan":19 , "Pullak":18}

# Union type for variable that can hold multiple types
identifier : Union[int , str] = 909090 , "Ranjan"