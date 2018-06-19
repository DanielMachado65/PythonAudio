# PythonAudio

[Apostila para Estudo](https://realpython.com/python-speech-recognition/)

> Programa que consegue ler a voz. Usando a linguagem Python.
#### Como instalar:

```shell
# você deverá fazer a instalação ou o upgrade
pip install --upgrade PyAudio
pip install --upgrade SpeechRecognition
pip install --upgrade pocketphink

# Para instalar o TensorFlow
pip install --upgrade tensorflow
```

#### Bibliotecas usadas:
  * `SpeechRecognition()` _(local)_ - basicamente é uma tradutora dos dados, para fazer a comunicação. Ela basicamente pede para a API uma requisição.
  ```python
  # requisição que ele trata.
    try:
      from urllib import urlencode
  except ImportError:
      from urllib.parse import urlencode

  language = "utf-8"
  key = "AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
  url = "http://www.google.com/speech-api/v2/recognize?{}".format(
      urlencode({
          "client": "chromium",
          "lang": language,
          "key": key
      })
  )
  ```

  * `Google-Speech_API` _(API)_ - API do google para fazer a tradução dos dados, do audio, enviado como **date** para **Json**, __sim__ ele voltará como um json de cada frase ou palavra.
  ```python
    try:
      response = urlopen(request, timeout=self.operation_timeout)
  except Exception as e:
      raise RequestError('Recognition request failed: {}'.format(e.reason))

  response_text = response.read().decode("UTF-8")

  # pular os espaços em brancos
  actual_result = []
  for line in response_text.split('\n'):
      if not line: continue
      result = json.loads(line)['result']
      if len(result) != 0:
          actual_result = result[0]
          break
      # retornar os resultados
      if show_all:
          return actual_result

  ```


* ### !links importantes:
  * link para [visualização rápida](https://www.youtube.com/watch?v=qpYpwf06SO8)
  * Como instalar [Speech Recognition ](https://www.youtube.com/watch?v=KNHlZ_MlnfU)
  * Como preparar ambiente para o desenvolvimento com [PocketSphink](https://www.youtube.com/watch?v=BNkn0EbuVKU&list=PL39zyvnHdXh-BAVY3Dz_DCG_RRucJz-uM&index=16)
  * Documentação oficial: [SpeechRecognition ](https://pypi.org/project/SpeechRecognition/) 3.8.1
