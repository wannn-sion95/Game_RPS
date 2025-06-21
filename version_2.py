import random
import sys
from enum import Enum


class GBK(Enum):

    GUNTING = 1
    BATU = 2
    KERTAS = 3


title = "Permainan Gunting Batu Kertas"
print(title.center(50, "="))

print("Pilih:\n1. Gunting ✂️\n2. Batu 🪨\n3. Kertas 📃\n")
pilihan_user = input("Masukkan pilihan Anda: ")
pemain = int(pilihan_user)

if pemain < 1 or pemain > 3:
    sys.exit("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")

lawan_bot = random.choice("123")
bot = int(lawan_bot)

print("\nAnda memilih  : " + str(GBK(pemain)).replace('GBK.', ""))
print("Bot memilih   : " + str(GBK(bot)).replace('GBK.', ""))


if pemain == 1 and bot == 3:
    print("\n🥳 Anda menang!")
elif pemain == 3 and bot == 2:
    print("\n🥳 Anda menang!")
elif pemain == 2 and bot == 1:
    print("\n🥳 Anda menang!")
elif pemain == bot:
    print("\n🤝 Permainan Seri!")
else:
    print("\n😢 Anda kalah!")
    
