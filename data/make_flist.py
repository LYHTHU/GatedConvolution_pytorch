import os


# For place2 <places365_standard> dataset only. 
def make_img_list(path='../places365_standard', train=True):
    flist = []
    if train:
        txt_path = os.path.join(path, 'train.txt')
    else:
        txt_path = os.path.join(path, 'val.txt')

    f = open(txt_path, 'r')
    file_list = f.readlines()
    f.close()
    for file in file_list:
        flist.append(os.path.join(path, file))
    return flist
            

def make_pkl_list(path, out_path):
    pass


if __name__ == "__main__":
    make_img_list()