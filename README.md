# EVENT ID GENERATOR
## What is this project?
It is a python script for generating ID badges for event participants.
When the participant list is long, preparing their IDs takes a lot of time. This tool finishes the task in seconds and leaves you with a PDF file (almost) ready to print.

Can also be used for participant diplomas or other named documents with generic layout.

## How to use?
1. Put a background image in the project directory.
2. Adjust the `BACKGROUND_PICTURE` constant in the code to the background file name.
3. Do the same with a font file or use the provided default.
4. Put a `names_list.txt` file in the project directory with every name in separate line.
5. Adjust the `NAME_FIELD_Y` constant to match the text position (pixels counted from the top of the image).
6. Adjust the `COLOR_CODING` constant to use eiter RGB or CMYK color coding.
7. *Optionally change the `FILE_EXTENSION` and `DESTINATION` constants to your liking. Be aware that CMYK color coding is only supported by JPEG images and PDF files.
8. Run the code:
```bash
python3 main.py
```

## How it works?
This script generates a list of named documents (i.e. ID badges, diplomas) and puts them in a separate directory. All generated images are saved in separate files as well as in a PDF file for easier pringing.