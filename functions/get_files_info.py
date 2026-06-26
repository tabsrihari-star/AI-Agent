import os

def get_files_info(working_dir : str, dir : str =".")-> str :
    
    abs_working_dir_path = os.path.abspath(working_dir)
    abs_dir_path = os.path.abspath(dir)

    if dir != ".":
        is_target_dir_valid = os.path.commonpath([abs_working_dir_path,abs_dir_path]) == abs_working_dir_path
        if is_target_dir_valid:
            target_dir_path = os.path.join(abs_working_dir_path,dir)
        else:
            return f'Error : Invalid directory path : "{abs_dir_path}" in working directory : "{abs_working_dir_path}"'
    else:
        target_dir_path = abs_working_dir_path
    if not os.path.isdir(target_dir_path):
        return f'Error: "{dir}" is not a directory'
   # contents = os.list
    return f'Sucess : "{dir}" is within the working directory : "{working_dir}"'