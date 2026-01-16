"""
House-GAN++: Generative Adversarial Layout Refinement Network
==============================================================

A deep learning framework for automated floorplan generation and refinement.

Reference:
    Nauata, N., Hosseini, S., Chang, K. H., Chu, H., Cheng, C. Y., & Furukawa, Y. (2021).
    House-GAN++: Generative Adversarial Layout Refinement Network towards Intelligent 
    Computational Agent for Professional Architects. 
    In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 
    (pp. 13632-13641).

Paper: https://arxiv.org/abs/2103.02574
Project Page: https://ennauata.github.io/houseganpp/page.html
"""

__version__ = "0.1.0"
__author__ = "Nelson Nauata"
__email__ = "nnauata@sfu.ca"

# Note: Submodules are available as houseganpp.dataset, houseganpp.models, etc.
# They are not imported here to avoid circular import issues with the flat package structure

__all__ = [
    "dataset",
    "models", 
    "misc",
    "scripts",
]
