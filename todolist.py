import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        pass

def update_task():
    try:
        selected_task_index = task_list.curselection()[0]
        my_task = entry.get()
        task_list.delete(selected_task_index)
        task_list.insert(selected_task_index, my_task)
        entry.delete(0, tk.END)
    except IndexError:
        pass


w= tk.Tk()
w.title(" My First To-Do List")


entry = tk.Entry(w, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=3)


task_list = tk.Listbox(w, width=50, selectmode=tk.SINGLE, font=("Arial", 14))
task_list.grid(row=1, column=0, columnspan=3)


add_button = tk.Button(w, text="Add", command=add_task, width=10, height=2)
delete_button = tk.Button(w, text="Delete", command=delete_task, width=10, height=2)
update_button = tk.Button(w, text="Update", command=update_task, width=10, height=2)
add_button.grid(row=2, column=0)
delete_button.grid(row=2, column=1)
update_button.grid(row=2, column=2)

w.mainloop()
