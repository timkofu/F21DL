

def visualize_image(image_dataframe, plt):
    """
    Visualizes a gray-scale image given a numpy array of it.

    Runs in a jupyter notebook and requires matplotlib be loaded and
    %matplotlib inline be run.
    """

    # Convert the pandas dataframe row to image
    image = image_dataframe.to_numpy()
    # Reshape it back to it's 48*48 pixel matrix
    image = image.reshape((48,48))

    plt.title(f"Index of the image is: {image_dataframe.index.values[0]}")
    # Show the image
    plt.imshow(
        image,
        cmap='gray',  # Tell matplot lib the image is grayscale
        vmin=0, vmax=255  # Tell matplotlib the range of pixels
    )

