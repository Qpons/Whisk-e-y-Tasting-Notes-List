from tkinter import *
import csv

root = Tk()
root.title('Whisk(e)y Tasting Notes')
root.geometry('500x350')

class Whiskey:
  def __init__(self, name, age, region, price, nose, palate, like):
    self.name = name
    self.age = age
    self.region = region
    self.price = price
    self.nose = nose
    self.palate = palate
    self.like = like

saved_list = []
name_var_list = []
list_length = 0
current_whiskey_var = IntVar()
current_whiskey_var.set(0)
entry_list = []

entry_var_list = []
for thing in range(0,7):
  var = StringVar()
  entry_var_list.append(var)

left_frame = Frame(root, width=20,height=350)
left_frame.grid(row=0,column=0)

space_frame = Frame(root, width=20)
space_frame.grid(row=0,column=1)
Label(space_frame, text='                  ').grid(row=0,column=0)

right_frame = Frame(root, width=20,height=350)
right_frame.grid(row=0,column=2)

Label(left_frame, text='Saved Notes').grid(row=0, column=0)
Button(left_frame, text='Add New', command=lambda:add_new_whiskey()).grid(row=1,column=0)

Label(right_frame, text='Whiskey Notes').grid(row=0,column=0)

def add_new_whiskey():
    global list_length
    var = StringVar()
    saved_list.append(Whiskey('Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'))
    name_var_list.append(var)
    name_var_list[list_length].set('No Name')
    Radiobutton(left_frame, textvariable=name_var_list[list_length], variable=current_whiskey_var, value=list_length, command=lambda p=list_length: generate_list(p)).grid(row=list_length+2, column=0)
    Button(left_frame, text='Delete', command=lambda p=list_length:delete_whiskey(p)).grid(row=list_length+2, column=1)
    list_length += 1
    print('Current: ' + str(list_length))
    
def generate_list(index_number):
    loop_count = 0
    print('Current: '+ str(list_length))
    for attr, value in saved_list[index_number].__dict__.items():
        Label(right_frame, text=attr).grid(row=loop_count+1,column=0)
        curr_entry = Entry(right_frame, textvariable=entry_var_list[loop_count])
        entry_list.append(curr_entry)
        curr_entry.grid(row=loop_count+1,column=1)
        curr_entry.delete(0,END)
        curr_entry.insert(0, value)
        print(attr, value)
        loop_count += 1
    Button(right_frame, text='Save', command=lambda p=index_number:save_current(p)).grid(row=9, column=0)
    print('Current: ' + str(index_number))

def save_current(index_number):
    saved_list[index_number].name = entry_var_list[0].get()
    name_var_list[index_number].set(entry_var_list[0].get())
    saved_list[index_number].age = entry_var_list[1].get()
    saved_list[index_number].region = entry_var_list[2].get()
    saved_list[index_number].price = entry_var_list[3].get()
    saved_list[index_number].nose = entry_var_list[4].get()
    saved_list[index_number].palate = entry_var_list[5].get()
    saved_list[index_number].like = entry_var_list[6].get()
    export_list = []
    for whiskey in saved_list:
        temp_list = []
        for attr, value in whiskey.__dict__.items():
            temp_list.append(value)
        export_list.append(temp_list)
    title = ['Name', 'Age', 'Region', 'Price', 'Nose', 'Palate', 'Like']
    with open('whiskey.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(title)
        writer.writerows(export_list)


def delete_whiskey(index_number):
    global list_length
    for label in left_frame.grid_slaves():
        if int(label.grid_info()["row"]) == index_number:
          label.grid_forget()
    saved_list.pop(index_number)
    list_length -= 1

mainloop()