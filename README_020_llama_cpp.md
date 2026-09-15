https://github.com/abetlen/llama-cpp-python
https://llama-cpp-python.readthedocs.io/en/latest/

xcode-select --install 
sudo xcode-select --switch /Library/Developer/CommandLineTools

python3 -m pip install --upgrade pip

python3 -m venv local_venv
source local_venv/bin/activate

pip3 install ninja
CMAKE_ARGS="-DGGML_METAL=on" pip3 install llama-cpp-python --no-cache-dir --force-reinstall

deactivate
