import os
import sys
import re


def filter(root):
    if not os.path.exists(root):
        print("The root file does not exist.")
        sys.exit(1)
        
    file_content = []
    with open(root, 'r') as f:
        file_content = f.readlines()
    
    ## Detect input command
    for line in file_content:
        if line.startswith("%"):
            continue
        res = re.search(r'\\input\{([^{}]+)\}', line)
        if res:
            parent_dir = os.path.dirname(root)
            child_file = res.group(1)
            child_path = os.path.join(parent_dir, child_file)
            file_content.extend(filter(child_path)) # TODO: correct file_content.append
            
    return file_content

def get_img_addr(root, file_content):
    root_dir = os.path.dirname(root)
    img_addr = []
    for line in file_content:
        res = re.search(r'\\includegraphics\[[^\]]*\]\{([^{}]+)\}', line)
        if res:
            file_name = res.group(1)
            ## append root dir to file_name
            img_addr.append(os.path.join(root_dir, file_name))
    return img_addr

def remove_unused_img(root, img_addr):
    ## get root dir
    root_dir = os.path.dirname(root)
    ## get all img files (which is file is not end with .tex, .bib, .cls)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".tex") or file.endswith(".bib") or file.endswith(".cls"):
                continue
            ## If is dircetory, continue
            if os.path.isdir(os.path.join(root, file)):
                remove_unused_img(os.path.join(root, file), img_addr)
            file_path = os.path.join(root, file)
            
            ## compare the file_path with img_addr with os.path.samefile
            is_img = False
            for img in img_addr:
                if os.path.samefile(file_path, img):
                    print("Keep: ", file_path)
                    is_img = True
                    break
            
            ## remove the file
            if not is_img:
                print("Remove: ", file_path)
                os.remove(file_path)
            

def main():
    if len(sys.argv) != 2:
        print("Usage: python filter.py <root_file>")
        sys.exit(1)
    
    root = sys.argv[1]
    file_content = filter(root)
    img_addr = get_img_addr(root, file_content)
    remove_unused_img(root, img_addr)
    print(img_addr)
    
if __name__ == "__main__":
    main()