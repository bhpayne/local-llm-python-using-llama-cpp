

# Which LLMs fit on a MacBook Air M2 with 8GB of RAM?

Rule of thumb: A 4B parameter model needs ~3.5GB, a 9B parameter model needs ~7GB,

# inference speed

"The M2's 100 GB/s LPDDR5 bandwidth is the single most important number for inference speed, because LLM token generation is memory-bandwidth-bound." 

```
Gemma 4 12B Q4_K_M            ~8.0 GB	  10-14 tok/s
Llama 3.1 8B Instruct Q4_K_M  ~6.5 GB	  15-20 tok/s
Ornith 1.0 9B Q4_K_M          ~5.6 GB	  14-18 tok/s
```

# What is QAT?

Quantization-Aware Training (QAT) that dramatically reduces memory requirements while maintaining high quality. 
Source: <https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/>


# Gemma 3
<https://developers.googleblog.com/en/introducing-gemma-3-270m/>

<https://huggingface.co/collections/google/gemma-3-release>

## Gemma 4 E2B and E4B

The "E" stands for effective parameters, meaning they use per-layer embeddings (PLE) to store large embedding tables in regular flash memory rather than heavy VRAM. Both models support a 128K context window and native text, image, and audio inputs.

Both models process audio clips capped at 30 seconds and video clips capped at 60 seconds at 1 frame per second

- E2B: 2.3 billion effective parameters; Uses 1–1.5 GB of memory; Runs at 20–35 tokens per second. Best for fast, low-latency tasks, simple classification, and real-time live voice transcription.
- E4B: 4.5 billion effective parameters; Uses 2–3 GB of memory; Runs at 12–20 tokens per second. Better at multi-step reasoning, complex function calling with overlapping schemas, and analyzing dense images or small text.

Models are at <https://huggingface.co/google/gemma-4-E2B> but no GGUF files.

Raw format of "safetensors" is available from the page <https://huggingface.co/google/gemma-4-E2B-it> under "safetensors" click on "files info" and then "download" at the top of the page.

The `model.safetensors` file is 9.5GB

Instruction-tuned: <https://huggingface.co/google/gemma-4-E4B-it>

### GGUF format

<https://unsloth.ai/docs/models/gemma-4/qat>

<https://gemma4-ai.com/blog/gemma4-gguf-guide>

<https://huggingface.co/collections/unsloth/gemma-4-qat>

<https://huggingface.co/unsloth/gemma-4-E2B-it-qat-GGUF>

<https://huggingface.co/unsloth/gemma-4-E2B-it-qat-GGUF/blob/main/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf>

The file `gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf` is 2.4GB

<https://huggingface.co/unsloth/gemma-4-E4B-it-qat-GGUF>
<https://huggingface.co/unsloth/gemma-4-E4B-it-qat-GGUF/blob/main/gemma-4-E4B-it-qat-UD-Q4_K_XL.gguf>


# Ornith

None of the models listed on <https://huggingface.co/collections/ornith-ai/ornith-15>
are below 9B parameters


