import os


def get_module_file_path():
    return(__file__)

def get_module_dir_path():
    return(os.path.dirname(__file__))

def get_module_file_name():
    return(os.path.basename(__file__))


if __name__ == "__main__":
    # This will generate an error
    print(get_module_file_path())
