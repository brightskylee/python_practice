import os


def num_of_python(root_dir):
    number_of_python = 0
    for path, sub_dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                number_of_python += 1
    for sub_dir in sub_dirs:
        number_of_python += num_of_python(os.path.join(path, sub_dir))
    return number_of_python

if __name__ == "__main__":
    root_dir = "."
    print(num_of_python(root_dir))
