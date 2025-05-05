import replicate

def predict(prompt, lora_scale=0.7):
    output = replicate.run(
        "stability-ai/sdxl",
        input={
            "prompt": prompt,
            "lora": [{"id": "mavaila/personamau", "scale": lora_scale}]
        }
    )
    return output
