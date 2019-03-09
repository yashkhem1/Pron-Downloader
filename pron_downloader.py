import requests
import bs4

if __name__ == "__main__":
    meriam_url = "https://www.merriam-webster.com/dictionary/"
    download_url = "https://media.merriam-webster.com/audio/prons/en/us/mp3/"
    file = open('audio.txt', 'r')
    count = 1
    for word in file:
        word = str(word)
        word = word.lower()
        url = meriam_url + word
        print(url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        prons = soup.select('a.play-pron.hw-play-pron')
        #print('a[title="How to pronounce ' + word + ' (audio)"]')
        # prons = soup.select('a')
        print(len(prons))
        subcount = 1
        for pron in prons:
            url1 = pron.get('href')
            url_add = url1.split('=')[-1]
            download = download_url + url_add[0] + '/' + url_add + '.mp3'
            print(download)
            raw = requests.get(download, allow_redirects=True)
            file_name = str(count) + '-0' + str(subcount) + '.mp3'
            open(file_name, 'wb').write(raw.content)
            subcount += 1
            # print(pron.get('class'))

        # break
        count += 1
