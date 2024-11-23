from marker.convert import convert_single_pdf
from marker.models import load_all_models
import os

class ParseThat_PDF_Agent:
    def __init__(self):
        self._images = None
        self._fulltext = None
        self._metadata = None

    def parse (self, filepath):
        fpath = fpath
        model_lst = load_all_models()
        full_text, images, out_meta = convert_single_pdf(fpath, model_lst)

        self._fulltext = full_text
        self._images = images
        self._metadata = out_meta
        
    def save (self, filepath, save_fulltext=True, save_images=True, save_metadata=True):
        # Define the output filepath is going to be with the same filename as the pdf
        output_md_path = ""

        if save_fulltext:
            # Save the full_text into a Markdown file
            with open(output_md_path, "w", encoding="utf-8") as md_file:
                md_file.write(self._fulltext)

            print(f"Markdown file saved at {output_md_path}")

        # Define the output folder for images to be "images" folder in the folder of the pdf

        # Create the folder if it doesn't exist
        os.makedirs(output_images_folder, exist_ok=True)

        # Save each image in the dictionary
        for filename, image in images.items():
            # Construct the full path for each image
            image_path = os.path.join(output_images_folder, filename)
            # Save the image
            image.save(image_path)

        print(f"Images saved in folder: {output_images_folder}")