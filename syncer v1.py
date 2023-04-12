import tkinter as tk
import shutil
import os
from tkinter import messagebox
dircheck = 'data\\mcdirs.txt'
if not os.path.isfile(dircheck):
    messagebox.showerror("File not found", f"File {dircheck} does not exist")
    root.quit()

if not os.path.exists('mods'):
    os.mkdir('mods')

if not os.path.exists('config'):
    os.mkdir('config')

if not os.path.exists('speedrunigt'):
    os.mkdir('speedrunigt')
def synccf():
    src_dir = "config"
    with open('data\\mcdirs.txt', 'r') as f:
        # Loop over each line in the file
        for line in f:
            # Find the index of the first tilde character in the line
            tilde_index = line.index('~')
                
            # Extract the directory path from the line starting from the tilde character
            dst_dir = line[tilde_index+1:].strip() + "\\config"

            for item in os.listdir(src_dir):
                # Construct full file path for the item
                src_path = os.path.join(src_dir, item)
                dst_path = os.path.join(dst_dir, item)
                
                # Check if the item is a file or folder
                if os.path.isfile(src_path):
                    # Use shutil.copy2 to copy the file to the destination directory
                    shutil.copy2(src_path, dst_path)
                    print("Sync config to " + dst_dir + " done!")
                elif os.path.isdir(src_path):
                    # Use shutil.copytree to copy the folder to the destination directory
                    shutil.copytree(src_path, dst_path)

