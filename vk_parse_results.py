import sys
import time
import random
import stealth_requests


def fetch_data(vk_id):
    services = [
        f"https://onli-vk.ru/pivatfriends.php?id={vk_id}",
        f"https://onli-vk.ru/id{vk_id}",
        f"https://topdb.ru/id{vk_id}",
        f"https://poiski.pro/vk/user/id{vk_id}",
        f"https://looka.one/vk_user/id{vk_id}"
    ]

    results = {}

    for service in services:
        try:
            response = stealth_requests.get(service, timeout=15)

            if response.status_code == 200:
                if "onli-vk.ru/pivatfriends.php" in service:
                    filename = f"onli-vk.ru_privatefriends_{vk_id}.html"
                elif "onli-vk.ru/id" in service:
                    filename = f"onli-vk.ru_{vk_id}.html"
                else:
                    filename = f"{service.split('//')[1].split('/')[0]}_{vk_id}.html"

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(response.text)
                results[service] = f"Results saved in {filename}"
            else:
                results[service] = f"Error: Unable to retrieve data. Status code {response.status_code}"
        except Exception as e:
            results[service] = f"Error: {str(e)}"

        time.sleep(random.uniform(30, 100))

    return results


def main():
    print('#Enter the id in format:"111111111"')
    print('#id you can get with services like "https://regvk.com/id/"')
    vk_id = input('>>>')

    results = fetch_data(vk_id)

    print("\nSearch Results:")
    for service, message in results.items():
        print(f"{service}: {message}")


if __name__ == '__main__':
    main()
