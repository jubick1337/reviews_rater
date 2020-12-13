import torch

from ml.model import ReviewsModel

model = ReviewsModel(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
