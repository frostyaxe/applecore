from re import search
from os import path
import difflib
import pkgutil

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

def python_module_not_found(raw_build_log):
    print("Executing action for python module not found error...")
    m = search('ModuleNotFoundError: No module named \'(\w+)\'', raw_build_log)
    module_name_ = m.group(1)

    modules = []
    for _, module_name, _ in pkgutil.iter_modules():
        modules.append(module_name)
    from fuzzywuzzy import process
    mod_matches = process.extractBests(module_name_,modules)
    
    return '''
        - You might be getting the ModuleNotFound error because the module name used with import is incorrect. Please find some of the closest matching modules below:
            {modules} 
    '''.format(modules=mod_matches)