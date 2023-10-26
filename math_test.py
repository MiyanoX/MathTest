import os
import shutil
import random
from datetime import datetime

# Create the directory if it doesn't exist.
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        
def read_files_in_directory(directory_path):
    try:
        # List all files in the directory
        files = os.listdir(directory_path)
        return files
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
def choose_random_problems(directory_path, number):
    try:
        files = read_files_in_directory(directory_path)
        random_problems = random.sample(files, number)
        return random_problems
            
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_file_to_directory(file_path, target_directory):
    try:
        # Check if the provided target directory exists. If not, create it.
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # Copy the file to the target directory.
        shutil.copy(file_path, target_directory)
        print(f"File '{file_path}' has been copied to '{target_directory}'")

    except shutil.SameFileError:
        print("Source and destination represent the same file.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def add_files_new_directory(random_problems, directory_path, new_directory_path):
    for problem in random_problems:
        copy_file_to_directory(directory_path + "/" + problem, new_directory_path)
        
def rename_files_sequentially(directory_path, pre_name):
    try:
        # Get a list of all files in the directory
        files = os.listdir(directory_path)

        for idx, filename in enumerate(files):
            # Get the file extension
            extension = os.path.splitext(filename)[1]

            # Build the new filename. This consists of the count and the original extension.
            new_filename = pre_name + str(idx+1) + extension

            # Get the full paths for the source and destination
            source = os.path.join(directory_path, filename)
            destination = os.path.join(directory_path, new_filename)

            # Check if we're not trying to rename a directory
            if os.path.isfile(source):
                # Rename the actual file
                os.rename(source, destination)
                print(f"Renamed file {filename} to {new_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
        
def random_problem(new_directory_name, problem_number):
    directory_problem_path = "./Problems"
    directory_answer_path = "./Answers"
    new_directory_path = "./" + new_directory_name
    new_directory_problem_path = new_directory_path + "/Problems"
    new_directory_answer_path = new_directory_path + "/Answers"
    
    random_problems = choose_random_problems(directory_problem_path, problem_number)
    
    add_files_new_directory(random_problems, directory_problem_path, new_directory_problem_path)
    add_files_new_directory(random_problems, directory_answer_path, new_directory_answer_path)
    
    rename_files_sequentially(new_directory_problem_path, "Problem")
    rename_files_sequentially(new_directory_answer_path, "Answer")


now = datetime.now()
random_problem(now.strftime("%Y-%m-%d-%H-%M-%S"), 20)