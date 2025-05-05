import replicate

class Predictor:
    def predict(self, prompt: str) -> str:
        output = replicate.run(
            "stability-ai/sdxl:latest",
            input={
                "prompt": prompt,
                "lora": "mavaila/personamau"
            }
        )
        return output
