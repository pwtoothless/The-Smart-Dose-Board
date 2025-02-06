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
  global medSelected
  if medSelected == 1:
    medSelected += 1
    selected_medication = listbox.get(listbox.curselection())
    dosage = medications[selected_medication]  # Get the dosage for the selected medication

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
    medSelected += -2
    # Perform further actions based on the selected medication
  
def GetWeight(event):
    global medSelected
    global window
    if medSelected == 0:
      medSelected += 1
      new_window = tk.Toplevel(root)
      new_window.title("Get Weight")

      # Make the new window transient, so it stays on top of the main window
      new_window.transient(root)
      new_window.geometry("250x100")
      new_window.resizable(False, False)
      new_window.button = tk.Button(new_window, text="Get Weight", command=select_medication, anchor="center")
      if window == 1:
        new_window.destroy()
        window += -1
      new_window.button.pack()
      new_window.label = tk.Label(new_window, text="Getting Patient's Weight...")
      new_window.label.pack()

# Create the main window
root = tk.Tk()
root.title("Medication Selection")
root.resizable(False, False)
root.geometry("210x500")

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox to display medications
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, font=("Arial", 14))
for medication in medications:
  listbox.insert(tk.END, medication)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Configure the listbox to scroll with the scrollbar
scrollbar.config(command=listbox.yview)

# Bind an event to select a medication when double-clicked
listbox.bind("<Double-Button-1>", GetWeight)

# Run the application
root.mainloop()
