#!/bin/bash
export VQA_MODEL="./cache/huggingface/hub/Qwen/Qwen2-VL-7B-Instruct-GPTQ-Int4"
export API_KEY="token-abc123"
export BASE_URL="http://localhost:8000/v1;http://localhost:8001/v1"
python3 tools/CoT_extract.py --config configs/extract_info/ScienceQA_config.yaml