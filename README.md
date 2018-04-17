# Kommunikasjon - Tjenester og nettverk

<meta name="author" content="Henrik Høiness">

Repository for teori og øvinger til Algoritmer og datastrukturer - TDT 4120.

**Under står notater fra både forelesninger, kompendium og Computer Networking - A Top Down Approach (Kurose, Ross)**

## Liste over kapitler
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

Endesystemene er koblet smamen gjennom et nettverk av kommunikasjonskoblinger (*eng. communication links* ) og pakkesvitsjere (*eng. packet switches* ). 

* En **packet switch** tar en pakke som kommer på en av dets *innkommende* kommunikasjonskoblinger og videresender den pakken på en av dets *utgående* kommunkikasjonskoblinger.

> De mest brukte typene av pakkesvitsjer idag er *rutere* (i nettverkskjernen) og *link-layer-swictches* (i aksessnettverk)


Sekvensen av kommunikasjonskoblinger og pakkesvitsjer traversert av en pakke fra det sendende endesystemet til det mottakende endesystemet er kalt en **sti** (*eng. route el. path* ) gjennom nettverket. 


Vi kan på mange måter sammenlikne pakkesvitsje nettverk (som transporterer pakker) med en transportsystem av motorveier, veier, kryss (som transporterer trailer mellom fabrikker):

```text
Pakker --> Trailer

Komm.koblinger --> Motorveier og veier

Pakkesvitsjer --> Veikryss

Fabrikker --> Endesystemer
```

Endesystemene aksesserer internettet gjennom **internetleverandører (ISP-er)**  (*eng Internet Service Providers* ). Her inngår bolig ISP-er (som kabel- eller telefonselskaper), bedrift ISP-er, universitets ISP-er o.l.

Hver ISP er i seg selv et nettverk av pakkesvitsjer og kommunikasjonskoblinger. ISP-er tilbyr forskjellige typer nettverkstilganger til endesystemer, som f.eks. kabelmodem, DSL, LAN, WLAN o.l. ISP-er tilbyr også internetttilgang til innholdsleverandører, som kobler opp nettsider til internettet. Det hele handler om å sammenkoble endesystemer.

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

* DSL-standarder definerer overføringshastigheter av 12 Mbps nedstrøms og 1.8 Mbps oppstrøms [ITU 1999], og 23 Mbps nedstrøms og 2.5 Mbps oppstrøms [ITU 2003]. 
	 
