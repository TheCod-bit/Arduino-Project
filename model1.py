
import torch
import torch.nn as nn


class GestureCNN(nn.Module):

    def __init__(self, num_classes=4):
        super().__init__()

        # Feature extraction layers
        self.features = nn.Sequential(

            # First convolutional layer
            nn.Conv1d(
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                padding=2
            ),

            nn.BatchNorm1d(16),
            nn.ReLU(),

            nn.MaxPool1d(kernel_size=2),

            # Second convolutional layer
            nn.Conv1d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.BatchNorm1d(32),
            nn.ReLU(),

            # Reduce sequence to one feature vector
            nn.AdaptiveAvgPool1d(1)
        )

        # Classification layers
        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Dropout(0.2),

            nn.Linear(32, num_classes)
        )

    def forward(self, x):

        x = self.features(x)

        x = self.classifier(x)

        return x
