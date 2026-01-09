from google import genai

def generate_text(api_key: str | None, prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Returns plain text from Gemini.
    If api_key is None/empty, the SDK will use GEMINI_API_KEY from the environment.
    """
    client = genai.Client(api_key=api_key) if api_key else genai.Client()

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    # response.text is the canonical quickstart pattern
    return response.text or ""
