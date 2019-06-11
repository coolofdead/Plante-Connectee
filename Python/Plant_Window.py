from tkinter import *

"------------------------- CONSTANTS -------------------------------"
PLANT_NAME_INDEX = 0
PLANT_TEMPERATURE_INDEX = 1
PLANT_AIR_HUMIDTY_INDEX = 2
PLANT_GROUND_HUMIDTY_INDEX = 3
PLANT_LUMINOSITY_INDEX = 4

database_plant_name = "FILE.csv"
"------------------------- FUNCTIONS -------------------------------"
def FillPlantListBox(plants):
    global plant_datas
    global plant_list
    
    plant_datas = plants
    for plant in plants:
        plant_list.insert(END, plant[PLANT_NAME_INDEX])

def ReadPlantData(file_name, separator):
    global plant_datas
    
    plant_datas = []
    with open(file_name, "r") as f:
        for elem in f.read().split("\n"):
            if(elem != ""):
                plant_datas.append(elem.split(separator))
        
def OnListChange(evt):
    global plant_datas
    DisplayOptimalPlantData(plant_datas[plant_list.curselection()[0]])

def OnEntrySearch(evt=None):
    global search_entry
    global plant_datas
    
    search_value = search_entry.get()
    if(search_value == ""):
        return
    
    p=None
    for plant in plant_datas:
        if(plant[PLANT_NAME_INDEX] == search_value):
            p=plant
            
    if(p != None):
        DisplayOptimalPlantData(p)
    else:
        from tkinter import messagebox
        messagebox.showwarning("Error", "The plant " + search_value + " n'a pas été trouvé")

def DisplayCurrentPlant():
    global current_temp_value_label
    
    from main import GetPlantData
    from main import ressources
    datas = GetPlantData()
    #{"out":{"humidity":99.9}}
    plant_temp = datas[PLANT_TEMPERATURE_INDEX]["out"][ressources[PLANT_TEMPERATURE_INDEX]] if "out" in datas[PLANT_TEMPERATURE_INDEX] else "error"
    current_temp_value_label.config(text=str(plant_temp))

def DisplayOptimalPlantData(plant):
    global optimal_temp_value_label

    optimal_temp = plant[PLANT_TEMPERATURE_INDEX]
    optimal_temp_value_label.config(text=str(optimal_temp) + "°")

def OpenWindow():
    window = Tk()
    window.title("Plant searcher")
    window.minsize(400, 400)
    window.resizable(0, 0)
    
    plant_list_title = Label(window, text="Plants")
    plant_list_title.pack()

    plant_list_frame = Frame(window)
    plant_list_frame.place(relx=0.1, rely=0.1, anchor=NW)

    plant_list_scrollbar = Scrollbar(plant_list_frame, orient="vertical")
    
    global plant_list
    plant_list = Listbox(plant_list_frame, yscrollcommand=plant_list_scrollbar.set)
    plant_list.bind("<<ListboxSelect>>", OnListChange)
    plant_list.pack(side=LEFT)

    plant_list_scrollbar.config(command=plant_list.yview)
    plant_list_scrollbar.pack(side=RIGHT, fill=Y)

    search_entry_title = Label(window, text="Enter your plan name:")
    search_entry_title.place(relx=0.55, rely=0.13, anchor=W)

    global search_entry
    search_entry = Entry(window)
    search_entry.bind("<Return>", OnEntrySearch)
    search_entry.place(relx=0.55, rely=0.2, anchor=W)

    search_validate_button = Button(window, text="Validate", command=OnEntrySearch)
    search_validate_button.place(relx=0.7, rely=0.3, anchor=CENTER)

    optimal_condition_frame = Frame(window)
    optimal_condition_frame.place(relx=0.25, rely=0.65, anchor=CENTER)

    optimal_condition_label = Label(optimal_condition_frame, text="Optimal plant conditions")
    optimal_condition_label.pack()

    optimal_temp_label = Label(optimal_condition_frame, text="Temp")
    optimal_temp_label.pack()

    global optimal_temp_value_label
    optimal_temp_value_label = Label(optimal_condition_frame, text="0°")
    optimal_temp_value_label.pack()

    current_condition_frame = Frame(window)
    current_condition_frame.place(relx=0.7, rely=0.65, anchor=CENTER)

    current_condition_label = Label(current_condition_frame, text="Current plant conditions")
    current_condition_label.pack()

    current_temp_label = Label(current_condition_frame, text="Temp")
    current_temp_label.pack()

    global current_temp_value_label
    current_temp_value_label = Label(current_condition_frame, text="0°")
    current_temp_value_label.pack()
    
    ReadPlantData(database_plant_name, ";")
    FillPlantListBox(plant_datas)

    window.after(1000, DisplayCurrentPlant)
