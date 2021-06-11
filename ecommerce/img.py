from PIL import Image

i1 = Image.open(r'C:\Users\Haroon fayaz\Desktop\Test\first.JPG')
i2 = Image.open(r'C:\Users\Haroon fayaz\Desktop\Test\fifth.JPG')
i3 = Image.open(r'C:\Users\Haroon fayaz\Desktop\Test\third.JPG')

ic1 = i1.convert('RGB')
ic2 = i2.convert('RGB')
ic3 = i3.convert('RGB')

imlist =[ic2,ic3]

ic1.save(r'C:\Users\Haroon fayaz\Desktop\Test\bunch.pdf',save_all = True,append_images = imlist)