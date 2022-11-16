# Projeto Gestão de Estagiários
## Autor: Lucas Carvalho Gomes Santiago
## Email: lucsallk@hotmail.com

--- 

Segue o passo a passo de como inicializar a aplicação. 

### Frontend
Abra a pasta client no terminal e utilize dos comandos abaixo para instalar e rodar a aplicação.
```
npm install
npm run dev
```

### Backend
Abra a pasta restapi no terminal e utilize dos comandos abaixo para instalar e rodar a API.

```
py -m venv venv
venv\Scripts\activate

```

> O comando presente na segunda linha pode variar dependendo do sistema operacional
> - On Unix or MacOS, using the bash shell: `source /path/to/venv/- bin activate`
> - On Unix or MacOS, using the csh shell: `source /path/to/venv/-  bin/activate.csh`
> - On Unix or MacOS, using the fish shell: `source /path/to/venv/bin/activate.fish`
> - On Windows using the Command Prompt: - `path\to\venv\Scripts\activate.bat`
On Windows using PowerShell: `path\to\venv\Scripts\Activate.ps1`

Prosseguindo

```
pip install -r requirements
py manage.py runserver
```
Nesse momento a aplicação avisará há uma série de _migrations_ não aplicadas, e que a aplicação não rodará da maneira correta até serem aplicadas. Agora iremos parar a aplicação no terminal e digitaremos o comando a baixo.

```
manage.py migrate
```