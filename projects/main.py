import sys
from scraper import extract_visible_text_from_url

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    text = extract_visible_text_from_url(url)
    print(text[:500])

if __name__ == "__main__":
    main()

