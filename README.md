# G26_Introducci-_a_Github_Actions_lab5

# Software Engineering Pipeline

Aquest projecte és una petita aplicació de calculadora utilitzada per aprendre a configurar fluxos de treball àgils i integració contínua (CI) mitjançant GitHub Actions.

## Preguntes de Reflexió (Laboratori 5)

### 1. Per què és millor tenir un job de lint separat del job de test?
Separar-los permet estalviar temps i recursos. El "lint" (estil del codi) és molt ràpid d'executar. Si el codi no compleix les regles bàsiques (com PEP 8), és millor que la pipeline falli immediatament abans d'aixecar entorns més pesats per fer els testos unitaris.

### 2. Què passa si el job lint falla? Per què no s'executa el job test?
Si el job `lint` falla, la pipeline s'atura. El job `test` no s'executa perquè hem configurat una dependència (`needs: lint`). Això actua com un "Quality Gate": si el codi no està ben escrit visualment o té errors sintàctics detectats pel linter, no es considera apte per ser provat lògicament.

### 3. Com connecta el concepte de quality gate amb els principis de XP (Extreme Programming) i Agile?
El "quality gate" garanteix un feedback ràpid. En Agile i XP, volem detectar errors el més aviat possible (Shift-Left Testing) per mantenir el codi sempre en un estat que es pugui desplegar.

### 4. Quina diferència hi ha entre CI (Integració Contínua) i CD (Desplegament Continu)?
- **CI:** Automatitza la integració de codi de diversos col·laboradors i el valida amb tests.
- **CD:** Automatitza el lliurament o desplegament d'aquest codi validat als servidors de producció perquè l'usuari final el pugui utilitzar.

### 5. Quins problemes sorgirien si un equip de 10 desenvolupadors fes push directament a main sense branques ni pipeline CI?
Hi hauria conflictes de codi constants, la branca principal es trencaria sovint (codi que no funciona) i seria impossible mantenir una versió estable del producte per ensenyar al client.

### 6. Per què és més barat detectar un error a l'stage de lint o test que després de fer merge a main?
Perquè el desenvolupador encara recorda què ha programat i ho pot arreglar en minuts. Un cop fet el merge, l'error pot afectar altres companys o arribar a producció, on el cost de correcció (temps d'aturada, mala imatge, hores de depuració) és molt més alt.

### 7. Com canviaria la pipeline si l'equip afegís una etapa de desplegament automàtic?
S'afegiria un nou job al final anomenat `deploy`, que dependria de l'èxit del job `test`. Normalment, aquest job només s'executaria quan es fa un merge a la branca `main`.
