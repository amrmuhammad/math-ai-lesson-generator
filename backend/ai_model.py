from llama_cpp import Llama
import os
import re

# Path to your downloaded small (≤2GB) GGUF model file.
# Example: TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf
MODEL_PATH = os.path.join(os.path.dirname(__file__), "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

# Initialize the model only once for efficiency.
_llm = None
def get_llm():
    global _llm
    if _llm is None:
        # Reduce n_ctx to further lower memory use if needed.
        _llm = Llama(model_path=MODEL_PATH, n_ctx=512, n_threads=4)
    return _llm

def generate_lesson(topic):
    llm = get_llm()

    messages = [
    	{"role": "system", "content": "You are a math teacher creating structured lessons."},
    	{"role": "user", "content": f"""
Write a short but complete high-school math lesson on "{topic}".
Follow this exact structure:

1. **Definition** – clear and simple.
2. **Key Properties / Rules** – concise bullet points.
3. **Worked Example** – step-by-step solution in LaTeX.
4. **Practice Problem** – with solution in LaTeX.

Make sure to use $$...$$ for all math expressions.
"""		}
    ]


    # Use chat completion instead of raw prompt
    output = llm.create_chat_completion(messages=messages, max_tokens=400)
    text = output['choices'][0]['message']['content'].strip()

    # ✅ Extract LaTeX expressions safely
    latex_list = re.findall(r"\$\$(.*?)\$\$", text, re.DOTALL) if "$$" in text else []

    return text, latex_list

