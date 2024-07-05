import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    def show_animal(animal, streich):
        global photo2, photo3, photo4, photo5

        if animal == "Pferd" and streich == "ja":
            label3.config(image=photo2, text="Zeus wäre das perfekte Patentier für dich!", compound="bottom")
            label3.image = photo2

        elif animal == "Pferd" and streich == "nein":
            label3.config(image=photo4, text="Blink wäre gern dein neuer bester Freund!", compound="bottom")
            label3.image = photo4

        elif animal == "Ziege" and streich == "ja":
            label3.config(image=photo3, text="Siggi wäre das perfekte Patentier für dich!", compound="bottom")
            label3.image = photo3

        elif animal == "Ziege" and streich == "nein":
            label3.config(image=photo5, text="Simon freut sich auf deine Patenschaft!", compound="bottom")
            label3.image = photo5

        label2.grid_forget()
        button1.grid_forget()
        button2.grid_forget()
        label4.grid_forget()
        button3.grid_forget()
        button4.grid_forget()
        return_button.grid(row=5, column=1, pady=10, sticky="ew")

    def show_streich(streich):
        animal = selected_animal.get()
        show_animal(animal, streich)

    def return_to_selection():
        # Frage und Buttons wieder anzeigen
        label2.grid(row=1, column=0, padx=10, pady=10)
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2.grid(row=1, column=2, padx=10, pady=10)
        label4.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        button3.grid(row=2, column=1, padx=10, pady=10)
        button4.grid(row=2, column=2, padx=10, pady=10)
        # Zurück-Button ausblenden
        return_button.grid_forget()
        # Bild und Text im label3 zurücksetzen
        label3.config(image='', text='')
        selected_animal.set('')

    root = tk.Tk()
    root.title("Tierpatenschaft übernehmen")
    root.geometry("900x600")
    root.resizable(width=False, height=False)

    image1 = Image.open("banner.png").resize((800, 150))
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("Zeus.png").resize((250, 250))
    photo2 = ImageTk.PhotoImage(image2)

    image3 = Image.open("Siggi.png").resize((250, 250))
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open("blink.png").resize((250, 250))
    photo4 = ImageTk.PhotoImage(image4)

    image5 = Image.open("Simon.png").resize((250, 250))
    photo5 = ImageTk.PhotoImage(image5)

    label1 = ttk.Label(root, text="Wir freuen uns, dich kennenzulernen!", image=photo1, compound=tk.TOP,
                       padding=(0, 10))
    label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    label1.configure(font=("Book antica", 15))

    label2 = ttk.Label(root, text="Für welches Tier interessierst du dich? : ")
    label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    label2.configure(font=("Book antica", 12))

    selected_animal = tk.StringVar()

    button1 = ttk.Button(root, text="Pferd", command=lambda: selected_animal.set("Pferd"))
    button1.grid(row=1, column=1, padx=10, pady=10)

    button2 = ttk.Button(root, text="Ziege", command=lambda: selected_animal.set("Ziege"))
    button2.grid(row=1, column=2, padx=10, pady=10)

    label4 = ttk.Label(root, text="Ist es dir wichtig, dass dein Patentier gern gestreichelt wird? : ")
    label4.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    label4.configure(font=("Book antica", 12))

    button3 = ttk.Button(root, text="Oh ja, ich schmuse auch gern!", command=lambda: show_streich("ja"))
    button3.grid(row=2, column=1, padx=10, pady=10)

    button4 = ttk.Button(root, text="Nicht unbedingt.", command=lambda: show_streich("nein"))
    button4.grid(row=2, column=2, padx=10, pady=10)

    label3 = ttk.Label(root, text="", font=("Book antica", 12), padding=10)
    label3.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    return_button = ttk.Button(root, text="Deine Antworten ändern", command=return_to_selection, padding=(2, 2))
    return_button.grid(row=5, column=1, columnspan=3, pady=10, sticky="ew")
    return_button.grid_forget()

    root.mainloop()

except Exception as e:
       print ("Ups der Fehler ist aufgetreten: ", e.args[0])


git config --global user.name "Florence-Neu"
git config --global user.email "florence.neu@outlook.com"