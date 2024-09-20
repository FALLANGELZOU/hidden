
import os
import torch
import torchvision.utils as vutils
def gen_dataset(root_path= "./dataset", train_num = 1, val_num = 1):
    os.mkdir(root_path)
    train_path = os.path.join(root_path, "train", "class_1")
    val_path = os.path.join(root_path, "val", "class_1")
    os.mkdir(os.path.join(root_path, "train"))
    os.mkdir(os.path.join(root_path, "val"))
    os.mkdir(train_path)
    os.mkdir(val_path)
    # 随机生成512x512的图片
    for i in range(train_num):
        img = torch.randn(1, 3, 512, 512)
        vutils.save_image(img, os.path.join(train_path, f"{i}.png"))
    for i in range(val_num):
        img = torch.randn(1, 3, 512, 512)
        vutils.save_image(img, os.path.join(val_path, f"{i}.png"))
    pass


if __name__ == "__main__":
    gen_dataset()