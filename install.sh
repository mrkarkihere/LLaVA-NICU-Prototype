#!/bin/bash

# Exit on error
set -e

echo "Setting up Linux environment for LLaVA..."

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run with sudo"
    exit 1
fi

# Update package list
echo "Updating package list..."
apt-get update

# Install Python and pip if not present
echo "Installing Python and pip..."
apt-get install -y python3 python3-pip python3-venv

# Install system dependencies for PyAV
echo "Installing system dependencies for PyAV..."
apt-get install -y \
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

# Create virtual environment directory with appropriate permissions
echo "Creating Python virtual environment..."
mkdir -p /opt/llava_env
python3 -m venv /opt/llava_env
chown -R $SUDO_USER:$SUDO_USER /opt/llava_env

# Switch to the user who ran sudo
if [ -n "$SUDO_USER" ]; then
    # Activate virtual environment and install packages as the original user
    su - $SUDO_USER << 'EOF'
    source /opt/llava_env/bin/activate
    
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
EOF
fi

echo "Setup complete!"
echo "To activate the environment, run:"
echo "source /opt/llava_env/bin/activate"

# Create an activation script in /usr/local/bin
cat > /usr/local/bin/activate_llava << 'EOF'
#!/bin/bash
source /opt/llava_env/bin/activate
EOF

chmod +x /usr/local/bin/activate_llava

echo "You can also activate the environment by running: activate_llava"
