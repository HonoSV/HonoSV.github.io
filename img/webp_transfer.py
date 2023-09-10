import os
from PIL import Image


TYPE_LIST = [".png", ".jpg", ".jpeg"]


def pic_2_webp(root, file):
    # 读入文件
    ori_file = os.path.join(root, file)
    im = Image.open(ori_file)

    # 保存
    im.save(os.path.join(root, file.split('.')[0] + ".webp"))

    # 删除原文件
    # os.remove(ori_file)


def walk_files(path):
    for (root, dirs, files) in os.walk(path):
        for file in files:
            for suffix in TYPE_LIST:
                if file.endswith(suffix) or file.endswith(suffix.upper()):
                    pic_2_webp(root, file)


walk_files("./")
