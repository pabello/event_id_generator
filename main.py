from PIL import Image, ImageDraw, ImageFont
from os import path, makedirs


BACKGROUND_PICTURE = 'orkiestralia_dyplom_uczestnik_imienny_dyplom.jpg'
NAME_LIST_FILE = 'names_list.txt'  # Path to the file containing names
FONT_PATH = 'font/SourceSerif4_36pt-SemiBold.ttf'  # Path to the font file
DESTINATION_DIRECTORY = 'generated'  # Directory to save the generated images

COLOR_CODING = 'CMYK'  # Change to 'RGB' if you want to use RGB color mode
NAME_FIELD_Y = 600  # Y-coordinate of the center of the name field
FILE_EXTENSION = '.jpeg'  # File extension for the saved images

# Create a new blank image for the ID card
background = Image.open(BACKGROUND_PICTURE).convert(COLOR_CODING)
width, height = background.size
image = Image.new(COLOR_CODING, (width, height), (255, 255, 255))
image.paste(background, (0, 0))
name_font = ImageFont.truetype(FONT_PATH, size=157)  # Relative path to the font file

if not path.exists(DESTINATION_DIRECTORY):
    makedirs(DESTINATION_DIRECTORY)

with open(NAME_LIST_FILE, "r") as file:
    lines = file.readlines()

images:list[Image.Image] = []
for line in lines:
    copy = image.copy()
    draw = ImageDraw.Draw(copy)

    participant_name = line.strip()
    text_width, text_height = name_font.font.getsize(participant_name)[0]
    draw.text((width / 2 - text_width / 2, NAME_FIELD_Y - text_height / 2), participant_name, fill='rgb(47, 47, 46)', font=name_font)
    images.append(copy)
    
    # Save the image with participant's name
    output_filename = f'{DESTINATION_DIRECTORY}/{participant_name}.jpeg'
    copy.save(output_filename, dpi=(300, 300))

images[0].save(f'{DESTINATION_DIRECTORY}/_print.pdf', save_all=True, dpi=(300, 300), append_images=images[1:])
