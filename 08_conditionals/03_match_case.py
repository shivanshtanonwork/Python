status = int(input("Enter status code"))

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found!")
    case _:
        print("Unknown status") 
