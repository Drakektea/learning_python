class Tea:
    __a = 1
    b = 2
    _c = 3


tea1 = Tea()
tea2 = Tea()

tea1.b = 3
Tea._Tea__a = 9

Tea.e = 4
print(Tea.e)

print(tea1._Tea__a)
