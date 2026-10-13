import tkinter
from tkinter import messagebox
import json

def main_window():
    data_file = "Score.json"   #file nam ewhere user data is stored

    def load_data():
        try:
            with open(data_file, "r") as file:
                return json.load(file)  #reads JSON data and converts it into a python dictionary
        except FileNotFoundError:
            return {}

     


    # Save data to file
    def save_data(data):
        with open(data_file, "w") as file:
            json.dump(data, file) #.dump is used to write something directly to the file

    def login(data):
        User_name = username_entry.get()  # gets user name typed in the username box
        password = password_entry.get()   # gets password typed in the password box
       
        if User_name in data:  #checks if name already exists
            if data[User_name]['password'] == password:  #checks if password matches the stored password
                print("Login successful!")
            else:
                print("Incorrect password.")
                return None
        else:
            print("New user. Please register.")
            data[User_name] = {"password": password, "High Score" : 0}  #creates new user entry in the file
            save_data(data) #saves the data of the new user
            print("Registration successful!")
            return User_name




    main_window = tkinter.Tk()  #creates an main window
    main_window.title = ("Login Window")  #sets title of the screen

    window_width = 240
    window_height = 100

    screen_width= main_window.winfo_screenwidth()
    screen_height= main_window.winfo_screenheight()



    x= (screen_width-window_width)//2 # calculate x position for centering the window
    y = (screen_height-window_height)//2 # calculate y position for centering the window
    main_window.geometry(f"{window_width}x{window_height}+{x}+{y}") #sets window size and position


    main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


    username_label = tkinter.Label(main_window, text = "Username")
    username_label.grid(row = 0,column = 0,padx = 5,pady = 5)
    password_label = tkinter.Label(main_window, text = "password")
    password_label.grid(row = 1,column = 0,padx = 5,pady = 5)
    username_entry = tkinter.Entry(main_window)
    username_entry.grid(row = 0,column = 1,padx =5,pady= 5)
    password_entry = tkinter.Entry(main_window)
    password_entry.grid(row = 1,column = 1,padx =5,pady= 5)

    data = load_data()  
    login_button = tkinter.Button(main_window, text = "login",command = lambda:login(data))
    #The lambda function waits for the button to be clicked and it is used when we have to pass an argument in the function
    login_button.grid(row = 2,column = 1)


    main_window.mainloop() #keeps window running
   

main_window()