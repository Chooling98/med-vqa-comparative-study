import os
import torch
from torch.utils.data import Dataset
from PIL import Image
from torchvision import transforms


class YesNoVQADataset(Dataset):
    def __init__(self, data, answer_vocab, question_vocab, image_dir):
        self.samples = [
            x for x in data
            if x["answer_type"].lower() == "closed"
            and x["answer"].lower() in ["yes", "no"]
        ]

        self.answer_vocab = answer_vocab
        self.question_vocab = question_vocab
        self.image_dir = image_dir

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sample = self.samples[idx]

        # Load image
        image_path = os.path.join(self.image_dir, sample["image_name"])
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image)

        # Encode question
        question_ids = [
            self.question_vocab.get(w, self.question_vocab["<unk>"])
            for w in sample["question"].lower().split()
        ]

        # Encode answer
        answer_id = self.answer_vocab[sample["answer"].lower()]

        return {
            "image": image,
            "question": torch.tensor(question_ids, dtype=torch.long),
            "answer": torch.tensor(answer_id, dtype=torch.long)
        }