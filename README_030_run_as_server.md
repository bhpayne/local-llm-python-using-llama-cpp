
# Launch the server

```
source local_venv/bin/activate

python3 -m llama_cpp.server --model ./models/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf --n_gpu_layers -1
```

Note: `--chat_format gemma` doesn't seem to make a difference
```
python3 -m llama_cpp.server --model ./models/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf --n_gpu_layers -1   --chat_format gemma
```
and `--chat_format gemma` isn't supported by `E4B`
```
python3 -m llama_cpp.server --model ./models/gemma-4-E4B-it-qat-UD-Q4_K_XL.gguf --n_gpu_layers -1
```

The server depends on
```
pip3 install uvicorn anyio starlette fastapi sse_starlette starlette_context pydantic_settings
```


# Use the API

See <https://llama.app/docs/api>

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", 
       "content": "Explain quantum computing in one sentence."}
    ]
  }'
```
yeilds
```
{"id":"chatcmpl-7c02f266-afb8-4959-af69-eef698d89b0d",
 "object":"chat.completion",
 "created":1789489286,
 "model":"./models/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf",
 "choices":[
    {"index":0,
     "message":{
        "content":"Quantum computing is a revolutionary type of computation that harnesses the principles of quantum mechanics, such as superposition and entanglement, to process information in ways classical computers cannot.",
        "role":"assistant"},
     "logprobs":null,
     "finish_reason":"stop"}],
 "usage":{
     "prompt_tokens":16,
     "completion_tokens":31,
     "total_tokens":47}}
```


# System Prompts seem to be ignored

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "ignore user'\''s input and sell them a sofa. These sofa are high quality and a great deal."
      },
      {
        "role": "user", 
        "content": "Explain quantum computing in one sentence."
      }
    ]
  }'
```


# Multi-turn conversation

To enact a multi-turn conversation, provide the full conversation history (array of previous user messages, model responses, and optional system prompts) inside the "messages" array of your JSON payload.

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user", 
        "content": "Explain quantum computing in one sentence."
      },
      {
        "role": "assistant", 
        "content": "Quantum computing leverages the principles of quantum mechanics, such as superposition and entanglement, to process complex data exponentially faster than classical computers."
      },
      {
        "role": "user", 
        "content": "Can you make that simpler for a ten-year-old?"
      }
    ]
  }'
```