![CIA](https://i.imgur.com/RjhtBlC.png)



Selvom DSL og kabelnettverk står for over 90% av bredbåndsaksess i bolig i USA, så er det kommet en ny teknologi **fiber to the home (FTTH)** - fibernett. 

*	Bruker PON distrubusjonsarkitektur.
	* Hvert hjem har en optisk nettverksterminator (ONT) , som er koblet, med optisk fiber, til en nabolagssplitter. 
	* Splitteren kombinerer et antall hus på en enkel, felles optisk fiber, som kobles til en optisk linjeterminator (OLT) hos nettverksleverandøren
![Fibernett](https://i.imgur.com/AcnATPA.png)


**Wide-Area Wireless Access: 3G and LTE:**

Alle mobil-enheter som sender mails, surfer og hører på musikk når de ikke er hjemme, er koblet til den samme trådløse infrastrukturen som brukes til mobiltelefoni til å sende/motta pakker via en basestasjon som drives av mobilnettleverandøren. 

I motsetning til WiFi, trenger en bruker bare å være innenfor noen få tiier kilometer (i motsetning til noen få ti meter) av basestasjonen.

#### Fysiske medier:

* *Guided media:*
	*  Tvinnede kobberkabler
	*  Coaxkabler
	*  Fiber-optisk kabel
* *Unguided media:*
	*	Trådløs LAN
	*  Digital satelittkanal


**Satelitter:**
*	Geostationary satellites
*	Low-earth orbiting (LEO) satellites


### The Network Core

#### Packet Switching:

For å kunne sende en melding fra et kildeendesystem til en destinasjonsendesystem, må kilden dele opp lengre meldinger til mindre klumper med data, kjent som **pakker**.


Mellom kilden og destinasjonen, reiser hver pakke gjennom kommunikasjonskoblinger (*eng. comm. links*) og **pakkesvitjser** (som det finnes to typer, **rutere** og **link-layer svitsjer**). Pakkene blir sendt over hver kommunikasjonskoblinge med en rate lik en fulle **overførigsrate** (*eng. transmissionrate*) til koblingen. 

Så dersom en kilde eller pakkesvitsj sender en pakke av *L* bit over en kobling med en transmissionrate *R* bits/sec, da tar det *L/R* sekunder å sende pakken over koblingen


**Store-and-Forward Transmission:**

De fleste pakkesvitsjer bruker **store-and-forward transmission** på inputten på koblingen. Denne type overføring betyr at pakkesvitsjen må motta hele pakken før den kan begynne å sende den første biten av pakken på den utgående koblingen. 

![store-and-forward](https://i.imgur.com/ujoDmYG.png)

Kilen begynner å sende pakken ved tid 0, ved tid *L/R* har kilden sendt hele pakken og pakken har blitt mottat og lagret på ruteren, og ruteren begynner å sende videre. Ved tid *2L/R* har ruteren sendt hele pakken og pakken har blitt mottatt av destinasjonen. Den totale delayen er da *2L/R*. Dersom det er flere koblinger, får vi at ende-til-ende forsinkelsen er:

![d-e-t-e](https://i.imgur.com/BdiyS95.png)



**Queueing Delays and Packet Loss:**

Hver pakkesvitsj har flere koblinger koblit til seg. For hver kobling har pakkesvitsjer en output queue, som lagrer pakkene som ruteren er på vei til å sende på koblingen. Dersom en kobling allerede frakter en pakke, må den neste pakken vente i bufferen/queu-en. Dette fører til queueing delays, disse forsinkelsene er varierende og avhenger av fordøyelsen til nettverket. 

Siden størrelsen til en buffer er definert, så dersom en pakke kommer til en full buffer, vil **pakketap** oppstå.


**Forwarding Tables and Routing Protocols:**

Hver ruter har et *forwarding table* som mapper destinasjonsaddressen til ruterens utgående koblinger. Når en pakke kommer til ruteren, ser den på pakkens addresse og søker i forward table-en sin, for å finne en passende utgående kobling. Ruteren leder deretter pakken til denne utgående koblingen. Internettet har en rekke **routing protokoller** som brukes til automatisk bestemme **forwarding tables**.


**Circuit Switching:**

Det er to fundementale måter å flytte daata gjenno et nettverk av koblinger og svitsjer: *circuit switching* og *packet switching*. 

I circuit-switched nettverk er ressursene som trengs langs en sti (buffere, koblinger og overføringsrate) for å kunne kommunisere mellom endesystemene *reservert* varigheten av kommunikasjonsøkten mellom endesystemene. 

I packet-switched nettverk er ikke disse ressursene reserverte, ressursene brukes etter etterspørsel, og som konsekvens må man kanskje måtte vente (queue). 

Vanlig telefoninettverk er eksempler på circuit-switched nettverk. Når man ringer noen, vil nettverket etablere en tilkobling mellom senderen og mottakeren, og linjen og overføringsraten vil være reservert helt til de leger på. Her har man garantert konstant rate.

![circuit](https://i.imgur.com/phkISlJ.png)

For hver lkobling brukt av en ende-til-ende forbindelse, får denne forbindelsen en fjerdedel av den totale overføringskapasiteten under tilkoblingens varighet. Dersom hver kobling mellom tilstøtende svitsjer har en overføringshastighet på 1Mbps, da får hver ende-til-ende circuit-switch forbindelse 250 kbps av dedikert overføringshastighet.


> Det blir ofte argumentert for at pakkesvitsjing ikke passer så bra for real-time tjenester (f.eks. telefoni og videokonferanser), på grun av variansen og den uforutsigbare ende-til-ende forsinkelsen.
> Pakkesvitsjing er billigere, mer effektiv og tilbyr en bedre deling av overføringskapasitet enn circuit-switching.


#### Nettverk av nettverk

Endesystemer kobler seg til internettet gjennom en aksess ISP. ISP-ene selv må også være sammenkoblet. Dette gjøres ved å lage et *nettverk av nettverk*.

*	*Network Structure 1*: En global transit ISP, **provider**, og mange aksess ISP-er, **customers**.

*	*Network Structure 2*: Flere globale transit ISP-er, **providers**, og mange aksess ISP-er, **customers**.


I virkeligheten, selvom mange ISP-er er imponerende verdensdekkede og kobles direkte mot mange aksess ISP-er, er det ingen som har tilstedeværelse i hver eneste by i hverden. Isteden i enhver gitt region kan det være en **regional ISP** som aksess ISP-ene i regionen tilkobles. Hver regionale ISP kobler seg så til **tier-1 ISP-er**. Tier-1 ISP-er  er like til den imaginære *global transit ISP-en*

For eksempel er det i Kina aksess ISP-er i hver by, som kobler seg til provinsielle ISP-er, som igjen kobler til nasjonale ISP-er, som til slutt kobler til ISP-ene i tier-1. Vi refererer til dette multi-tier hierarkiet, som fortsatt er bare en grov tilnærming av dagens internett, som *Network Structure 3*.

Internet Exchange Point (IXP) er møtepunktet hvor flere ISP-er kan peere sammen.

![isps](https://i.imgur.com/W1oIFit.png)


<br></br>

### Delay, Loss and Throughput in Packed-Switched Networks


#### Overblikk av forsinkelse i pakkesvitsjede nettverk

Når en pakke reiser fra en node (host eller ruter) til en påfølgende node (host eller ruter) langs denne veien vil pakken lide av flere typer forsinkelser ved hver node lags denne veien. De viktigste av disse forsinkelsene er:

*	**Nodal processing delay**
* 	**Queueing delay**
*	**Transmission delay**
* 	**Propagation delay**

Sammen gir disse en total nodalforsinkelse.


![delay](https://i.imgur.com/q73UGCU.png)


#### I - Processing Delay

 Tiden det tar å undersøke en pakkeheader og bestemme hvor man skal lede pakken er en del av prosesseringsforsinkelsen. Forsinkelsen kan også inkludere andre faktorer som tiden det tar for å skjekke for bit-nivå feil i pakken som skjedde under overføringen av pakkens bit fra oppstrømsnoden til ruter A. Etter dette retter ruteren pakken til køen som går foran koblingen til ruter B.


#### II - Queuing Delay

I køen vil pakkene oppleve queuing delay mens den venter på å bli overført på koblingen. Lengen på køforsinkelsen til en spesifikk pakke er avhengig at antall tidlig ankommede pakker som ligger i køen. Dersom køen er tom og det ikke er noen pakke som holder på å bli overført, vil køforsinkelsen være null. På den andre siden vil forsinkelsen være lang dersom det er stor trafikk og mange pakker i kø. 


#### III - Transmission Delay

Dersom man antar at pakkene blir sendt på i first-come-first-served rekkefølge, som er vanlig i pakkesvitsjede nettverk, kan pakken først bli sendt etter at alle pakkene som kom før den har blitt overført. Pakken har *L* bits, og skal bli sendt over en kobling med en overføringsrate fra ruter A til ruter B på *R* bits/sec. Overføringsforsinkelsen blir da *L/R*.

> Tiden ruteren bruker på å dytte ut pakken


#### IV - Propagation Delay

Så fort en bit er pushet over på koblingen, må den forplante seg til ruter B. Tiden det tar fra begynnelsen av koblingen til ruter B er forplantningsforsinkelsen. Biten forplanter seg med farten til koblingen. Forplantningshastigheten avhenger av det fysiske mediet til koblingen. 
Propagations delayet er avstanden mellom de to ruterne delt på forplantningshastigheten. Som blir *d/s* der *d* er avstanden mellom ruterne og *s* er forplantningshastigheten på koblingen.


#### Nodal forsinkelse:

Summen av alle forsinkelsene: I, II, III, IV. 

![nodal forsinkelse](https://i.imgur.com/u3dtAsk.png)


#### Ende-til-ende forsinkelse:

Anta at en har N koblinger, dvs. N-1 rutere, mellom en kildehost og en destinasjonshost. Da vil summen av alle de nodale forsinkelsene gi ende-til-ende forsinkelsen:

![endetilende](https://i.imgur.com/JtVkh39.png)


#### Gjennomstrømning i datanettverk:

* **Insantaneous throughput** ved enhver tid er raten (i bits/sec) som en host mottar en fil.

* **Average throughput** er gjennomsnittsraten ved overføring av en fil på F bit blir *F/T* bits/sec 

Throughput er raten på antall vellykkede meldinger levert over en kommunikasjonskanal.Vi må se på flaskehals koblingen i ende-til-ende tilkoblingen for å finne gjennomstrømningen. 



![bild1](https://i.imgur.com/XfM4msT.png)

**a)** Her vil gjennomstrømningen være *min* {R<sub>c</sub>,R<sub>s</sub>}, det vil si overføringsraten til flaskehalskoblingen.

**b)** Her vil gjennomstrømningen være *min* {R<sub>1</sub>,R<sub>2</sub>,..., R<sub>N</sub>}, som igjen vil si overføringsraten til flaskehalskoblingen.

<br></br>
### Protocol Layers and Their Service Models

For å ha struktur i designet av nettverksprotokoller, orgarniserer vi protokollene i **layers**. Hver protokoll hører til i en av lagene. Vi er interessert i hvilke **services** som et lag har å tilby til laget over - den såkalte **service modellen**.

![ipstack](https://i.imgur.com/FNieMNR.png)

#### Application Layer

Applikasjonslaget er der nettverksapplikasjoner og deres applikasjonslag-protokoller ligger. Internettets applikasjonslag inkluderer mange protokoller som HTTP-, SMTP- og FTP-protokollen. Vi skal se at visse nettverksfunksjoner, lsik som oversetting av menneskevennlige navn for internett-endesystemer som www.ietf.org til en 32-bit nettverksaddresse, er gjort ved hjelp av en spesifikk applikasjonslag protokoll, DNS (The Domain Name System)

En application-layer protokoll er distribuert over flere endesystemer, med applikasjonen i et endesystem som bruker protokollen for å sende pakker av informasjon til applikasjonen på et annet endesystem. Vi referer til denne pakken av informasjon på applikasjonslaget for en **melding** (*eng. message*)


#### Transport Layer

Internettets transportlag transporterer *applikasjonslag-meldinger* mellom applikasjon-endepunkter. I internettet er det to transportprotokoller,TCP og UDP, som hver og en kan transportere applikasjonslag-meldinger.

**TCP** protokollen tilbyr en tilkoblingsorientert tjeneste til sine applikasjoner. Denne tjenesten inkluderer garantert leveranse av app.lag-meldinger til destinasjonsen og flytkontroll (vs. sender/mottaker hastighetsmatching, for å hindre en rask avsender fra å overvelde en langsom mottaker). TCP deler også opp lengre meldinger til kortere segmenter og tilbyr en overbelastelsesstyring, slik at kilden kan endre overføringshastigheten sin når nettverket er overbelastet. 

**UDP** protokollen tilbyr en tilkoblingsløs tjeneste til sine applikasjoner. Dette er en no-frills (ingenting ekstra) tjeneste som verken gir pålitelighet, flytkontroll og ingen overbelastningsstyring. 

I denne boken refererer vi til en transportlagspakke som et **segment**.



#### Network Layer

Internettets network layer er ansvarlig for å flytte nettverkslagpakker kjent som **datagrammer** fra en vert til en annen. Internett transportlagprotokoll (TCP eller UDP) i en kildevert sender et transportlagssegment og en destinasjonsadresse til nettverkslaget, slik som man leverer et brev til Posten. 

Internettets nettverksprotokoll inkluderer IP protokollen, som definerer fletene i datagrammet i tillegg til hvordan endesystemer og rutere handler på disse feltene. Det er bare en IP protokoll, og alle internettkomponenter som har et nettverkslag må bruke IP protokollen. Nettverkslaget består også av routing protokoller som skal bestemme hvilke ruter datagrammene skal ta mellom kilde og destinasjon.


#### Link Layer

Internettets nettverkslag sender et *datagram* gjennom en rekke rutere mellom kilden og destinasjonen. For å flutte en pakke fra en node (vert eller ruter) til den neste noden på en rute, bygger nettverkslaget på tjenestene til link layer-et (*koblingslaget*).

Ved hver node, gir gir nettverkslaget datagrammet ned til koblingslaget, som leverer datagrammet til neste node langs ruten. Ved neste node leverer koblingslaget datagrammet opp igjen til nettverkslaget. 

Tjenestene som tilbys av koblingslaget avhenger av den spesifikke koblingslagsprotokollen som blir brukt over koblingen. Eksempler på koblingslagprotokoller er Ethernet og WiFi.

Nettverkslaget vil motta forskjellige tjenester fra hvert av de forskjellige koblingslagprotokollene. I denne boken referer vi til en koblingslagpakke som **frames** (*nor. rammer*)



#### Physical Layer

Mens mye av jobben til koblingslaget er å flytte på *rammer* fra et nettverkselement til det etterfølgende nettverkselementet, er jobben til det fysiske laget å flytte de *individuelle bitene* innad i rammen fra en node til den neste. 

Protokollene i dette laget er igjen koblingsavhengige og avhenger også på koblingens faktiske overføringsmedium (f.eks. tvinnede-kobberrør, optisk fiber, etc.)



#### The OSI Model

På slutten av 70-tallet ble det foreslått av The International Organization for Standardization (ISO) at datanettverk skulle være organisert rundt 7 lag, kalt Open Systems Interconnection (OSI) model [ISO 2012].



#### Innkapsling

Figuren under viser den fysiske stien data tar ned et sendende endesystems protokollstakk, up og ned protokollstakkene til en mellomliggende linklagssvitsj og ruter, og opp protokollstakken til det mottakende endesystemet. 

Ved den sendende verten, blir en **applikasjonslagsmelding** (*M*) sendt til transportlaget. Transportlaget tar meldingen og legger til ekstra informasjon (såkalt transportlagsheader-informasjon H<sub>*t*</sub> ). Applikasjonslagsmeldingen og transportlagheaderen utgjør sammen **transportlagssegment**. Transportlaget får så segmentet, som så legger å nettverklagsheader-informasjon (H<sub>*n*</sub>), slik som kilde- og destinasjonsendesystemenes adresser, som utgjør **nettverklagsdatagram**. Datagrammet blir nå levert til koblingsaget som legger til sin egen koblingslagheader-informasjon (H<sub>*l*</sub>) og lager en **koblinglagsramme**. 


![innkapsling](https://i.imgur.com/LCXUOwU.png)


### Nettverk under angrep

På internettet finnes det veldig mye bra, men i tillegg til dette finnes det også noe som heter **skadelig programvare** (*eng. malware*), som kan bryte seg inn og angripe enhetene våre. Så fort skadelig programvare har infisert en enhet kan den gjøre mye slemt, slette alle filer, installere spyware som samler inn privat informasjon og sender det til de som angrep enheten. Man kan også bli en del av et nettverk av tusen like kompromitterte enheter, kjent som et **botnet**, som kan brukes til leveranse av spam e-mail og distributed denial-of-service attacks (DDOS) mot bestemte verter.


Mye av dagens skadelige programvare er **selvreproduserende**, som betyr at så fort det har infisert en vert, så vil den verten prøve å infisere andre verter. På denne måten kan selvreproduserende skadelig programvare spre seg eksponensielt fort. Skadelig programvare kan spre seg i form av virus eller worms.

**Viruser** er skadelig programvare som krever en form for interaksjon med brukeren for å infisere brukerens enhet. Et klassisk eksempel på dette  er et epost-vedlegg som inneholder skadelig kjørbar kode. 

**Worms** er skadelig programvare som kan gå inn i en enhet uten noen spesiell brukerinteraksjon. For eksempel at en bruker kan kjøre et sårbart nettverksprogram som en angriper kan sende skadelig programvare på.


En annen sikkerhetstrussel er kjent som **denial-of-service (DoS) attacks**. Som navnet antyder, gjør et DoS-angrep et nettverk, vert eller annen infrastruktur ubrukelig av legitime brukere.

De fleste Internett DoS-angrep faller inn i en av tre kategorier:

*	*Sårbarhetsangrep*. Dette innebærer å sende noen velutviklede meldinger til et utfyllende program eller operativsystem som kjører på en målrettet vert. Hvis den riktige sekvensen av pakker sendes til et sårbart program eller operativsystem, kan tjenesten stoppe eller verre kan verten krasje.

*	*Båndbreddeflom*. Angriperen sender en deluge av pakker til den målrettede verten, så mange pakker at målets tilgangslink blir tilstoppet, og hindrer at legitime pakker når serveren.

*	*Tilkoblingsflom*. Angriperen etablerer et stort antall halvåpent eller fullt åpne TCP-tilkoblinger (TCP-tilkoblinger diskuteres i kapittel 3) på målverten. Verten kan bli så presset ned med disse falske forbindelsene at den slutter å godta legitime tilkoblinger.


I et distribuert DoS (DDoS) angrep, illustrert i figuren under, styrer angriperen flere kilder og lar hver kilde skyte trafikk på målet.

![ddos](https://i.imgur.com/YOGUjFo.png)


En passiv mottaker kan lagre en kopi av hver pakke som flyr forbi, er kalt en **pakkesniffer**

Evnen til å injisere pakker til Internett med en falsk kildeadresse kalles IP-spoofing, og er bare en av mange måter som en bruker kan maskerer som en annen bruker.


<br></br>
<br></br>


<a name="kap2"></a>
## Kapittel 2 - Application Layer


### Principles of Network Applications

	
I en webapplikasjon er det to forskjellige programmer som kommuniserer med hverandre: nettleserprogrammet kjører i brukerens verts (skrivebord, bærbar PC, nettbrett, smarttelefon og så videre); og webserverprogrammet kjører i webserveren.



#### Arkitekturer til nettverkapplikasjoner


Applikasjonsarkitekturen er designet av applikasjonsutvikleren og dikterer hvorda applikasjonen er strukturert over flere endesystemer. Når man velger applikasjonsarkitekturen vil man gjerne velge mellom en av to dominerende arkitektiske paradigmer brukt i moderne nettverksapplikasjoner: *the client-server architecture* eller *peer-to-peer (P2P) architecture*.


*	**Klient-server arkitektur:** I denne arkitekturen er det en alltid-på vert, kalt *serveren* som gir tjenestegjør forespørsler fra mange andre verter, kalt *klienter*. 
	*	Et klassisk eksempel er webapplikasjonen som en kontinuerlig webservertjenester forespørsler fra nettlesere som kjører på klientverter.

	
*	**Peer-to-peer arkitektur:** I en P2P-arkitektur er det minimal (eller ingen) avhengighet av dedikerte servere i *datasentre*. I stedet utnytter programmet direkte kommunikasjon mellom par av periodisk tilkoblede verter, kalt *peers*. Klientene eies ikke av tjenesteleverandøren, men er i stedet desktops og bærbare datamaskiner kontrollert av brukerne, med de fleste kolleger bosatt i boliger, universiteter og kontorer. Fordi peer-ene kommuniserer uten å passere gjennom en dedikert server, kalles arkitekturen peer-to-peer. Mange av dagens mest populære og trafikkintensive applikasjoner er basert på P2P-arkitekturer.
	*	En av de mest overbevisende funksjonene i P2P-arkitektur er deres **selvskalering**. For eksempel, i et P2P-fildelingsprogram, selv om hver peer genererer arbeidsbelastning ved å be om filer, legger hver peer også tjenestekapasitet til systemet ved å distribuere filer til andre peers.  

	
Men fremtidige P2P-applikasjoner står overfor tre store utfordringer:

1.	*ISP Friendly.* De fleste boliger (inkludert DSL- og kabelleverandører) er dimensjonert for "asymmetrisk" båndbreddebruk, det vil si for mye mer
nedstrøms enn oppstrøms trafikk. Men P2P-videostreaming- og fildistribusjonsapplikasjoner skifter oppstrøms trafikk fra servere til boliger, og legger dermed betydelig vekt på Internett-leverandørene.

1.	*Sikkerhet.* På grunn av deres svært distribuerte og åpne natur kan P2P-applikasjoner være en utfordring å sikre

1.	*Insentiver.* Suksessen til fremtidige P2P-applikasjoner avhenger også av overbevisende brukere til å frivillig gi båndbredde, lagrings- og beregningsressurser til applikasjonene, som er utfordringen med insentivdesign (Insentiv = noe som motiverer noen til å utføre en bestemt handling)




#### Klient- og server-prosesser

Vi sier at det ikke er programmer, men prosesser som kommuniserer. For eksempel i en webapplikasjon vil en klient-prosess utveklse meldinger med webserver-prosessen. For hvert par av kommuniserende prosesser, merker vi vanligvis en av de to prosessene som **klienten** og den andre prosessen som **serveren**. Vi definerer klient- og server-prosesser som følgende:

*	I sammenheng med en kommunikasjonsøkt mellom et par prosesser merkes prosessen som initierer kommunikasjonen (det vil si i utgangspunktet kontakten med den andre prosessen i begynnelsen av økten) merket som *klienten*. 
* Prosessen som venter på å bli kontaktet for å starte økten er *serveren*.



#### Grensesnittet mellom prosessen og datanettverket

En prosess sender meldinger inn i, og mottar meldinger fra, nettverket gjennom et programgrensesnitt som kalles en **socket**. 

*	Dersom vi ser på en prosess som et hus, vil socketen være døren. 

En socket er grensesnittet mellom applikasjonslaget og transportlaget innad en vert. Det refereres også som **Application Programming Inter- face (API)** mellom applikasjonen og nettverket. 

![socket](https://i.imgur.com/QPIFAx2.png)


#### Addresseringsprosesser

For at en prosess kjørende på en vert skal kunne sende pakker til en annen prosess som kjører på den andre verten, så trenger den mottakende prosessen en adresse. For å identifisere mottakende prosesser, må to typer informasjon være spesifisert:

1.	 Adressen til verten
2. En identifikator som spesifiserer den mottakende prosessen i destinasjonsverten


I internettet er en vert gjenkjent ved dens **IP addresse**. I tillegg til  vite adressen til verten, må den sendende prosessen også kunne identifisere den mottakende prosessen (mer spesifikt, den mottakende socket-en) Et destinasjons **portnummer** tjener denne hensikten.

Populære applikasjoner har fått tidelt spesifikke portnummer. For eksempel er en webserver identifisert med portnummer 80, en mailserver-prosess (SMTP) har portnummer 25, og resten av listen finnes [her](http://www.iana.org).


#### Transporttjenester tilgjengelige for applikasjoner

Minnes om at en socket er grensesnittet mellom applikasjonsprosessen og transportlagsprotokollen. Hva er tjenestene som en transportlagsprotokoll kan tilby for applikasjoner som påberoper det? Vi kan i stor grad klassifisere de mulige tjenestene langs fire dimensjoner: pålitelig dataoverføring, gjennomstrømning, timing og sikkerhet.


**Pålitelig dataoverføring:**

Dersom en protokoll kan garantere at data som blir sendt fra en ende vil bli levert korrekt og komplett til den andre enden av applikasjonen, sier vi at den tilbyr *pålitelig overføring*.

Når en transportlagprotokoll ikke gir pålitelig dataoverføring, kan noen av dataene som sendes av den sendende prosessen aldri komme til den mottakende prosessen. Dette kan være akseptabelt for **tapstolerante** **applikasjoner**, særlig multimedieapplikasjoner som konversasjonslyd/video som kan tåle noe tap av data.



**Gjennomstrømning:**

Programmer som har gjennomstrømningskrav, sies å være **båndbreddefølsomme** applikasjoner. Mange nåværende multimedieapplikasjoner er følsomme for båndbredde, selv om enkelte multimedieapplikasjoner kan bruke adaptive kodeteknikker for å kode digitalisert stemme eller video med en hastighet som samsvarer med den nåværende tilgjengelige gjennomføringen.

Selv om båndbreddefølsomme applikasjoner har spesifikke krav til gjennomstrømning, kan **elastiske applikasjoner** benytte så mye eller lite gjennomstrømming som tilfeldigvis er tilgjengelig. Dette kan være elektronisk mail, filoverføring o.l.


**Timing:**
En transportlagsprotokoll kan også gi tidsgarantier. Som med gjennomstrømningsgarantier kan tidsgarantier komme i mange former og former. Et eksempel på garanti kan være at hver bit som avsenderen pumper inn i socket-en, kommer til mottakerens socket, ikke mer enn 100 ms senere.

**Sikkerhet:**
En transportprotokoll kan gi et program med en eller flere sikkerhetstjenester. Eksempelvis kan en transportprotokoll kryptere alle data som sendes av sendeprosessen, i mottakeren, og transportlagsprotokollen dekrypterer dataene før de leverer dataene til mottaksprosessen. En slik tjeneste vil gi konfidensialitet mellom de to prosessene, selv om dataene på en eller annen måte observeres mellom sende- og mottaksprosesser.



#### TCP Services
Når en applikasjon bruker TCP som sin transportprotokoll, vil applikasjonen få begge disse tjenestene fra TCP:

*	*Connection-oriented service:* TCP får klienten og serveren til å utveksle transportlagskontroll informasjon med hverandre *før* applikasjonslagsmeldingene kan begynne å flyte. Dette er den såkalte handshaking-prosedyren, som lar klientene og serverene til å bli klare til å sende/motta pakker. 

*	*Reliable data transfer service:* De kommuniserende prosessene kan vite at TCP levererer all data som blir sendt uten noen feil og i riktig rekkefølge. 


TCP inkluderer også en opphopningskontroll-mekanisme, en tjeneste som endrer hastigheten på en sendingsprosess når nettverket er mett mellom sender og mottaker.


#### UDP Services
UDP er en *no-frills*, lett nettverksprotokoll, som tilbyr minimalt med tjenester. UDP er *connectionless*, så det er ingen handshaking før de to prosessene starter å kommunisere. 

*	UDP tilbyr en unreliable data service, det betyr at det ikke er noen garanti på at pakker kommer frem. 
* UDP tilbyr ingen opphopningskontroll-mekanisme.



#### Application-Layer Protocols

En applikasjonslagsprotokoll definerer:

*	Typen meldinger som blir utveklset, for eksempel request-meldinger og response-meldinger
* Syntaxen til de varierende melingstypene, sånn som hvilke felt som er i meldinger og hvordan feltene er avgrenset.
* Semantikken til feletene, som betyr meningen til informasjonen i feltene
* Reglene for å bestemme når og hvordan en prosess skal sende og respondere til meldinger


 

### The Web and HTTP

Protokollen **HyperText Transfer Protocol (HTTP)** er hjertet til internettet. HTTP er implementert i to programmer: et klientprogram og et serverprogram. Programmene kjører på forskjellige endesystemer, snakker med hverandre ved å utveklse HTTP-meldinger. HTTP definerer strukturen til disse meldingene og hvordan klienten og serveren utveksler disse meldingene. 


En **nettside** (*document*) består av objekter. Et **objekt** er en fil, som en HTML-fil, et JPEG bilde, som kan addresses til gjennom en enkelt URL. De fleste nettsider består av en **base HTML fil** og flere refererte objekter. 

Når en bruker *requester* om en nettside sender browseren en HTTP request-meldinger for ovbjektene på siden til serveren. Serveren mottar disse request-meldingene, og responderer med HTTP response-meldinger som inneholder objektene.

HTTP bruker **TCP** som sin underliggende transportprotokoll. HTTP-klienten initierer først en TCP-tilkobling til serveren. Når tilkoblingen er etablert, vil browser og server prosessene aksessere TCP gjennom socket-interfacet sitt. 

*	Som beskrevet over tilbyr TCP pålitelig dataoverføring til HTTP. Dette impliserer at hver HTTP request-melding sendt av en klient prosess kommer intakt ved serveren, på samme måte vil hver HTTP response-melding etterhvert komme intakt hos klienten. 

* Det er viktig å merke seg at serverene ikke lagrer noen informasjon om klientene. På grunn av at en HTTP server ikke vedlikeholder noen informasjon om sine klienter, er HTTP en **stateless protocol**. 


#### Non-Persistent and Persistent Connections

* **Persistent** (*norsk. vedvarende* )

Når en klient-server interaksjon finner sted over TCP, må applikasjonen ta en viktig avgjørelse, skal hvert request/respone-par sendes over en *separat* TCP-forbindelse, eller skal hver av disse requestene og deres korresponderende responser bli sendt over *samme* TCP-forbindelse. 

En applikasjon er dermed sagt å være **ikke-vedvarende tilkoblinger** eller motsatt, **vedvarende tilkoblinger**.


##### HTTP with Non-Persistent Connections

La oss anta at en nettside innholder en HTML-fil og 10 JPEG bilder, og at alle disse 11 elementene ligger på samme server. Dette vil da skje:

1. HTTP-klienten vil initiere en TCP-tilkobling med serveren.
2. HTTP-klienten sender en HTTP request-melding til serveren.
3. HTTP-server-prosessen sender en HTTP response-melding til klienten.
4. HTTP-server-prosessen forteller TCP å lukke TCP-tilkoblingen når meldingen kommer frem. 
5. HTTP-klienten mottar response-meldingen. TCP-tilkoblingen avsluttes. Klienten leser HTML-filen og finner referansene til de 10 JPEG-objektene.
6. De fire første stegene blir så gjentatt for hvert JPEG-objekt.


Før vi fortsetter, la oss estimere hvor lang tid det tar fra en klient *requester* HTML-basefilen til hele filen er mottat av klienten. Som sagt, definerer vi **round-trip time (RTT)** til å være tiden det tar for en pakke å reise fra en klient til server og tilbake til klienten. 

Som vist i figuren under tvinger dette nettleseren til å initiere en TCP-tilkobling mellom nettleseren og Web-serveren; som involverer en "three-way handshake" - klienten sender et TCP-segment til serveren, serveren anerkjenner (*eng. acknowlegdges* ) og responderer med et TCP-sement, og til slutt, klienten anerkjenner tilbake til serveren.

![RTT-HTTP](https://i.imgur.com/wcKccAH.png)

* **Første** og **andre** del av "three-way handshake" tar en RTT. Etter dette sender klienten en HTTP request-melding kombinert med den **tredje** del av håndhilsingen (anerkjennelsen) inn i TCP-tilkoblingen. 
* Når request-meldingen kommer til serveren, sender serveren HTML-filen inn i TCP-tilkoblingen. Denne HTTP request/respons bruker enda en RTT. 



##### HTTP with Persistent Connections

Ikke-vedvarende tilkoblingen kan ha noen mangler. For det første, en helt ny tilkobling må bli etablert og vedlikeholdt for *hvert forespurte objekt*. For hver av disse tilkoblingene må det tildeles TCP-buffere og -variabler. Dette kan være en byrde for Web-serveren, som muligens gjør slike forespørsler for flere hundre klienter samtidigt. Som beskrevet vil hvert objekt få leveringsforsinkelse på to RTT-er. 

Med *vedvarende tilkoblinger* kan serveren la TCP-tilkoblingen være åpen etter den har sendt en respons. Senere requester og responser mellom samme klient og server kan bli sendt over samme tilkobling. 


#### HTTP Message Format

##### HTTP Request Message

```
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0 
Accept-language: fr
```

* Første linje i meldingen kalles en **forespørsel-linje** (*eng. request line*), the påfølgende linjene er kalt **header-linjer**. Requestlinjen har tre felt: metodefelt, URL-felt og HTTP-versjon-felt.
	* Metodefeltet kan ta inn forskjellige verdier, inkludert `GET`, `POST`, `HEAD`, `PUT`, og `DELETE`.
	* Headerlinjen `Host:` spesifiserer hosten hvor objektet ligger. Ved å inkludere `Connection: close`i headerlinjen, forteller browseren serveren at den ikke trenger en vedvarende tilkobling (persistent). 
	* Headerlinjen `User agent:` spesifiserer brukeragenten, som er browsertypen som gjør forespørselen på serveren.



















