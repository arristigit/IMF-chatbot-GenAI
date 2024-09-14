import openai

# Not required. Used by v0 model_handler & v1 model_handler itself have the below code
class TextSummarizer:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def summarize(self, text: str) -> str:
        # Using OpenAI GPT model for summarization
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=f"Summarize this text: {text}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
