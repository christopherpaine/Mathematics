import os
import subprocess
import time

def watch_directory(path='.'):
    before = {f: os.path.getmtime(f) for f in os.listdir(path)}
    while True:
        time.sleep(5)
        after = {f: os.path.getmtime(f) for f in os.listdir(path)}
        added = [f for f in after if f not in before]
        removed = [f for f in before if f not in after]
        modified = [f for f in after if f in before and before[f] != after[f]]

        if added:
            print("Added: ", ", ".join(added))
        if removed:
            print("Removed: ", ", ".join(removed))
        if modified:
            print("Modified: ", ", ".join(modified))
            if is_python_file(modified[0]): 
                print ("this was a python file")
                run_bash_command("jupytext --sync "+str(modified[0]))  
                run_bash_command("jupyter nbconvert --to notebook --inplace --execute --allow-errors "+remove_file_extension(modified[0])+".ipynb")
                run_bash_command("jupyter nbconvert --to html " + remove_file_extension(modified[0])+".ipynb" + " --output "+ remove_file_extension(modified[0])+ ".html")
                run_bash_command("jupyter nbconvert --to html --no-input --no-prompt " +remove_file_extension(modified[0])+".ipynb" + " --output "+ remove_file_extension(modified[0]) + "-clean.html")
                print("done  -  in 15 seconds will push to github and take snapshots of timestamps")
                time.sleep(15)
                run_bash_command("git add .")
                run_bash_command("git commit -m '.'")
                run_bash_command("git push")
                after = {f: os.path.getmtime(f) for f in os.listdir(path)}
                added = [f for f in after if f not in before]
                removed = [f for f in before if f not in after]
                modified = [f for f in after if f in before and before[f] != after[f]]
        before = after
        print("waiting...")


def run_bash_command(command):
    result = subprocess.run(command, shell=True, capture_output=False, text=True)

def remove_file_extension(filename):
    return '.'.join(filename.split('.')[:-1]) if '.' in filename else filename

def is_python_file(filename):
    return filename.endswith('.py')




watch_directory()


one
