# VQA-RAD Dataset

This folder should contain the VQA-RAD dataset files.

## Download Instructions

1. Visit the official VQA-RAD repository: [https://osf.io/89kps/](https://osf.io/89kps/)

2. Download the following files:
   - `VQA_RAD Dataset Public.json` - The main dataset file
   - `VQA_RAD Image Folder.zip` - All radiological images

3. Extract to this folder:
   ```
   data/
   ├── VQA_RAD Dataset Public.json
   └── VQA_RAD Image Folder/
       ├── synpic100033.jpg
       ├── synpic100077.jpg
       └── ... (315 images total)
   ```

## Dataset Statistics

- **Images**: 315 radiological images
- **Questions**: 2,248 question-answer pairs
- **Train Split**: 1,810 pairs
- **Test Split**: 438 pairs
- **Question Types**: PRES, ABN, ORGAN, MODALITY, POSITION, SIZE
- **Answer Types**: CLOSED (yes/no), OPEN (free-form)

## Citation

If you use this dataset, please cite:

```bibtex
@article{lau2018dataset,
  title={A dataset of clinically generated visual questions and answers about radiology images},
  author={Lau, Jason J and Gayen, Soumya and Ben Abacha, Asma and Demner-Fushman, Dina},
  journal={Scientific Data},
  volume={5},
  pages={180251},
  year={2018},
  publisher={Nature Publishing Group}
}
```

## Note

**The dataset files are NOT included in this repository due to size and licensing.**
Please download them from the official source.