# SVida - Sistema de Coleta de Sinais Vitais 📋❤️

Este projeto representa a **primeira versão** do sistema **SVida**, desenvolvido como parte de um trabalho acadêmico da faculdade. Foi também a **minha primeira experiência prática utilizando o framework Django**, junto com HTML, CSS e JavaScript.
O objetivo da aplicação é fornecer uma solução web simples para auxiliar estudantes de cursos técnicos de enfermagem na **coleta e registro de sinais vitais (SSVV) de pacientes**.

**📂 Estrutura do Projeto**  
O repositório segue a seguinte estrutura de diretórios:
bash  
SVida-main/  
├── SVida-main/  
│ └── svida/  
│ ├── manage.py  
│ ├── svida/ # Configurações principais do Django (settings.py, urls.py, etc)  
│ └── ... # Apps Django (ex: accounts, patients, etc)  
└── README.md # Este arquivo 
  
**✅ Requisitos**  
Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:
- Python 3.12 ou superior
- Django 4.x
- SQLite3 (já incluso com Django por padrão)
- Visual Studio Code (recomendado)

Dica: Use um ambiente virtual para isolar as dependências do projeto.


**🚀 Passos para Executar o Projeto Localmente**
1. Abrir o terminal e navegar até o diretório do projeto:
cd C:\Users\user\Downloads\SVida-main\SVida-main\svida ------------------------ Adicionar o caminho correto em que o arquivo foi descompactado.
2. Rodar o servidor de desenvolvimento do Django:
*//python manage.py runserver//*


**🌐 Acessando a Aplicação**  
Após executar o comando acima, o servidor estará rodando localmente no seguinte endereço: **http://127.0.0.1:8000**


**⚠️ Observação Importante:**  
Atualmente, não há uma página inicial (/) configurada. Ao acessar a URL raiz, você verá um erro 404 (Page Not Found).
Para iniciar a navegação pela aplicação, acesse diretamente o endpoint de login: **http://127.0.0.1:8000/login**

**📌 Endpoints Disponíveis**  
/admin/	------------------ Painel administrativo do Django  
/register/	------------------ Tela de registro de novos usuários  
/login/	------------------ Tela de login  
/logout/	------------------ Logout do usuário  
/add_patient/	------------------ Cadastro de novos pacientes  
/add_vital_sign/<int:patient_id>/	------------------ Adicionar sinais vitais a um paciente específico  
/vital_sign_history/<int:patient_id>/	------------------ Histórico de sinais vitais do paciente  
/menu/	------------------ Menu principal da aplicação  
/success/	------------------ Página de sucesso (exibição pós ação bem-sucedida)  
/save_edit_patient/<int:patient_id>/	------------------ Salvar edição dos dados de um paciente  
/patient/edit/<int:patient_id>/	------------------ Formulário de edição de um paciente  
/patients/	------------------ Listagem de todos os pacientes  
/select_patient_for_vital_signs/	------------------ Seleção de paciente para coleta de sinais vitais  
/delete_patient/<int:patient_id>/	------------------ Exclusão de um paciente  
/edit_patient/<int:patient_id>/	------------------ Edição detalhada de um paciente  


**🛠️ Próximas Melhorias**  
* Criar uma página inicial (/) para redirecionamento automático para o login ou para exibir um menu de navegação.
* Melhorar o design das páginas com Bootstrap.
* Implementar autenticação por níveis de usuário (ex: administrador, enfermeiro, aluno).
* Adicionar testes unitários.

**📃 Licença**  
Este projeto é apenas para fins educacionais.
