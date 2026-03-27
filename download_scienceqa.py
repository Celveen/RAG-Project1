import json
import os
from PIL import Image
import requests
from io import BytesIO

# 加载problems.json文件
with open('/home/xiaochen/RCTS-RAG/Dataset/ScienceQA/data/scienceqa/problems.json', 'r') as f:
    problems = json.load(f)

# 定义保存路径
save_path = '/home/xiaochen/RCTS-RAG/Dataset/ScienceQA/data/scienceqa'

# 创建目录结构
os.makedirs(os.path.join(save_path, 'train'), exist_ok=True)
os.makedirs(os.path.join(save_path, 'val'), exist_ok=True)
os.makedirs(os.path.join(save_path, 'test'), exist_ok=True)

# 从Hugging Face下载图像
def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

# 保存图像文件
for qid, problem in problems.items():
    if problem.get('image'):
        # 获取split
        split = problem['split']
        if split == 'validation':
            split_dir = os.path.join(save_path, 'val')
        else:
            split_dir = os.path.join(save_path, split)
        
        # 创建问题ID目录
        qid_dir = os.path.join(split_dir, qid)
        os.makedirs(qid_dir, exist_ok=True)
        
        # 下载并保存图像
        # 注意：这里需要根据实际情况修改图像URL
        # 由于没有直接的图像URL，我们创建一个占位图像
        image_path = os.path.join(qid_dir, 'image.png')
        
        # 创建一个简单的占位图像
        img = Image.new('RGB', (256, 256), color='white')
        img.save(image_path)
        
        print(f"Created placeholder image for {split} question {qid}")

print("ScienceQA dataset placeholder images created successfully!")
