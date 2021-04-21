import os
path = "test_dir"
files = os.listdir(path)
files = [os.path.join(path, file) for file in files]
files = [file for file in files if os.path.isfile(file)]
res = max(files, key=os.path.getctime)
print(res)
filename, file_extension = os.path.splitext(str(res))
if file_extension == ".txt":

# filename, file_extension = os.path.splitext(str(res))
# print(file_extension)