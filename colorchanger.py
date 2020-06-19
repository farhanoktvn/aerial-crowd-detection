import os
from PIL import Image

def main(folder):
    
    try:
        cur_dir = os.path.dirname(__file__) + "/" + folder
        for count, filename in enumerate(os.listdir(cur_dir)):
            img = Image.open(cur_dir + "/" + filename).convert('LA').convert("RGB")
            img.save(cur_dir + "/" + filename)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    folder = str(input("Which folder do you want to change color? "))
    main(folder)