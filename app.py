import av
import cv2
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer

from turn import get_ice_servers

# https://github.com/whitphx/streamlit-webrtc


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # ここに、カメラ画像 img に対する処理を記述する
    # 【サンプル】バウンディングボックスとラベルを表示する
    BOXES = [(100, 100, 250, 250), (20, 20, 120, 120)]
    LABELS = ["Object A", "Object B"]
    COLORS = [(15, 15, 255), (0, 128, 0)]

    for i in range(2):
        xmin, ymin, xmax, ymax = BOXES[i]
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), COLORS[i], 2)
        x = xmin + 5 if xmin + 5 < xmax - 5 else xmin
        y = ymin - 10 if ymin - 10 > 15 else ymin + 15
        cv2.putText(img, LABELS[i], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[i], 2)
    # 処理ここまで

    return av.VideoFrame.from_ndarray(img, format="bgr24")


st.title("Real-time video streaming")
st.caption("リアルタイムのカメラ画像を表示します")

webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": get_ice_servers(),
        "iceTransportPolicy": "relay",
    },
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
