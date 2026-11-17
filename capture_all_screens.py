import subprocess
import os
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_path = os.path.abspath("lumo-prototype.html")
out_dir = os.path.abspath("screenshots")
os.makedirs(out_dir, exist_ok=True)

targets = [
    ("01-runway.png", f"file:///{html_path}"),
    ("02-topics-matrix.png", f"file:///{html_path}#screen-2"),
    ("03-practice-front.png", f"file:///{html_path}#screen-3"),
    ("03-practice-back.png", f"file:///{html_path}#screen-3-back"),
    ("04-citation-drawer.png", f"file:///{html_path}#screen-4"),
    ("06-session-debrief.png", f"file:///{html_path}#screen-6"),
    ("07-student-profile.png", f"file:///{html_path}#screen-7"),
]

for name, url in targets:
    out_file = os.path.join(out_dir, name)
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--window-size=430,932",
        f"--screenshot={out_file}",
        url
    ]
    print(f"Capturing {name}...")
    subprocess.run(cmd, check=True)
    time.sleep(0.3)

print("All screens captured successfully!")
