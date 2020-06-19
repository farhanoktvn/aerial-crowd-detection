import os

def main(folder):
    
    try:
        cur_dir = os.path.dirname(__file__) + "/" + folder
        for count, filename in enumerate(os.listdir(cur_dir)):
            dst = cur_dir + "/" + folder + "_" + str(count) + "." + filename.split(".")[-1]
            src = cur_dir + "/" + filename
            os.rename(src, dst)
    except:
        pass

if __name__ == "__main__":
    folder = str(input("Which folder do you want to rename? "))
    main(folder)