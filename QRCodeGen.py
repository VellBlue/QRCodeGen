import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


def generate_qr_code():
    # Ottieni il testo inserito dall'utente
    testo_o_url = entry.get()
    if testo_o_url.strip() == "":
        messagebox.showerror("Errore", "Inserisci un testo o un URL.")
        return

    try:
        # Genera il codice QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(testo_o_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Mostra il codice QR in una nuova finestra
        show_qr_code(img)
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {str(e)}")


def show_qr_code(image):
    qr_window = tk.Toplevel(root)
    qr_window.title("Codice QR")

    # Visualizza l'immagine del codice QR
    img_label = tk.Label(qr_window)
    img_label.pack(padx=10, pady=10)

    # Converti l'immagine per essere visualizzata nella finestra
    img = ImageTk.PhotoImage(image)
    img_label.config(image=img)
    img_label.image = img

    # Pulsante per scaricare l'immagine
    download_button = tk.Button(qr_window, text="Scarica QR Code", command=lambda: download_qr_code(image))
    download_button.pack(padx=10, pady=5)


def download_qr_code(image):
    file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_name:
        image.save(file_name)
        messagebox.showinfo("Successo", f"Codice QR salvato come '{file_name}'")


# Creazione della finestra principale
root = tk.Tk()
root.title("Generatore di Codice QR")
root.geometry("500x200")  # Imposta le dimensioni della finestra

# Etichetta e campo di inserimento per il testo/URL
label = tk.Label(root, text="Inserisci il testo o l'URL:", font=("Arial", 14))
label.pack()

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack()

# Pulsante per generare il codice QR
generate_button = tk.Button(root, text="Genera QR Code", command=generate_qr_code, font=("Arial", 14))
generate_button.pack()

# Avvia la finestra
root.mainloop()
