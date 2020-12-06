import os

latest = max([f for f in os.listdir("days") if f.startswith("day")])
print(latest)
os.system(f"python days/{latest}")
