FROM python:3.12-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk-3-dev \
    libxcb-xinerama0 libxcb-randr0 libxcb-shape0 libxcb-xfixes0 \
    libxrender1 libxext6 libx11-xcb1 \
    libegl1-mesa libgl1-mesa-glx x11-xserver-utils

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .