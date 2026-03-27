import qrcode
url=input("Enter your url : ")
filename=input("File name you want save it as : ")
if not(filename.endswith(".png")):
    filename=filename + ".png"



img=qrcode.make(url)
img.save(filename)
