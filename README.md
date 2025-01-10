
# Jetson Nano Environment Setup

This guide provides a step-by-step process for setting up a Jetson Nano environment with essential tools, including CUDA, cuDNN, TensorRT, Python, and OpenCV.

---

## Installed by Jetpack SDK

- **CUDA Toolkit**: 10.2
- **cuDNN**: 8.2.1
- **TensorRT**: 8.2.1
- **Environment Variables**: 

```bash
export PATH=$PATH:/usr/src/tensorrt/bin:/usr/local/cuda/bin
```
---

## Install DeepStream

### Step 1: Check Compatible DeepStream Version

```bash
sudo apt-cache search deepstream
```

### Step 2: Install DeepStream

```bash
sudo apt install deepstream-6.0
```

---

## Install Python

### Step 1: Install Dependencies

```bash
sudo apt-get update
sudo apt-get install -y build-essential libffi-dev libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libgdbm-dev libnss3-dev liblzma-dev
```

### Step 2: Download and Extract Python Source Code

Download Python 3.9.17 source code from the official Python website:

```bash
wget https://www.python.org/ftp/python/3.9.17/Python-3.9.17.tgz
tar -xf Python-3.9.17.tgz
cd Python-3.9.17
```

### Step 3: Configure the Build for Optimization

```bash
./configure --enable-optimizations
```

### Step 4: Build and Install

```bash
make -j$(nproc)
sudo make altinstall
```

---
### Step 5: Install Virtual Python Environment
```bash
python3.9 -m venv workenv                                                
source workenv/bin/activate
```

## Install OpenCV

### Step 1: Query GPU Compute Capability

Run the following command to check the GPU compute capability, required for `CUDA_ARCH_BIN`:

```bash
nvidia-smi --query-gpu=compute_cap --format=csv
```

### Step 2: Install Dependencies

```bash
sudo apt-get install -y build-essential cmake git unzip pkg-config zlib1g-dev \
libjpeg-dev libjpeg8-dev libjpeg-turbo8-dev libpng-dev libtiff-dev libglew-dev \
libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libgtk-3-dev "libcanberra-gtk*" \
python-dev python-numpy python-pip python3-dev python3-numpy python3-pip \
libxvidcore-dev libx264-dev libtbb2 libtbb-dev libdc1394-22-dev libxine2-dev \
gstreamer1.0-tools libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev \
libv4l-dev v4l-utils v4l2ucp qv4l2 libtesseract-dev libpostproc-dev libavresample-dev \
libvorbis-dev libfaac-dev libmp3lame-dev libtheora-dev libopencore-amrnb-dev \
libopencore-amrwb-dev libopenblas-dev libatlas-base-dev libblas-dev \
liblapack-dev liblapacke-dev libeigen3-dev gfortran libhdf5-dev libprotobuf-dev \
protobuf-compiler libgoogle-glog-dev libgflags-dev -y
```

### Step 3: Clone OpenCV Repositories

```bash
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

### Step 4: Checkout OpenCV Version 4.10.0

```bash
cd opencv_contrib
git checkout 4.9.0
cd ../opencv
git checkout 4.9.0
mkdir build && cd build
```

### Step 5: Configure and Build OpenCV

Run the following `cmake` command with required flags:

```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
  -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
  -D WITH_OPENCL=OFF \
  -D CUDA_ARCH_BIN=${ARCH} \
  -D CUDA_ARCH_PTX=${PTX} \
  -D WITH_CUDA=ON \
  -D WITH_CUDNN=ON \
  -D WITH_CUBLAS=ON \
  -D ENABLE_FAST_MATH=ON \
  -D CUDA_FAST_MATH=ON \
  -D OPENCV_DNN_CUDA=ON \
  -D ENABLE_NEON=ON \
  -D WITH_QT=OFF \
  -D WITH_OPENMP=ON \
  -D BUILD_TIFF=ON \
  -D WITH_FFMPEG=ON \
  -D WITH_GSTREAMER=ON \
  -D WITH_TBB=ON \
  -D BUILD_TBB=ON \
  -D BUILD_TESTS=OFF \
  -D WITH_EIGEN=ON \
  -D WITH_V4L=ON \
  -D WITH_LIBV4L=ON \
  -D WITH_PROTOBUF=ON \
  -D OPENCV_ENABLE_NONFREE=ON \
  -D INSTALL_C_EXAMPLES=OFF \
  -D INSTALL_PYTHON_EXAMPLES=OFF \
  -D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
  -D OPENCV_GENERATE_PKGCONFIG=ON \
  -D BUILD_EXAMPLES=OFF \
  -D CMAKE_CXX_FLAGS="-march=native -mtune=native" \
  -D CMAKE_C_FLAGS="-march=native -mtune=native" ..
```

Compile and install:

```bash
sudo make install -j$(nproc)
sudo ldconfig
```
Check OpenCV:
```bash
ls /usr/lib/aarch64-linux-gnu/ | grep opencv
```
---
