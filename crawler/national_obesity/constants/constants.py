START_URL = "https://catalog.data.gov/dataset"

DATASET = "National Obesity By State"

DATASET_XPATH = {
    "search": "//span//input[contains(@id, 'search-big')]",
    "link": "//ul[contains(@class, 'dataset-list')]//h3/a[contains(@href, 'obesity-by-state')]",
    "download": "//ul[contains(@class, 'resource-list')]//li//a[contains(@title, 'CSV')]/following-sibling::div//a[contains(@href, 'csv')]"
}