import tkinter as tk
# import Scale_Code

medSelected = 0
medications = {
  "Aspirin": 10,
  "Tylenol": 15,
  "Glucagon": 0.5,
  "Naloxone": 0.8,
  "Epinephrine": 0.01,
  "Ibuprofen": 10,
  "Benadryl": 1,
  "Amoxicillin": 20,
  "Azithromycin": 10,
  "Prednisone": 1,
  "Morphine": 0.1,
  "Diazepam": 0.2,
  "Ceftriaxone": 50,
  "Lisinopril": 0.3,
  "Warfarin": 0.2,
  "Cefepime": 70,
}

# Function to convert pounds to kilograms
def pounds_to_kg(weight_in_pounds):
  return weight_in_pounds * 0.453592

def select_medication():
  global new_window
  global medSelected
  if medSelected == 1:
    medSelected += 1
    selected_medication = listbox.get(listbox.curselection())
    dosage = medications[selected_medication]  # Get the dosage for the selected medication

    kill_window()

    # Code to Get the Weight From the Weighing Program
    # file_path = './Weight.txt'
    # file = open(file_path)
    # patient_weight_in_pounds = float(file.read())
    # file.close()

    # Simulate scale reading by directly entering patient's weight
    patient_weight_in_pounds = float(input("Enter patient's weight in pounds: "))
    patient_weight_in_kg = pounds_to_kg(patient_weight_in_pounds)

    # Calculate dosage based on patient's weight
    dosage_for_patient = dosage * patient_weight_in_kg
    print("Selected Medication:", selected_medication)
    print("Dosage for Patient (mg):", dosage_for_patient)
    medSelected += -1
    # Perform further actions based on the selected medication
  
def GetWeight(event):
    global kill_window
    global medSelected
    global window
    if medSelected == 0:
      medSelected += 1  
      # weight window config
      new_window = tk.Toplevel(root)

      def kill_window():
        global window
        global medSelected
        new_window.destroy()
        medSelected += -1

      new_window.title("Get Weight")
      new_window.transient(root)
      new_window.geometry("250x100")
      new_window.resizable(False, False)
      new_window.button = tk.Button(new_window, text="Get Weight", command=select_medication, anchor="center")
      new_window.label = tk.Label(new_window, text="Getting Patient's Weight...")
      new_window.protocol("WM_DELETE_WINDOW" , kill_window)

      # render weight window
      new_window.button.pack()
      new_window.label.pack()

def update_list(event=None):
    search_term = search_var.get()
    listbox.delete(0, tk.END)
    for item in medications:
        if search_term.lower() in item.lower():
            listbox.insert(tk.END, item)

# Create the main window & other widgets
root = tk.Tk()
root.title("Medication Selection")
root.resizable(False, False)
root.geometry("220x500")

# listbox and scrollbar config
scrollbar = tk.Scrollbar(root)
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, font=("Arial", 14))
scrollbar.config(command=listbox.yview)
for item in medications:
    listbox.insert(tk.END, item)
listbox.bind("<Double-Button-1>", GetWeight)

# searchbox config
search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var)
search_entry.bind("<KeyRelease>", update_list)

# Render the widgets on the window
search_entry.pack(pady=5)
listbox.pack(side=tk.LEFT,  fill=tk.Y, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
