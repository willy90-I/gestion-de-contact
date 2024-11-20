# main.py
import tkinter as tk
from ui import add_contact_ui, display_contacts_ui, search_contacts_ui, delete_contact_ui, modify_contact_ui
from database import create_db

def main():
    create_db()  # Créer la base de données si elle n'existe pas

    root = tk.Tk()
    root.title("Gestion de Contacts")

    # Interface graphique
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Recherche
    label_search = tk.Label(frame, text="Rechercher un contact:")
    label_search.grid(row=0, column=0)
    entry_search = tk.Entry(frame)
    entry_search.grid(row=0, column=1)
    button_search = tk.Button(frame, text="Rechercher", command=lambda: search_contacts_ui(entry_search, listbox))
    button_search.grid(row=0, column=2)

    # Liste des contacts
    listbox_frame = tk.Frame(root)
    listbox_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
    listbox = tk.Listbox(listbox_frame, width=50, height=10, yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Formulaire d'ajout de contact
    frame_add = tk.Frame(root)
    frame_add.pack(pady=10)

    label_nom = tk.Label(frame_add, text="Nom:")
    label_nom.grid(row=0, column=0)
    entry_nom = tk.Entry(frame_add)
    entry_nom.grid(row=0, column=1)

    label_prenom = tk.Label(frame_add, text="Prénom:")
    label_prenom.grid(row=1, column=0)
    entry_prenom = tk.Entry(frame_add)
    entry_prenom.grid(row=1, column=1)

    label_telephone = tk.Label(frame_add, text="Téléphone:")
    label_telephone.grid(row=2, column=0)
    entry_telephone = tk.Entry(frame_add)
    entry_telephone.grid(row=2, column=1)

    label_email = tk.Label(frame_add, text="Email:")
    label_email.grid(row=3, column=0)
    entry_email = tk.Entry(frame_add)
    entry_email.grid(row=3, column=1)

    button_add = tk.Button(frame_add, text="Ajouter Contact", 
                           command=lambda: add_contact_ui(entry_nom, entry_prenom, entry_telephone, entry_email, listbox))
    button_add.grid(row=4, column=0, columnspan=2)

    # Boutons pour les opérations
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=10)

    button_modify = tk.Button(frame_buttons, text="Modifier Contact", command=lambda: modify_contact_ui(listbox))
    button_modify.grid(row=0, column=0, padx=5)

    button_delete = tk.Button(frame_buttons, text="Supprimer Contact", command=lambda: delete_contact_ui(listbox))
    button_delete.grid(row=0, column=1, padx=5)

    # Afficher les contacts au démarrage
    display_contacts_ui(listbox)

    root.mainloop()

if __name__ == "__main__":
    main()