def myfunction(myparameter: int) -> str:
    return f'{myparameter+10}'

def otherfunction(otherparameter:str):
    print(otherparameter)

### python 3.9+  def dosth(param:list[int])

print(myfunction(10))

otherfunction(myfunction(20))