from PIL import Image
image1 = Image.open(r'./out/certificate.png')
im1 = image1.convert('RGB')
im1.save(r'./out/certificate.pdf')