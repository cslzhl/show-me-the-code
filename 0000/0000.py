from PIL import Image, ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font = ImageFont.truetype("msyh.ttf",min(width//6,height//6))
    fillcolor = '#ff0000'
    draw.text((width-font.getsize('99')[0],0),'99',font=font,fill= fillcolor)
    img.save('result.png')
    return 0
if __name__== '__main__':
    image = Image.open('image.png')
    add_num(image)

