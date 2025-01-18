brew install git-lfs
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/hexgrad/Kokoro-82M

cd Kokoro-82M
brew install espeak-ng
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip install phonemizer transformers scipy munch soundfile