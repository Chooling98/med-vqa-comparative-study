import random
from collections import defaultdict


def split_by_qid(data, test_ratio=0.2, seed=42):
    """
    Split VQA-RAD data by qid_linked_id to avoid paraphrase leakage
    """
    random.seed(seed)

    # Group samples by qid_linked_id
    groups = defaultdict(list)
    for sample in data:
        groups[sample["qid_linked_id"]].append(sample)

    group_keys = list(groups.keys())
    random.shuffle(group_keys)

    num_test = int(len(group_keys) * test_ratio)
    test_keys = set(group_keys[:num_test])

    train_data, test_data = [], []

    for key, samples in groups.items():
        if key in test_keys:
            test_data.extend(samples)
        else:
            train_data.extend(samples)

    return train_data, test_data
