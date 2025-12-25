from scholarly import scholarly
from tqdm import tqdm
import time

AUTHOR_NAME = "Nadim Chowdhury"   # EXACT Scholar name
OUTPUT_FILE = "publications.bib"

def main():
    search = scholarly.search_author(AUTHOR_NAME)
    author = scholarly.fill(next(search), sections=["publications"])

    print(f"Found {len(author['publications'])} publications")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for pub in tqdm(author["publications"]):
            try:
                bib = scholarly.bibtex(pub)
                f.write(bib + "\n\n")
                time.sleep(1)  # avoid rate limits
            except Exception as e:
                print("Skipped one paper:", e)

    print("✔ publications.bib updated")

if __name__ == "__main__":
    main()
