import pathlib

path_object = pathlib.Path.home() / "my_folder"
path_object.mkdir(exist_ok=True)
new_file = path_object / "my_file.txt"
new_file.touch()
print(path_object.exists())
print(new_file.exists())

file_path = path_object
print(file_path.exists())
print(path_object)
print(new_file.parent)
