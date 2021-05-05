# Framworm
Framworm est un vers informatique éducaatif et qui se veut modulable.

## Architecture
Voici l'architecture macroscopique de notre vers :
```mermaid
graph
    subgraph WORM
        subgraph Boucle d'éxecution
            DIS["1 - Dissimulations"]
            ATT["2 - Attaques"]
            ACT["3 - Actions diverses"]
            DIS ==> ATT ==> ACT ==> |"Rebouclage"| DIS
        end
        subgraph  
            LOGDIS[(Pile de logs inhérents<br>à dissimulations)]
            LOGATT[(Pile de logs inhérents<br>à attaques)]
            LOGACT[(Pile de logs inhérents<br>à actions diverses)]
        end
        DIS -.-> |"Stockage des logs"| LOGDIS
        ATT -.-> |"Stockage des logs"| LOGATT
        ACT -.-> |"Stockage des logs"| LOGACT
    end
```
Les composants *Dissimulations*, *Attaques* et *Actions diverses* sont des modules codés par l'utilisateur.

