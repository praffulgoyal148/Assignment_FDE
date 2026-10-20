import json
from pathlib import Path
from datetime import datetime

data_dir = Path("./data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir/"user.json"

session_data = {
   "user":"AI",
   "createdData":datetime.now().isoformat()
}

with open(file_path,"w") as f:
    json.dump(session_data,f,indent=4)

with open(file_path,"r") as f:
    loaded_data = json.load(f)
    print(loaded_data)