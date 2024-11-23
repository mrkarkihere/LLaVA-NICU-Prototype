NUM_GPUS=1
DISTRIBUTED_ARGS="
    --nnodes=1 \
    --nproc_per_node ${NUM_GPUS} \
    --rdzv_backend c10d \
    --rdzv_endpoint localhost:0
"

MODEL_ID=llava-next-video-7b
TRAIN_DATA_PATH=/content/video_metadata.json
EVAL_DATA_PATH=/content/video_metadata.json
IMAGE_FOLDER=./example_data/images
VIDEO_FOLDER=/content/drive/MyDrive/Capstone/Videos
NUM_FRAMES=8

# Disable vision encoder training for memory efficiency
TRAIN_VISION_ENCODER=False
USE_VISION_LORA=False
TRAIN_VISION_PROJECTOR=False

# Enable LORA, but disable q-lora for simplicity
USE_LORA=True
Q_LORA=False
LORA_R=8
LORA_ALPHA=8

RUN_ID=${MODEL_ID}_lora-${USE_LORA}_qlora-${Q_LORA}

DS_STAGE=zero3
# Reduce batch size for smoother execution
PER_DEVICE_BATCH_SIZE=1
GRAD_ACCUM=2  # Increase gradient accumulation for larger effective batch size
NUM_EPOCHS=5

LR=2e-5
MODEL_MAX_LEN=512

# Optimize training with mixed precision
torchrun $DISTRIBUTED_ARGS train.py \
    --model_id $MODEL_ID \
    --data_path $TRAIN_DATA_PATH \
    --eval_data_path $EVAL_DATA_PATH \
    --image_folder $IMAGE_FOLDER \
    --video_folder $VIDEO_FOLDER \
    --num_frames $NUM_FRAMES \
    --output_dir ./checkpoints/$RUN_ID \
    --report_to wandb \
    --run_name $RUN_ID \
    --deepspeed ./ds_configs/${DS_STAGE}.json \
    --bf16 True \
    --num_train_epochs $NUM_EPOCHS \
    --per_device_train_batch_size $PER_DEVICE_BATCH_SIZE \
    --per_device_eval_batch_size $PER_DEVICE_BATCH_SIZE \
    --gradient_accumulation_steps $GRAD_ACCUM \
    --eval_strategy "epoch" \
    --save_strategy "epoch" \
    --save_total_limit 1 \
    --learning_rate ${LR} \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length $MODEL_MAX_LEN \
    --gradient_checkpointing True \
    --dataloader_num_workers 2 \
    --train_vision_encoder $TRAIN_VISION_ENCODER \
    --use_vision_lora $USE_VISION_LORA \
    --train_vision_projector $TRAIN_VISION_PROJECTOR \
    --use_lora $USE_LORA \
    --q_lora $Q_LORA \
    --lora_r $LORA_R \
    --lora_alpha $LORA_ALPHA
