import streamlit as st
import tempfile
from utils.physics import calculate_physics

st.title("Pendelanalyse")

video = st.file_uploader("MP4 hochladen", type=["mp4"])

length = st.number_input("Pendellänge (m)", value=1.0)

if video:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video.read())

    st.video(tfile.name)

    if st.button("Analysieren"):
        T, f, g = calculate_physics(tfile.name, length)

        st.write("Periodendauer:", round(T, 2), "s")
        st.write("Frequenz:", round(f, 2), "Hz")
        st.write("Erdbeschleunigung:", round(g, 2), "m/s²")
