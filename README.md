# Kommunikasjon - Tjenester og nettverk

<meta name="author" content="Henrik Høiness">

Repository for teori og øvinger til Algoritmer og datastrukturer - TDT 4120.

**Under står notater fra både forelesninger, kompendium og Computer Networking - A Top Down Approach (Kurose, Ross)**

## Liste over forelesninger
1. [Kapittel 1 - *Computer Networks and the Internet*](#kap1)
2. [Kapittel 2 - *Application Layer*](#kap2)
3. [Kapittel 3 - *Transport Layer*](#kap3)
4. [Kapittel 4 - *The Network Layer*](#kap4)
5. [Kapittel 5 - *The Link Layer: Links, Access Networks, and LANs*](#kap5)
6. [Kapittel 6 - *Wireless and Mobile Networks*](#kap6)
7. [Kapittel 7 - *Multimedia Networking*](#kap7)
8. [Kapittel 8 - *Security in Computer Networks*](#kap8)
9. [Kapittel 9 - *Network Management*](#kap9)

<a name="kap1"></a>
## Kapittel 1

### What Is the Internet

Internettet er et nettverk som kobler sammen flere hundre millioner dataenheter i verden. Alle disse enhetene kaller vi **hosts** eller **ende systemer**.

Endesystemene er koblet smamen gjennom et nettverk av kommunikasjonsforbindelser (*eng. communication links* ) og pakkesvitsjere (*eng. packet switches* ). 

* En **packet switch** tar en pakke som kommer på en av dets *innkommende* kommunikasjonsforbindelser og videresender den pakken på en av dets *utgående* kommunkikasjonsforbindelser.

> De mest brukte typene av pakkesvitsjer idag er *rutere* (i nettverkskjernen) og *link-layer-swictches* (i aksessnettverk)


Sekvensen av kommunikasjonsforbindelser og pakkesvitsjer traversert av en pakke fra det sendende endesystemet til det mottakende endesystemet er kalt en **sti** (*eng. route el. path* ) gjennom nettverket. 


Vi kan på mange måter sammenlikne pakkesvitsje nettverk (som transporterer pakker) med en transportsystem av motorveier, veier, kryss (som transporterer trailer mellom fabrikker):

```text
Pakker --> Trailer

Komm.forbindelser --> Motorveier og veier

Pakkesvitsjer --> Veikryss

Fabrikker --> Endesystemer
```

Endesystemene aksesserer internettet gjennom **internetleverandører (ISP-er)**  (*eng Internet Service Providers* ). Her inngår bolig ISP-er (som kabel- eller telefonselskaper), bedrift ISP-er, universitets ISP-er o.l.

Hver ISP er i seg selv et nettverk av pakkesvitsjer og kommunikasjonsforbindelser. ISP-er tilbyr forskjellige typer nettverkstilganger til endesystemer, som f.eks. kabelmodem, DSL, LAN, WLAN o.l. ISP-er tilbyr også internetttilgang til innholdsleverandører, som kobler opp nettsider til internettet. Det hele handler om å sammenkoble endesystemer.

Internettet bruker protokoller som kontrollerer sending og mottakelse av informasjon i internettet. **Transmission Control Protocol (TCP)** og **Internet Protocol (IP)** er de to viktigste protokollene i internettet.

IP protokollen spesifiserer formatet til pakkene som blir sent og mottat over rutere og endesystemer. Internettets prinsipp protokoller er *kollektivt* kjent som **TCP/IP**


**Internet standarder** blir utviklet av Internet Engineering Task Force (IETF). IETF standard dokumentene er kalt for **request for comments (RFCs)**. RFCs er veldig tekniske og detalsjerte. De definerer protokoller som TCP, IP, HTTP og SMTP.


Vi kan også se på internettet som en *infrastruktur som tilbyr tjenester til applikasjoner*. Internet applikasjoner kjører på endesystemer - de kjører ikke i pakkesvitsjene i nettverkskjernen. 

* Endesystemer som er tilkoblet internettet har en **Application Programming Interface (API)** som spesifiserer hvordan et program som kjører på et endesystem spør internett-infrastrukturen om å levere data til en spesifikk program-destinasjon som kjører på et annet endesystem. 
	* Internet API-er er et sett med regler som det sendene programmet må følge slik at internettet kan levere dataen til program-destinasjonen.




### What is a protocol? 

#### A Human Analogy

For å forstå hva en nettverksprotokoll er kan vi føsrt se på noen humane analogier. Se for det at du ønsker å spørre noen om hva klokken er.
Da vil man typisk:

1. Si "Hei" - initiere kommunikasjon med en annen

2. Få responsen "Hei" tilbake - En responsmelding som indikerer at du kan fortsette å spørre om hva klokken er

3. Du spør "Hva er klokken?" - siden det var en hyggelig respons, tør du å spørre hva klokken var.

4. Du får vite at klokken er "2:00:


Dersom den første responsmeldingen hadde vært uhyggelig, så hadde du kanskje ikke turt å spørre om tiden. Sånn fungerer også nettverksprotokollene. 
 


![Nettverksprotokoll](https://i.imgur.com/UHcUWtt.png)


#### Nettverksprotokoller

En nettverksprotokoll er lik til en human protokoll, bortsett fra at entitetene utveksler melinger og aksjoner er hardware eller software komponenter av en eller annen enhet. 

All aktivitet i internettet som involverer to eller flere kommuniserende entiteter blir overvåket av en protokoll. 


> *A **protocol** defines the format and the order of messages exchanged between two or more communicating entitites, as well as the actions taken on the transmission and/or receipt of a message or other event.*



### The Network Edge

Endesystemer blir også referert til som **verter** (*eng. hosts* ) fordi de verter (som betyr, kjører) applikasjonsprogrammer som en Web-browser program, Web-server program, e-mail klient program eller en e-mail server program. 

> *host = end system*

Hoster blir i mange tilfeller delt videre inn i: **klienter** og **servere**. Klienter pleier å være skrivebords- eller mobile PCer, smarttelefoner osv, mens servere pleier å være sterke maskiner som lagrer og distribuerer Websider, strømmer videoer, releér eposter osv. 


#### Aksessnettverk

La oss nå se på aksessnettverket - nettveket som fysisk kobler sammen et endesystem tl den første ruteren (også kjent som "egde router") på en *sti* fra endesystemet til et annet endesystem.

I dag er de to vanligste typene av bredbåndsaksess i bolig **digital subscriber line (DSL)** og kabel.

* DSL Internettaksess får man ofte fra det lokale telefonselskapet (telco) - Når en bruker DSL er kundens telco også dens ISP.
> På telco-en har de en DSLAM som skiller mellom data- og telefonsignaler

![DSL](https://i.imgur.com/M5ChhwY.png)

* Kabel internettaksess bruker kabel-TV leverandørene sin eksisterende kabel-TV  infrastruktur.
	* Kabel internettaksess trenger spesielle modemer - kalt kabelmodemer.
> På kabelhode-enden har de en CMTS (cabel modem termination system) som endrer de analoge signalene sendt fra kabelmodemet til digitalt format. 
	 
![CIA](https://i.imgur.com/RjhtBlC.png)

Selvom DSL og kabelnettverk står for over 90% av bredbåndsaksess i bolig i USA, så er det kommet en ny teknologi **fiber to the home (FTTH)**
