import random
import sys

title = "Permainan Gunting Batu Kertas"
print(title.center(50, "="))

print("Pilih:\n1. Gunting ✂️\n2. Batu 🪨\n3. Kertas 📃\n")
pilihan_user = input("Masukkan pilihan Anda: ")
pemain = int(pilihan_user)

if pemain < 1 or pemain > 3:
    sys.exit("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")

lawan_bot = random.choice("123")
bot = int(lawan_bot)

print("\nAnda memilih: " + pilihan_user)
print("Bot memilih: " + lawan_bot)


if pilihan_user == 1 and bot == 3:
    print("🥳 Anda menang!")
elif pilihan_user == 3 and bot == 2:
    print("🥳 Anda menang!")
elif pilihan_user == 2 and bot == 1:
    print("🥳 Anda menang!")
elif pilihan_user == bot:
    print("🤝 Permainan Seri!")
else:
    print("😢 Anda kalah!")
