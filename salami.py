#
#
#

from PIL import Image

# Import from text file
def import_text():
    '''
    opens txt file with one row to be translated
    '''
    text_file = open('text.txt','r') 
    text = text_file.read()
    text_file.close()
    return text

# Import Letters
def import_image():
    image = Image.open('letters.png')
    return image  
# Generate new text

# Output

print(import_text())
image = import_image()
image.show()
