import argparse
import requests
from openai import OpenAI

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Generate and save an image using DALL-E.')
parser.add_argument('prompt', type=str, help='Prompt for generating the image')
args = parser.parse_args()

# Initialize OpenAI client
client = OpenAI()

# Generate the image using DALL-E
response = client.images.generate(
    model="dall-e-3",
    prompt=args.prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

# Extract image URL
image_url = response.data[0].url

# Download the image
response = requests.get(image_url)

# Save the image
with open('image.jpg', 'wb') as file:
    file.write(response.content)

print("Image saved as image.jpg")
