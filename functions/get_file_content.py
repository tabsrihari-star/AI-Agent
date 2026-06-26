import os 
from config import MAX_CHARS
def get_file_content (working_dir : str, file_path : str)->str:
    abs_working_dir_path= os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(file_path)
    is_file_path_valid=os.path.commonpath([abs_working_dir_path,abs_file_path]) == abs_working_dir_path
    if not is_file_path_valid:
        return f' the file path: "{file_path}" is not found in the working directory:{working_dir}'

    # if file_path is not a file: 
    if not os.path.isfile(file_path):
        return f'Error : The given "{file_path}" is not a file'
    with open(abs_file_path,"r") as f :
        f.read(MAX_CHARS)
        # check if the file was larger than the limit 
        if f.read(1):
            content +=f'[..File "{file_path}" truncated at "{MAX_CHARS}"]'
    
    return