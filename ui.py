# ui.py
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button
from database import add_contact, update_contact, delete_contact, get_all_contacts, search_contacts
from contact import Contact

def add_contact_ui(entry_nom, entry_prenom, entry_telephone, entry_email, listbox):
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    telephone = entry_telephone.get()
    email = entry_email.get()

    if nom and prenom and telephone:
        contact = Contact(None, nom, prenom, telephone, email)
        add_contact(contact)
        messagebox.showinfo("Succès", "Contact ajouté avec succès")
        display_contacts_ui(listbox)
    else:
        messagebox.showerror("Erreur", "Nom, prénom et téléphone sont obligatoires")

def display_contacts_ui(listbox):
    listbox.delete(0, tk.END)
    contacts = get_all_contacts()
    for contact in contacts:
        listbox.insert(tk.END, f"ID:{contact.id} {contact.nom} {contact.prenom} - {contact.telephone} ({contact.email})")

def search_contacts_ui(entry_search, listbox):
    query = entry_search.get()
    contacts = search_contacts(query)
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"ID:{contact.id} {contact.nom} {contact.prenom} - {contact.telephone} ({contact.email})")

def delete_contact_ui(listbox):
    try:
        selected_contact = listbox.curselection()[0]
        contact_info = listbox.get(selected_contact)
        contact_id = int(contact_info.split(" ")[0].split(":")[1].strip())
        delete_contact(contact_id)
        messagebox.showinfo("Succès", "Contact supprimé avec succès")
        display_contacts_ui(listbox)
    except IndexError:
        messagebox.showerror("Erreur", "Veuillez sélectionner un contact à supprimer")

def modify_contact_ui(listbox):
    try:
        selected_contact = listbox.curselection()[0]
        contact_info = listbox.get(selected_contact)
        contact_id = int(contact_info.split(" ")[0].split(":")[1].strip())

        # Récupérer les informations actuelles
        current_contact = next((c for c in get_all_contacts() if c.id == contact_id), None)

        if not current_contact:
            messagebox.showerror("Erreur", "Impossible de trouver le contact sélectionné")
            return

        # Fenêtre pour modifier le contact
        modify_window = Toplevel()
        modify_window.title("Modifier Contact")

        Label(modify_window, text="Nom:").grid(row=0, column=0)
        entry_nom = Entry(modify_window)
        entry_nom.insert(0, current_contact.nom)
        entry_nom.grid(row=0, column=1)

        Label(modify_window, text="Prénom:").grid(row=1, column=0)
        entry_prenom = Entry(modify_window)
        entry_prenom.insert(0, current_contact.prenom)
        entry_prenom.grid(row=1, column=1)

        Label(modify_window, text="Téléphone:").grid(row=2, column=0)
        entry_telephone = Entry(modify_window)
        entry_telephone.insert(0, current_contact.telephone)
        entry_telephone.grid(row=2, column=1)

        Label(modify_window, text="Email:").grid(row=3, column=0)
        entry_email = Entry(modify_window)
        entry_email.insert(0, current_contact.email)
        entry_email.grid(row=3, column=1)

        def save_modification():
            nom = entry_nom.get()
            prenom = entry_prenom.get()
            telephone = entry_telephone.get()
            email = entry_email.get()

            if nom and prenom and telephone:
                updated_contact = Contact(contact_id, nom, prenom, telephone, email)
                update_contact(updated_contact)
                messagebox.showinfo("Succès", "Contact modifié avec succès")
                display_contacts_ui(listbox)
                modify_window.destroy()
            else:
                messagebox.showerror("Erreur", "Nom, prénom et téléphone sont obligatoires")

        Button(modify_window, text="Enregistrer", command=save_modification).grid(row=4, column=0, columnspan=2)

    except IndexError:
        messagebox.showerror("Erreur", "Veuillez sélectionner un contact à modifier")
