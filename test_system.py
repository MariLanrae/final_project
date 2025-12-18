from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_web_interface():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("http://localhost:5000")

    try:
        assert "Космический Атлас" in driver.title

        page_source = driver.page_source
        assert "Туманность Ориона" in page_source or "Галактика Андромеда" in page_source

        print("Системный тест прошёл успешно!")

    except Exception as e:
        print(e)
        raise

    finally:
        driver.quit()