
from llama_cpp import Llama

# Initialize the model and offload all layers to the Metal GPU
llm = Llama(
    model_path="./models/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf",
    n_gpu_layers=-1, # -1 offloads all layers to GPU
    n_ctx=2048       # Set context window size
)

# raw text completion method
output = llm(
    "Q: Name three primary colors. A: ",
    max_tokens=32,
    stop=["\n"],
    echo=True
)

print(output["choices"][0]["text"])
