# llava_infer.py
import torch
from transformers import AutoProcessor, LlavaForConditionalGeneration

model_id = "llava-hf/llava-1.5-7b-hf"

# ✅ 只定义，不执行
processor = AutoProcessor.from_pretrained(model_id)

model = LlavaForConditionalGeneration.from_pretrained(
    model_id,
    device_map="auto",
    dtype=torch.float16,
    low_cpu_mem_usage=True
)

# ✅ 把 inference 变成函数
def run_llava(image_pil, question):
    prompt = f"USER: <image>\n{question}\nASSISTANT:"

    inputs = processor(
        text=prompt,
        images=image_pil,
        return_tensors="pt"
    )

    for k, v in inputs.items():
        if isinstance(v, torch.Tensor):
            inputs[k] = v.to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=40,
            do_sample=False
        )

    return processor.decode(output[0], skip_special_tokens=True)


# ✅ 只有“直接运行这个文件”才会执行下面的代码
if __name__ == "__main__":
    from PIL import Image

    image = Image.open("test.jpg")
    ans = run_llava(image, "Is there ascites?")
    print(ans)