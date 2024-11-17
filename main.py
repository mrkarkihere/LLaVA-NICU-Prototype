import av
import numpy as np
import torch
from transformers import LlavaNextVideoForConditionalGeneration, LlavaNextVideoProcessor
from safetensors.torch import load_file
import json

# GLOBALS
VIDEO_PATH = "videos/PulseOximeter2.mp4"
PROMPT = "Among the following actions (positive pressure ventilation, chest compressions, Endotracheal intubation, Drying, Pulse Oximetry, Reposition, Suction, Umbilical Venous Catheter), what is the PRIMARY action being performed? Focus only on the most prominent procedure visible in the clip."
MAX_TOKEN = 50
RUN_ORIGINAL_MODEL = True
RUN_FINE_TUNED_MODEL = False
BASE_MODEL_NAME = "llava-hf/LLaVA-NeXT-Video-7B-hf"
CHECKPOINT_PATH = "./checkpoints/llava-next-video-7b_lora-True_qlora-False"

def read_video_frames(container, indices):
    """
    Decode specific frames from a video using PyAV decoder.
    """
    frames = []
    container.seek(0)
    start_index, end_index = indices[0], indices[-1]
    
    for i, frame in enumerate(container.decode(video=0)):
        if i > end_index:
            break
        if i >= start_index and i in indices:
            frames.append(frame)
    
    return np.stack([x.to_ndarray(format="rgb24") for x in frames])

def create_video_prompt(text_prompt=PROMPT):
    """
    Create a conversation prompt for video analysis.
    """
    return [{
        "role": "user",
        "content": [
            {"type": "text", "text": text_prompt},
            {"type": "video"},
        ],
    }]

def process_video(video_path, processor, num_frames=8):
    """
    Process video file and prepare it for model inference.
    """
    container = av.open(video_path)
    total_frames = container.streams.video[0].frames
    
    # Sample frames uniformly from the video
    indices = np.arange(0, total_frames, total_frames / num_frames).astype(int)
    clip = read_video_frames(container, indices)
    
    # Create and process the prompt
    conversation = create_video_prompt()
    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    
    # Process video frames
    inputs_video = processor(
        text=prompt,
        videos=clip,
        padding=True,
        return_tensors="pt"
    )
    
    return container, inputs_video

def load_model(model_name, is_finetuned=False, checkpoint_path=None, device=0):
    """
    Load either the base or fine-tuned LLaVA model.
    """
    # Load base model
    model = LlavaNextVideoForConditionalGeneration.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    ).to(device)
    
    # If fine-tuned, load and apply adapter weights
    if is_finetuned and checkpoint_path:
        adapter_weights = load_file(f"{checkpoint_path}/adapter_model.safetensors")
        model.load_state_dict(adapter_weights, strict=False)
        
        # Load adapter config (for future use if needed)
        with open(f"{checkpoint_path}/adapter_config.json", "r") as f:
            adapter_config = json.load(f)
    
    return model

def generate_description(model, inputs_video, processor, max_tokens=MAX_TOKEN):
    """
    Generate video description using the model.
    """
    inputs_video = inputs_video.to(model.device)
    output = model.generate(
        **inputs_video,
        max_new_tokens=max_tokens,
        do_sample=True
    )
    return processor.decode(output[0], skip_special_tokens=True)

def main():
    # Initialize processor
    processor = LlavaNextVideoProcessor.from_pretrained(BASE_MODEL_NAME)
    
    # Process video once for both models
    container, inputs_video = process_video(VIDEO_PATH, processor)
    
    # Test original model
    if RUN_ORIGINAL_MODEL:
        print("Original Model Output:")
        original_model = load_model(BASE_MODEL_NAME)
        description = generate_description(original_model, inputs_video, processor)
        print(description)
        del original_model
    
    # Test finetuned model
    if RUN_FINE_TUNED_MODEL:
        print("\nFinetuned Model Output:")
        finetuned_model = load_model(
            BASE_MODEL_NAME,
            is_finetuned=True,
            checkpoint_path=CHECKPOINT_PATH
        )
        description = generate_description(finetuned_model, inputs_video, processor)
        print(description)
        del finetuned_model

if __name__ == "__main__":
    main()