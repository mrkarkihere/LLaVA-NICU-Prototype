import os
import json
import random

# Define the video folder and category mappings
video_folder = '/content/drive/MyDrive/Capstone/Videos2'
folder_to_category = {
    "CPR": "Chest Compression",
    "ETT": "Endotracheal Intubation",
    "PPV": "Positive Pressure Ventilation",
    "Pulse Oximeter": "Pulse Oximetry",
    "Suction": "Suction",
    "Drying-Warming-Stimulate": "Drying",
    "Reposition": "Reposition",
    "UVC": "Umbilical Venous Catheter"
}

# Define action descriptions with fully spelled-out names
action_descriptions = {
    "Positive Pressure Ventilation": "1",
    "Chest Compression": "2",
    "Endotracheal Intubation": "3",
    "Drying": "4",
    "Pulse Oximetry": "5",
    "Reposition": "6",
    "Suction": "7",
    "Umbilical Venous Catheter": "8"
}

train_output = []
eval_output = []

# Loop through each subfolder
for folder_name, category in folder_to_category.items():
    folder_path = os.path.join(video_folder, folder_name)
    print(f"Processing folder: {folder_path}")

    if os.path.isdir(folder_path):
        videos = [video for video in os.listdir(folder_path) if video.endswith(".mp4")]

        # Shuffle videos to ensure random sampling
        random.shuffle(videos)

        # Split videos: 80% train, 20% eval
        split_index = int(0.8 * len(videos))
        train_videos = videos[:split_index]
        eval_videos = videos[split_index:]

        # Process training videos
        for video in train_videos:
            train_output.append({
                "video": os.path.join(folder_name, video),
                "conversations": [
                    {
                        "from": "human",
                        "value": (
                            "<video>ACTION CLASSIFICATION TASK\n"
                            "Classify this neonatal resuscitation action video with the corresponding action number:\n"
                            "1=Positive Pressure Ventilation\n"
                            "2=Chest Compression\n"
                            "3=Endotracheal Intubation\n"
                            "4=Drying\n"
                            "5=Pulse Oximetry\n"
                            "6=Reposition\n"
                            "7=Suction\n"
                            "8=Umbilical Venous Catheter"
                        )
                    },
                    {
                        "from": "gpt",
                        "value": action_descriptions.get(category, "This video shows an action related to the specified category.")
                    }
                ]
            })

        # Process evaluation videos
        for video in eval_videos:
            eval_output.append({
                "video": os.path.join(folder_name, video),
                "conversations": [
                    {
                        "from": "human",
                        "value": (
                            "<video>ACTION CLASSIFICATION TASK\n"
                            "Classify this neonatal resuscitation action video with the corresponding action number:\n"
                            "1=Positive Pressure Ventilation\n"
                            "2=Chest Compression\n"
                            "3=Endotracheal Intubation\n"
                            "4=Drying\n"
                            "5=Pulse Oximetry\n"
                            "6=Reposition\n"
                            "7=Suction\n"
                            "8=Umbilical Venous Catheter"
                        )
                    },
                    {
                        "from": "gpt",
                        "value": action_descriptions.get(category, "This video shows an action related to the specified category.")
                    }
                ]
            })
    else:
        print(f"Folder does not exist: {folder_path}")

# Write the train and eval JSON files
with open("/content/train.json", "w") as train_file:
    json.dump(train_output, train_file, indent=4)

with open("/content/eval.json", "w") as eval_file:
    json.dump(eval_output, eval_file, indent=4)

print("Train and Eval JSON files created successfully!")