


# Which LLMs fit on a MacBook Air M2 with 8GB of RAM?

Rule of thumb: A 4B model needs ~3.5GB, a 9B needs ~7GB,

The M2's 100 GB/s LPDDR5 bandwidth is the single most important number for inference speed, because LLM token generation is memory-bandwidth-bound. 

```
Gemma 4 12B Q4_K_M	~8.0 GB	10-14 tok/s
Llama 3.1 8B Instruct Q4_K_M	~6.5 GB	15-20 tok/s
Ornith 1.0 9B Q4_K_M	~5.6 GB	14-18 tok/s
```

Quantization-Aware Training (QAT) that dramatically reduces memory requirements while maintaining high quality. 
Source: <https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/>

# Models

# Gemma 3
<https://developers.googleblog.com/en/introducing-gemma-3-270m/>
<https://huggingface.co/collections/google/gemma-3-release>

## Gemma 4 E2B 
<https://huggingface.co/google/gemma-4-E2B>

From the page <https://huggingface.co/google/gemma-4-E2B-it> under "safetensors" click on "files info" and then "download" at the top of the page.

The `model.safetensors` file is 9.5GB

<https://huggingface.co/google/gemma-4-E4B-it>


<https://gemma4-ai.com/blog/gemma4-gguf-guide>

<https://huggingface.co/collections/unsloth/gemma-4-qat>
<https://huggingface.co/unsloth/gemma-4-E2B-it-qat-GGUF>
<https://huggingface.co/unsloth/gemma-4-E2B-it-qat-GGUF/blob/main/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf>


## Ornith

None of the models listed on <https://huggingface.co/collections/ornith-ai/ornith-15>
are below 9B parameters
