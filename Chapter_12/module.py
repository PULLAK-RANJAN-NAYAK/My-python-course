# This module file is used to show __name__ and main behavior
# It can be run directly or imported into 9_main.py

def myFunc():
    print("Hello main")

# CASE 1: When this IF block IS written
if __name__ == "__main__":
    print("We are directly running this file")
    myFunc()
    print(__name__)

# CASE 2: If this IF block is NOT written
# (i.e., if myFunc() and print(__name__) were written directly)
# → They would execute BOTH when:
#   1) this file is run directly
#   2) this file is imported into 9_main.py
#
# Using this IF block prevents automatic execution on import
