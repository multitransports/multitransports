#!/bin/bash

echo "[[[PASSWORD SUDO DISABLE]]]"
sed -i "s/%sudo ALL=(ALL) ALL/%admin ALL=(ALL) NOPASSWD:ALL/" /etc/ssh/sshd_config
#Désactive le mot de passe sudo le temps de l'installation

#La commande echo permet d'afficher un commentaire
#La commande timedateectl permet de changer de fuseau horaire au niveau du serveur
echo "[[[Time zone change for Paris]]]"
timedatectl set-timezone Europe/Paris
echo
echo "[[[UBUNTU POST-INSTALL SCRIPT]]]"
echo "[[[Updating APT...]]]"
apt-get -y update
apt-get -y upgrade
#La commande sudo permet d'exécuter la commande en super-utilisateur
#La commande apt-get permet d'effectuer l'installation et la désinstallation de paquets en provenance d'un dépôt APT.
#Update permet de mettre à jour la commande placer juste avant

echo "[[[Password desactivation]]]"
 sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
#Désactive l'authentification ssh par mot de passe
 /etc/init.d/ssh restart
#Relance le servcie ssh pour appliquer les modifications
echo "[[[Installing base packages]]]"
 apt-get install --yes git git-extras build-essential python3-pip
 pip3 install -r multitransports/requirements.txt
# sudo myvenv/bin/pip install --upgrade pip 
# sudo myvenv/bin/pip install flask
#install permet d'installer les applications ou paquets demandés juste après
#--yes permet de répondre yes si des questions sont demandées

echo "[[[PASSWORD SUDO ENABLE]]]"
sed -i "s/%sudo ALL=(ALL) NOPASSWD:ALL/%admin ALL=(ALL) ALL/" /etc/ssh/sshd_config
#Remet le mot de passe sudo à la fin de l'installation


python3 /home/stephanie/multitransports/app.py &
python3 /home/stephanie/multitransports/serveur_http.py