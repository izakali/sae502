# Projet SAÉ 5.02 - Automatisation NetBox

## Description
Déploiement automatisé d'une infrastructure DCIM (NetBox) entièrement conteneurisée via Ansible.
Le projet inclut le provisioning automatique des données initiales (Sites, Préfixes).

## Architecture
* **Hôte** : Docker + Docker Compose
* **Conteneurs** : NetBox, Postgres, Redis, Nginx, Worker.
* **Orchestration** : Ansible

## Prérequis
* Une machine cible Ubuntu 22.04/24.04
* Accès SSH avec clé publique configurée
* Utilisateur avec droits sudo

## Installation
1. Configurer l'inventaire dans `inventory/hosts.ini`
2. Lancer le playbook :
   ```bash
   ansible-playbook site.yml -K
