
import importlib.util
import sys
import os

def load_module(file_name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def load_scan_functions():
    module_files = [dir for dir in os.listdir(os.path.join('core','scripts'))]
    detection_functions = []
    for file in module_files:
        detection_functions.append(load_module(os.path.join("core","scripts",file),file.removesuffix(".py")).scan)

    return detection_functions

def load_results_functions():
    module_files = [dir for dir in os.listdir(os.path.join('core','scripts'))]
    detection_functions = []
    for file in module_files:
        detection_functions.append(load_module(os.path.join("core","scripts",file),file.removesuffix(".py")).show_results)

    return detection_functions

def load_header_functions():
    module_files = [dir for dir in os.listdir(os.path.join('core','scripts'))]
    detection_functions = []
    for file in module_files:
        detection_functions.append(load_module(os.path.join("core","scripts",file),file.removesuffix(".py")).show_header)

    return detection_functions
