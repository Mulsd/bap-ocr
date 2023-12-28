# coding: utf-8
import base64
from flask import request
from flask import Flask
import os
import time
app=Flask(__name__)
# 定义路由
@app.route("/photo", methods=['POST'])
def get_frame():
    # 接收图片
    upload_file = request.files['file']
    # 获取图片名
    file_name = upload_file.filename
    # 返回到脚本的上传处理时间
    timewup = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 文件保存目录
    file_path=r'./'
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片
        upload_file.save(file_paths)
        # 转接上剪切识别的py文件，
        #with open(r'file_paths', 'rb') as f:
        with open(r'./ocr.py', errors = 'ignore') as f:
            res = exec(f.read())
            return timewup
if __name__ == "__main__":
    app.run()