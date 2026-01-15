import torch
import torch.nn as nn
from torchvision import models


class CNNLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=100, hidden_dim=256, num_answers=2):
        super().__init__()

        # CNN encoder
        cnn = models.resnet50(pretrained=True)
        self.cnn = nn.Sequential(*list(cnn.children())[:-1])
        self.cnn_fc = nn.Linear(2048, hidden_dim)

        # Freeze CNN
        for p in self.cnn.parameters():
            p.requires_grad = False

        # Question encoder
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)

        # Classifier
        self.classifier = nn.Linear(hidden_dim * 2, num_answers)

    def forward(self, images, questions):
        questions = questions.long()
      
        # Image branch
        img_feat = self.cnn(images).squeeze(-1).squeeze(-1)
        img_feat = self.cnn_fc(img_feat)

        # Question branch
        emb = self.embedding(questions)
        _, (h, _) = self.lstm(emb)
        ques_feat = h[-1]

        # Fusion
        fused = torch.cat([img_feat, ques_feat], dim=1)
        return self.classifier(fused)
