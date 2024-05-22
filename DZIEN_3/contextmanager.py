class ContextManager:
    def __init__(self):
        print("wywołanie funkcji __init__")

    def __enter__(self):
        print("wywołanie funkcji __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("wywołanie funkcji __exit__")


with ContextManager() as manager:
    print("wykonanie bloku with...")
