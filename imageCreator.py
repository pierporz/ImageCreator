import openai
from PIL import Image
from io import BytesIO
import requests
import tkinter as tk

def create_image():

  # Get the API key entered by the user
  api_key = entry_apikey.get()

  # Get the size selected by the user
  size = var_size.get()

  # Get the prompt entered by the user
  prompt = text_text.get("1.0", "end")

  # Set the API key for the OpenAI API
  openai.api_key = api_key

  # Create the image
  response = openai.Image.create(
    prompt = prompt,
    n=2,
    size = size
  )

  # Get the image data and show
  image_url = response['data'][0]['url']
  response = requests.get(image_url)
  img = Image.open(BytesIO(response.content))
  img.show()

# Create the root window
root = tk.Tk()
root.geometry("800x600")
root.minsize(width=800, height=600)

# Create the entry field for the API key
label_apikey = tk.Label(root, text="Enter API KEY:")
label_apikey.pack()
entry_apikey = tk.Entry(root, width=100, validate="key", validatecommand=(root.register(lambda s: len(s) <= 100), "%P"))
entry_apikey.pack()

# Create the variable to store the selected size
label_size = tk.Label(root, text="Choose image size:")
label_size.pack()
var_size = tk.StringVar(value="1024x1024")
size_menu = tk.OptionMenu(root, var_size, "1024x1024", "512x512", "256x256")
size_menu.pack()

# Create the text field for the prompt
label_text = tk.Label(root, text="Enter prompt (max 100 words):")
label_text.pack()
text_text = tk.Text(root, height=20, width=70, wrap=tk.WORD)
text_text.pack()

# Create the "Create Image" button
button_create_image = tk.Button(root, text="Create Image", command=create_image)
button_create_image.pack()

root.mainloop()