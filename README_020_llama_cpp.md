<https://github.com/abetlen/llama-cpp-python>
<https://llama-cpp-python.readthedocs.io/en/latest/>

for Mac
```
xcode-select --install 
sudo xcode-select --switch /Library/Developer/CommandLineTools
```

it's been a while
```
python3 -m pip install --upgrade pip
```

venv:
```
python3 -m venv local_venv
source local_venv/bin/activate
```

```
pip3 install ninja
CMAKE_ARGS="-DGGML_METAL=on" pip3 install llama-cpp-python --no-cache-dir --force-reinstall
```

and finally
```
deactivate
```


