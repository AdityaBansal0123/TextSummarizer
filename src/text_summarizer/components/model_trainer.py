from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
from datasets import load_from_disk
import os
from src.text_summarizer.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # --- device selection ---
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")

        # --- tokenizer load ---
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)

        # --- model load with device_map for CPU/GPU split ---
        try:
            model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
                self.config.model_ckpt,
                device_map="auto",  # automatically splits layers across available devices
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
            print("Model loaded with automatic CPU/GPU layer mapping")
        except Exception as e:
            print("Warning: Could not use device_map. Loading on default device.")
            model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
            model_pegasus.to(device)

        # --- data collator ---
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # --- load dataset ---
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # --- training arguments ---
        trainer_args = TrainingArguments(
            output_dir=os.path.join(self.config.root_dir, 'pegasus-samsum'),
            num_train_epochs=1,
            warmup_steps=500,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            weight_decay=0.01,
            logging_steps=10,
            eval_steps=500,
            save_steps=1_000_000,
            gradient_accumulation_steps=16,
            dataloader_drop_last=False
        )

        # --- trainer ---
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"]
        )

        # --- train ---
        trainer.train()

        # --- save model & tokenizer ---
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))

        print("Training completed and model saved successfully!")
