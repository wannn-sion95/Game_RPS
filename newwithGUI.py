import customtkinter as ctk
import random
from enum import Enum
from tkinter import messagebox


class GBK(Enum):
    GUNTING = 1
    BATU = 2
    KERTAS = 3


def mainkan(pilihan_user):
    bot = random.randint(1, 3)
    user_choice = GBK(pilihan_user).name.capitalize()
    bot_choice = GBK(bot).name.capitalize()

    if pilihan_user == bot:
        hasil = "🤝 Permainan Seri"
    elif (pilihan_user == 1 and bot == 3) or \
         (pilihan_user == 2 and bot == 1) or \
         (pilihan_user == 3 and bot == 2):
        hasil = "🥳 Kamu Menang!"

    else:
        hasil = "😢 Kamu Kalah!"

    result_label.configure(
        text=f"Anda memilih: {user_choice}\nBot memilih: {bot_choice}\n\n{hasil}")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Wannn | Sion ")
app.geometry("400x500")

judul = ctk.CTkLabel(app, text="Gunting Batu Kertas",
                     font=ctk.CTkFont(size=24, weight="bold"))
judul.pack(pady=20)

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

btn_gunting = ctk.CTkButton(
    btn_frame, text="✂️ Gunting", width=100, command=lambda: mainkan(1))
btn_batu = ctk.CTkButton(btn_frame, text="🪨 Batu",
                         width=100, command=lambda: mainkan(2))
btn_kertas = ctk.CTkButton(btn_frame, text="📃 Kertas",
                           width=100, command=lambda: mainkan(3))

btn_gunting.grid(row=0, column=0, padx=10, pady=10)
btn_batu.grid(row=0, column=1, padx=10, pady=10)
btn_kertas.grid(row=0, column=2, padx=10, pady=10)

result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
result_label.pack(pady=20)

app.mainloop()
