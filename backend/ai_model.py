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
        {"role": "system", "content": "You are a math teacher who explains clearly and gives step-by-step examples."},
        {"role": "user", "content": f"""
Write a clear high-school math lesson on "{topic}".
Follow this exact format:

### 1. Definition
- Write a short, simple definition of the topic.

### 2. Key Properties / Rules
- List 3–5 important properties or rules.

### 3. Worked Example
- Solve one problem step by step.
- Show each step with LaTeX, for example: $$3x + 5x = 8x$$.

### 4. Practice Problem
- Give one practice problem.
- Then show the full solution in LaTeX.

Rules:
- Always include at least one equation in LaTeX format ($$...$$).
- Keep the language simple and student-friendly.
"""}
    ]

    # ✅ Use chat completion
    output = llm.create_chat_completion(messages=messages, max_tokens=400)
    text = output['choices'][0]['message']['content'].strip()

    # ✅ Extract LaTeX equations (if any)
    latex_list = re.findall(r"\$\$(.*?)\$\$", text, re.DOTALL) if "$$" in text else []

    return text, latex_list

