#!/bin/bash

# Exit on error
set -e

echo "Setting up Linux environment for LLaVA..."

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Python and pip if not present
echo "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Install system dependencies for PyAV
echo "Installing system dependencies for PyAV..."
sudo apt-get install -y \
    python3-dev \
    pkg-config \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavutil-dev \
    libswscale-dev \
    libswresample-dev \
    libavfilter-dev \
    ffmpeg

# Create virtual environment in user's home directory
echo "Creating Python virtual environment..."
VENV_PATH="$HOME/llava_env"
python3 -m venv $VENV_PATH

# Activate virtual environment and install packages
source $VENV_PATH/bin/activate

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
python3 -c "
import av
import numpy as np
import torch
from transformers import LlavaNextVideoForConditionalGeneration, LlavaNextVideoProcessor
from safetensors.torch import load_file
import json

print('All dependencies successfully installed!')
"

# Create activation script in user's bin directory
mkdir -p "$HOME/bin"
cat > "$HOME/bin/activate_llava" << EOF
#!/bin/bash
source $VENV_PATH/bin/activate
EOF

chmod +x "$HOME/bin/activate_llava"

# Add to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
    echo "Added $HOME/bin to PATH"
fi

echo "Setup complete!"
echo "To activate the environment, run:"
echo "source $VENV_PATH/bin/activate"
echo "or simply:"
echo "activate_llava"
echo ""
echo "Note: You may need to restart your terminal or run 'source ~/.bashrc' to use the activate_llava command"
