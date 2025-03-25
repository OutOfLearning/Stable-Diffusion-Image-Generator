from diffusers import StableDiffusionPipeline
import torch

# Enable TensorFloat32 (only applies if using CUDA)
torch.backends.cuda.matmul.allow_tf32 = True

# Load Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"

# Check if a GPU is available
if torch.cuda.is_available():
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.to("cuda")  # Use GPU
else:
    pipe = StableDiffusionPipeline.from_pretrained(model_id)  # Remove float16
    pipe.to("cpu")  # Use CPU

# Define prompt
prompt = input("Enter Text : ")

# Generate an image
image = pipe(prompt).images[0] 

# Save the image
image.save("Robotic Flower.png")

print("Image generated successfully!")