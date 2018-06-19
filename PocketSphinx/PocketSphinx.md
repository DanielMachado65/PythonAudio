# PocketSphink

### Como instalar:

```shell
#!/usr/bin/env bash
sudo apt-get install git
sudo apt-get install automake
sudo apt-get install libtool
sudo apt-get install bison
sudo apt-get install python-dev
sudo apt-get install swig
sudo apt-get install make
sudo apt-get install pkg-config

# começo do git
git clone https://github.com/cmusphinx/sphinxbase.git
cd sphinxbase
./autogen.sh
make
sudo make install
cd ..


git clone https://github.com/cmusphinx/pocketsphinx.git
cd pocketsphinx
./autogen.sh
make
sudo make install
cd ..

git clone https://github.com/cmusphinx/sphinxtrain.git
cd sphinxtrain
./autogen.sh
make
sudo make install
cd ..
```

o ambiente de desenvolvimento, ainda não está completo. Definir outros compontentes. Provável que você vai querer utilizar o modelo acustico;
* Python3.7 = modelo acustico.
