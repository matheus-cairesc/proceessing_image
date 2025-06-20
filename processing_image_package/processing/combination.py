import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity as ssim

# Compara as imagens e retorna a diferença entre elas
def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = ssim(gray_image1, gray_image2, full=True)
    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    return normalized_difference_image

# Faz a correção de tons de cor da imagem.
def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image