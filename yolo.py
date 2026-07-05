import argparse
from pathlib import Path
 
 
def main():
    parser = argparse.ArgumentParser(description="YOLO 이미지 분류 모델 학습")
    parser.add_argument("--data", type=str, required=True,
                         help="dataset 폴더 경로 (내부에 train/, val/ 폴더가 있어야 함)")
    parser.add_argument("--model", type=str, default="yolo11n-cls.pt",
                         help="기반 사전학습 모델 (예: yolo11n-cls.pt, yolo11s-cls.pt)")
    parser.add_argument("--epochs", type=int, default=30, help="학습 반복 횟수")
    parser.add_argument("--imgsz", type=int, default=224, help="입력 이미지 크기 (기본 224x224)")
    parser.add_argument("--batch", type=int, default=16, help="배치 크기")
    args = parser.parse_args()
 
    data_path = Path(args.data)
    if not (data_path / "train").exists():
        raise FileNotFoundError(
            f"'{data_path}/train' 폴더를 찾을 수 없습니다. "
            "위 안내대로 dataset/train/<클래스명>/이미지... 구조로 만들어주세요."
        )
 
    from ultralytics import YOLO
 
    print(f"📦 기반 모델 '{args.model}' 로딩 중... (최초 실행 시 자동 다운로드됩니다)")
    model = YOLO(args.model)
 
    print(f"🚀 학습 시작: data={args.data}, epochs={args.epochs}, imgsz={args.imgsz}")
    results = model.train(
        data=str(data_path),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
    )
 
    print("\n✅ 학습 완료!")
    print("아래 경로의 best.pt 파일을 Streamlit 앱(app_yolo_classifier.py)에서 불러와 사용하세요:")
    print("   runs/classify/train/weights/best.pt")
 
    # 검증 데이터로 정확도 확인
    metrics = model.val()
    print(f"\n📊 검증 정확도 — Top-1: {metrics.top1:.3f} / Top-5: {metrics.top5:.3f}")
 
 
if __name__ == "__main__":
    main()