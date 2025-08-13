def salary(**kwargs):
    #kwargs is a dictionary with all the key value pairs which were passed to salary
    for item in kwargs.keys():
        print(f"The salary of {item} is {kwargs[item]}")

salary(shivansh=150000, vidushi=125000, himanshu=250000)