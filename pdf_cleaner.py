# pdf_cleaner.py

import os
import sys
from pdf2image import convert_from_path
import cv2
import numpy as np
from PIL import Image

if len(sys.argv) < 2:
    print("사용법: python pdf_cleaner.py <PDF 파일 경로> [출력폴더] [area값]")
    sys.exit(1)

pdf_file = sys.argv[1]
output_dir = sys.argv[2] if len(sys.argv) > 2 else "./cleaned_images/"
area_value = int(sys.argv[3]) if len(sys.argv) > 3 else 50  # 기본값 50

poppler_path = r"Poppler 바이너리 경로"   # <-- 여기를 사용자 환경의 poppler 경로로 수정하세요.

os.makedirs(output_dir, exist_ok=True)
pages = convert_from_path(pdf_file, poppler_path=poppler_path)
png_files = []

for i, page in enumerate(pages):
    img_path = os.path.join(output_dir, f"page_{i+1}.png")
    page.save(img_path, 'PNG')
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"이미지 파일을 읽을 수 없습니다: {img_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=3)
    binary = cv2.adaptiveThreshold(
        opening, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 35, 15
    )
    mask = np.copy(binary)
    cnts, _ = cv2.findContours(255-mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area < area_value:
            cv2.drawContours(mask, [cnt], -1, 255, -1)
    clean_img_path = os.path.join(output_dir, f"cleaned_page_{i+1}.png")
    cv2.imwrite(clean_img_path, mask)
    png_files.append(clean_img_path)

clean_images = [Image.open(png).convert("RGB") for png in png_files]
result_pdf = os.path.join(output_dir, "cleaned_result.pdf")
clean_images[0].save(result_pdf, save_all=True, append_images=clean_images[1:])
