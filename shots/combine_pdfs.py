from PIL import Image
from reportlab.pdfgen import canvas
import os

def convert_pngs_to_pdf():
    # Get all PNG files and sort them numerically
    png_files = [f for f in os.listdir('.') if f.endswith('.png')]
    png_files.sort(key=lambda x: int(x.split('.')[0]))
    
    # Create output PDF
    output_pdf = "combined_output.pdf"
    c = canvas.Canvas(output_pdf)
    
    # Process each PNG file
    for png_file in png_files:
        # Open the PNG file
        img = Image.open(png_file)
        
        # Get image dimensions
        width, height = img.size
        
        # Set PDF page size to match image size
        c.setPageSize((width, height))
        
        # Draw the image on the PDF
        c.drawImage(png_file, 0, 0, width=width, height=height)
        
        # Add a new page for the next image
        c.showPage()
    
    # Save the PDF
    c.save()
    print(f"PDF has been created successfully: {output_pdf}")

if __name__ == "__main__":
    convert_pngs_to_pdf() 