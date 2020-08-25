class dog:

    species="animal"

    def __init__(self,name,age):
        self.name=name
        self.age=age



german=dog("german",10)
australian=dog("australian",8)


print("german is a {}".format(german.__class__.species))
print("australian is a {}".format(australian.__class__.species))


print("{} is {} years old".format(german.name,german.age))
print("{}is {} year old ".format(australian.name,australian.age))


