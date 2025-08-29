from google import genai
from PIL import Image
import io
import os
from dotenv import load_dotenv

load_dotenv('cred.env')
gemini_api_key = os.getenv('gemini_api_key')
gemini_client = genai.Client(api_key=gemini_api_key)

def get_llm_response(image_data: bytes) -> str:
    image = Image.open(io.BytesIO(image_data))
    image = image.convert("RGB")

    # Instantiate the GenerativeModel object
    

    prompt_text = (
        "Analyze the image and describe the mood in a few sentences."
        "How is the mood of the image?"
        "Is the mood of the image sad or happy or what else?"
    )

    # Use generate_content() to handle both text and image
    response = gemini_client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, prompt_text]
)

    # The response text is now accessed via the .text attribute
    generated_text = response.text

    return generated_text