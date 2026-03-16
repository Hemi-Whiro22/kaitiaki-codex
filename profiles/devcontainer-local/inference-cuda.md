## Purpose

This note captures the current local CUDA-backed inference profile for the
`devcontainer-local` branch. It is a profile example, not a framework lock-in.

## Current Shape

- Runtime: `llama.cpp`
- Model format: local `GGUF`
- Offload: NVIDIA GPU via CUDA
- Capability exposure: optional MCP surface over the local inference endpoint

## Known Working Machine Notes

Source lineage from the earlier local machine notes shows:

- GPU: `NVIDIA GeForce RTX 5060 Ti`
- Driver: `590.48.01`
- CUDA runtime reported by `nvidia-smi`: `13.1`
- `nvcc` installed
- `llama.cpp` successfully reporting CUDA device discovery

The previous verification output included:

- `ggml_cuda_init: found 1 CUDA devices`
- `Device 0: NVIDIA GeForce RTX 5060 Ti`

## Prior Local Runtime Defaults

The older local runtime used a shape equivalent to:

```bash
llama-server \
  -m "$LLAMA_MODEL_PATH" \
  --host 0.0.0.0 \
  --port 8090 \
  -c 8192 \
  --temp 0.8 \
  --top_p 0.95 \
  -ngl 99 \
  --cache-type-k f16 \
  --cache-type-v f16 \
  -b 512 \
  --threads 8
```

## Important Boundary

- MCP does not create GPU offload.
- CUDA offload comes from how `llama.cpp` is built and launched.
- MCP only exposes the local capability surface to tools or clients.

## Suggested Local Checks

```bash
nvidia-smi
nvcc --version
~/llama.cpp/build/bin/llama-cli --help
```

Signs the profile is healthy:

- `nvidia-smi` sees the NVIDIA GPU
- `nvcc` is available
- `llama-cli --help` shows CUDA initialization output

## Environment Notes

Use `llama.env.example` in this profile as the starting point for:

- `LLAMA_SERVER_BIN`
- `LLAMA_MODEL_PATH`
- `LLAMA_ARG_N_GPU_LAYERS`
- `LLAMA_ARG_MAIN_GPU`
- `LLAMA_API_PORT`

## Scope Limit

This note only captures the current local CUDA profile for coding and local
inference support. It does not define production inference, cloud providers, or
multi-host serving.
