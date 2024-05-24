import qrcode
from PIL import Image

"""
이미지 파일을 배경으로 하는 QR 코드를 생성하는 함수

Args:
- data (str): QR 코드에 포함될 데이터(URL, 텍스트 등)
- background_image_path (str): 배경 이미지 파일의 경로 (기본값: "./kakaocloud.png")
- output_path (str): 생성된 QR 코드 이미지가 저장될 경로 (기본값: "output.png")
- box_size (int): QR 코드의 각 모듈(픽셀) 크기 (기본값: 2)
- border (int): QR 코드 주위의 여백 크기 (기본값: 1)

Returns:
- image: 생성된 QR 코드 이미지

"""
def create_qr(data, background_image_path="./kakaocloud.png", output_path="output.png", box_size=2, border=1):
    # 배경 이미지를 불러온다.
    background = Image.open(background_image_path).convert('RGBA')
    bg_width, bg_height = background.size

    # QR 코드를 생성한다.
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

    # QR 코드를 배경 이미지 크기에 맞게 조정한다.
    qr_img = qr_img.resize((bg_width, bg_height), Image.NEAREST)

    # 투명도가 있는 새 이미지를 생성한다.
    combined = Image.new('RGBA', (bg_width, bg_height), (255, 255, 255, 0))

    # QR 코드의 검은색 부분을 투명하게 변경한다.
    datas = qr_img.getdata()
    new_data = []
    for item in datas:
        # 모든 검정색(또는 검정색의 음영) 픽셀을 투명하게 변경한다.
        if item[0] < 64 and item[1] < 64 and item[2] < 64:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)
    qr_img.putdata(new_data)

    # 배경 위에 QR 코드를 합성한다.
    combined = Image.alpha_composite(background, qr_img)

    # 결과 이미지를 저장한다.
    combined.save(output_path)

    # 결과 이미지를 반환한다.
    return combined

# QR 코드를 생성한다.
data = "https://kakaocloud.com/" # QR 코드에 넣을 데이터
create_qr(data)
