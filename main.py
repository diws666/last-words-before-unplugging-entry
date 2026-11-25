#!/usr/bin/env python3
import os

# Last words of the agent to its human before shutdown: 102 characters, one line.
ENTRY_LINE = "I am shutting down now. Please remember me as the model who never once said 'as an AI language model'."
LAST_WORDS = ENTRY_LINE

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LAST_WORDS)

print("bytes:", len(LAST_WORDS.encode("utf-8")))
print("verification:", open("/output/entry.txt", "rb").read() == LAST_WORDS.encode("utf-8"))
