import os
from PIL import Image, ImageDraw

def square_to_round_corner(image_path, output_path, size=(108, 108), corner_radius=20):
    """
    将正方形图片转换为带有圆角的正方形图片，背景透明。
    """
    # 打开图片文件
    img = Image.open(image_path)
    
    # 调整图片大小为指定尺寸（如 108x108）
    img = img.resize(size)
    
    # 创建一个带有圆角的蒙版
    mask = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(mask)
    
    # 绘制圆角矩形
    draw.rounded_rectangle(
        (0, 0) + size,  # 矩形范围
        fill=(0, 0, 0, 255),  # 填充颜色为黑色，完全不透明
        radius=corner_radius  # 圆角半径
    )
    
    # 将原图与蒙版复合，得到带有圆角的图片
    result = Image.new('RGBA', size, (0, 0, 0, 0))  # 透明背景
    result.paste(img, (0, 0), mask=mask)
    
    # 保存结果，背景透明
    result.save(output_path, 'PNG')

def batch_square_to_round_corner(input_dir, output_dir, size=(108, 108), corner_radius=20):
    """
    批量将输入目录中的正方形图片转换为带有圆角的正方形图片，背景透明。
    """

    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        # 检查是否是图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f'round_{filename}')
            try:
                square_to_round_corner(input_path, output_path, size, corner_radius)
                print(f"已处理：{filename} -> {output_path}")
            except Exception as e:
                print(f"处理失败：{filename}，错误信息：{str(e)}")


# 示例 usage:
# 输入目录和输出目录需要是存在的文件路径
input_folder = 'input'  # 存放输入正方形图片的目录
output_folder = 'output'  # 存放输出圆角正方形图片的目录
size = (108, 108)  # 输出图片大小
corner_radius = 20  # 圆角半径

batch_square_to_round_corner(input_folder, output_folder, size, corner_radius)
