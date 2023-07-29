import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer

# https://github.com/whitphx/streamlit-webrtc


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # ここに、カメラ画像 img に対する処理を記述する
    # 【サンプル】バウンディングボックスとラベルを表示する
    BOXES = [(10, 10, 100, 100), (50, 60, 150, 150)]
    LABELS = ["Object A", "Object B"]
    COLORS = [(15, 15, 255), (0, 128, 0)]

    for i in range(2):
        xmin, ymin, xmax, ymax = BOXES[i]
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), COLORS[i], 2)
        x = xmin + 5 if xmin + 5 < xmax - 5 else xmin
        y = ymin - 10 if ymin - 10 > 15 else ymin + 15
        cv2.putText(
            img, LABELS[i], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[i], 2
        )
    # 処理ここまで

    return av.VideoFrame.from_ndarray(img, format="bgr24")


def main():
    st.title("Real-time video streaming")
    st.caption("リアルタイムのカメラ画像を表示します")

    webrtc_streamer(
        key="streamer",
        video_frame_callback=video_frame_callback,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    )


if __name__ == "__main__":
    main()
