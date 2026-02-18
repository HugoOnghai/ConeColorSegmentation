# Hugo Onghai
# ECE5242 Project 1: Color Segmentation
# Due 2/9/2026 at 4:05PM

## Updated to include my new Gaussian Mixture Model!

My project requires Python and uv, a package manager for Python. I chose to use uv instead of pip because, after some initial work to install it, I believe it will be much faster and more convenient than pip for you as it is for me. It can be installed following [these steps](https://docs.astral.sh/uv/#highlights). To apply my code to test images, launch `train-GMM.ipynb` with uv.

From the project root, run the following:
```bash
uv run --with jupyter jupyter lab
```

Then, inside jupyter lab, navigate to `train-GDA.ipynb` or 'EM-implementation.ipynb' depending on if you would like to run the single gaussian discriminant analysis model or the gaussian mixture model fit with expectation maximization, respectively.

To perform color segmentation on a desired test image, place the image inside the directory `/Proj1TestImages/` at the root of the project. Then, run all cells in the Jupyter notebook. The second-to-last cell will display all results as printed statements and matplotlib figures in its output.


