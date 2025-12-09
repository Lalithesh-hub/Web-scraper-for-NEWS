# Web Scraper

A simple Python web scraper that extracts article titles and content from web pages and saves them to a JSON file.

## Features

- Scrapes article titles and content from web pages
- Automatically adds `https://` protocol if missing
- Saves scraped data to JSON format
- Handles errors gracefully
- Simple command-line interface

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the main script:

```bash
python main.py
```

2. When prompted, enter the article URL:

```
Enter the article URL: https://example.com/article
```

You can also enter the URL without the `https://` prefix - the script will automatically add it:

```
Enter the article URL: example.com/article
```

3. The scraper will extract the article title and content, then save it to `scraped_article.json`

## Output

The scraper creates a JSON file (`scraped_article.json`) with the following structure:

```json
{
    "url": "https://example.com/article",
    "title": "Article Title",
    "content": "Article content here..."
}
```

## Project Structure

```
WebScraper/
├── main.py                      # Main entry point
├── scaper/
│   └── scrape_newyorktimes.py  # Scraping function
├── scraped_article.json         # Output file (generated)
└── README.md                    # This file
```

## How It Works

1. The script prompts for a URL
2. If the URL doesn't start with `https://`, it automatically prepends it
3. Makes an HTTP GET request to fetch the webpage
4. Parses the HTML using BeautifulSoup
5. Extracts:
   - Title from the first `<h1>` tag
   - Content from all `<p>` tags
6. Saves the data to `scraped_article.json`

## Error Handling

The scraper handles various errors:
- Invalid URLs
- Network errors
- Missing HTML elements
- File writing errors

If an error occurs, the output JSON will contain:
```json
{
    "url": "https://example.com/article",
    "title": "Error",
    "content": "Error message here..."
}
```

## Limitations

- Works best with static HTML content
- May not work correctly with JavaScript-heavy websites that load content dynamically
- Extracts content from `<h1>` and `<p>` tags - may need customization for different website structures

## Notes

- The scraper uses Python's built-in `html.parser` (no additional parser installation required)
- The output file is overwritten each time you run the scraper
- Make sure you have permission to scrape the target website and comply with their terms of service

## License

This project is provided as-is for educational purposes.

