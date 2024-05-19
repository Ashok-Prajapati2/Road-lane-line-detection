import numpy as np
import torch
from torchvision import transforms

def preprocess_image(image, target_size=(224, 224)):
    """
    Preprocess the input image before feeding it into the CNN model.
    
    Args:
        image (numpy.ndarray): Input image as a NumPy array.
        target_size (tuple): Target size for the input image.
        
    Returns:
        torch.Tensor: Preprocessed image as a PyTorch tensor.
    """
    # Convert image to PIL Image
    pil_image = transforms.functional.to_pil_image(image)
    
    # Apply transformations (resize, convert to tensor, normalize)
    preprocess = transforms.Compose([
        transforms.Resize(target_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    preprocessed_image = preprocess(pil_image)
    
    # Add batch dimension
    preprocessed_image = preprocessed_image.unsqueeze(0)
    
    return preprocessed_image

def postprocess_output(output):
    """
    Postprocess the output of the CNN model.
    
    Args:
        output (torch.Tensor): Output tensor from the CNN model.
        
    Returns:
        numpy.ndarray: Postprocessed output as a NumPy array.
    """
    # Convert output tensor to NumPy array
    output_array = output.detach().cpu().numpy()
    
    # Perform any necessary postprocessing steps here
    
    return output_array

