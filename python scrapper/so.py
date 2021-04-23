import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("a", {"class": "s-link"}).get_text()
    company, location = html.find("h3", {"class": "fc-black-700"}).find_all(
        "span", recursive=False
    )
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}",
    }


def extract_so_jobs(last_page):
    jobs = []
    for page in range(1, last_page):
        result = requests.get(f"{URL}pg={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    jobs = []
    last_page = get_last_page()
    extract_so_jobs(last_page)
    return jobs
