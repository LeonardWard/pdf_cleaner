# pdf_cleaner.py

```

이 스크립트는 PDF 파일의 작은 블롭(노이즈)을 제거하여 깨끗한 PDF로 저장합니다.

## 사용법

```
python pdf_cleaner.py <PDF 파일 경로> [출력폴더] [area값]
```

- `<PDF 파일 경로>`: 처리할 PDF 파일 경로
- `[출력폴더]`: 이미지 및 결과 PDF가 저장될 폴더 (기본값: ./cleaned_images/)
- `[area값]`: 제거할 블롭(노이즈)의 최대 면적 값 (기본값: 50)

## 필수 패키지

requirements.txt 파일을 참고하여 아래의 패키지를 설치하세요.

```
pip install -r requirements.txt
```

- pdf2image
- opencv-python
- numpy
- Pillow

## Poppler 설치 안내

pdf2image 사용 시 poppler가 필요하며, 아래와 같이 poppler 바이너리 경로를 지정해야 합니다.

```
poppler_path = r"Poppler 바이너리 경로"
```

Windows: https://github.com/oschwartz10612/poppler-windows/releases  
Mac: brew install poppler  
Linux: apt install poppler-utils

## 출력 결과

- 개별 페이지 이미지(`page_X.png`, `cleaned_page_X.png`)
- 전체 결과 PDF(`cleaned_result.pdf`)

## 문의

오류 발생 시, 사용법과 패키지 설치 여부를 확인한 후 이슈를 남겨주세요.
```
