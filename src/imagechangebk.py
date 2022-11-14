from removebg import RemoveBg
from PIL import Image

rmbg = RemoveBg("kfKrPF2o8LGv1RBURitZdwBL", "error.log")
file_in = 'D:\\345.png'
file_out = 'D:\\outimage.png'
# 换背景色
# 白色
color = (255, 255, 255)
# 蓝色
color = (0, 125, 255)
# 红色
color = (255, 0, 0)

p, s = file_in.split(".")
rmbg.remove_background_from_img_file(file_in)
file_no_bg = "{}.{}_no_bg.{}".format(p, s, s)
no_bg_image = Image.open(file_no_bg)
x, y = no_bg_image.size
new_image = Image.new('RGBA', no_bg_image.size, color=color)
new_image.paste(no_bg_image, (0, 0, x, y), no_bg_image)
new_image.save(file_out)
new_image.show(file_out)
