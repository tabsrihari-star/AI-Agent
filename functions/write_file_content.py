import os
def write_file_content(working_dir: str, file_path: str, content: str) -> str:
    
    abs_working_dir_path= os.path.abspath(working_dir)
    #abs_file_path = os.path.normpath(os.path.join(abs_working_dir_path,file_path))
    abs_file_path = os.path.abspath(os.path.join(working_dir,file_path))

    if not os.path.isdir(abs_working_dir_path):
        return f'Error: Working directory "{working_dir}" does not exist or not a directory'
    
        # if path points to existing directory
    if os.path.isdir(abs_file_path):
        f'Error: Cannot write to "{file_path}" as it is a directory'

    # if the file path contained a parent_dir
    parent_dir = os.path.dirname(abs_file_path)

    #check if parent_dir actually exists
    if not os.path.isdir(parent_dir):
        try :
            os.makedirs(parent_dir)
        except Exception as e :
            f'Error: Could not make the parent directory: "{parent_dir}" , Exception= "{e}"'
    
    is_file_path_valid=os.path.commonpath([abs_working_dir_path,abs_file_path]) == abs_working_dir_path
    if not is_file_path_valid:
        return f'Error: the file path: "{file_path}" is not found inside the working directory:{working_dir}'

    # if file_path is not a file: 
    if not os.path.isfile(abs_file_path):
        pass
    try:
        print("Parent Directory: ", parent_dir,"\n", "Abs file path : ", abs_file_path, "\n", "Abs Work Dir path : ", abs_working_dir_path,"---------")

        with open(abs_file_path,"w") as f :
            f.write(content) # overwriting the file with
        print("Parent Directory: ", parent_dir,"\n", "Abs file path : ", abs_file_path, "\n", "Abs Work Dir path : ", abs_working_dir_path)
        return f'Success: Successfully wrote content of length : "{len(content)}" in path : "{file_path}"'
    except Exception as e :
        return f'Error: cannot write to file, exception: "{e}"'

    