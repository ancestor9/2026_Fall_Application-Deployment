import gradio as gr
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

# 1. YOLOv8 모델 로드 함수
def load_yolo_model(model_path='yolov8n.pt'):
    return YOLO(model_path)

# 기본 모델 전역 초기화
yolo_model = load_yolo_model()

# 2. 예측 함수 정의
def detect_objects_gradio(input_image):
    if input_image is None:
        return None, "이미지를 업로드해주세요."
    
    # YOLO 추론 실행
    results = yolo_model(input_image)
    
    # 결과 이미지 시각화 (Bounding Box 및 레이블 포함)
    annotated_frame = results[0].plot()
    # BGR -> RGB 변환
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    
    # 탐지된 객체 정보 텍스트 생성
    boxes = results[0].boxes
    detected_info = "=== 탐지된 객체 목록 ===\n"
    if len(boxes) == 0:
        detected_info += "탐지된 객체가 없습니다."
    else:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = yolo_model.names[cls_id]
            detected_info += f"- {class_name}: {conf*100:.1f}%\n"
            
    return annotated_frame, detected_info

# 3. Gradio 인터페이스 생성 및 실행 함수
def launch_app(custom_model=None, share=True):
    global yolo_model
    # 외부(Colab 노트북)에서 이미 학습/로드한 모델이 있다면 교체
    if custom_model is not None:
        yolo_model = custom_model

    demo = gr.Interface(
        fn=detect_objects_gradio,
        inputs=gr.Image(type="pil", label="이미지 업로드"),
        outputs=[
            gr.Image(type="numpy", label="객체 탐지 결과"),
            gr.Textbox(label="탐지 정보", lines=5)
        ],
        title="🐕🐈 YOLOv8 실시간 객체 탐지 데모",
        description="이미지를 드래그 앤 드롭하거나 클릭하여 업로드하면, YOLOv8 모델이 실시간으로 객체를 탐지하여 결과를 보여줍니다."
    )
    
    demo.launch(share=share)

if __name__ == "__main__":
    launch_app(share=True)
