# Fine-Tuning Gemma 2B for WSDM Chatbot Arena Preference Prediction

## 🧠 Problem Description

This project focuses on fine-tuning a large language model to align with human preferences using the WSDM Chatbot Arena dataset. The goal is to train a model that can predict which chatbot response a human would prefer in a head-to-head comparison.

**Competition summary**:
"This competition challenges you to predict which responses users will prefer in a head-to-head battle between chatbots powered by large language models (LLMs). You'll be given a dataset of conversations from the Chatbot Arena, where different LLMs generate answers to user prompts. By developing a winning machine learning model, you'll help improve how chatbots interact with humans and ensure they better align with human preferences."

📊 **Dataset**

The dataset contains multilingual conversations between users and multiple LLMs.

**For each sample**:

A user prompt is provided

Two model responses (A and B) are shown

A human-annotated label indicates the preferred response

The task is formulated as a binary classification: given the full input, predict if A or B is preferred.

## 🧪 Implementation Details

🔧 **Model Setup**

***Base model***: Gemma-2-2B

***Model class***: Gemma2ForSequenceClassification

***Framework***: Hugging Face Transformers

***Training platform***: Google Colab A100 GPU

⚙️ **Fine-Tuning Strategy**

***Quantization***: 4-bit via bitsandbytes

***Parameter-Efficient Fine-Tuning (PEFT)***:

Used LoRA adapters for efficiency

First 6 transformer layers frozen to preserve core semantics

Only upper layers were trainable

Truncation Strategy: Head+Tail

Retained the first and last segments of input (user prompt + model responses)

***Max token length***: 1900 tokens

🗂️ **Data Handling**

Train/Validation/Test split: 70/10/20

Tokenization and padding using Gemma's tokenizer

Preprocessing logic included custom logic to concatenate, truncate, and label samples

📈 **Optimization**

***Optimizer***: AdamW

***Learning rate scheduler***: Linear warmup

***Evaluation metric***: Accuracy

## ✅ Key Learnings

PEFT and quantization make it feasible to fine-tune large models under resource constraints

Selective freezing and LoRA allow task-specific learning without retraining the whole model

Truncation design significantly impacts long-form data tasks

## 🔭 Future Work

Extend this fine-tuning approach to train reward models for RLHF

Explore inference-time optimizations for deployment in constrained environments
