# pip install python-barcode
# import EAN13 from barcode module
from barcode import EAN13
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

def generator(number):
    # Let us create an object of EAN13 class and pass the number with the ImageWriter() as the writer
    my_code = EAN13(number,writer=ImageWriter())
    my_code.save("bar_code")

if __name__ == "__main__":
    # Make sure to pass the number as string
    generator(input('Enter 12 Digit Number To Generate Bar Code:'))