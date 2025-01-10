
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
