from tkinter import *

"------------------------- CONSTANTS -------------------------------"
ONLINE_STATUS = "green yellow"
OFFLINE_STATUS = "tomato2"

"------------------------- FUNCTIONS -------------------------------"
def Validate():
    global devices_list
    global devices
    global window
    
    device_name = devices_list.get(devices_list.curselection())
    
    if(PullDeviceUpdates() == -1):
        UpdateDeviceList()
        loading_label.config(text="request time out")
        loading_label.placeplace(relx=0.2, rely=0.62, anchor=W)
        loading_label.after(3000, loading_label.place_forget)
        return
    
    for device in devices:
        if(device["device"] == device_name):
            if(device["connection"]["active"] == True):                
                window.destroy()
                from main import SetDevice
                SetDevice(device_name)
                from Plant_Window import OpenWindow as OpenPlantWindow
                OpenPlantWindow()
            else:
                loading_label.config(text="The device is offline")
                loading_label.place(relx=0.2, rely=0.62, anchor=W)
                loading_label.after(3000, loading_label.place_forget)

def Return():
    window.destroy()
    from Login_Window import OpenWindow as OpenLoginWindow
    OpenLoginWindow()

def OnListChange(evt=None):
    global cur_device_label
    global cur_device__status_label
    
    device_name = devices_list.get(devices_list.curselection())
    loading_label.config(text="Loading device " + device_name)
    
    state_color = OFFLINE_STATUS
    device_state = "Inactive"
    
    if("device" in devices and device["device"] == device_name):
        state_color = ONLINE_STATUS if device["connection"]["active"] else OFFLINE_STATUS
        device_state = "Active" if device["connection"]["active"] else "Inactive"
    
    cur_device_label.config(text="- " + device_name)
    cur_device__status_label.config(text=device_state, fg=state_color)

    loading_label.place_forget()

def PullDeviceUpdates():
    try:
        global devices
        from main import GetDevices
        devices = GetDevices()
        return 0
    except:
        #time out
        return -1

def UpdateDeviceList():
    global devices_list
    global devices
    
    loading_label.config(text="Loading list")
    
    if(len(devices) == 0):
        loading_label.config(text="Error, no devices found")

    devices_list.delete(0, END)
    for device in devices:
        devices_list.insert(END, device["device"])

    loading_label.place_forget()

def OpenWindow():
    global window
    window = Tk()
    window.wm_title("Devices")
    window.resizable(0,0)

    devices_list_frame = Frame(window)
    devices_list_frame.place(relx=0.1, rely=0.1, anchor=NW)

    devices_list_label = Label(devices_list_frame, text="Devices")
    devices_list_label.pack(side=TOP)
    
    devices_list_scrollbar = Scrollbar(devices_list_frame, orient="vertical")
    devices_list_scrollbar.pack(side=RIGHT, fill=Y)

    global devices_list
    devices_list = Listbox(devices_list_frame, yscrollcommand=devices_list_scrollbar.set)
    devices_list_scrollbar.config(command=devices_list.yview)
    devices_list.pack(side=LEFT)
    
    devices_list.bind("<<ListboxSelect>>", OnListChange)
    
    cur_device_title = Label(window, text="Current device:")
    cur_device_title.place(relx=0.6, rely=0.2, anchor=W)

    global cur_device_label
    cur_device_label = Label(window, text="- ")
    cur_device_label.place(relx=0.6, rely=0.25, anchor=W)

    cur_device_status_title = Label(window, text="Status:")
    cur_device_status_title.place(relx=0.6, rely=0.4, anchor=W)

    global cur_device__status_label
    cur_device__status_label = Label(window, text="Inactive", fg=OFFLINE_STATUS)
    cur_device__status_label.place(relx=0.6, rely=0.45, anchor=W)

    validate_button = Button(window, text="Validate", width=10, height=2, command=Validate)
    validate_button.place(relx=0.55, rely=0.8, anchor=CENTER)

    return_button = Button(window, text="Return", width=10, height=2, command=Return)
    return_button.place(relx=0.8, rely=0.8, anchor=CENTER)

    global refresh_image
    refresh_image = PhotoImage(file="refresh.png")
    
    global refresh_button
    refresh_button = Button(window, image=refresh_image, width=25, height=25, command=UpdateDeviceList)
    refresh_button.place(relx=0.14, rely=0.62, anchor=CENTER)

    global loading_label
    loading_label = Label(window, text="loading...")
    loading_label.place(relx=0.2, rely=0.62, anchor=W)

    window.minsize(400, 400)

    if(PullDeviceUpdates() == -1):
        loading_label.config(text="request time out")
        loading_label.after(3000, loading_label.place_forget)
    UpdateDeviceList()
