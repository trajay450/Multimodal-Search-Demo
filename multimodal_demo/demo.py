import json
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
from .core import COLORS, SHAPES, render, search, recall_at_k

def main():
    out=Path("outputs"); out.mkdir(exist_ok=True)
    items=[{"id":f"{c}_{s}","color":c,"shape":s} for c in COLORS for s in SHAPES]
    sheet=Image.new("RGB",(3*130,3*125),"#eeeeee")
    d=ImageDraw.Draw(sheet)
    for i,item in enumerate(items):
        img=render(item["color"],item["shape"])
        x=(i%3)*130+17; y=(i//3)*125+5
        sheet.paste(img,(x,y)); d.text((x,y+98),item["id"],fill="black")
    sheet.save(out/"contact_sheet.png")
    queries=[{"text":f"{c} {s}","relevant_ids":[f"{c}_{s}"]} for c in COLORS for s in SHAPES]
    result={"recall_at_1":recall_at_k(items,queries,1),"example_query":"blue triangle","results":search(items,"blue triangle",3)}
    (out/"results.json").write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__ == "__main__": main()
