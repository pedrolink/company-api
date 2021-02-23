Site da api: https://api-test-company-hero.herokuapp.com/

Para utilizar o envio de formulário será necessário um Token aplicado para um usuário específico criado na base de dados. Isso fornece segurança a API para que outras pessoas não acessem a informação direta.

Key = Authorization
Token = Token 0fc48e132c1ce108b87edcf92de0affb93240327

Usuário master criado para o envio de formulário na API.
Obs: Este usuário não tem acesso a base de dados, pois não inclui ele para acesso direto ao /admin

Usuário: company_api
Senha: company@2021

Para acessar o /admin com usuário master vou deixar disponibilizado também o usuário:
https://api-test-company-hero.herokuapp.com/admin/
Usuário: admin
Senha: admin@123

ENVIOS DE FORMULÁRIOS:

LEMBRE-SE: Passar o token de autenticação para estar fazendo a busca no formulário, caso ao contrátio, você não terá permissão.

#Listar todas as informações das empresas
https://api-test-company-hero.herokuapp.com/empresas/

#Listar todas informações dos usuários
https://api-test-company-hero.herokuapp.com/usuarios/

#Criei uma tabela a mais no banco de dados para fazer um ligamento de informações, a busca pelo link de usuários já conseguimos todas as informações, acabei criando para uma visualização mais ampla e por vinculos
https://api-test-company-hero.herokuapp.com/plataforma/

#Listar usuário por username e trazer as empresas que ele pertence
https://api-test-company-hero.herokuapp.com/usuarios/pedro_link 

#ou caso queira selecionar um usuário específico: 
https://api-test-company-hero.herokuapp.com/usuarios/nome_usuário

#Também podemos fazer buscas nos filtros da URL, como por exemplo:
https://api-test-company-hero.herokuapp.com/usuarios/?id=1 #Busca o usuário de id = 1
https://api-test-company-hero.herokuapp.com/empresas/?nome=Company%20Hero #Busca a empresa com o nome "Company Hero"

#Trazer todas as informações da empresa e seus usuários:
https://api-test-company-hero.herokuapp.com/plataforma/?id=&funcionario=&id_empresas=1&id_usuario= #Busca informações da empresa específica, por exemplo aqui buscamos os funcionarios da Company Hero.

https://api-test-company-hero.herokuapp.com/plataforma/?id=&funcionario=&id_empresas=3&id_usuario= #Aqui teríamos da empresa Future DevStack, conforme os id's cadastrados no banco de dados.

Seria isso! =D

