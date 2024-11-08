import av
import torch
import numpy as np
from huggingface_hub import hf_hub_download
from transformers import LlavaNextVideoProcessor, LlavaNextVideoForConditionalGeneration

model_id = "llava-hf/LLaVA-NeXT-Video-7B-hf"

model = LlavaNextVideoForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True, 
).to(0)

processor = LlavaNextVideoProcessor.from_pretrained(model_id)

def read_video_pyav(container, indices):
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

# Define a simple conversation with just the video analysis question
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Considering the 8 key actions (PPV, CPR, ETT, Drying, Pulse Oximeter, Reposition, Suction, and UVC) outlined in the Neonatal Resuscitation Program, which action is being performed in this video clip, and with what level of confidence? Briefly and only one action."},
            {"type": "video"},
        ],
    },
]

prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

# Load and process the video
video_path = "videos\PPV2.mp4"
container = av.open(video_path)

total_frames = container.streams.video[0].frames
indices = np.arange(0, total_frames, total_frames / 8).astype(int)
clip = read_video_pyav(container, indices)

# Process the video and generate output
inputs_video = processor(text=prompt, videos=clip, padding=True, return_tensors="pt").to(model.device)
output = model.generate(**inputs_video, max_new_tokens=100, do_sample=False)

# Decode and print the result
result = processor.decode(output[0][2:], skip_special_tokens=True)
print(result)