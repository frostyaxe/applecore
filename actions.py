from re import search
from os import path

def command_not_found(raw_build_log):
    
    m = search('\'(\w+)\' is not recognized as an internal or external command', raw_build_log)
    command = ""
    path_exist_status = ""
    if m:
        command = m.group(1)
        if path.exists(command):
            path_exist_status = "{} : Path exists".format(command)
        else:
            path_exist_status = "{} : Path does not exist".format(command)
    else:
        return ""

    return f''' 
    - Please verify whether software is installed or not.
    - If you are trying to execute the script then here is the additional details:
            + {path_exist_status}
    '''

def artifact_not_found(raw_build_log):
    return "Artifacts"