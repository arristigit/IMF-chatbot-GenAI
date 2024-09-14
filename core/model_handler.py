from openai import OpenAI

class ModelHandler:
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key
        self.model = None
        self.client = None

    def load_model(self):
        try:
            self.model = self.model_name
            self.client = OpenAI(api_key=self.api_key)
            print(f"Model '{self.model_name}' loaded successfully.")
        except Exception as e:
            print(f"Failed to load model '{self.model_name}': {str(e)}")
            raise

    def get_summary(self, text: str) -> str:
        if not self.model:
            raise Exception("Model not loaded. Call load_model() before requesting a summary.")

        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are an assistant specialized in summarizing financial reports."},
                    {"role": "user", "content": f"Summarize this text: {text}"}
                ],
                max_tokens=150,
                temperature=0.7,
                top_p=1.0
            )
            summary = completion.choices[0].message
            return summary

        except Exception as e:
            print(f"Failed to generate summary: {str(e)}")
            raise
