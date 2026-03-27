#!/bin/bash
# 使用本地Hugging Face模型
CUDA_VISIBLE_DEVICES=0 python3 main_baseline.py --config configs/main/ScienceQA_mctsquery.yaml