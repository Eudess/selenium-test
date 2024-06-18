START_URL = "https://catalog.data.gov/dataset"

DATASET = "Obesity in California, 2012 and 2013"

DATASET_XPATH = {
    "filter": "//li/a[contains(@href, 'organization=ca')]",
    "search": "//span//input[contains(@id, 'search-big')]",
    "link": "//ul[contains(@class, 'dataset-list')]//h3/a[contains(@href, 'obesity-in-california-2012-and-2013')]",
    "download": "//ul[contains(@class, 'resource-list')]//li//a[contains(@title, 'CSV')]/following-sibling::div//a[contains(@href, 'csv')]"
}