import os
from google import genai  # package name per quickstart; adjust import per SDK
# NOTE: adjust according to the SDK you install; some docs use 'from google import genai' or 'import google_genai'

class GeminiClient:
    def __init__(self, api_key: str = None, model: str = "gemini-1.5-pro"):
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, user_text, system_prompt="", context_docs=None, temperature=0.2, max_output_tokens=512):
        contents = []
        if system_prompt:
            contents.append({"role":"system", "parts":[{"text": system_prompt}]})
        if context_docs:
            # include retrieved docs as assistant/system context or appended to prompt
            for d in context_docs:
                contents.append({"role":"system","parts":[{"text":f"Context doc: {d['content'][:500]}"}]})
        contents.append({"role":"user","parts":[{"text":user_text}]})

        resp = self.client.models.generate_content(
            model=self.model,
            contents=contents,
            temperature=temperature,
            max_output_tokens=max_output_tokens
        )
        # parse response (SDK returns structured object)
        out_text = ""
        try:
            out_text = resp.output[0].content[0].text
        except Exception:
            out_text = str(resp)
        # function_call handling is SDK-specific — adapt per returned shape
        parsed = {"text": out_text}
        # parse function_call if present
        return parsed

    def execute_function(self, name, args):
        # implement mapping + safety checks
        if name == "run_code_snippet":
            # run in sandboxed env or return simulated result
            return {"status":"ok","output":"(simulated) code executed"}
        return {"error":"unknown function"}
