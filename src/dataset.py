import json
import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class VQARADDataset(Dataset):
    def __init__(self, json_path, image_dir, transform=None):
        with open(json_path, "r") as f:
            self.data = json.load(f)

        self.image_dir = image_dir

        self.transform = transform if transform else transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]

        image_path = os.path.join(self.image_dir, sample["image_name"])
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image)

        return {
            "image": image,
            "question": sample["question"],
            "answer": sample["answer"],
            "answer_type": sample["answer_type"],
            "question_type": sample["question_type"],
            "phrase_type": sample["phrase_type"],
            "image_organ": sample["image_organ"],
            "qid": sample["qid"],
            "qid_linked_id": sample["qid_linked_id"]
        }