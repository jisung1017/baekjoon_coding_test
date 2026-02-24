import os
import json
import re

BASE_DIR = "."
PROB_DIR = "problems"
META_FILE = "metadata.json"
WRONG_NOTE = "wrong_notes.md"

def load_metadata():
    if not os.path.exists(META_FILE):
        return {}
    with open(META_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_metadata(data):
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def extract_meta_from_file(filepath):
    type_val, note_val = None, None
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("# type:"):
                type_val = line.replace("# type:", "").strip()
            if line.startswith("# note:"):
                note_val = line.replace("# note:", "").strip()
    return type_val, note_val

def update_wrong_notes(problem_id, note):
    if not note:
        return
    with open(WRONG_NOTE, "a", encoding="utf-8") as f:
        f.write(f"## 문제 {problem_id}\n")
        f.write(f"{note}\n\n")

def main():
    os.makedirs(PROB_DIR, exist_ok=True)
    metadata = load_metadata()

    for filename in os.listdir(BASE_DIR):
        if not filename.endswith(".py"):
            continue
        if filename in ["organize.py"]:
            continue

        m = re.match(r"(\d+)", filename)
        if not m:
            continue

        problem_id = m.group(1)

        # 파일에서 type과 note 읽기
        type_val, note_val = extract_meta_from_file(filename)

        # metadata.json 업데이트
        metadata[problem_id] = {
            "type": type_val,
            "note": note_val
        }

        # wrong_notes.md 업데이트
        if note_val:
            update_wrong_notes(problem_id, note_val)

        # 파일 이동
        new_path = os.path.join(PROB_DIR, f"{problem_id}.py")
        os.replace(filename, new_path)

    save_metadata(metadata)

if __name__ == "__main__":
    main()
