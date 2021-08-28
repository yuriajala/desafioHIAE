Este repositório é privado com o intuito de participar da seleção para vaga de Desenvolvedor e Engenheiro de Dados do HIAE.
Trata-se de uma página para upload de um arquivo DICOM (`.dcm`) e exibição de seu cabeçalho.

A página é um arquivo HTML (`templates/index.html`) e o código para tratamento do arquivo é em Python (`app.py`) com Flask como servidor local e pandas para exibição do cabeçalho.

Como utilizar:

Baixe todos os arquivos (ou zip) e monte com docker no powershell

    docker build -t dicomreader . 
    
Depois de montado o conteiner (pode demorar alguns minutos), entre a seguinte linha no powershell

    docker run -d -p 80:80 dicomreader
   
Em seguida, digite `localhost` ou `http://127.0.0.1` na barra de endereços do navegador para acessar a página local. 
