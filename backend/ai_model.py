from llama_cpp import Llama
import os

# Path to your downloaded GGUF model file. Adjust the filename if needed.
MODEL_PATH = os.path.join(os.path.dirname(__file__), "mistral-7b-instruct-v0.2.Q4_K_M.gguf")

# Initialize the model only once for efficiency.
_llm = None
def get_llm():
    global _llm
    if _llm is None:
        _llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=8)
    return _llm

def generate_lesson(topic):
    prompt = f"""[INST]Create a comprehensive, student-friendly math lesson on the topic: \"{topic}\".\nInclude definitions, worked examples, and at least one practice problem with solution. Use clear explanations.[/INST]"""
    llm = get_llm()
    output = llm(prompt, max_tokens=600, stop=["</s>"])
    return output['choices'][0]['text'].strip()