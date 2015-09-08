from PIL import Image

def change_image(image_path,size=(1136,640)):
    im = Image.open(image_path)
    size = (size[1],size[0]) if im.size[1] >im.size[0] else size
    im.thumbnail(size,Image.ANTIALIAS)
    im.save('result-'+image_path)

if __name__ == '__main__':
    change_image('test.jpg')
