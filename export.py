'''
Export
'''

from datetime import datetime
import os

def export_briefing(text, user_id):
    os.makedirs("briefings", exist_ok=True)
    dattime = datetime.now().strftime("%Y-%m-%d")

    filepath = f"briefings/{user_id}_{dattime}.md"

    with open(filepath, "w") as f:
        f.write(text)
    return filepath

if __name__ == "__main__":
    print(export_briefing("test content", "testuser"))