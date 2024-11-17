#!/bin/bash

# Exit on error
set -e

echo "Setting up Python environment for LLaVA..."

# Create and activate a virtual environment
python3 -m venv llava_env
source llava_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install PyTorch (CPU version - uncomment CUDA version if needed)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# For CUDA support, use:
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other dependencies
pip install av
pip install numpy
pip install transformers
pip install safetensors

# Verify installations
echo "Verifying installations..."
python3 -c "
import av
import numpy as np
import torch
from transformers import LlavaNextVideoForConditionalGeneration, LlavaNextVideoProcessor
from safetensors.torch import load_file
import json

print('All dependencies successfully installed!')
"

echo "Setup complete! To activate the environment, run:"
echo "source llava_env/bin/activate"
