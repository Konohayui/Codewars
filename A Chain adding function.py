class custom_add(int):
    def __call__(self, num):
        return custom_add(self + num)
        
def add(num):
    return custom_add(num)
