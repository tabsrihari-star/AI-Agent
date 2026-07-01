import os
def write_file_content(working_dir: str, file_path: str, content: str) -> str:
    
    abs_working_dir_path= os.path.abspath(working_dir)
    abs_file_path = os.path.normpath(os.path.join(abs_working_dir_path,file_path))
    
    is_file_path_valid=os.path.commonpath([abs_working_dir_path,abs_file_path]) == abs_working_dir_path
    if not is_file_path_valid:
        return f' the file path: "{file_path}" is not found inside the working directory:{working_dir}'
    # if path points to existing directory
    if os.path.isdir(abs_file_path):
        f'Error: Cannot write to "{file_path}" as it is a directory'

    # if file_path is not a file: 
    if not os.path.isfile(abs_file_path):
        made_dir = os.makedirs(abs_file_path,exist_ok=True) #exist_ok set to True to create any missing directories
        try:
            with open(made_dir,"w") as f :
                f.write(content) # overwriting the file with
        except Exception as e :
            return f'Error: cannot write to file, exception: "{e}"'
    parent_dir = os.path.dirname(abs_file_path)
    try:
        with open(made_dir,"w") as f :
            f.write(content) # overwriting the file with
    except Exception as e :
        return f'Error: cannot write to file, exception: "{e}"'

    return f'Succesfully wrote content of length : "{len(content)}" in path : "{file_path}"'