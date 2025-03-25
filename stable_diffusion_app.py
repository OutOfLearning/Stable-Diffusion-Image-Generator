import gradio as gr
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

# Define function for image generation
def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image

# Create Gradio UI
demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter a prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="Stable Diffusion Image Generator",
    description="Enter a text prompt and generate an AI image using Stable Diffusion."
)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(share=True)
