import multiprocessing
import requests


def downloadFile(_url, name):
    print(f"Started Download {name}")
    response = requests.get(_url)
    open(f"files/{name}.jpg", "wb").write(response.content)
    print(f"Finished Download {name}")


if __name__ == '__main__':
    pros = []
    url = "https://picsum.photos/1280/800"
    for i in range(10):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
