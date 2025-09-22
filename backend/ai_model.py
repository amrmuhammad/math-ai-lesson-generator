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
        _llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=4)
    return _llm


def generate_lesson(topic):
    llm = get_llm()

    messages = [
        {"role": "system", "content": "You are a math teacher creating structured high-school lessons with LaTeX formatting."},

        # --- FEW-SHOT EXAMPLE 1 ---
        {"role": "user", "content": 'Write a lesson on "Pythagorean Theorem".'},
        {"role": "assistant", "content": """### 1. Definition
The **Pythagorean Theorem** states that in a right triangle:
$$a^2 + b^2 = c^2$$  
where \(a\) and \(b\) are the legs, and \(c\) is the hypotenuse.

### 2. Key Properties / Rules
- Works only for **right triangles**.  
- The hypotenuse is always the **longest side**.  
- Can be used to **find missing side lengths**.  

### 3. Worked Example
Find the hypotenuse of a right triangle with legs \(a = 3\) and \(b = 4\).  

$$a^2 + b^2 = c^2$$  
$$3^2 + 4^2 = c^2$$  
$$9 + 16 = c^2$$  
$$25 = c^2$$  
$$c = 5$$  

### 4. Practice Problem
Find the missing leg if \(c = 13\) and \(a = 5\).  

**Solution:**  
$$a^2 + b^2 = c^2$$  
$$5^2 + b^2 = 13^2$$  
$$25 + b^2 = 169$$  
$$b^2 = 144$$  
$$b = 12$$  
"""},

        # --- TASK PROMPT ---
        {"role": "user", "content": f"""
Write a short but complete high-school math lesson on "{topic}".
Follow the same structure as the example:
1. Definition
2. Key Properties / Rules
3. Worked Example (step-by-step in $$...$$)
4. Practice Problem (with solution in $$...$$)
"""}
    ]

     # ✅ Streaming response to avoid cut-off
    text = ""
    for chunk in llm.create_chat_completion(messages=messages, max_tokens=1000, stream=True):
        if "choices" in chunk:
            delta = chunk["choices"][0]["delta"].get("content", "")
            text += delta

    text = text.strip()

    # Extract LaTeX expressions
    latex_list = re.findall(r"\$\$(.*?)\$\$", text, re.DOTALL) if "$$" in text else []

    return text, latex_list

