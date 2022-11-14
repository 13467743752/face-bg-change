from rembg import remove

# 待处理的图片路径
input_path = 'D://234.png'
# 处理后存储的图片路径
output_path = 'D://output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)