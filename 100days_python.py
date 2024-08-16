# import random

# jackpot = random.randint(1, 50)
#
# guess = int(input("chal guess kar"))
# counter = 1
#
# while guess != jackpot:
#     if guess < jackpot:
#         print("guess higher")
#     else:
#         print("guess lower")
#     guess = int(input("chal guess kar"))
#     counter += 1
#
# print("sahi jawab")
# print("you took", counter,"attempts")

# L = [12,23,343,353,]
# print(L)
#
#
#
#
# T = tuple("chhatra")
# print(T)

# convert PDF to docx using Python

# from pdf2docx import converter
#
# pdf_file = "coding.pdf"
# docx_file = "coding.docx"
#
# cv = converter(pdf_file)
# cv.converter(docx_file)
# cv.close()



# from pdf2docx import Converter
# import os
#
#
# # Input PDF file path
# pdf_file = "coding.pdf"
#
# # Output DOCX file path
# docx_file = "coding.docx"
#
# # Create a Converter object
# cv = Converter(pdf_file)
#
# # Convert the PDF to DOCX
# cv.convert(docx_file, start=0, end=None)
#
# # Close the Converter
# cv.close()
#
# print(f"Conversion from {pdf_file} to {docx_file} complete.")





# Operators in python -
# arithmatic
# assignment
# comparison
# logical
# bitwise
# identity
# membership





# Remove Image background using python


# 1st try

# from rembg import remove
# from PIL import Image
#
# input_path = "Chhatra.jpg"
# output_path = "Chhatra.jpg"
# ch = Image.open(input_path)
# output = remove.
# output.save(output_path)


# 2nd try

# from rembg import remove
# from PIL import Image
#
# # Input image file path
# input_image_path = "iit.jpg"
#
# # Output image file path (without background)
# output_image_path = "iit.jpg"
#
# # Use the remove() function from the rembg library
# with open(input_image_path, "rb") as input_file:
#     with open(output_image_path, "wb") as output_file:
#         output = remove(input_file)
#         output_file.write(output)
#
# # Display the output image (optional)
# output_image = Image.open(output_image_path)
# output_image.show()

#
#
# from pytube import YouTube
#
#
# # Replace 'video_url' with the URL of the YouTube video you want to download
# video_url = 'https://www.youtube.com/watch?v=gbmwWZRq72Y&list=PLrN_S08trZepmNfyTjsbGNr0XMciQcIMM&ab_channel=freeCodeCampHindi'
#
# # Create a YouTube object
# yt = YouTube(video_url)
#
# # Get the highest resolution stream available
# video_stream = yt.streams.filter(res="720p")
#
# # Replace 'path_to_save' with the path where you want to save the downloaded video
# path_to_save = 'D:\Computer_code'
#
# # Download the video
# video_stream.download(output_path=path_to_save)
#
#
# print("Video downloaded successfully!")


#
#
# import os
# from pytube import YouTube
#
# # Define the URL of the YouTube video you want to download
# video_url = "https://www.youtube.com/watch?v=gbmwWZRq72Y&list=PLrN_S08trZepmNfyTjsbGNr0XMciQcIMM&ab_channel=freeCodeCampHindi"
#
# # Define the path where you want to save the downloaded video
# save_path = "D:\Computer_code"
#
# # Create a custom progress callback function
# def on_progress(stream, chunk, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage = (bytes_downloaded / total_size) * 100
#     print(f"Downloading... {percentage:.2f}% complete", end="\r")
#
# # Create a YouTube object and select the video stream to download
# yt = YouTube(video_url, on_progress_callback=on_progress)
# video_stream = yt.streams.get_highest_resolution()
#
# # Start the download
# print("Downloading video...")
# video_stream.download(output_path=save_path)
# print("Download completed!")

