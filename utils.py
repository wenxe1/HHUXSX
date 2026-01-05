# XOR
KEY = 1 

import os

def xor_crypt_file(filepath):
    # 1. 读取原始数据
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())
    
    # 2. 进行异或混淆 (加密/解密是同一个操作)
    for i in range(len(data)):
        data[i] ^= KEY
        
    # 3. 覆盖写入
    with open(filepath, 'wb') as f:
        f.write(data)
    print(f"✅ 已处理: {filepath}")

if __name__ == "__main__":
    target_dir = "questions" # 你的题库文件夹
    
    if not os.path.exists(target_dir):
        print("❌ 找不到 questions 文件夹")
        exit()

    print(f"正在对 {target_dir} 下的所有 .docx 进行混淆/还原...")
    print("⚠️  注意：再次运行此脚本会将文件还原！")
    
    for filename in os.listdir(target_dir):
        if filename.endswith(".docx"):
            full_path = os.path.join(target_dir, filename)
            xor_crypt_file(full_path)
            
    print("🎉 全部完成！现在的 .docx 文件直接打开会报错。")
