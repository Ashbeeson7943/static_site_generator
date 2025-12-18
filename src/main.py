import os
import shutil


def main():
    static_file_path = "./static"
    public_file_path = "./public"
    clear_public(public_file_path)
    copy_static_to_public(static_file_path, public_file_path)

def clear_public(base_path):
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path)

def copy_static_to_public(base_path, destination_path):
    file_list = os.listdir(base_path)
    for item in file_list:
        item_path = os.path.join(base_path, item)
        if not os.path.isfile(item_path):
            dir_path = os.path.join(destination_path, item)
            print(f"Creating directory: {dir_path}")
            os.mkdir(dir_path)
            copy_static_to_public(item_path, dir_path)
        else:
            dest_path = os.path.join(destination_path, item)
            print(f"Copying: {item_path} to {dest_path}")
            shutil.copy(item_path, dest_path)



main()