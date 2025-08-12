def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
    
@repeat(6)
def manifest_job(a):
    print(f"I got 20lpa {a}")

manifest_job("Job")