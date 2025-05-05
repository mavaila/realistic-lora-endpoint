import replicate

def predict(prompt: str):
    output = replicate.run(
        "stability-ai/sdxl:latest",
        input={
            "prompt": prompt,
            "lora": "mavaila/personamau"
        }
    )
    return output
