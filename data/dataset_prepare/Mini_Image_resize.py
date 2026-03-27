from PIL import Image

def resize_image(input_path, output_path, target_size=512):
    """
    简单的图像尺寸调整函数
    """
    try:
        img = Image.open(input_path)
        img.thumbnail((target_size, target_size))
        img.save(output_path)
    except Exception as e:
        print(f"Error resizing image: {e}")
