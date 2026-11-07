import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from skimage.color import rgb2hsv

st.set_page_config(page_title="Ekstraksi Warna", page_icon="🎨", layout="centered")
st.title("Aplikasi Ekstraksi Fitur Warna Citra")
st.write("Aplikasi sederhana untuk menganalisis warna dominan pada gambar menggunakan ruang warna HSV.")

file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png", "bmp"])

if file:
    image = Image.open(file).convert("RGB")
    rgb = np.asarray(image)
    hsv = rgb2hsv(rgb / 255.0)

    # Ringkasan fitur warna
    mean_h = float(np.mean(hsv[:, :, 0]))
    mean_s = float(np.mean(hsv[:, :, 1]))
    mean_v = float(np.mean(hsv[:, :, 2]))
    std_h = float(np.std(hsv[:, :, 0]))
    std_s = float(np.std(hsv[:, :, 1]))
    std_v = float(np.std(hsv[:, :, 2]))

    # Warna dominan sederhana: rata-rata kanal RGB
    mean_rgb = np.mean(rgb.reshape(-1, 3), axis=0).astype(int)
    swatch = np.zeros((100, 300, 3), dtype=np.uint8)
    swatch[:, :] = mean_rgb

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gambar input")
        st.image(image, use_container_width=True)
    with col2:
        st.subheader("Warna rata-rata RGB")
        st.image(swatch, caption=f"RGB = {tuple(mean_rgb)}", use_container_width=True)

    st.subheader("Histogram warna RGB")
    fig, ax = plt.subplots()
    for idx, channel in enumerate(["Red", "Green", "Blue"]):
        ax.hist(rgb[:, :, idx].ravel(), bins=64, range=(0, 255),
                histtype="step", label=channel)
    ax.set_xlabel("Intensitas (0–255)")
    ax.set_ylabel("Frekuensi piksel")
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

    results = pd.DataFrame([
        ["Mean Hue", mean_h], ["Mean Saturation", mean_s], ["Mean Value", mean_v],
        ["Std Hue", std_h], ["Std Saturation", std_s], ["Std Value", std_v],
        ["Mean Red", int(mean_rgb[0])], ["Mean Green", int(mean_rgb[1])],
        ["Mean Blue", int(mean_rgb[2])]
    ], columns=["Fitur", "Nilai"])

    st.subheader("Hasil ekstraksi fitur")
    st.dataframe(results, hide_index=True, use_container_width=True)

    csv = results.to_csv(index=False).encode("utf-8")
    st.download_button("Unduh hasil CSV", csv, "hasil_ekstraksi_warna.csv", "text/csv")
else:
    st.info("Unggah gambar untuk memulai analisis.")