def modsync():
    repl = var.get()
    src_dir = 'mods'
    if repl == False:
        with open('data\\mcdirs.txt', 'r') as f:
            # Loop over each line in the file
            for line in f:
                # Find the index of the first tilde character in the line
                tilde_index = line.index('~')
                
                # Extract the directory path from the line starting from the tilde character
                dst_dir = line[tilde_index+1:].strip() + "\\mods"

                for item in os.listdir(src_dir):
                    # Construct full file path for the item
                    src_path = os.path.join(src_dir, item)
                    dst_path = os.path.join(dst_dir, item)
                    
                    # Check if the item is a file or folder
                    if os.path.isfile(src_path):
                        # Use shutil.copy2 to copy the file to the destination directory
                        shutil.copy2(src_path, dst_path)
                    elif os.path.isdir(src_path):
                        # Use shutil.copytree to copy the folder to the destination directory
                        shutil.copytree(src_path, dst_path)
                print("Sync atum to " + dst_dir + " done!")
    if repl == True:
        with open('data\\mcdirs.txt', 'r') as f:
            # Loop over each line in the file
            for line in f:
                # Find the index of the first tilde character in the line
                tilde_index = line.index('~')
                
                # Extract the directory path from the line starting from the tilde character
                dst_dir = line[tilde_index+1:].strip() + "\\mods"

                # Remove all files in the destination directory
                for item in os.listdir(dst_dir):
                    item_path = os.path.join(dst_dir, item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                print("Removed all items in " + dst_dir + " done!")

                # Copy files from source directory to destination directory
                for item in os.listdir(src_dir):
                    # Construct full file path for the item
                    src_path = os.path.join(src_dir, item)
                    dst_path = os.path.join(dst_dir, item)
                    
                    # Check if the item is a file or folder
                    if os.path.isfile(src_path):
                        # Use shutil.copy2 to copy the file to the destination directory
                        shutil.copy2(src_path, dst_path)
                    elif os.path.isdir(src_path):
                        # Use shutil.copytree to copy the folder to the destination directory
                        shutil.copytree(src_path, dst_path)
                print("Sync atum to " + dst_dir + " done!")
    
def atum_sync():
    seed = entry1.get()
    dif = entry2.get()
    gen = entry3.get()
    struc = var1.get()
    chest = var2.get()
    print("seed", seed)
    print("dif", dif)
    print("gen", gen)
    if struc:
        print("struc true")
    else:
        print("struc false")    
    if chest:
        print("chest true")
    else:
        print("chest false")   
    
    with open('data\\mcdirs.txt', 'r') as f:
        for line in f:
            tilde_index = line.index('~')    
            atumf = line[tilde_index+1:].strip() + "\\config\\atum\\"
            with open(atumf + "atum.properties", "r") as u:
                lines = u.readlines()

            with open(atumf + "atum.properties", "w") as u:
                for line in lines:
                    if line.startswith("seed="):
                        line = "seed=" + seed + "\n"  
                    u.write(line)
            
            with open(atumf + "atum.properties", "r") as u:
                lines = u.readlines()
            
            with open(atumf + "atum.properties", "w") as u:
                for line in lines:
                    if line.startswith("difficulty"):
                        line = "difficulty=" + dif + "\n"  
                    u.write(line)

            with open(atumf + "atum.properties", "r") as u:
                lines = u.readlines()

            with open(atumf + "atum.properties", "w") as u:
                for line in lines:
                    if line.startswith("generatorType"):
                        line = "generatorType=" + gen + "\n"  
                    u.write(line)

            with open(atumf + "atum.properties", "r") as u:
                lines = u.readlines()
            if struc:
                with open(atumf + "atum.properties", "w") as u:
                    for line in lines:
                        if line.startswith("structures"):
                            line = "structures=true\n"  
                        u.write(line)
            else:
                with open(atumf + "atum.properties", "w") as u:
                    for line in lines:
                        if line.startswith("structures"):
                            line = "structures=false\n"  
                        u.write(line)

            with open(atumf + "atum.properties", "r") as u:
                lines = u.readlines()
            if chest:
                with open(atumf + "atum.properties", "w") as u:
                    for line in lines:
                        if line.startswith("bonusChest"):
                            line = "bonusChest=true\n"  
                        u.write(line)
            else:
                with open(atumf + "atum.properties", "w") as u:
                    for line in lines:
                        if line.startswith("bonusChest"):
                            line = "bonusChest=false\n"  
                        u.write(line)
            print("Sync atum to " + atumf + " done!")

def syncof():
    op = 'options.txt'
    with open('data\\mcdirs.txt', 'r') as f:
        for line in f:
            tilde_index = line.index('~')    
            mc = line[tilde_index+1:].strip()
            shutil.copy(op, mc)
            print("Sync options.txt to " + mc + " done!")

def syncsp():
    spr = 'speedrunigt'
    with open('data\\mcdirs.txt', 'r') as f:
        for line in f:
            tilde_index = line.index('~')
            dst_dir = line[tilde_index+1:].strip() + "\\speedrunigt"
            for file_name in os.listdir(dst_dir):
                file_path = os.path.join(dst_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error: {e}")
            for file_name in os.listdir(spr):
                source_file_path = os.path.join(spr, file_name)
                destination_file_path = os.path.join(dst_dir, file_name)
                try:
                    if os.path.isfile(source_file_path):
                        shutil.copy(source_file_path, destination_file_path)
                        print("Sync speedrun config to " + dst_dir + " done!")
                except Exception as e:
                    print(f"Error: {e}")

def iconfig():
    with open("data\\mcdirs.txt", "r") as f:
        for line in f:
            if line.startswith("1~"):
                o = line[2:].strip() + '\\config'
                # Copy all files from source folder to destination folder
                for filename in os.listdir(o):
                    source_path = os.path.join(o, filename)
                    destination_path = os.path.join('config', filename)
                    try:
                        shutil.copy2(source_path, destination_path)
                        print("Import config done!")
                    except Exception as e:
                        print(f"Error: {e}")
def ispr():
    with open("data\\mcdirs.txt", "r") as f:
        for line in f:
            if line.startswith("1~"):
                o= line[2:].strip() + '\\speedrunigt'
                for filename in os.listdir('speedrunigt'):
                    file_path = os.path.join('speedrunigt', filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f"Error: {e}")

                for filename in os.listdir(o):
                    source_path = os.path.join(o, filename)
                    destination_path = os.path.join('speedrunigt', filename)
                    try:
                        shutil.copy2(source_path, destination_path)
                        print("Import speedrunigt config done!")
                    except Exception as e:
                        print(f"Error: {e}")

def imods():
    with open("data\\mcdirs.txt", "r") as f:
        for line in f:
            if line.startswith("1~"):
                o= line[2:].strip() + '\\mods'
                for filename in os.listdir('mods'):
                    file_path = os.path.join('mods', filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f"Error: {e}")

                for filename in os.listdir(o):
                    source_path = os.path.join(o, filename)
                    destination_path = os.path.join('mods', filename)
                    try:
                        shutil.copy2(source_path, destination_path)
                        print("Import mods done!")
                    except Exception as e:
                        print(f"Error: {e}")

def iopt():
    destination_folder = os.getcwd()
    with open("data\\mcdirs.txt", "r") as f:
        for line in f:
            if line.startswith("1~"):
                o = line[2:].strip()+ '\\options.txt'
                shutil.copy(o, destination_folder)
                print('Import options.txt to folder done!')

    
window = tk.Tk()

window.title("Syncer")
window.geometry("400x650")

tk.Label(window).pack(pady=1)

version = tk.Label(window, text="Syncer v1.0.0 by canhvjp")
version.pack()

tk.Label(window).pack(pady=1)

var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Remove all mods when sync", variable=var)
checkbox.pack()

button = tk.Button(window, text="Sync mods!", command=modsync)
button.pack()

tk.Label(window).pack(pady=1)

atumh = tk.Label(window, text="Atum options")
atumh.pack()

label1 = tk.Label(window, text="Seed: ")
label1.pack()

entry1 = tk.Entry(window, width=45)
entry1.pack()

label2 = tk.Label(window, text="Difficulty: ")
label2.pack()

entry2 = tk.Entry(window, width=3)
entry2.insert(0, "1")
entry2.pack()

label3 = tk.Label(window, text="generatorType ")
label3.pack()

entry3 = tk.Entry(window, width=3)
entry3.insert(0, "0")
entry3.pack()

var1 = tk.BooleanVar(value=True)
checkbox1 = tk.Checkbutton(window, text="Structure", variable=var1)
checkbox1.pack()

var2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(window, text="Bonus chest", variable=var2)
checkbox2.pack()

button = tk.Button(window, text="Sync atum properties!", command=atum_sync)
button.pack()

tk.Label(window).pack(pady=1)

button = tk.Button(window, text="Sync config", command=synccf)
button.pack()

tk.Label(window).pack(pady=1)

button = tk.Button(window, text="Sync options.txt", command=syncof)
button.pack()

button = tk.Button(window, text="Sync speedrunIGT options", command=syncsp)
button.pack()

tk.Label(window).pack(pady=1)

button = tk.Button(window, text="Import mods", command=imods)
button.pack()

button = tk.Button(window, text="Import config", command=iconfig)
button.pack()

button = tk.Button(window, text="Import speedrunigt", command=ispr)
button.pack()

button = tk.Button(window, text="Import options.txt", command=iopt)
button.pack()

tk.Label(window).pack(pady=1)

end = tk.Label(window, text="Import setting will import data from instace 1")
end.pack()

window.mainloop()
