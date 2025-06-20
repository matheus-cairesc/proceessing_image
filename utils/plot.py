import matplotlib.pyplot as plt

# Exibe uma imagem em escala cinza com tamanho ajustado, sem mostrar os eixos.
def plot_image(image):
    plt.figure(figsize=(12, 4)) 
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

# Exibe multiplas imagens lado a lado em uma única linha com títulos.
def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols= number_images, figsize=(12, 4))
    names_lst =  [f'Image {i}' for i in range(1, number_images)]
    names_lst.append('Result')
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

# Plota os histogramas dos canais de cor (R, G, B) de uma imagem RGB.
def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title(f'{color.title()} histogram')
        ax.hist(image[:, :, index].ravel(), bins= 256, color= color, alpha= 0.8)
    fig.tight_layout()
    plt.show()