# script to import the checkpoint and run the model

import av
import numpy as np
import torch
from transformers import (
    LlavaNextVideoForConditionalGeneration,
    LlavaNextVideoProcessor,
    BitsAndBytesConfig
)

# Global Configuration
PROMPT = "Please provide a detailed description of the video."
VIDEO_PATH = "/content/drive/MyDrive/Capstone/TRIALS_VID/Suction/Suction5.mp4"
MODEL_PATH = "/content/drive/MyDrive/Capstone/CHECKPOINTS/checkpoints/llava-next-video-7b_lora-True_qlora-True"
MAX_TOKENS = 100

# Model Configuration
BNB_CONFIG = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
)

class VideoAnalyzer:
    """A class to handle video analysis using LLaVA-NeXT model."""
    
    def __init__(self):
        """Initialize the VideoAnalyzer with model configurations."""
        self.processor = LlavaNextVideoProcessor.from_pretrained(
            "llava-hf/LLaVA-NeXT-Video-7B-hf"
        )
        self.model = LlavaNextVideoForConditionalGeneration.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float16,
            quantization_config=BNB_CONFIG,
            low_cpu_mem_usage=True,
        ).to("cuda:0")

    def _read_video_frames(self, container, indices):
        """Decode video frames using PyAV decoder."""
        frames = []
        container.seek(0)
        start_index = indices[0]
        end_index = indices[-1]
        
        for i, frame in enumerate(container.decode(video=0)):
            if i > end_index:
                break
            if i >= start_index and i in indices:
                frames.append(frame)
                
        return np.stack([x.to_ndarray(format="rgb24") for x in frames])

    def analyze_video(self, video_path=VIDEO_PATH, prompt=PROMPT):
        """Analyze a video and generate a description."""
        conversation = [{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "video"},
            ],
        }]
        
        formatted_prompt = self.processor.apply_chat_template(
            conversation, 
            add_generation_prompt=True
        )

        container = av.open(video_path)
        total_frames = container.streams.video[0].frames
        indices = np.arange(0, total_frames, total_frames / 8).astype(int)
        clip = self._read_video_frames(container, indices)
        
        inputs = self.processor(
            text=formatted_prompt,
            videos=clip,
            padding=True,
            return_tensors="pt"
        ).to("cuda:0")
        
        output = self.model.generate(
            **inputs,
            max_new_tokens=MAX_TOKENS,
            do_sample=True
        )
        
        return self.processor.decode(output[0], skip_special_tokens=True)

    def __del__(self):
        """Clean up resources when the analyzer is deleted."""
        if hasattr(self, 'model'):
            del self.model

# Initialize and run
analyzer = VideoAnalyzer()
description = analyzer.analyze_video()
print(description)
del analyzer