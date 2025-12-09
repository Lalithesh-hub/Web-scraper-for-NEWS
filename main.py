import json
from scaper.scrape_newyorktimes import scrape_article

def main():
    print ("Starting the article scraping...")
    print ("---------------------------------------")
    url=input("Enter the article URL: ").strip()

    if not url:
        print("No URL provided. Exiting.")
        return

    if not url.startswith("https://"):
        url = "https://" + url
    
    print(f"Scraping article from: {url}")
    article_data = scrape_article(url)

    output_file = "scraped_article.json"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(article_data, f, ensure_ascii=False, indent=4)
        print(f"Article data saved to {output_file}")
        print(f"Title: {article_data['title']}")

    except Exception as e:
        print(f"Failed to save article data: {e}")
if __name__ == "__main__":
    main()
