# Match is similar to switch case in c language 

def http_status(status):
    match status:
        case 200:
            return "OK"

        case 404:
            return "Not found"
        
        case 500:
            return "Internal server error"
        
        case _:
            return "Unknown Error"
        
status = int(input("Enter the case(200,404,500,_) : "))
result = http_status(status)
print(result)