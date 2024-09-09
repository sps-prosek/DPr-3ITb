# Úvod do Gitu

Git je **distribuovaný systém pro správu verzí** (VCS), který umožňuje sledovat změny v souborech projektu v průběhu času. Tento systém zaznamenává změny a umožňuje návrat k jakékoliv předchozí verzi souborů. Je skvělým nástrojem pro **spolupráci** - každý vývojář může mít vlastní verzi projektu na svém počítači a později sloučit své změny s hlavní verzí projektu.

Git je oblíbený nástroj pro řízení projektů a spolupráci mezi jednotlivci i týmy. Znalost práce s Git je v současnosti nepostradatelnou dovedností pro každého vývojáře a je skvělým přírůstkem do životopisu!

> :information_source: Více na oficiální stránce Gitu: [https://git-scm.com/](https://git-scm.com/)

# Instalace a nastavení

Git se nejčastěji používá přes příkazový řádek. Nejdříve si ověřte, že máte Git nainstalovaný na vašem počítači.

> :information_source: Git můžete stáhnout zde: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Stáhněte si verzi pro váš operační systém a postupujte podle průvodce instalací.

Po instalaci spusťte terminál a zadejte příkaz:

```bash
git --version
```

Zobrazí se vám verze Gitu nainstalovaná na vašem počítači.

### Nastavení jména a e-mailu

Zadejte v terminálu následující příkazy:

```bash
git config --global user.name "Vaše Jméno"
git config --global user.email "vas@email.com"
```

Nahraďte hodnoty svým jménem a e-mailem. Tyto údaje se používají k identifikaci v historii změn, nikoli pro přihlášení.

# Repozitáře

**Repozitář** je projekt spravovaný pomocí Gitu.

Existují dva hlavní typy repozitářů:

- **Místní repozitář** – uložený na vašem počítači, kde můžete pracovat na své verzi projektu.
- **Vzdálený repozitář** – uložený na serveru, kde mohou spolupracovat týmy, sdílet kód a integrovat změny.

# Vytvoření repozitáře

Chcete-li vytvořit nový repozitář, otevřete terminál, přejděte do složky projektu a zadejte:

```bash
git init
```

Tímto vytvoříte skrytý adresář `.git`, kde Git ukládá data o verzích projektu.

# Přidávání změn a commitování

**Commit** je záznam změn, který ukládá aktuální stav kódu. Pomáhá sledovat vývoj projektu a umožňuje návrat k předchozím verzím.

Před commitováním je potřeba změny **přidat do staging oblasti**.

## Zjištění stavu

Pro zjištění aktuálního stavu repozitáře použijte příkaz:

```bash
git status
```

Ukáže vám, které soubory byly změněny, sledují se a které čekají na přidání do staging oblasti.

## Přidání souborů do staging oblasti

Pro přidání konkrétního souboru do staging oblasti použijte:

```bash
git add file.js
```

Pro přidání všech změněných souborů najednou použijte:

```bash
git add .
```

## Commitování změn

Pro vytvoření commitu s popisnou zprávou použijte:

```bash
git commit -m "Popis commitu"
```

Popis by měl stručně vystihovat provedené změny.

## Historie commitů

Pro zobrazení historie commitů použijte příkaz:

```bash
git log
```

Tento příkaz vám zobrazí všechny předchozí commity, včetně autora, hash kódu a data.

Pro návrat k určitému commitu použijte:

```bash
git checkout <commit-hash>
```

Pro návrat k poslední verzi na větvi master použijte:

```bash
git checkout master
```

# Ignorování souborů

Pokud nechcete sledovat některé soubory, vytvořte v hlavní složce soubor **.gitignore** a přidejte do něj názvy souborů či složek, které chcete ignorovat.

Více informací najdete [zde](https://help.github.com/en/articles/ignoring-files).

# Práce s větvemi

**Větve** umožňují pracovat na různých verzích projektu paralelně. Výchozí větev projektu se nazývá **master**, ale můžete si vytvořit vlastní větve pro experimentální funkce nebo úpravy.

## Vytvoření nové větve

Pro vytvoření nové větve použijte:

```bash
git branch <nová-větev>
```

## Přepínání mezi větvemi

Pro přechod do jiné větve použijte:

```bash
git checkout <název-větve>
```

Pokud chcete vytvořit novou větev a ihned do ní přejít, použijte:

```bash
git checkout -b <nová-větev>
```

## Sloučení větví

Po otestování nových funkcí ve vaší větvi je můžete sloučit zpět do hlavní větve (master) pomocí příkazu:

```bash
git merge <název-větve>
```

## Mazání větví

Pokud už větev nepotřebujete, můžete ji smazat pomocí:

```bash
git branch -d <název-větve>
```

# Další zdroje

Pro více informací o Gitu navštivte:

- Oficiální dokumentace Gitu: [https://git-scm.com/doc](https://git-scm.com/doc)
- Bezplatná kniha **Pro Git**: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
- Další informace o GitHubu: [https://guides.github.com/](https://guides.github.com/)
