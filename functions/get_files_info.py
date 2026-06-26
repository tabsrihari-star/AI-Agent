import os

def get_files_info(working_dir : str, dir : str =".")-> str :
    
    abs_working_dir_path = os.path.abspath(working_dir)
    abs_dir_path = os.path.abspath(dir)

    if dir != ".":
        is_target_dir_valid = os.path.commonpath([abs_working_dir_path,abs_dir_path]) == abs_working_dir_path
        if is_target_dir_valid:
            target_dir_path = os.path.join(abs_working_dir_path,dir)
        else:
            return f'Error :directory path : "{abs_dir_path}" not found in working directory : "{abs_working_dir_path}"'
    else:
        target_dir_path = abs_working_dir_path
    if not os.path.isdir(target_dir_path):
        return f'Error: "{dir}" is not a directory'

    #return f'Sucess : "{dir}" is within the working directory : "{working_dir}"'
    # now we should iterate over the contents in the diretory
    contents = os.listdir(target_dir_path)
    print(f'Result for {dir} directory : \n')
    for content in contents :
        content_path=os.path.join(target_dir_path,content)
        #print("Content Path :",content_path)
        file_size=os.path.getsize(content_path)
        is_dir = os.path.isdir(content_path)
        print(f' name:"{content}", file_size="{file_size}",is_dir="{is_dir}"')
    