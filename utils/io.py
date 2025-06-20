from skimage.io import imread, imsave

# Faz a leitura da imagem.
def read_image(path, is_gray=False):
    image = imread(path, as_gray=is_gray)
    return image

# Salvando a imagem.
def save_image(image, path):
    imsave(path, image)
