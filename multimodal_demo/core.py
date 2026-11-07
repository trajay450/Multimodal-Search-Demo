import numpy as np
from PIL import Image, ImageDraw

COLORS = {"red": (220, 55, 65), "green": (55, 180, 85), "blue": (65, 100, 220)}
SHAPES = ("circle", "square", "triangle")
FEATURES = tuple(COLORS) + SHAPES

def render(color, shape, size=96):
    if color not in COLORS or shape not in SHAPES: raise ValueError("Unknown color or shape")
    im = Image.new("RGB", (size, size), "white")
    d = ImageDraw.Draw(im)
    if shape == "circle": d.ellipse((18,18,size-18,size-18), fill=COLORS[color])
    elif shape == "square": d.rectangle((18,18,size-18,size-18), fill=COLORS[color])
    else: d.polygon([(size//2,14),(14,size-16),(size-14,size-16)], fill=COLORS[color])
    return im

def encode_tags(tags):
    return np.array([float(t in tags) for t in FEATURES], dtype=float)

def search(items, query, k=3):
    if k < 1: return []
    words = set(query.lower().split())
    q = encode_tags(words)
    if not np.any(q): return []
    qnorm = np.linalg.norm(q)
    ranked = []
    for item in items:
        v = encode_tags({item["color"], item["shape"]})
        score = float(np.dot(q, v) / (qnorm * np.linalg.norm(v)))
        ranked.append((score, item["id"]))
    return [{"id": name, "score": round(score, 6)} for score, name in sorted(ranked, key=lambda x: (-x[0], x[1]))[:k]]

def recall_at_k(items, queries, k=1):
    if not queries: raise ValueError("Queries cannot be empty")
    scores=[]
    for q in queries:
        found = {x["id"] for x in search(items,q["text"],k)}
        relevant=set(q["relevant_ids"])
        if not relevant: raise ValueError("Missing relevant IDs")
        scores.append(len(found & relevant)/len(relevant))
    return sum(scores)/len(scores)
