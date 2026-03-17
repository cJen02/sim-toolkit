FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV MUJOCO_GL=egl
ENV PYOPENGL_PLATFORM=egl

RUN apt-get update && apt-get install -y \
    python3.10 python3-pip \
    git wget libgl1-mesa-dev libglew-dev \
    libosmesa6-dev libglfw3 libglfw3-dev \
    libgles2-mesa-dev patchelf ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install mujoco myosuite

RUN pip install stable-baselines3[extra] gymnasium tensorboard

RUN pip install torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu121

RUN pip install jupyter ipykernel

WORKDIR /workspace
CMD ["/bin/bash"]