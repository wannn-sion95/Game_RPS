import random


def play_rock_paper_scissors():
    choices = ['gunting', 'batu', 'kertas']
    print("Selamat datang di permainan Gunting, Batu, Kertas!\n")
    while True:
        user_choice = input(
            "Pilih\n1. Gunting ✂️\n2. Batu 🪨\n3. Kertas 📃\n\n(Jika anda ingin berhenti bermain, ketik 'quit'): ").strip().lower()
        print("\nKamu memilih:", user_choice)

        if user_choice == 'quit':
            print("Terima kasih telah bermain! Sampai jumpa!")
            break

        if user_choice not in choices:
            print("Pilihan tidak valid. Pilih 3 pilihan itu.")
            continue

        computer_choice = random.choice(choices)
        print(f"Bot memilih: {computer_choice}")

        if user_choice == computer_choice:
            print("😲 Permainan Seri!")
        elif (user_choice == 'batu' and computer_choice == 'gunting') or \
             (user_choice == 'kertas' and computer_choice == 'batu') or \
             (user_choice == 'gunting' and computer_choice == 'kertas'):
            print("🥳 Kamu menang!\n")
        else:
            print("🥲", " ", "Kamu kalah!\n")


play_rock_paper_scissors()
