import os
import shutil


def delete_folder(base_dir, dir_name):

    for path, subdirs, files in os.walk(base_dir):
        print(subdirs)
        # print(subdirs)
        if not subdirs:
            return

        for subdir in subdirs:
            if subdir == dir_name:
                # shutil.rmtree(os.path.join(path, subdir))
                print("find " + subdir)
                print(os.path.join(path, subdir))
                return

        for subdir in subdirs:
            if subdir == "Users":
                print("executing " + "delete_folder(" + os.path.join(path, subdir) + ", " + dir_name + ")");
                delete_folder(os.path.join(path, subdir), dir_name)
                return





root_dir = "."
dir_name = "HLi"
delete_folder(root_dir, dir_name)