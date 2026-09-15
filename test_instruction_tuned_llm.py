from llama_cpp import Llama

llm = Llama(
    model_path="./models/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf",
    n_gpu_layers=-1,  # -1 offloads all layers to GPU
    n_ctx=2048,  # Set context window size
    flash_attn=True,  # Enable Flash Attention
    verbose=False
)

prompt = "Name three primary colors."

# Use create_chat_completion for instruction-tuned (-it) models
output = llm.create_chat_completion(
    messages=[{"role": "user", # one of these: "system", "user", "assistant", "tool"
               "content": prompt}],
    max_tokens=500,
)

print("\nPrompt was")
print(prompt)
print("\nLLM response:")
# Print just the model's response content
print(output["choices"][0]["message"]["content"])