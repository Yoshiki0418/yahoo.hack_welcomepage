import requests


# # 背景を削除したい画像のパスを指定します。
# image_path = 'static/image/situation1.png'

# # 背景が削除された画像を保存するパスを指定します。
# output_path = 'static/image/result.png'

def transparency(image_path, output_path):
    # APIキーをここに入力します。
    api_key = ''

    # Remove.bgのAPIにリクエストを送信します。
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(image_path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': api_key},
    )

    # レスポンスを確認して、成功した場合は画像を保存します。
    if response.status_code == requests.codes.ok:
        with open(output_path, 'wb') as out:
            return out.write(response.content)
    else:
        return print("Error:", response.status_code, response.text)

transparency(image_path, output_path)