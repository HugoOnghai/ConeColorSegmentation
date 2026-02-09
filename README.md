# Hugo Onghai
# ECE5242 Project 1: Color Segmentation
# Due 2/9/2026 at 4:05PM

My project requires Python and uv, a package manager for Python. I chose to use uv instead of pip because, after some initial work to install it, I believe it will be much faster and more convenient than pip for you as it is for me. It can be installed following [these steps](https://docs.astral.sh/uv/#highlights). To apply my code to test images, launch `train-GMM.ipynb` with uv.

From the project root, run the following:
```bash
uv run --with jupyter jupyter lab
```

Then, inside jupyter lab, navigate to `train-GMM.ipynb`.

To perform color segmentation on a desired test image, place the image inside the directory `/Proj1TestImages/` at the root of the project. Then, run all cells in the Jupyter notebook. The second-to-last cell will display all results as printed statements and matplotlib figures in its output.

Here is what the output looks like for all training data:
```
ImageName: train_1_dist915.png, Down: 306, Right: 400, Distance: 929.8781250000001 cm
ImageName: train_1_dist915.png, Down: 166, Right: 400, Distance: 1125.7587878787879 cm
ImageName: train_6_dist305.png, Down: 508, Right: 382, Distance: 279.37034373248645 cm
ImageName: train_5_dist760.png, Down: 124, Right: 359, Distance: 758.9308333333333 cm
ImageName: train_5_dist760.png, Down: 126, Right: 402, Distance: 854.2421052631578 cm
ImageName: train_2_dist305.png, Down: 142, Right: 379, Distance: 362.9163043478261 cm
ImageName: train_2_dist305.png, Down: 15, Right: 469, Distance: 578.4490566037737 cm
ImageName: train_2_dist305.png, Down: 31, Right: 404, Distance: 1135.4740740740742 cm
ImageName: train_3_dist460.png, Down: 57, Right: 459, Distance: 505.8181650246306 cm
ImageName: train_4_dist450.png, Down: 121, Right: 114, Distance: 155.2840505226481 cm
ImageName: train_4_dist450.png, Down: 542, Right: 221, Distance: 285.0485884804851 cm
ImageName: train_7_dist305.png, Down: 480, Right: 596, Distance: 138.3289772727273 cm
ImageName: train_7_dist305.png, Down: 318, Right: 735, Distance: 471.6584615384616 cm
ImageName: train_7_dist305.png, Down: 275, Right: 637, Distance: 828.5891891891893 cm
ImageName: train_12_dist245.png, Down: 400, Right: 379, Distance: 242.2458592425099 cm
ImageName: train_13_dist185.png, Down: 390, Right: 332, Distance: 183.6063921377518 cm
ImageName: train_14_dist490.png, Down: 312, Right: 487, Distance: 465.3935483870968 cm
ImageName: train_10_dist610.png, Down: 479, Right: 370, Distance: 620.2324211502784 cm
ImageName: train_15_dist90.png, Down: 346, Right: 191, Distance: 96.65480797288501 cm
ImageName: train_16_dist730.png, Down: 431, Right: 431, Distance: 781.0313235294118 cm
ImageName: train_17_dist245.png, Down: 317, Right: 388, Distance: 252.2531202319194 cm
ImageName: train_18_dist150.png, Down: 192, Right: 379, Distance: 162.87100383631713 cm
ImageName: train_20_dist245.png, Down: 151, Right: 376, Distance: 246.38557017543857 cm
ImageName: train_21_dist305.png, Down: 295, Right: 300, Distance: 315.0557057416268 cm
ImageName: train_19_dist460.png, Down: 412, Right: 348, Distance: 448.2476911976912 cm
ImageName: train_22_dist215.png, Down: 448, Right: 210, Distance: 210.42871002132193 cm
ImageName: train_24_dist365.png, Down: 303, Right: 354, Distance: 360.34165103189497 cm
ImageName: train_29_dist150.png, Down: 287, Right: 393, Distance: 270.51 cm
ImageName: train_27_dist915.png, Down: 89, Right: 384, Distance: 873.5218750000001 cm
ImageName: train_25_dist580.png, Down: 112, Right: 363, Distance: 567.7370370370371 cm
ImageName: train_25_dist580.png, Down: 119, Right: 462, Distance: 754.2948700410398 cm
ImageName: train_26_dist915.png, Down: 474, Right: 391, Distance: 915.3621212121212 cm
ImageName: train_31_dist305.png, Down: 279, Right: 511, Distance: 315.2284552845528 cm
```
