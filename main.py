from glob import glob

all_files= glob("quotes/*.txt")

for file in all_files:
    with open(file, 'r') as f:
        print('filename:', file)
        print('quotes:', f.read())
        print("--------------------------------------------------")