# -*- coding: utf-8 -*-
 
from PIL import Image,ImageFont,ImageDraw,ImageColor
 
def add_num(image,text):
    #1.打开图片
    #2.设置字体
    font = ImageFont.truetype("arial.ttf",50)
    #3.设置字体颜色
    fontcolor = ImageColor.colormap.get('red')
    #4.将字体加到图片上
    draw = ImageDraw.Draw(image)
    width , height = image.size
    draw.text((width-30,10),text,font=font,fill=fontcolor)
    #5.保存图片
    image.save("D:\\awesome-python3-webapp\\exercise\\directory\\2.jpg")
 
 
if __name__ == '__main__':
    image = Image.open("D:\\awesome-python3-webapp\\exercise\\directory\\1.jpg")
    text = "3"
    add_num(image,text)
