import os
import cv2
import easyocr
import json
import time
# 检查json是否存在，若不存在就按个模版进去
rank = json.dumps({'1': '-', '2': '-', '3': '-', '4': '-', 'tm': '-', 'ins': '-', 'ex': '-', 'update': '-'}, sort_keys=True, indent=4, separators=(',', ': '))
if os.path.exists('rank.json'):
    print('Ready.')
else:
    with open('rank.json', 'w') as f:
        print(rank, file=f)
# 处理1档图片
    #剪切图片
if os.path.exists(r'./simg1.png'):
    img = cv2.imread("simg1.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimg1.png", cropped)
    # OCR识别
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    result1 = reader.readtext(r"./cimg1.png", detail = 0)
    # 写入json
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["1"] = result1
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    # 删除原图片，阻止屎山代码疯狂计算
    os.remove("./simg1.png")
else:
    print('Rank1:Skin')
# 处理2档图片，不再详细注释
if os.path.exists(r'./simg2.png'):
    img = cv2.imread("simg2.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimg2.png", cropped)
    #设置识别中英文两种语言
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    result2 = reader.readtext(r"./cimg2.png", detail = 0)
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["2"] = result2
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    os.remove("./simg2.png")
else:
    print('Rank2:Skin')
# 处理3档图片
if os.path.exists(r'./simg3.png'):
    img = cv2.imread("simg3.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimg3.png", cropped)
    #设置识别中英文两种语言
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    result3 = reader.readtext(r"./cimg3.png", detail = 0)
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["3"] = result3
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    os.remove("./simg3.png")
else:
    print('Rank3:Skin')
# 处理4档图片
if os.path.exists(r'./simg4.png'):
    img = cv2.imread("simg4.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimg4.png", cropped)
    #设置识别中英文两种语言
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    result4 = reader.readtext(r"./cimg4.png", detail = 0)
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["4"] = result4
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    os.remove("./simg4.png")
else:
    print('Rank4:Skin')
# 处理TM难度图片
if os.path.exists(r'./simgtm.png'):
    img = cv2.imread("simgtm.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimgtm.png", cropped)
    #设置识别中英文两种语言
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    resulttm = reader.readtext(r"./cimgtm.png", detail = 0)
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["tm"] = resulttm
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    os.remove("./simgtm.png")
else:
    print('RankTM:Skin')
# 处理INS难度图片
if os.path.exists(r'./simgins.png'):
    img = cv2.imread("simgins.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimgins.png", cropped)
    #设置识别中英文两种语言
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    resultins = reader.readtext(r"./cimgins.png", detail = 0)
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["ins"] = resultins
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    os.remove("./simgins.png")
else:
    print('RankINS:Skin')
# 处理EX难度图片
if os.path.exists(r'./simgex.png'):
    img = cv2.imread("simgex.png")
    print(img.shape)
    cropped = img[396:634, 773:1198]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./cimgex.png", cropped)
    #设置识别中英文两种语言
    reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
    resultex = reader.readtext(r"./cimgex.png", detail = 0)
    with open("rank.json", "r") as f:
        old_data = json.load(f)
        old_data["ex"] = resultex
    with open("rank.json", "w") as f:
        json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    os.remove("./simgex.png")
else:
    print('RankEX:Skin')
# 标记更新时间
timeup = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open("rank.json", "r") as f:
    old_data = json.load(f)
    old_data["update"] = timeup
with open("rank.json", "w") as f:
    json.dump(old_data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
