### app 
## Instalações
 *npm install*
 *npm install expo*
 *npm install axios*
 - se houver erros
 expo doctor --fix-dependencies
 
 por padrão a API FLASK EXECUTA NA POR 5000
 - APÓS BAIXAR O NGROK USAR:
 **ngrok http 5000**
 - após rodar copiar o link e colar no constructor da tela home.js
- colar no stado *url*
 
 - se já isntaldo axios usá-lo para buscar os dados
  - ir para HOme.js 
  1. ->> escrever função getPlanets para obter os dados da url
  2. ->> Chamar a função em componentDidMount
  3. ->> Renderizar os items na flatlist
    - props: KeyExtractor, data, rederItem

  # ATUALIZANDO PACKGES
   - *npm i -g expo-cli*
    - para rodar: npx expo start
  - ou usar o *npm run start*

  ➡️ Upgrading your app
Here’s how to upgrade your app to Expo SDK 49 from 48:

Update to the latest version of EAS CLI (if you use it):
**npm i -g eas-cli.**
Install the new version of the Expo package:
**npm install expo@^49.0.0 or yarn add expo@^49.0.0**
Upgrade all dependencies to match SDK 49:
**npx expo install --fix**
**npm install --save fix**
    - npm audit fix --force
    - npx expo install --fix

*Utilizando porps type: *
-npm i deprecated-react-native-prop-types@2.2.0
