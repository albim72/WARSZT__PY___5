class Basic:
    def __init__(self):
        print("obiekt zotał utworzony...")

    def __call__(self,a,b):
        print("instancja jest wywoływana przez funkcję specjalną: __call__")
        print(a**2+b**2)

fn = Basic()
fn(4,7)
