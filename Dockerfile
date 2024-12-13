FROM python:3.9-slim    

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    ffmpeg \
    libfontconfig1 \
    libxcb1 \
    python3-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer1.0-dev \
    libpng-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \  
    libtiff-dev \
    libwebp-dev \
    libgtk-3-dev \
    libgtk2.0-dev \
    libv4l-dev \
    v4l-utils \
    python3-pip \
    python3-setuptools \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Update pip and install packages
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create directories for mounting
RUN mkdir -p /app/data/images
RUN mkdir -p /app/data/videos

EXPOSE 8000

CMD ["python", "source/main.py"]