## **Présentation du projet plante connectée :**

### Mise en place de l'Arduino

Pour faire fonctionner ce projet, il vous faudra télécharger les fichiers suivant :
- Arduino
- Python

De plus il faudra pouvoir avoir un [compte Arduino](https://id.arduino.cc/) et accès à internet.

Une fois un compte crée il vous faut copier coller le [code Arduino](https://github.com/coolofdead/Plante-Connectee/blob/master/Arduino/Capteur/Capteur.ino) et le coller sur le l'[IDE Web Arduino](https://create.arduino.cc/editor).

Changer les valeurs suivantes :
- **define SSID** => Votre nom de wifi
- **define SSID_PASSWORD** => Votre mot de passe de wifi

Une fois cela fait, choisissez dans les boards l'**Arduino Uno Wifi Rev2** :
![Arduino Board Select](/Images/Arduino_Board.png)

Il ne vous reste plus qu'à téléverser le tout dans l'Arduino.


### Mise en place du python

La partie python est très simple, vous n'avez qu'à lancer le programme nommé **main.py**.

Vous pouvez utilisez pour vous connecter les identifiants suivants :
- **id** : coolofdead
- **password** : password

Ensuite l'application vous guidera pas à pas.
