# Projeto RPA - Emissão de Notas Fiscais no Site da Prefeitura de Patos-PB

Este projeto automatiza o processo de emissão de notas fiscais no site da prefeitura de Patos-PB, utilizando uma base de dados fornecida em formato Excel. A automação foi desenvolvida utilizando o Selenium para interagir com o site e o Pandas para manipulação dos dados fornecidos. O projeto foi realizado para a empresa **Infortech**, onde informações sensíveis, como credenciais e dados de clientes, foram tratadas com cuidado.

## Tecnologias Utilizadas

- **Pandas**
- **Selenium**
- **Orientação a Objetos**

## Fluxo do Processo

1. **Leitura da base de dados**: A planilha Excel contendo as informações dos clientes e dos serviços prestados é lida.
2. **Login no portal**: A automação realiza o login no portal da prefeitura de Patos-PB utilizando credenciais protegidas.
3. **Preenchimento dos dados**: Cada linha da planilha é processada, e os campos necessários no site são preenchidos automaticamente.
4. **Emissão da nota fiscal**: Após o preenchimento dos dados, o processo é concluído com a emissão da nota fiscal.
5. **Verificação e log**: O sistema verifica se a nota foi emitida com sucesso e mantém um log dos eventos para facilitar o acompanhamento.

## Segurança e Privacidade

Algumas partes deste projeto foram omitidas ou modificadas para garantir a privacidade dos dados da **Infortech** e de seus clientes. Entre as informações protegidas, estão:

- **Credenciais de login**: As senhas e logins usados para acessar o portal da prefeitura foram movidos para variáveis privadas e não estão expostas no código público.
- **Dados dos clientes**: A base de dados real contendo as informações dos clientes e serviços não será disponibilizada aqui.
