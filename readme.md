# Image Generation Program
## Features
* Allows the user to select an image size, and enter a prompt
* Uses the OpenAI API to generate an image based on the prompt and size selected by the user
* Displays the generated image to the user

## Requirements

This application requires a valid API key for the OpenAI API. You can find more information on how to create a valid key and its usage on the OpenAI page https://beta.openai.com/docs/api-reference/authentication

It also requires the following Python libraries:

* openai
* pillow
* requests

You can install these libraries by running the following command:

```pip install -r requirements.txt```
## Usage
1. To use the application, run the script main.py
2. Enter your API key
3. Select an image size
4. Enter a prompt
5. Press the "Create Image" button
6. After some seconds (based on size chosen), the generated image will be displayed
## Limitations
* The program can only generate a single image at a time
* The prompt must not exceed 100 words
* The program can only generate images of the sizes 1024x1024, 512x512 and 256x256
## Note
* Make sure you have a valid OpenAI API key before running the program. 
* Make sure the required libraries are installed