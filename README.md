
---

# 📜 India Government Scheme Scraper

![Python Badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Web Scraping Badge](https://img.shields.io/badge/Web%20Scraping-%23FF6F61.svg?style=for-the-badge)

This script allows users to scrape data in the form of list from websites. The extracted data includes the scheme name, external link, description, and a backup link.

## 🚀 Features

- Fetches scheme details across multiple pages.
- Export data to a CSV file.
- Modular codebase for easy integration and modification.

## 🛠️ Setup & Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/NandishRana/web-scrapper.git
    cd web-scrapper
    ```

2. **Install the required packages:**
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

3. **Run the script:**
    ```bash
    python main.py
    ```

4. 🎉 The scraped data will be saved to `catalogue.csv`.

## 📚 Dependencies

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML and extracting data.
- `pandas`: For handling and saving the data.

## 📝 Note

Always ensure you have the right permissions and you're respectful of the website's `robots.txt` file and any rate limits they might have before scraping.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

---
