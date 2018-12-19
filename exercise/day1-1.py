# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw, ImageColor

def add_num(image, text):
	font = ImageFont.truetype("arial.ttf", 50)
	fontcolor = ImageColor.colormap.get('blue')
	draw = ImageDraw.Draw(image)
	width, hight = image.size
	draw.text((width-30,10), text, font = font, fill = fontcolor)
	image.save("D:\\awesome-python3-webapp\\exercise\\directory\\3.jpg")
	
if __name__ == '__main__':
	image = Image.open("D:\\awesome-python3-webapp\\exercise\\directory\\1.jpg")
	text = "3"
	add_num(image,text)