from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_highlights(text):
    """
    Extract key highlights and important points from the legal document using OpenAI.

    Args:
        text: The document text to extract highlights from

    Returns:
        str: AI-generated highlights

    Raises:
        Exception: If API call fails
    """
    try:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        # Limit text to first 4000 characters to avoid token limits
        prompt = f"Highlight the key topics and important points from this legal document. List them clearly:\n{text[:4000]}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        raise Exception(f"Error extracting highlights: {str(e)}")
