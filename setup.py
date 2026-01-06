from setuptools import setup, find_packages

setup(
    name="xmem2",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-contrib-python",
        "pillow",
        "numpy",
        "scipy",
        "requests",
        "tqdm",
    ],
)
