model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Only 1.1B parameters (Fast on CPU)
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Choose a lightweight model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # Use TinyLlama for CPU

print("Loading model... (This may take a while)")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,  # Use float32 (float16 requires GPU)
    device_map="cpu"  # Force CPU usage
)

def chat_with_llama(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Start Chat
print("\n🚀 AI Chatbot Ready! Type 'exit' to stop.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_llama(user_input)
    print("🤖 AI:", response)
