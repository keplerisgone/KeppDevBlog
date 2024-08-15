import os

def replace_spaces_with_hyphens(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if ' ' in filename:
                new_filename = filename.replace(' ', '-')
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

if __name__ == "__main__":
    target_directory = input("Enter the directory path: ")
    replace_spaces_with_hyphens(target_directory)
