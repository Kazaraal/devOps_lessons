# This is lesson 3 assignment

# # 1.
# a = 1/0

# 2.
# try:
#     a = 1/0
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# 3.
# try:
#     x = 1
# finally:
#     print("finally")

# 4.
# All exception types

# 5.
# It's not very clear on what error happened. 

# 6.
# except IOError - error with input/output, like a file not found issue.
# except ZeroDivisionError - an error when a number is divided by zero.

# 7 & 8 & 9.
# This function takes you input and puts it in file wowords.txt
# def create_file():
#     with open("words.txt", "w") as f:
#         name = input("Enter your name: ")
#         f.write(f"Hello, {name} that's your name, right?!")

# create_file()
# cat words.txt (in the Terminal)

# 10.
# def write_to_file():
#     with open("words.txt", "w", encoding='utf-8') as f:
#         f.write("\nשמי קן")

# write_to_file()
# cat words.txt (in the Terminal)

# 11.
########################################
# THE FLASK APP
########################################
# Create a virtual environment (python3 -m venv env)
# Activate said environment (source env/bin/activate)
# Install Flask (pip install Flask)
# 
# 
# from flask import Flask, jsonify, Response

# app = Flask(__name__)

# # Path to the text file
# file_path = "example.txt"


# @app.route("/content", methods=["GET"])
# def read_file():
#     try:
#         with open(file_path, "r") as file:
#             content = file.read()
#         return Response(content, status=200, mimetype="text/plain")
#     except FileNotFoundError:
#         return jsonify({"error": "File not yet found"}), 404
    
# @app.route("/register")
# def write_to_file():
#     try:
#         with open(file_path, "w") as file:
#             file.write("Hello")
#         return jsonify({"message": "Success"})
#     except IOError:
#         return jsonify({"error": "Error writing to file"}), 500
#     finally:
#         file.close()


# if __name__ == "__main__":
#     # Run app on port 30000
#     app.run(host="0.0.0.0", port=30000)
# Example of browser address (http://192.168.1.115:30000/content)
# /register will create the file and add text
# /content will read the file

# # 12.
# First install the module pillow (pip install pillow)
# from PIL import Image, ImageDraw, ImageFont

# # Create a blank image (RGB mode) with white background
# width, height = 200, 100
# image = Image.new("RGB", (width, height), "white")

# # Initialise ImageDraw to draw on the image
# draw = ImageDraw.Draw(image)

# # Save the image as a PNG file
# image.save("created_image.png")

# # Display the image 
# image.show()