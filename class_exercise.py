import pathlib

path = pathlib.Path("/cohort14/private.img")
cwd_path = pathlib.Path.cwd() / "Ridwanullah" / "private.py"
#path = pathlib.Path("c:\kelloges\hello.txt")
print(cwd_path)
#print("Parent -", cwd_path.parent)
#print(list(path.parents))
#print("Anchor - ", path.anchor)
#print("Name -", path.name)
#print("Suffix - ", path.suffix)
#print("Stem - ", path.stem)


#cwd_path.mkdir(exist_ok=True)
#print(fake_path.exist())
print(cwd_path.exists())







