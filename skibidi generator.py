import random
import customtkinter as ctk
import pyperclip

words = [
    "Skibidi", "Ohio", "Rizz", "FanumTax", "Sigma", "Gyatt", "NPC",
    "Goofy", "Skull", "Jit", "BingChilling", "WaffleHouse", "TopG", "Goku",
    "azbest", "bambik", "czemó", "fe!in", "glamur", "GOAT", "oddaje", 
    "oporowo", "rel", "rizz", "sigma", "skibidi", "slay", "yapping"
]

special_chars = "!@#$%^&*"

def generate_brainrot_password():
    return random.choice(words) + random.choice(words) + str(random.randint(10, 99)) + random.choice(special_chars)

def show_password():
    password = generate_brainrot_password()
    label_result.configure(text=f"Twoje hasło: {password}")

def copy_password():
    password = label_result.cget("text").replace("Twoje hasło: ", "")
    pyperclip.copy(password)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Skibidi Password Generator")
root.geometry("400x250")
root.iconbitmap(None)

btn_width = 200
btn_height = 40
font_style = ("Comic Sans MS", 16)
pady = 10

label = ctk.CTkLabel(root, text="Kliknij, aby wygenerować hasło:", font=("Arial", 14))
label.pack(pady=pady)

button_generate = ctk.CTkButton(root, text="Generuj hasło", command=show_password, width=btn_width, height=btn_height)
button_generate.pack(pady=pady)

label_result = ctk.CTkLabel(root, text="Twoje hasło pojawi się tutaj", font=font_style, text_color="white")
label_result.pack(pady=pady)

button_copy = ctk.CTkButton(root, text="Kopiuj hasło", command=copy_password, width=btn_width, height=btn_height, border_width=0)
button_copy.pack(pady=pady)

root.mainloop()
