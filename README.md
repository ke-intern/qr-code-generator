# QR 코드 생성기

## 🌟 프로젝트 소개

사용자가 제공한 배경 이미지와 QR 코드에 담을 데이터를 받아, 새로운 QR 코드를 생성하는 기능을 제공합니다.

생성된 QR 코드는 아래와 같이 배경 이미지 위에 합성되어 저장되며,

이를 통해 사용자는 자신만의 맞춤형 QR 코드를 만들 수 있습니다.

<p align="center">
    <image src="./docs/img_before_and_after.png">
</p>

## 🏃 실행 방법

0. python이 설치되어 있어야 합니다. (저는 Python 3.9.6 사용해 개발하였습니다.)

1. 가상 환경 생성
    ```bash
    python3 -m venv venv
    ```

2. 가상 환경 활성화
    ```bash
    source venv/bin/activate
    ```

3. 필요한 라이브러리 설치
    ```bash
    pip install Pillow qrcode
    ```

4. (선택) 기본 이미지 설정
   
    기본 배경 이미지로 사용될 이미지를 준비합니다. 

    기본적으로 [카카오클라우드](./kakaocloud.png) 이미지가 사용됩니다. 

    다른 이미지를 사용하려면, 해당 이미지 파일의 경로를 create_qr 함수의 background_image_path 인자로 전달합니다.

    ```bash
    create_qr(data, background_image_path="path/to/your/image.png")
    ```

5. 파일 실행
    ```bash
    python3 generator.py
    ```
