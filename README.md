# 🗣️ Open AI - TTS Recognition 
Talk with OpenAI using Speech Recognition.

<img src="https://i.ibb.co/0cRkZ3Y/Screenshot-2022-12-07-002152.png" style="width: 70%" alt="Alt text" title="Optional title">

## Description
* This software uses OpenAI Model '**text-davinci-003**'.
* It speaks back the output using your system voices.
* You must **provide your own api-key** when prompt.
* Response length is limited to 2000 words.
* For some reason his name is John.

## Usage
* Download last version from [releases](https://github.com/NxRoot/OpenAI-TTS-Recognition/releases/tag/Release).

## How to Build from Source

* Create a Virtual Environment
```js
py -m venv venv
// or
python -m venv venv
```
* Activate the Virtual Environment
```
./venv/Scripts/activate
```

* Install required libraries
```
pip install -r requirements.txt
```
* Build into Executable
```
pyinstaller --name OpenAI --noconsole --onefile main.py --icon icon.ico
```
