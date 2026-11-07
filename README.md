# Multimodal Search Demo

A **zero-download** text-to-image search baseline built on visual color and shape attributes. This project shows the retrieval pipeline and evaluation mechanics that underlie multimodal search, without claiming to implement CLIP or another foundation model.

## Features
- Generates original synthetic shape images (circle, square, triangle).
- Extracts image color/shape features and maps text queries into the same feature space.
- Ranks images by cosine similarity; computes Recall@k.
- Produces a contact sheet and JSON results.

## Run
```bash
python -m pip install -r requirements.txt
python -m multimodal_demo.demo
python -m unittest discover -s tests -v
```

## Upgrade ideas
Add pretrained CLIP embeddings (optional dependency), a larger properly licensed image corpus, batch indexing, and a web interface. The included baseline is deliberately small and deterministic.

MIT licensed.
