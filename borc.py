def marketborclari():
    borc = int(input("borcunuz ne kadar?"))
    borcode = int(input("borcunuzun ne kadarını ödemek istiyorsunuz"))
    borckalan= (int(borc)-int(borcode))
    print(f"borcunuz {borc},ödediğiniz borç{borcode},kalan borc{borckalan} ")
marketborclari()