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

![httpreq](https://i.imgur.com/mZWGizl.png)

* Første linje i meldingen kalles en **forespørsel-linje** (*eng. request line*), the påfølgende linjene er kalt **header-linjer**. Requestlinjen har tre felt: *metodefelt, URL-felt* og *HTTP-versjon-felt*.

	* Metodefeltet kan ta inn forskjellige verdier, inkludert `GET`, `POST`, `HEAD`, `PUT`, og `DELETE`.
	* Headerlinjen `Host:` spesifiserer hosten hvor objektet ligger. Ved å inkludere `Connection: close`i headerlinjen, forteller browseren serveren at den ikke trenger en vedvarende tilkobling (persistent). 
	* Headerlinjen `User agent:` spesifiserer brukeragenten, som er browsertypen som gjør forespørselen på serveren.
	* Entitets-bodyen til en GET-request er tom, men blir brukt med POST-metoden.

* `HEAD`-metoden er lignende `GET`-metoden. Når en server mottar en HEAD-metode, responderer den med en HTTP-melding, men uten det forespurte objektet.
	* Applikasjonsutviklere bruker ofte HEAD-metoden for debugging eller testing

* `PUT`-metoden blir ofte brukt til å laste opp et objekt på en spesifikk path (dir) på en spesifikk webserver.

* `DELETE`-metoden tillater en bruker, eller en applikasjon, til å slette et objekt på en webserver.



##### HTTP Response Message

```
HTTP/1.1 200 OK 
Connection: close
Date: Tue, 09 Aug 2011 15:44:04 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Tue, 09 Aug 2011 15:11:03 GMT Content-Length: 6821
Content-Type: text/html

(data data data data data ...)
```

![httpres](https://i.imgur.com/PRcst7j.png)

* Den består av tre deler: en **statuslinje**, seks **header-linjer** og **entitets-bodyen**.
* Entitetskroppen/bodyen er kjøttet til meldingen - den innelholder det forespurte objektet selv, representert med `(data data data data ...)`
	* *Statuslinjen* har tre felt: protokollen, versjonskoden og en korresponderende statusmelding.
	* Headerlinjen `Connection: close` forteller klienten at den kommer til å lukke TCP-tilkoblingen etter sendelsen av meldingen. `Date: `-headeren forteller tiden og datoen HTTP-responsen ble laget og sent av serveren. `Server:`-headerlinjen indikerer hva slags server som har generert meldingen. `Last-modified:`-feltet forteller når objektet ble laget eller sist oppdatert. `Content-type:`-feltet forteller oss hva slags filtype objektet er. 

	
*Kjente statuskoder:*

* `200 OK`: Request suksessfull og informasjon returnert i respons
* `301 Moved Permanently`: Forespurt objekt er flyttet til en ny URL, spesifisert i `Location:`-feltet i responsen
* `400 Bad Request`: Denne responsen kommer når serveren ikke forstod request-meldingen
* `404 Not Found`: Det forespurte dokumentet eksisterer ikke på serveren
* `505 HTTP Version Not Supported`: Den forespurte HTTP-protokollversjonen støttes ikke av serveren


#### User-Server Interaction: Cookies
Vi nevnte at en HTTP-server er tilstandsløs. En server kan håndtere tusen av samtidige TCP-tilkoblinger. Men ofte er det ønsket at en ønsker å kunne identifisere brukere, enten fordi serveren ønsker å begrense brukertilgang eller fordi den ønsker å vise innhold som en funksjon av brukeridentiteten. For disse formålene bruker HTTP Cookies (*norsk. informasjonskapsler*). Cookies tillater nettsteder å holde oversikt over brukere. De fleste store kommersielle nettsteder bruker informasjonskapsler i dag.

Som vist i figuren under har informasjonskapselsteknologien fire komponenter (1) en cookie header.linje i HTTP response-meldingen, (2) en cookie headerlinje i HTTP request-meldingen, (3) en cookie-fil lagret på brukerens endesystem og styrt av av brukerens nettleser, og (4) en backend-database på nettstedet.

* HTTP request-meldingen har headerfeltet `Cookie:`og HTTP response-meldingen har `Set-cookie:`-headerfeltet.

![Cookies](https://i.imgur.com/szHIVDo.png)


Som man ser i figuren over, så vil cookien bli i lengre tid, og når man etter en uke går tilbake til samme sted vil cookien man fikk tildelt sist bestemme hvordan respons man får av serveren.



#### Web Caching

En **web cache** - også kalt en **proxy server** - (*norsk. nettbuffer*) er en nettverksentitet som tilfredstiller HTTP forespørsler på vegne av en webserver.
Nettbufferen har en egen lagringsenhet og holder kopier av nylig forespurte objekter. Som ivst i figuren under kan en brukers nettleser konfigureres slik at alle nettleser-forespørsler rettes mot nettbufferen. 

![nettbuffer](https://i.imgur.com/dtByG5Y.png) 

Dette skjer:

1. Nettleseren lager en TCP-tilkobling til nettbufferen og sender den en HTTP-request for objektet på nettbufferen.
2. Nettbufferen skjekker om den har en kopi lagret lokalt. Dersom den har det returnerer den objektet med en HTTP-response til klient-nettleseren.
3. Dersom nettfufferen *ikke* ar objektet, åpner nettbufferen en TCP-tilkobling til den originale serveren. Nettbufferen forespør så om objektet, nettserveren sender objektet med en HTTP-response til nettbufferen
4. Når nettbufferen får objektet, lagrer den en kopi lokalt og sender en kopi, i en HTTP response-melding, til klient-nettleseren (over den eksisterende TCP-tilkoblingen)

> Typisk er en nettbuffer kjøpt og installert av en nettverksleverandør

Nettbuffring blir implementert på Internettet av to grunner:

* For det **første** kan en nettbuffer redusere responstiden for en klientforespørsel vesentlig, spesielt hvis flaskehalsbåndbredden mellom klienten og opprinnelsesserveren er mye mindre enn bottenhalsbåndbredden mellom klienten og hurtigbufferen.

* For det **andre**, som snart illustrere med et eksempel, kan web-caches betydelig redusere trafikken på institusjonens tilgangskoblingen til internettet. Ved å redusere trafikken trenger institusjonen (for eksempel et firma eller et universitet) ikke å oppgradere båndbredden så fort, og dermed redusere kostnadene. 

Videre kan nettbuffere betydelig redusere webtrafikk på Internett som helhet, og dermed forbedre ytelsen for alle applikasjoner.

![bottleneck/nettbuffer](https://i.imgur.com/tchdzcz.png)

Anta at den gjennomsnittlige objektstørrelsen er 1 Mbits, og at gjennomsnittlig forespørselshastighet fra institusjonens nettlesere til opprinnelsesserverne er 15 forespørsler per sekund.

Trafikkintensiteten på LAN-et er

* `(15 requests / s) * (1 Mbits / requests) / (100 Mbps) = 0.15`

mens trafikkintensiteten på tilgangslinken (fra Internett-ruteren til institusjonen-ruteren) er

* `(15 forespørsler / s) (1 Mbits / requests) / (15 Mbps) = 1`

Denne typen intensitet vil gi veldig stor forsinkelse på koblingen, og kan være oppmot minutter. Dersom man legger til en nettbuffer, og antar at den har 40% hitratio, vil gjennomsnittlig forsinkelse være:

* `0.4 * (0.01 s) + 0.6 * (2.01 s) ≈ 1.2 s`

> Som vil er en kjempeforbedring enn det det var. Også mye billigere enn å øke aksesskoblingen mot internettet.



##### The Conditionally GET

Selvom buffring kan redusere bruker-oppfattede responstider, introduserer den et nytt problem - kopien av et objekt som ligger i hurtigbufferen, kan være foreldet. Med andre ord kan objektet lagret i bufferen være endret siden kopien ble cachet ved klienten. 

Heldigvis har HTTP en mekanisme som lar en nettbuffer verifisere at objektene sine er oppdaterte. Denne mekanismen kalles **conditional GET** (*norsk. betinget*). En HTTP request-melding er en såkalt betingen GET melding hvis (1) request-meldingen bruker GET-metoden og (2) request-meldingen inkluderer en `If-Modified-Since:`-headerlinje.

* Anta at en klient forespør et objekt og nettbufferen henter dette fra en webserver, og lagrer en kopi i bufferen sin. Nettbufferen lagrer dette objektet sammen med headerlinjen `Last-Modified:`. 
* En uke senere kommer en ny klient og ber om samme objekt. Siden objektet kan være endret den siste uken, så gjør nettbufferen en *betinget GET-request* til serveren, og får vite om filen er endret eller ikke (304 Not Modified-status).


### Electronic Mail in the Internet

Som vanlig post er eposter en asynkront kommunikasjonsmedium - folk svarer og leser meldinger når det passer dem. I motsetning til vanlig post er epost raskt, enkelt å distribuere og billig. Man kan legge til vedlegg, hyperlinker og HTML-formatert tekst. 
 
Vi skal å se på applikasjonslag protokollene som er hjertet av internettets eposter. 

![smtp](https://i.imgur.com/4KDPLOw.png)

Denne figuren inneholder mange komponenter som **brukeragenter**, **mailservere**, og **SMTP-protokollen** (*eng. Simple Mail Transfer Protocol*). Christian sender en epost til en mottaker Bob. brukeragentene lar brukere lese, svare, videresende, lagre meldinger. Apple Mail og Outlook er eksempler på brukeragenter for epost. Når Christian er ferdig med å skrive eposten sin sender brukeragenten hans meldingen til mailserveren hans, hvor meldingen blir plassert i mailserverens utgående meldingskø. Når Bob ønsker å lese meldinger vil lese meldingen, henter brukeragenten hans meldingen fra mailboksen i mailserveren hans. 

SMTP er hoved applikasjonsprotokollen for elektronisk post. Den bruker den pålitelige dataoverføringsprotokollen TCP. 

* Når en mailserver sender en mail til en annen mailserver, oppfører den seg som en SMTP-klient.
* Når en mailserver mottar en mail fra en annnen mailerver, oppfører den seg som en SMTP-server.



![smtp-ex](https://i.imgur.com/JVbbjQb.png)

1. Alice bruker brukeragenten hennes for epost, oppgir Bobs epost-adresse, skriver en melding og ber agenten sende eposten.
2. Alice sin brukeragent sender meldingen hennes til mailserveren hennes, og plasserer den i meldingskøen.
3. Klientsiden av SMTP, som kjører på Alice sin mailserver, ser meldingen i køen. Åpner en TCP-tilkobling til en SMTP-server, kjørende på Bob sin mail server.
4. Etter SMTP-handshaking, sender SMTP-klienten Alice sin melding gjennom TCP-tilkoblingen.
5. Ved Bob sin mailserver, vil server-siden av SMTP motta meldingen. Mailserveren til Bob lagrer så meldingen i mailboksen til Bob.
6. Bob spør så brukeragenten sin om å lese meldingen når han ønsker.



SMTP-klienten etablerer en TCP-tilkobling på port 25 hos SMTP-serveren. Når TCP-tilkoblingen er etablert, vil serveren og klienten utføre noen applikasjonslag-handshaking. SMTP-klientene og serverene introduserer hverandre før de sender informasjon. 

*Handshaking:*
> Server (S - `Hostname: hamburger.edu`)

> Client (C - `Hostname: crepes.fr`)

```
S: 220 hamburger.edu
C: HELO crepes.fr
S: 250 Hello crepes.fr, pleased to meet you
C: MAIL FROM: <alice@crepes.fr>
S: 250 alice@crepes.fr ... Sender ok
C: RCPT TO: <bob@hamburger.edu>
S: 250 bob@hamburger.edu ... Recipient ok
C: DATA
S: 354 Enter mail, end with “.” on a line by itself 
C: Do you like ketchup?
C: How about pickles?
C: .
S: 250 Message accepted for delivery
C: QUIT
S: 221 hamburger.edu closing connection
```

##### Sammenligning med HTTP

Begge protokoller brukes til å overføre filer fra et endesystem til en annet. HTTP overfører filer (kalt objekter) fra en webserver til en webklient (typisk nettleser). SMTP overfører filer (som er epost-meldinger) fra en mailserver til en annen mailserver. 

Når filene overføres bruker begge protokollene vedvarende/persistent tilkolbinger.

HTTP er i hovedsak en **pull protocol** - noen vil ha informasjon fra en nettserver og bruker HTTP for å hente informasjonen ved serveren etter deres ønske. Spesielt, TCP-tilkoblingen blir initialisert på maskinen som ønsker filen.

SMTP er på den andre siden en **push protocol** - den sendende mailserveren sender dytter filen til den mottakende mailserveren. Spesielt, TCP-tilkoblingen blir initialisert på maskinen som ønsker å sende filen. 

En annen forskjell er at SMTP krever at hver melding, inkludert kroppen til hver melding, skal være i 7-biters ASCII-format. Hvis meldingen inneholder tegn som ikke er 7-biters ASCII (for eksempel franske tegn med aksenter) eller inneholder binære data (for eksempel en bildefil), må meldingen kodes inn i 7-biters ASCII. HTTP-data pålegger ikke denne begrensningen.

HTTP innkapsler hvert objekt i sin egen HTTP-svarmelding. Internett-post plasserer alle meldingsobjektene i en melding.

##### Mail-format

```
From: alice@crepes.fr
To: bob@hamburger.edu
Subject: Searching for the meaning of life.

(melding)
```

#### Mail-aksess protokoller

![smtp-protokoller](https://i.imgur.com/YfOUYkC.png)

##### POP3 - Post Office Protocol v. 3

* Enkel epost-aksessprotokoll, derav liten funksjonalitet.
* OP3 begynner når en brukeragent (klienten) åpner en TCP-tilkobling til mailserveren (serveren) på port 110. Med TCP-tilkoblingen etabler begynner POP3 å gå igjennom tre faser: autoriserting, transaksjon og oppdatering.

	1. Autorisering: Brukeragent sender brukernavn og passord, for å autentisere brukeren. `user <username>` og `pass <password>`
	2. Transaksjon: Brukeragent bruker kommandoene `list`,`retr`,`dele` og `quit` for å få listet alle mailenes størrelser, retrievet innholdet i mail og slettet mail. 
	3. Oppdatering: Etter å ha behandlet `quit`-kommandoen, går POP3-serveren i oppdateringsfasen og fjerner meldinger fra postkassen.

* Under POP3-sessionen mellom en brukeragent og mailserveren, lagrer POP3-serveren noen tilstander, spesielt hvilke eposter som har blitt markert som slettet. Men lagrer det ikke til senere sessions. 



##### IMAP - Internet Message Access Protocol

Med POP3-tilgang så kan Bob slette, lagre, markere og organisere mailene sine i mapper og strukturer på sin lokale maskin. Men dersom han ønsker å kunne aksessere denne strukturen på enhver maskin, må denne organiseringen lagres på en ekstern server. Dette kan man med IMAP-protokollen. 

En IMAP-server vil assosiere en melding med en mappe, når en mail først innkommer er den assosiert med INBOX-mapen. IMAP-protokollen tillater en bruker å lage mapper, og flytte eposter til forskjellige mapper. 

##### Web-Based E-Mail

Flere og flere begynner å sende og aksessere epostene sine gjennom nettlesere. Med en slik tjeneste er brukeragenten en vanlig nettleser som kommuniserer med den eksterne mailboksen gjennom HTTP. 

Nettleseren bruker HTTP for å snakke med mailserveren istedet for POP3- eller IMAP-protokollen


### DNS - The Internet's Directory Service

* En internett vert er identifisert med `hostname`, som *cnn.com* eller *www.yahoo.com*, også IP-adresser, som *121.7.106.83*


#### Tjenester tilbudt av DNS

Vi har nettopp sett at det er to måter å identifisere en vert ved, med vertsnavn og en IP-adresse. Folk foretrekker den mer lettleselige vertsnavnidentifikatoren, mens rutere foretrekker IP-adresser. For å forene disse innstillingene trenger vi en katalogtjeneste som oversetter vertsnavn til IP-adresser. Dette er hovedoppgaven til internettets **domain name system** (**DNS**).

DNS-en er *(1)* en distribuert database implementert i et hierarki av DNS-servere, og *(2)* en applikasjonslagsprotokoll som tillater verter å sende spørringer til den distribuerte databasen

* DNS brukes vanligvis av andre protokoller for applikasjonslag, inkludert HTTP og SMTP, for å oversette brukerleverte vertsnavn til IP-adresser.


Dette skjer dersom en nettleser ber om URL-en *www.someschool.edu/index.html*:

1. Samme brukermaskin kjører klientsiden til DNS-applikasjonen
2. Nettleseren henter vertsnavnet, *www.someschool.edu*, fra URL-en og gir det til klientsiden av DNS-applikasjonen.
3. DNS-klienten sender en spørring med vertsnavnet til DNS-applikasjonen
4. DNS-klienten mottar etterhvert en respons, inkludert IP-adressen for vertsnavnet
5. Når nettleseren får IP-adressen fra DNS, kan den initialisere en TCP-tilkobling til HTTP-server-prosessen på port 80 på den IP-adressen.


* **Vertsnavn aliaser:** Verter med kompliserte navn kan ha vertsnavnaliaser for å gjøre vertsnavnene lettere for mennesker å lese og huske. Da må nettleseren bruke DNS for å få hentet det kanoniske (lange og kompliserte) vertsnavnet sammen med den korresponderende IP-addressen

* **Mailserver aliaser:** Nettsider med stor trafikk er ofte replikert over flere servere, der hver server kjører på forskjellige endesystemer med hver sin IP-adresse. For replikerte webservere, et sett av IP-adresser, er er da assosiert med ett kanonisk vertsnavn, som *cnn.com*. Når en nettleser spør om IP-adressen til vertsnavnet får man returnert hele settet med IP-adresser, som nettleseren velger en fra, gjerne den første i settet.

* **Lastfordeling:** DNS er også brukt til lastfordeling på replikerte servere, som replikerte webservere. Når en nettleser ber om en IP-adresse til et vertsnavn med replikerte webservere, får den et sett med IP-adresser. Rekkefølgen på disse IP-adressene blir bestemt av DNS-en..


##### Hvordan funker DNS

* Applikasjonen vil bruke klientsiden av DNS, og spesifiserer vertsnavnet som skal bli oversatt. på UNIX-baserte maskiner, brukes ofte funksjonen *gethostbyname()*. DNS-en lager så en spørring som sendes i nettverket. Alle DNS-spørringer sendes med UDP datagrammer på port 53. 

* Etter en forsinkelse på alt fra millisekunder til sekunder, får DNS-en i brukerens vert DNS-responsmeldingen med den ønskede mappingen. 


I et enkelt design for DNS, ville det ha vært en DNS-server som har alle mappingsene. I dette sentraliserte designe kan det være flere problemer:

- *Single point of failure.* Dersom DNS-serveren krasjer, gjør også hele internettet
- *Traffic volume.* En enkel DNS server må håndtere alle DNS-spørringer (for alle HTTP-requestene og epostene generert av flere undre millioner verter)
- *Langveis sentralisert database.* En enkelt DNS-server kan ikke være nærme alle de spørrende klientene. Dette kan føre til forsinkelser.
- *Vedlikeholding.* EN enkelt DNS-server vil måtte holde data for alle verter på internettet. Ikke bare vil denne sentraliserte databasen være stor, men måtte oppdateres 


**En distribuert, hierkisk database:**

![DNS1](https://i.imgur.com/te3HQ2s.png)

* Dersom en klient vil ha IP-adressen til *amazon.com*, vil man først spørre en av rot-serverene som vil gi ip-adresser for TLD-serverene (*top-level-domain*) på top-nivå-domenet *com*. Klienten kontakter så en av disse TLD-serverene og får returnert IP-adressen til *amazon.com*

* **Rot-DNS-servere.** Finnes 13 stk i verden (A-M). En rot-DNS-server er et nettverk av replikerte servere.
* **Top-nivå-domene-servere (TLD).** Disse serverene er ansvarlige for top-nivå-domener slik som *com*, *net*, *edu* og *gov*.
* **Autorative DNS-servere.** Hver organisasjon med offentlig tilgjengelige verter på internettet på gi offentlig aksessbare DNS-data som mapper alle vertsnavnene til IP-adresser.
* **Lokal DNS-server**. En lokal DNS-server hører ikke til i hierarkiet av servere, men er likevel sentral i DNS-arkitekturen. Hver ISP har en lokal DNS-server. Når en vert kobler seg på en ISP, vil ISPen gi vertens IP-adressen til en av dens lokale DNS-servere. Når man gjør en DNS-forespørsel vil den først gå gjennom den *lokale DNS-serveren*, som vil oppføre seg som en proxy.

 ![dns2](https://i.imgur.com/eQGIQ8m.png)
 
 ![dns3](https://i.imgur.com/iRysZbd.png)
 
 
##### DNS Caching:

En kritisk del av DNS-systemet. DNS utnytter i stor grad DNS-caching for å forbedre forsinkelsesytelsen og redusere antall DNS-meldinger som sendt rundt på internettet.

Ideen bak DNS-caching er veldig enkel. I en spørringskjede, når en DNS-server mottar et DNS-svar (som for eksempel inneholder en mappingen fra et vertsnavn til en IP-adresse), kan det cache mappingen i sitt lokale minne.



#### DNS poster og meldinger

DNS-serverne som sammen implementerer den distribuerte DNS-databasen lagrer **ressursposter** (**RRs - Resource Records**), inkludert RR-er som gir vertsnavn-til-IP-adresse mappinger. Hver DNS response-melding bærer en eller flere resurrsposter.

En ressurspost er en fir-tuppel med følgende felter:

`(Name, Value, Type, TTL)`

* Dersom `Type=A`, da er `Name` vertsnavn og `Value` er IP-adressen til vertsnavnet

* Dersom `Type=NS`, da er `Name` et domene og `Value` er vertsnavnet til den autorative DNS-serveren

* Dersom `Type=CNAME`, da er `Name` vertsnavn-alias og `Value` er kanonisk vertsnavn

* Dersom `Type=MX`, da er `Name` vertsnavn-alias og `Value` er kanonisk vertsnavn for mailserver


##### DNS-meldinger

Jeg har tidligere nevt DNS-spørringer og respons-meldinger. Dette er de to typene vi har av DNS-meldinger. Slik er semantikken til DNS-meldinger:

* De første 12 bytene er *header-seksjonen*, som har et antall felter. Første feltet er et 16-bit nummer som identifiserer spørringen. Denne identifikatoren blir kopiert over i respons-meldingen. Det er også et antall flagg. En 1-bit *query/reply-flagg* indikerer spørring(0) og respons(1). Andre 1-bit flagg er *authoritative-*, *recursion-desired* og *recursion-available*. Ellers er det også også 4 antall-av-felt. Disse feltene indikerer antall av forekomster av dataseksjonene under headeren.

* *Spørsmålseksjonen* inneholder informasjonen om spørringen som skal bli gjort. Denne seksjonen inneholder:
	* Navn-felt med navn på det skal bli forespurt
	* Typefelt som indikerer typen spørring (Type A eller f.eks. Type MX)

* *Svarseksjon*, i et svar fra en DNS-server, inneholder ressurspostene for navnet som i utgangspunktet ble forespurt.

* *Autoritetsseksjonen* inneholder poster av andre autorative servere.

* *Tilleggsseksjonen* inneholder andre hjelpfulle poster.  

 
##### Innsetting i DNS Databasen

Når man lager et nytt domene må man gjøre dette gjennom en **registrar**. En registrar er en kommersiell enhet som bekrefter det unike domenenavnet, går inn i domenenavnet i DNS-databasen, og samler en liten avgift fra deg for sine tjenester.

Dersom en ny nettside skal innsettes, og en antar at navnene og IP-adressene er *dns1.networkutopia.com, dns2.networkutopia.com, 212.212.212.1,* og *212.212.212.2. *. Da må en sette inn følgende ressurspostene i DNS-systemet:

* (*networkutopia.com*, *dns1.networkutopia.com*, NS)
* (*dns1.networkutopia.com*, *212.212.212.1*, A)




### Peer-to-Peer Application

Applikasjonene introdusert hittil - inkludert Internettet, epost og DNS - er alle klient-server arkitekturer som avhenger av alltid-på infrastruktur servere.

I P2P-arkitektur er det minimal (eller ingen) avhengighet av alltid-på-infrastruktur servere. I stedet kommuniserer par av tilkoblede verter, kalt peers, direkte med hverandre.

Vi skal se på applikasjoner som er spesielt velegnet for P2P-design. Den vi skal se på er filfordeling, hvor applikasjonen fordeler en fil fra en enkelt kilde til et stort antall peers. Fildistribusjon er et fint sted å starte vår undersøkelse av P2P, da det tydeligvis avslører selvskalering av P2P-arkitekturer.

#### P2P Fildistribusjon

Vi skal se på å distribuere en stor fil fra en enkelt server til et stor antall verter (kalt peers). I en P2P fildistribusjon kan hver peer redistribuere enhver del av filen som den har mottatt fra andre peers, og dermed hjelpe serveren med å distribusjonsprosessen.

I 2012 var den mest fildistribusjonsprotokollen BitTorrent. 


#### Skalerbarhet av P2P-arkitekturer

For å sammenlikne klient-server arkitekturer med P2P-arkitekturer og illustrere den iboende selv-skalerbarheten til P2P, skal vi se på en enkelt model for å distribuere en fil til et antall peers med begge arkitekturene. 

Som vist i figuren under er både server og klienter koblet til internettet med aksesskoblinger. Betegn opplastningsraten til serveren er u<sub>s</sub>, opplastningsraten til det *i*-te peers aksesskobling er u<aub>i</sub>, og nedlastningsraten til det *i*-te peers aksesskobling er d<aub>i</sub>.

Betegn også størrelsen på filen til å bli distribuert med *F*, og antall peers osm vil ha filen er *N*.

![fildistribusjon](https://i.imgur.com/jzRrAHk.png)

**Distribusjonstiden** er tiden det tar for at alle peers-ene får en kopi av filen. 


La oss først regne ut distribusjonstiden for **klient-server-arkitekturen**, som vi betegner D<sub>*cs*</sub>. I denne arkitekturen hjelper ingen av peers-ene med på å distribuere filen. Vi gjør følgende observasjoner:

* Serveren må distribuere *F* bits til *N* peers. Det vil si sende *NF* bits. Siden serveren har en opplastningsrate på u<sub>s</sub>. Da blir distribusjonstiden minst *NF/u<sub>s</sub>*.
* La *d<sub>min</sub>* være nedlastningsraten til peeren med den laveste nedlastningsraten. Derfor vil distribusjonstiden være minst *F/d<sub>min</sub>*.

Setter vi sammen disse observasjonene får vi, 
D<sub>*cs*</sub> ≥ max { *NF/u<sub>s</sub>*, *F/d<sub>min</sub>* }



La oss nå regne ut distribusjonstiden for *peer-to-peer-arkitekturen*, som vi betegner D<sub>*P2P*</sub>. Vi gjør følgende observasjoner:

* Ved begynnelsen av distribusjonen, er det kun serveren som har filen. For å få denne filen til et fellesskap med peers, må serveren sende filen minst en gang gjennom aksesskoblingen. Dermed må distribusjonstiden være minst *F/u<sub>s</sub>*
* Som i klient-server-arkitekturen, kan ikke peeren med lavest nedlastningsrate få filen kjappere enn *F/d<sub>min</sub>* sekunder. Som blir et minimum for distribusjonstiden.
* Til slutt, observer at den totale opplastningskapasiteten til systemet som en helhet er opplastningsraten til serveren pluss opplastningsraten til alle de individuelle peers-ene. Systemet må laste opp F bits til hver av de N peer-ene, altså *NF* bits. Dette kan ikke bli gjort kjappere enn *NF/(u<sub>s</sub> + u<sub>1</sub> + ... + u<sub>N</sub>)*.

Setter vi sammen disse observasjonene får vi,
D<sub>*P2P*</sub> = max {*F/u<sub>s</sub>* , *F/d<sub>min</sub>* , *NF/(u<sub>s</sub> + ∑ u<sub>i</sub>* }


### Socket Programming: Creating Network Applications

Nå har vi sett på et antall viktige nettverksapplikasjoner, nå skal vi se på hvordan nettverk applikasjons-programmer blir laget. Husk fra Kap. 2 at en typisk nettverksappliksjon består av et par av programmer - et klientprogram og et serverprogram - liggende på to forskjellige endesystemer.

Når disse programmene startes, startes en klientprosess og en serverprosess, og disse prosessene kommuniserer med hverandre gjennom sockets (*norsk. nettverkssocket*)

Det finnes to typer nettverksapplikasjoner:

* Den ene typen er en implementering der operasjoner er spesifisert i en protokollstandard, for eksempel en RFC eller et annet standarddokument. Et slikt program kalles noen ganger "åpen", siden reglene som angir operasjonen er kjent for alle. For en slik implementering må klient- og serverprogrammene overholde de regler som er angitt av RFC.

* Den andre typen nettverksapplikasjon er et proprietært nettverksprogram. I dette tilfellet bruker klient- og serverprogrammene en protokoll for applikasjonslag som ikke har blitt offentliggjort i en RFC eller et annet sted. Utvikleren har full kontroll over hva som skjer i koden. 

Når en skal utvikle en klient-server applikasjon, må man først bestemme seg for om applikasjonen skal kjøre over TCP eller over UDP. 

* TCP: Koblingsorientert og pålitelig dataoverføring
* UDP: Koblingsløs og sender uavhengige pakker av data uten leveringsgaranti.

#### Sock Programming with UDP

Vi kan se på hver prosess som et hus og hver socket som døren. Når man bruker UD, må man først legge til destinasjonsadressen på pakken. Etter at pakken går igjennom senderens socket, il internettet bruke destinasjonsadressen til å guide pakken frem til socketen på den mottakende prosessen. 

Denne destinasjonsadressen er destinasjonsvertens *IP-adresse*, samt *portnummeret* til socketen. I tillegg legges også ved senderens IP-adresse og portnummer, men dette gjøres *ikke* av UDP-applikasjonskoden, men det underliggende systemet. 

Vi bruker følgende klient-server-applikasjon for å demonstrere programmering for både UDP og TCP:

1. Klienten leser linjer av karakterer (data) fra tastaturen og sender dataen til serveren.
2. Serveren mottar dataen og konverterer karakterene til blokkbokstaver.
3. Serveren sender den modifiserte dataen til klienten.
4. Klienten mottar den modifiserte dataen og viser linjen på skjermen. 


![UDP2](https://i.imgur.com/s4ebPze.png)


**UDPClient.py:**
```python
from socket import *
serverName = ‘hostname’
serverPort = 12000
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM) 
message = raw_input(’Input lowercase sentence:’) 
clientSocket.sendto(message,(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print modifiedMessage
clientSocket.close()
```

**UDPServer.py:**
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((’’, serverPort))
print ”The server is ready to receive” 
while 1:
	message, clientAddress = serverSocket.recvfrom(2048) 
	modifiedMessage = 	message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)

```


#### Socket Programming with TCP

I motsetning til UDP, er TCP en tilkoblings-orientert protokol. Dette betyr at klienten og serveren må handshake og etablere en TCP-tilkobling før de kan sende data til hverandre. 

Her kan serveren eller klienten kun slippe data ned i TCP-koblingen, uten å måtte legge ved ekstra data som ved UDP. 


![TCP2](https://i.imgur.com/wvn7fnC.png)

**TCPClient.py:**

```python
from socket import *
serverName = ’servername’
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) clientSocket.connect((serverName,serverPort))
sentence = raw_input(‘Input lowercase sentence:’)
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print ‘From Server:’, modifiedSentence 
clientSocket.close()
```

**TCPServer.py:**

```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((‘’,serverPort)) serverSocket.listen(1)
print ‘The server is ready to receive’ 
while 1:
	connectionSocket, addr = serverSocket.accept() 
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper() 	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
```

![TCP3](https://i.imgur.com/OOzeIrn.png)


### Oppsummering

* Applikasjonslagsprotokoller: HTTP, FTP, SMTP, POP3, IMAP og DNS
* Transportlagprotokoller: TCP, UDP


<br></br>
<br></br>

<a name="kap3"></a>
## Kapittel 3 - Transport Layer

### Introduction and Transport-Layer Services

En transportlagsprotokol tilbyr **logisk kommunikasjon** mellom applikasjonsprosesser kjørende på forskjellige verter. Med *logisk kommunikasjon* snakker vi fra en applikasjonsprosess, det blir som at vertene er direkte sammenkoblet, men i virkeligheten kan det hende at de er på forskjellige sider av jorden. 


Transportlagsprotokoller er implementert i endesystemer, men ikke i rutere. 

På den **sendende** siden vl trasportlaget konverterer applikasjonlags-meldingene den mottar til transportlag-pakker, som er kjent som transportlag **segmenter**.
Dette blir gjort ved å dele applikasjonsmeldingene opp i enda mindre biter, og legge på transportlags-headeren til hver bit, for å lage transportlagssegmentet. 
Transportlaget sender så segmentet til netverkslaget, hvor segmenetet blir innkapslet i en nettverklagspakke (*datagram*), og sendt til destinasjonen. Det er viktig å notere seg at nettverksrutere bare benytter seg av nettverklagsfeltene på datagrammet.

På den **mottakende** siden, henter nettverkslaget segementet innkapslet i datagrammet opp til transportlaget. Transprtlagt prosesserer det mottatte segmentet, og gjør dataen tilgjengelig for den mottakende applikasjonen.


* Det er flere enn en transportlagsprotokoll som er tilgjengelig for nettverksapplikasjoner. F.eks. har internettet to protokoller - TCP og UDP. Hver av disse protokollene tilbyr forskjellige sett med transportlagstjenester.


#### Forholdet mellom transport- og nettverkslaget

Minnes om at transportlaget ligger rett over nettverklaget i protokollstakken.
Mens en transportlagsprotokoll gir logisk kommunikasjon mellom prosesser som kjører på forskjellige verter, gir en nettverkslagprotokoll logisk kommunikasjon mellom verter. Denne forskjellen er subtil men viktig. La oss undersøke dette skillet ved hjelp av en husstandsanalyse.

* Se på to hus, ett på østkanten og et på vestkanten, og i hvert hus bor et dusin barn. Barna på østkanten søskenbarn med de på vestkanten. De liker å skrive brev til hverandre. I begge husstandene er det ett barn - Ann på vestkanten og Bill på østkanten - som er ansvarlige for å hente og levere port. Hver uke går Ann og Bill rundt og henter brev fra søskenen sine, leverer og henter posten, og leverer brev til søsknene sine.
	* I dette eksempelet tilbyr posten logisk kommunikasjon mellom de to husene. Ann og Bill tilbyr logisk kommunkasjon mellom søskenbarn. Analogien var slik:

	```
	applikasjonsmeldinger = brev i konvolutt
	prosesser = søksenbarn
	verter (endesystemer) = hus
	transportlagsprotokoller = Ann og Bill
	nettverklagsprotokoller = postvesenet
	```

![nettverkslaget](https://i.imgur.com/L8MALDb.png)


Visse tjenester kan bli tilbudt av transportprotokoller, selv når de underliggende nettverksprotokollene ikke tilbyr samme tjeneste på nettverkslaget. For eksempel kan en transportprotokoll tilby pålitelig dataoverføring til en applikasjon, selvom den underliggende nettverksprotokollen er upålitelig.  

#### Oversikt over transportlaget på internettet

Minnes at internettet, eller mer generelt et TCP/IP internett, har to distinkte transportlagsprotokoller tilgjengelige for appliksjonslaget. 

* Den første er **UDP** *(User Datagram Protocol)*, som tilbyr en upålitelig, koblingsløs tjeneste. 
* Den andre er **TCP** *(Transmission Control Protocol)*, som tilbyr pålitelig, koblingsorientert tjeneste til den brukende applikasjonen. 
	* TIlbyr flow control, congestion control, sequence numbers, acknowledgments og timere

> Når man skal lage en nettverksapplikasjon m man velge mellom UDP og TCP når man skal lage nettverkssockets. 

> En protokoll som tulbyr pålitelig dataoverføring og metningskontroll er nødvendigvis kompleks.


* Vi refererer til transportlagspakker som **segmenter** og nettverklagspakker som **datagrammer**.

Internettets nettverksprokol kalles **IP** (*Internet Protocol*), som tilbyr logisk kommunikasjon mellom verter. IP-tjenestemodellen er en **best-effort delivery service**. Hvilket betyr at IP gjør så godt den kan for å levere segmenter mellom verter, men *gir ingen garanti*, IP er derfor sagt å være en **upålitelig tjeneste**.

For å oppsummere:

Det mest grunnleggende ansvaret for UDP og TCP er å utvide IPs leveringstjeneste mellom to endesystemer til en leveringstjeneste mellom to prosesser som kjører på endesystemene. Utvidelse av **vert-til-vert**-levering til **prosess-til-prosess**-levering kalles *transportlagsmultipleksering* og *demultipleksing*.


### Multipleksing og Demultipleksing

Ved destinasjonsverten mottar transportlaget segmenter fra nettverkslaget rett under. Transportlaget har ansvaret for å lvere daten i segmentene til den riktige applikasjonsprosessen hos verten.

* Anta at du laster ned nettsider, samtidig som du laster ned en fil med FTP og har to Telnet-sessioner. Da har man 4 prosesser kjørende - to Telnet-, en FTP- og en HTTP-prosess. Når transportlaget mottar data fra nettverkslaget må den sende dataen til en av disse prosessene.

En prosess ka ha mer enn en **socket**, som fungerer som dører som data går igjennom fra nettverket til prosessen, og motsatt. Som Figur 3.2 viser, så vil transportlaget på den mottakende verten levere dataen til en mellomliggende socket, ikke direkte til prosessen. 

Hvert transportlags-segment har et sett med felt i segmentet. Ved mottakeren undersøker transportlaget disse feltene for å identifisere den mottakende socketen og leder deretter segmentet til denne socketen. 

Denne jobben med å levere dataene i et transportlagsegment til *riktig socket* kalles **demultiplexing**. Arbeidet med å samle databiter ved kildeverten fra forskjellige sockets, innkapsling av hver data-bit med header-informasjon (som senere vil bli brukt i demultiplexing) for å opprette segmenter, og å sende segmentene til nettverkslaget kalles multiplexing.

![multi-demult](https://i.imgur.com/MnuMtxt.png)

Transportlags multipleksing krever:

1. Sockets har unike identifikatorer
2. Hvert segment har spesielle felt, som indikerer hvilken socket segmentet skal bli levert hos. 

Disse spesielle feltene er **kilde-port-nummeret** og **destinasjons-port-nummeret**:

![segment1](https://i.imgur.com/zlaI7AS.png)

>  Hvert portnummer er et 16-biters nummer, alt fra 0 til 65535.
>  Når vi lager en ny applikasjon må vi tildele applikasjonen et portnummer.


#### Koblingsløs multipleksing og demultipleksing - UDP

Dersom vi kobler lager en UDP-socket og kobler den opp til et portnr, kan vi beskrive hvordan UDP multipleksing/demultipleksing.

	```python
	clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientSocket.bind((‘’, 19157))
	```
> En UDP-port er identifisert med en tuppel av to-tuppel av (*destinasjons IP-adresse, destinasjons port*)

La oss tenke oss at Vert A, med UDP-port 19157, ønsker å sende en haug med data til en prosess med UDP-port 46428 hos Vert B. Da lager transportprotokollen i Vert A et transportlags-segment som inkluderer dataen, klideportnummeret (19157), destinasjonsportnummeret (46428), og to andre verdier (ikke viktig enda). Transportlaget sendr så segmentet til nettverkslaget, som innkapsler segmentet i et IP-datagram og prøver å levere det.

Dersom segmentet kommer frem til Vert B, vil transportlaget eksaminere destinasjonsportnummeret på segmentet (46428), og levere det hos socketen identifisert med portnr 46428. 

Kildeportnummeret brukes som en *retur-adresse*, dersom Vert B ønsker å sende noe til Vert A. I python brukes metoden `recvfrom()` for å hente kildeportnummeret.

> To segmenter med samme kilde-portnummer og/eller kilde-IP-adresse vil kunne sendes til samme socket.




#### Koblings-orientert multipleksing og demultipleksing - TCP

En forskjell på en TCP-socket og en UDP-socket er at en TCP-socket er identifisert med en firtuppel (*kilde-IP-adresse, kilde-portnummer, destinasjons IP-adresse, destinasjons portnummer*). Når et TCP-segment ankommer verten, brukes alle fire verdiene for å demultiplekse segmentet til riktig socket. 

I kontrast med UDP, vil to ankommende TCP-segmenter med forskjellig kilde IP-adressser eller kilde-portnummer (med unntak av et TCP-segment som bærer den opprinnelige tilkoblings-etableringsforespørselen) sendes til to forskjellige porter.  


La oss se på TCP klient-server programmeringen fra forrige kapittel:

* TCP-serverapplikasjonen har en "welcoming sockt" som venter på tilkoblingsforespørsler fra TCP-klienter.
* TCP-klienter lager en socket og snder en tilkoblingsforespørsel til TCP-serveren.
* En tilkoblingsforespørsel er bare et TCP-segment med destinasjonsportnummer, og et spesielt tilkoblingsforespørsel-bit-set i TCP-headeren, i tilegg til kilde-portnummer.
* Når serveren får tilkoblingsforespørselen og aksepterer forespørselen, og serverprosesen lager en ny socket. 
	* Serveren noterer følgede felt fra tilkoblingsforespørsel-segmentet: (1) kilde-portnummer, (2) kildens IP-adresse, (3) destinasjons-portnummeret, (4) sin egen IP-adresse. Alle senere TCP-segmenter med disse verdiene vil bli demultiplekset til denne porten. 

	
 
 ![mult-demult](https://i.imgur.com/TeCYBtb.png)
 
 Situasjonen i Figur 3.5, der Vert C initialiserer to HTTP-sesjoner til server B, og Vert A initialiserer én HTTP-sesjon til server B. Vert A, C og server B har unike IP-adresser. Vert C tilegner to forskjellige portnummer (26145 og 7532) for sine to HTTP-koblinger. Siden A har valgt et kilde-portnummer uavhengig av C, som kanskje også er samme som C, er ikke dette noe problem å ha samme kilde-portnr siden de to tilkoblingene har forskjellige kilde-IP-adresser. 
 
> Både de opprinnelige tilkoblingsforespørsels-segmentene og segmentene som bærer HTTP-request-meldinger, vil ha destinasjonsport 80. 


### Connectionless Transport: UDP

UDP gjør omtrent like lite som en transportprotokoll kan gjøre. Bortsett fra multiplesking og demultipleksing og noen få enkle feilskjekker, legger den ingenting til IP. 

Faktsik hvis applikasjonsutvikleren velger UDP istedet for TCp, snakker applikasjonen nesten direkte med IP. UDP tar imot meldinger fra applikasjonsprosessen, legger til feltene *kilde- og destinasjonsportnummer*  for multipleksing / demultipleksing-tjenesten, legger til to andre små felt og overfører det resulterende segmentet til nettverkslaget.

Nettverkslaget innkaplser transportlagssegmentet i et IP-datagram og gjør deretter sitt beste forsøk på å levere segmentet til mottakeren. Hvis segmentet kommer til mottakeren, bruker UDP destinasjonsportnummeret til å levere segmentets data tl den riktige socketen / appliksjonsprosessen.


> I UDP er det **ingen handshaking** mellom de sendende og mottakende transportlags-entitetene før sending av et segment. På grunn av dette sies UDP å være ***koblingsløs***. 

DNS er et eksempel på en appliksjonslagsprotokoll som bruker UDP. Når DNS-applikasjonen hos en vert ønsker å gjøre en spørring så lager den en DNS-spørringsmelding og sender meldingen til UDP. Dersom DNS-applikasjonen hos den spørrende verten ikke får svar vil den sende enten en ny spørring til en annen DNS-server eller fortelle applikasjonen at den ikke får svar. 

Grunner for at mange appliksjoner vil heller bruke UDP, fremfor TCP:

* *Finere applikasjonsnivå kontroll over hvilke data som er sendt, og når.* Når man sender data til UDP vil UDP pakke daten inn i et UDP-segment og sende pakket umiddelbart til nettverkslaget. TCP har derimot en overbelastningskontroll (*congestion control* som sprer transportlagets  TCP-avsender når en eller flere koblinger mellom kilde- og destinasjonsverten blir for overbelastede.

* *Ingen tilkoblingsetablering*. TCP bruker en tre-veis handshake, før den begynnner å sende data. UDP, derimot, begynner å sende data uten noen formell innledning. Dermed er det ingen forsinkelse hos UDP for å opprette tilkobling. Dette er nok hovedgrunnen til at DNS kjører over UDP istedet for TCP. (Ville være mye tregere over TCP)

* *Ingen tilkoblingstilstand*. TCP vedlikeholder tilkoblingstilstanden i endesystemene. Denne tilkoblingtilstanden inkluderer motta- og sende-buffere, congestion-control-parametere, og sekvens- og bekreftelsesnummer-parametere. UDP har ingen av disse parameterene, og en server kan typisk støtte flere aktiv klienter når applikasjonsjonen går over UDP enn TCP. 

* *Små pakke-header overhead.* TCP-segmentet har 20 bytes av header overhead (sum av alt som ikke er data) i hvert segment, derimot har UDP kun 8 bytes av overhead. 

![tcp.vs.udp](https://i.imgur.com/lyAprK3.png) 


Som nevnt tidligere har UDP *ingen congestion control*. Dersom alle skulle begynt å strømme høy-bit-rate video uten noen congestion control, ville det ha vært så stor overflow hos ruterne at veldig få UDP-pakker ville suksessfullt ha traverst over kilde-til-destinasjonsruten.

Dermed kan mangelen på congestion control i UDP resultere i høye tapsrater mellom en UDP-avsender og mottaker, og overbelastningen av TCP-økter. 

Selvom man bruker UDP, som er upålitelig, *er* det mulig for en applikasjon å ha pålitelig dataoverføring med UDP. Dette kan bli gjort med å implementere pålitelighet i applikasjonen selv (f.eks. med bekreftelses- eller re-sendings-mekanismser.


#### UDP-segmentstruktur

Strukturen til et UDP-segment er som beskrevet i Figur 3.7. Applikasjonsdataen tar datafeltet i segmentet. F.eks. for DNS, vil data-feltet inneholde en spørringsmelding eller en responsmelding. 

Header-feltet har kun fire fleter, hver besåtende av to bytes. Som diskutert i forrige delavsnitt lar portnummerene destinasjonsverten levere dataen til riktig prosess (demultipleksingsprosessen). `Length`-feltet spesifiserer antall bytes i UDP-segmentet (*header + data*). `Checksum`-en er brukt av den mottakende verten for å skjekke om det har skjedd noen feil med segmentet.

![UDP-struktur](https://i.imgur.com/Z0y38kz.png)


#### UDP Checksum

UDP Checksum-en sørger for feilsøking. Det bety, at checksummen blir brukt for å bestemme om noen av bitene i UDP-segmentet har blitt endret på under reisen fra kilde til destinasjon. 

UDP på den sendende siden utfører 1s komplement på **summen** av alle 16-bit ord i segmentet. Dette resultatet blir puttet i `Checksum`-feltet til UDP-segmentet. 
	
<pre>
	<li><i>16-BIT ORD:</i></u>
	<i>I:</i>		011001
	<i>II:</i>		010101
	<i>III:</i>	100011
	
	<li><i>SUM I = I + II</i>
		011001
	+	010101
	<u>=   101110</u>
		
	<li><i>SUM II = SUM I + III</i>
		101110
	+	100011
	<u>=   010001</u>
		 
	<li><i>1s KOMPL. SUM II:</i>
	<u>=   101110</u>

	<b>Checksum = 101110</b>
</pre>



### Principles of Reliable Data Transfer

Dersom en tjenestemodell er pålitelig blir ingen overførte data-bit korrupte (vendt fra 0 til 1, eller omvendt) eller mistet, og alle leveres i den rekkefølgen de ble sendt i. Dette er nettopp tjenestemodellen som tilbys av TCP til Internett-applikasjoner som påberoper den.

Det er ansvaret for en *pålitelig dataoverføringsprotokoll* for å implementere denne tjenesteabstraksjonen. 

Denne oppgaven er vanskelig av det faktum at laget under den pålitelige dataoverføringsprotokollen *kan* være *upålitelig*. For eksempel er TCP en pålitelig dataoverføringsprotokoll som implementeres på toppen av et upålitelig (IP) ende-til-ende nettverkslag.

![rdt](https://i.imgur.com/RAuCi7f.png)

> *rdt = reliable data transfer*
>
> *udt = unreliable data transfer*


Vi skal å se på tilfellet av **enveis dataoverføring**, det vil si dataoverføring fra sendingen til mottakssiden. Saken om pålitelig **toveis** (det vil si fullsidig) **dataoverføring** er begrepsmessig ikke vanskeligere, men betydelig mer kjedelig å forklare.

#### Bygge en pålitelig dataoverføringsprotokoll

Vi skal nå se på en rekke protokoller, der hver blir mer kompleks og slutter med en feilfri, pålitelig dataoverføringsprotokoll.

**Pålitelig dataoverføring over en perfekt pålitelig kanal: rdt1.0:**

Tilstandsmaskinen (*eng. finite state machine - FSM*) definert for rdt1.0 er vist i Figur 3.9. Siden alt skjer over en helt fullstendig pålitelig kanal, trenger ikke den mottakende siden å gi noen feedback til den sendende siden - siden ingenting kan gå galt i kanalen.

![1.0](https://i.imgur.com/OBo0ah1.png)


**Pålitelig dataoverføring over en kanal med bitfeil: rdt2.0**

Her implementeres feedback-meldinger som **positive acknowledgements** ("OK") og **negative acknowledgements** ("Vær snill å gjenta."). Pålitelig dataoverføringsprotokoller som baserer seg på retransmitting er kjent som **ARQ (Automatic Repeat reQuest) protokoller**. 

Tre tilleggstjenester er krevt i ARQ-ptrokoller for å håndtere forekomst av bitfeil:

* *Feilsøking.* En mekanisme som lar mottaker skjekke om det har skjedd noen bit-endringer. Her benyttes *checksum*-feltet.
 
* *Tilbakemelding fra mottaker.* Siden sender og mottaker typisk kjører på forskjellige endesystemer, må mottakeren eksplisitt gi tilbakemelding til senderen. Positive (*ACK*) eller negative (*NAK*) bekreftelser er eksempler på slik tilbakemelding. Her kan 0 (NAK) eller 1 (ACK) benyttes.
 
* *Re-sending*. En pakke som mottas med feil ved mottakeren, blir sendt igjen av avsenderen.
	
Figuren under (3.10) viser tilstandsmaskinen til *rdt2.0*, en dataoverføringsprotokoll som har feilsøking, positive og negative bekreftelser.

![rdt2.0](https://i.imgur.com/fm9kfPz.png)

Her vil ikke senderen kunne sende noe mer data, før den har fått vite at mottakeren har mottat pakken. På grunn av dette kaller vi slike protokoller for **stop-and-wait**-protokoller. 


Det ser kanskje ut som protokoll *rdt2.0* fungerer, men uheldigvis så har den en kjempefeil. Vi har ikke tatt i beregning av at ACK eller NAK pakkene kan være korrupte! 

Vi kan innføre sekvensnummer. Mottakeren trenger kun å skjekke dette sekvensnummeret for å mestemme om den motatte pakken er en re-sending.

Figurene under er tilstandsmaskinen for *rdt2.1*, som nå har dobbelt så mange tilstander.

Dette skyldes at protokollstaten nå må gjenspeile om pakken som nå sendes (av avsenderen) eller er forventet (ved mottakeren), skal ha et sekvensnummer på 0 eller 1. 
Merk at handlingene i de tilstandene der en 0-nummerert pakke blir sendt eller forventet er speilbilder av de der en 1-nummeret pakke sendes eller forventes - De eneste forskjellene har å gjøre med håndteringen av sekvensnummeret.

Protokoll *rdt2.1* bruker både positive og negative bekreftelser fra mottakeren til avsenderen.

* Når en out-of-order-pakke mottas, sender mottakeren en positiv bekreftelse for pakken den har mottatt.
* Når en ødelagt pakke er mottatt, sender mottakeren en negativ bekreftelse.  
	* Vi kan oppnå samme effekt som en NAK hvis vi, i stedet for å sende en NAK, sender en ACK for den sist riktig mottatte pakken. 
* En avsender som mottar to ACKs for samme pakke (det vil si mottar duplikat ACKer) vet at mottakeren ikke mottok riktig pakken etter pakken som blir ACKed to ganger

![rdt2.1s](https://i.imgur.com/chx6OpT.png)

![rdt2.1r](https://i.imgur.com/7YUw2SH.png)

> Dersom vi legger til sekvensnummeret til pakken som blir ack-et, kan vi få en NAK-fri pålitelig dataoverføringsprotokoll.


**Pålitelig dataoverføring over en tapende kanal med bitfeil: rdt3.0**

Dersom en pakke ikke kommer frem i det hele tatt, så må senderen re-sende pakken. Dersom man implementerer en timer, som re-sender pakken når nedtellingstimeren slår ut. 

> En slik protokoll der sekvensnummeret alternerer mellom 0 og 1 er også kjent som *alternating-bit protocol*

![rdt3.0](https://i.imgur.com/DzxRQcM.png)

 
#### Pipelinet pålitelig dataoverføringsprotokoller

Protokoll *rdt3.0* er en funksjonell korrekt protokoll, men det er lite sannsynlige at noen vil være fornøyd med ytelsen dens. Slike *stop-and-go*-protokoller vil bruke mye dødtid på å vente, og det vil gi forsinkelser.

![pipeline1](https://i.imgur.com/rLmCyXy.png)

Løsningen på dette problemet er ganske enkel. Istedet for å operere på en *stop-and-go*-metode, vil senderen tillate å sende flere pakker, uten å vente på bekreftelse, illustrert over. Denne teknikken kalles **pipelining**. Pipelining har følgende konsekvenser for pålitelige dataoverføringsprotokoller:

* Utvalget av *sekvensnumre må økes*, siden hver transittpakke (ikke teller re-sendinger) må ha et unikt sekvensnummer og det kan være flere, uovervåkede in-transit-pakker.
* Avsender- og mottakersiden av protokollene må kanskje lagre mer enn én pakke. Minst må avsenderen buffere pakker som er overført, men ikke bekreftet. Buffering av riktig mottatte pakker kan også være nødvendig hos mottakeren, som beskrevet nedenfor.
* Antall sekvensnumre som kreves og bufferingskravene vil avhenge av måten en dataoverføringsprotokoll svarer til tapte, korrupte og altfor forsinkede pakker. To grunnleggende tilnærminger mot pipelined feilgjenoppretting kan identifiseres: **Go-Back-N** og **selektiv gjentakelse**.

![pipeline2](https://i.imgur.com/lLqGKIr.png)


#### Go-Back-N (GBN)

I en **Go-Back-N (GBN) protokoll** har senderen ov til å sende flere pakker uten å vente på bekreftelse (ACK), men er begrenset til å ikke ha mer enn et maksimalt lovlig nummer, N, av unacknowledged pakker i pipelinen. 

Dersom vi definerer `base`til å være sekvensnummeret til den eldste unacknowledgede pakken, og `nextseqnum` til å være det minste ubrukte sekvensnummeret (dvs. sekvensnummeret til neste pakke som skal sendes). Da har vi at:

* `[0, base - 1]` - er alle sendte og bekreftede pakker
* `[base, nextseqnum - 1]` - er alle sendte men ikke bekreftede pakker
* `[nextseqnum, base + N - 1]` - er alle usendte pakker, som er i vinduet
* `[base + N, ∞)` - er alle pakker som ikke er sendt som er utenfor vinduet

![gbn](https://i.imgur.com/LhXB4ab.png)

Som vist i Figur 3.19 kan serien av tillate sekvensnumre for sending, men som ikke er blitt bekreftet, sees på som et vindu av størrelse *N* over serien av sekvensnumre. Av denne grunn blir *N* ofte referert til som *vindustørrelsen* og GBN-protokollen selv en **sliding-window protocol**.

GBN-senderen må kunne respondere til tre typer hendelser:

* *Påkallelse (invocation) ovenfra.* Når *rdt_send()* kalles ovenfra, må senderen først skjekke om vinduet er fullt, det vil si om det er N utestående, ubekreftede pakker. Dersom vinduet ikke er fullt, kan det sendes en pakke. Om det er fullt må senderen si ifra til det øvre laget, og indikere at vinduet er fullt. 
* *Mottak av ACK.* Mottak av en ACK. I vår GBN-protokoll vil en bekreftelse for en pakke med sekvensnummer n bli tatt til å være en kumulativ bekreftelse, noe som indikerer at alle pakker med et sekvensnummer opp til og inklusive n er blitt mottatt korrekt på mottakeren.
* *En timeout-hendelse.* Protokollens navn, "Go-Back-N", som i stop-and-go-protokollen har GBN-protokolen er nedteller. Når en timeout skjer, vil senderen *re-sende alle pakker som har blitt sendt og ikke er bekreftet.

> Kummulativ acknowledgement er naturlig for GBN, da mottakeren kun godkjenner pakker når de kommer i riktig rekkefølge. Alle pakker som ikke kommer i rekkefølge vil bli forkastet. 
> 
> Dersom pakke `n` ikke er mottat og pakke `n+1` kommer, vil pakken forkastes, og mottakeren vil sende bekreftelse for pakke `n-1`


#### Selective Repeat (SR) 

GBN-protokollen lar senderen potentielt "fylle pipelinen" med pakker. Men det er noen scenarioer der GBN har ytelsesfeil. Spesielt når vindustørrelsen og båndbreddeforsinkelsen er høye. En enkelt pakkefeil kan dermed sørge for at et stort antall pakker på sendes på nytt. Slik ser GBN ut dersom den må re-sende pakker. 

![gbn-resending](https://i.imgur.com/VUDtxqz.png)

Selective Repeat, som navnet hentyder, unngår re-sending av pakker som den tror har opplevd feil hos mottakeren. Mottakeren må godkjenne individuelt godkjente mottate pakker 

En vindustørrelse på *N* vil igjen bli brukt til å begrense antall utestående, ubekreftede pakker i pipelinen. Men i motsetning til GBN, har avsenderen allerede mottatt ACKs for noen av pakkene i vinduet. 

![srI](https://i.imgur.com/hSjgm2b.png)

Pakker som ankommer i feil rekkefølge, vil bli buffret til alle manglende pakker (med lavere sekvensnummer) ankommer.  

![srII](https://i.imgur.com/kdn9GH4.png)



### Connection-Oriented Transport: TCP

#### TCP-koblingen

TCP er sagt være *koblingsorientert* da en applikasjonsprosess kan sende data til en annen, må de to prosessene **"handshake"** med hverandre - som betyr å sende hverandre noen segmenter for å fastslå noen parametere for den kommende dataoverføringen. Begge parter må initalisere flere variabler for tilkoblingen.

> Ettersom TCP-protokollen kun kjører på endesystemene og ikke i mellomliggende nettverkselementer (rutere m.m.), er de mellomliggende nettverkselementene helt uvitende om TCP-tilkoblingen - de ser datagrammer, ikke tilkoblinger.

En TCP-kobling tilbyr en **fullstendig** (*eng. full-duplex*) tjeneste: Dersom det er en TCP-kobling mellom Prosess `A` hos en vert, og Prosess `B` hos en annen vert, da kan applikasjonlagsdata flyte fra `A` til `B` samtidig som applikasjonslagsdata kan flyte fra `B` til `A`. 

En TCP-kobling er alltid **punkt-til-punkt**, det vil si mellom én sender og én mottaker. 

Når en TCP-kobling er etablert kan de to applikasjonsprosessene begynne å sende data til hverandre. La oss se på det å sende data fra klientprosessen til serverprosessen:

* Klientprosessen overfører en datastrøm gjennom socketen sin

* Når dataene passerer gjennom døren, er dataene i hendene på at TCP kjører hos klienten. Som vist i Figur 3.28, styrer TCP disse dataene til koblingens  **sende-buffer**, som er en av bufferne som settes til side under det første treveishåndtrykket. 

* Fra tid til annen tar TCP noe data fra *sende-bufferen* og sender dataene til nettverkslaget. 
	* Interessant er TCP-spesifikasjonen veldig avslappet tilbake når det gjelder å spesifisere når TCP faktisk skal sende bufferdata, og angir at TCP skal "sende dataene i segmenter på egen vilje." 

* Maksimal mengde data som kan bli tatt av TCP og plassert i et segment er begrenset av **maksimal segmentstørrelse** (**MSS**).
	* MSS er typisk satt ved å først se på den største datalinklags-rammen som kan bli sendt av klienten (såkalt **maximum transmission UNIT, MTU**).

![tcp1](https://i.imgur.com/nlspkGO.png)

* TCP parrer hver klump med data med en TCP-header, og dermed former **TCP-segmenter**. Disse segmentete blir videre gitt til nettverkslaget, som lager IP-datagrammer. 

* Når TCP mottar et segment fra det andre endesystemet, vil segmentets data bli plassert i TCP-koblingens **mottaker-buffer**, som vist i Figur 3.28 over. 
	* Hver side av tilkoblingen har en *sende- og mottaker-buffer*.

> TCP bruker ikke NAK!


#### TCP Segment Structure

TCP-segmentet består av header-felt og et data-felt. Sånn som UDP-segmentet har TCP **source og destination port numbers**, som blir brukt til multipleksing og demultipleksing, og også et **checksum-felt**. Et TCP-segment har også følgende felter:

* Den har et 32-bit **sekvensnummer-felt** og et 32-bit **acknowledgement number**, som blir brukt av TCP senderen og mottakeren for å implementere en pålitelig dataoverføringstjeneste. 

* 16-bit **receive window**-felt som brukes til flytkontroll.

* 4-bit **header-lengt field** som spesifisere lengden av TCP-headeren i 32-bit ord. Kan være variabel lengde, pga. TCP options-feltet.

* Det valgfrie og variabel-lengde **options field**-feltet brukes når sender og mottaker avtaler den maksimale segmentstørrelsen (MSS) eller for en vinduskaleringsfaktor eller for tidsstempling.

* **Flag field** feltet består av 6 bits. **ACK**-biten indikerer om verdien i acknowledgement-feltet er gyldig. **RST**, **SYN**, og **FIN** bitene er brukt for koblingsetablering og ødeleggelse. **PSH**-biten indikerer at mottakeren skal sende dataen til det øvre laget umiddelbart. Til sist, **URG**-biten brukes for å indikere at det er data i segmentet som senderen har markert som *urgent / haster*. Pekeren til denne *urgente* dataen er i det 16-bits feltet **Urgent data pointer**.

![segment_tcp](https://i.imgur.com/yGmRqIV.png)

#### Sequence Numbers and Acknowledgement Numbers

De to viktigste feltene i et TCP-segment er sekvensnummer-feltet og acknowledgementnummer-feltet. Disse er kritiske for å kunne tilby pålitelig dataoverføring. 

Sekvensnummeret til et segment er bytestrøm-nummeret til den første byten i segmentet. For eksempel dersom man skal sende en fil på 500,000 bytes, og MSS er 1,000 bytes, og den første byte med datastrøm være nummerert med 0. Slik vil man da dele opp filen i TCP-segmenter. 

![tcp-deling](https://i.imgur.com/r8dGzKx.png)

* Sekvensnummeret var bytestrøm-nummeret til første byte i dataen til segmentet. For første segment som sendes, vil sekvensnummeret være **0**. for andre segment vil det være **1000**, osv. 

* Acknowledgementnummeret er sekvensnummeret til den nest byten som mottakeren forventer å få fra senderen. 

> Så når segment 1 med sekvensnummer 0 er mottatt vil mottakeren sende ACK 1000, da byte med bytestrømnummer 1000 er neste byte som forventes. 



#### Telnet

Telnet er en populær applikasjonlagsprotokoll som blir brukt for ekstern pålogging. Den kjører over TCP, og er designet for å jobber mellom ethvert par av verter. Telnet er en interaktiv applikasjon. Mange bruker nå idag SHH istedet for Telnet. Data sendt i Telnet er ikke kryptert og er derfor usikkert. Under er en figur av to verter som bruker Telnet, og vi ser at dataen blir ekkoet tilbake til klienten. 

![telnet](https://i.imgur.com/IdFr18c.png)




#### Round-Trip Time Estimation and TImeout

TCP burker en timeout/re-sendingsmekanisme for å redde tapte/mistede segmenter. Timeouten skal klart være større enn koblingens **round-trip time (RTT)**, som er hvor lang tid det tar fra pakken er sendt til den er acknowledged. 

##### Estimere Round-Trip Time:

Det er vanlig å lage starte med en *SampleRTT* på TCP-koblingen, og deretter kalle den som det hittile gjennomsnittet som blir *EstimatedRTT*, når man får en ny *SampleRTT*, vil TCP oppdatere *EstimatedRTT* med følgende formel:

* *EstimatedRTT* = (1 - ⍺) · *EstimatedRTT* + ⍺ · *SampleRTT*

> Den anbefalte verdien for ⍺ er ⍺ = 0.125

Vi har også en variabel for variansen til RTT, som kalles *DecRTT*, som estimerer hvor mye *SampleRTT* typisk avviker fra *EstimatedRTT*


##### Sette og endre Timeout interavallet for re-sending

Gitt verdiene *EstimatedRTT* og *DevRTT* kan man regne ut hvilken verdi TCP sin timeout intervall skal være. Det er derfor vanlig å sette *TimeoutInterval* til å være:

* *TimeoutInterval* = *EstimatedRTT* + 4 · *DevRTT*

> En initiell TimeoutInterval-verdi på 1 sekund er anbefalt
>
> Dersom et timeout finner sted, dobles verdien til *TimeoutInterval* for å unngå for tidlig timeout. Men så fort segmentet blir bekreftet, regnes *EstimatedRTT* ut på nytt med formelen over. 


##### Pålitelig dataoverføring

Husk at Internettets nettverklagstjeneste (IP) er upåltelig. IP gir ingen garanti for datagram-leveranse, garanterer ikke in-order leveranse og garanterer heller ikke integriteten til dataen i datagrammene. 

TCÅ lager en pålitelig dataoverføringstjeneste på topen av IP sin upåligelige, best-effort tjeneste. TCPs rdt sørger for at datastrømmen som prosessen leser ut fra TCP-mottaker-bufferen er ukorrup, uten hull, uten duplisering, og i riktig rekkefølge. 

For å få til dette brukes mange av tingene som ble snakket om i forrige delkapittel. Tidligere har det vært diskutert om man skal ha en timer eller en per segment. Sistnevnte ville ført til stort overhead, og det anbefalte TCP timer-managmentet er å ha en *enkel* re-sendingstimer. 

**Et par scenarioer:**

![retrans](https://i.imgur.com/wDZM4z2.png)
> Her blir segment med sekvensnummer 92 sendt to ganger siden ACK-en ikke kom frem. 


![notretrans](https://i.imgur.com/lF4iXRh.png)
> Her kommer ingen av ACK-ene frem før timeout, men andre ACK kommer før timeout til andre segment og blir ikke re-sendt.


![kummtrans](https://i.imgur.com/Uume4dB.png) 
> Her kommer ikke ACK=100 frem, men det gjør ACK=120, før timeout intervallet, og pga. kummulativ bekreftelse trenger ikke TCP-senderen og re-sende første segment. 


**Timeout interval dobbling:**
Når en timeout skjer, så dobles som nevnt timeout intervallet hver gang timeout skjer og regnes ut på nytt når første ACK mottas. Dette er en begrenset form for congestion control.


**Fast Retransmit:**
Ett av problemene med timeout-baserte re-sendinger er at timeoutperioden kan være relativt lang. Når et segment mistes tvinger denne lange timeout-perioden senderen til å forsinke/vente med å re-sende det tapte segmentet, og dermed øke ende-til-ende-forsinkelsen.

Heldigvis kan senderen ofte detektere tapte pakker lenge før timeout, pga noe som kalles **duplikate ACK-er**. En *duplicate ACK* er en ACK som re-bekrefter et segment som senderen allerede har mottatt en ACK for. 

*	En mottaker merker at den mangler et segment dersom den mottar et segment med sekvensnummer høyere enn forventet, og sender dermed en duplikat ACK for forrige mottate pakke. 
* Når sender mottar en duplikat ACK, vil den legge til antall ACKs mottat for den pakken som mottakeren sier den bekrefter. Dersom denne verdien blir større enn 3, i dette tilfelle, vil TCP-senderen utføre en **fast retransmit**, og sender pakken *før* segmentets timer går ut.


##### Go-Back-N eller Selective Repeat?
Husk at TCP-Acknowledgements er kummulative og mottatt riktig mottatt men out-of-order segmenter er ikke individuelt ACK-et av mottakeren, og ligner kanskje gjerne på en GBN-type protokoll. Men det er mange forskjeller, som at TCP vil buffre riktig mottate med out-of-order segmenter. Dersom en pakke *n* forsvinner, vil GBN re-sende alle pakkene *n*,..,*N* fra vinduet, mens TCP kun vil sende pakke *n*. 

En foreslått modifisering av TCP, er den såkalte **selective acknowledgement**, som tillater TCP-mottakeren å bekrefte out-of-order segmenter, og TCP sammen med selective ACK vil se veldig ut som den generiske SR protokollen. 

Men, TCPs feilsøkingsmekanisme er trolig best kategorisert som en hybrid av GBN og SR protokoller.



#### Flytkontroll

Minner om at hver side av en TCP-tilkobling har en mottaker-buffer for koblingen. Dersom appliaksjonen som leser data fra denne er relativt treg på å lese data, kan senderen lett *overflowe* denne bufferen ved å sende for mye data for fort. 

TCP tilbyr en **flytkontroll-tjeneste** (*eng. flow control service*) ved å eliminere muligheten for at senderen overflower mottakerens buffer. Dette gjøres ved at senderen vedlikeholder en variabel kalt **recieve window**. Dette vinduet er brukt for å gi senderen en ida av hvor mye fri bufferplass som er ledig hos mottakeren. Begge vertene har hvert sitt *mottakervindu*. 

![mottakerbuffer](https://i.imgur.com/pW3wa01.png)

* *rwnd* = *RcvBuffer* - [*LastByteRcvd* - *LastByteRead*]

	* *rwnd* - ledig plass i buffer
	* *RcvBuffer* - total plass i buffer
	* *LastByteRcvd* - bytestrømnummeret på byten som ble sist mottatt fra nettverket
	* *LastByteRead* - bytestrømnummeret på byten som ble sist lest fra bufferen. 




#### TCP-tilkoblingsadministrasjon

Nå skal vi se på hvordan en TCP-tilkobling etableres og rives ned. 
Vi skal først se på hvordan man etablerer en TCP-tilkobling. Anta at en prosess på en vert (klient) øsnekr å initalisere en tilkobling med en annen prosess på en annen vert (server). Applikasjonsprosessen hos klienten informerer klient TCP-en at den ønsker å etablere en tilkobling til en prosess på serveren. TCP-en hos klienten begynner så å **z** TCP-tilkoblingen med TCP-en hos serveren på følgende måte: 


1. Klientsidens TCP sender et spesielt TCP-segment til serversidens TCP.
Dette spesielle segmentet inneholder ingen applikasjonsdata, men av flagg-btutene i segmentets header, **SYN-biten**, er satt til **1**. I tillegg velger klienten et tilfeldig start-sekvensnummer (*client_isn*), og plasserer det i sekvensnummerfeltet på den initielle TCP SYN-segmentet, som sendes til serveren.

2. Når IP-datagrammet med TCP SYN-segmentet kommer hos serveren, ekstraherer serveren segmentet fra datagrammet, allokerer TCP-buffere og variabler for koblignen. Den sender så et *connection-granted*-segment til client TCP-en. 
Den setter *SYN-flagget* til *1*, og acknowlegdenummeret til å være *client_isn + 1*. Serveren velger også sitt eget initielle sekvensnummer (*server_isn*). 
*Connection-granted*-segmentet refereres til som et **SYNACK-segment**.  

3. Når klienten mottar SYNACK-segmentet, allokerer også klienten buffere og variabler til tilkoblingen. Klienten sender serveren så igjen et annet segmen, som bekrefter SYNACK-segmentet. Setter acknowlegdenummeret til *server_isn + 1* i TCP-headeren, og *SYN-biten* til *0*, siden tilkoblingen er etablert. 


For å kunne etablere tilkobling mellom to verter, må det sendes tre pakker, og av den grunn kalles denne etableringsprosedyren for en **three-way handshake**

![3whandshake](https://i.imgur.com/XOodLhi.png)

Dersom klientapplikasjonen ønsker å lukke koblingen (noter at server også kan lukke kobling). Da skjer følgende:

1. Klienten sender TCP-segment med *FIN-bit* satt til *1*. Klienten går i FIN_WAIT_1-tilstanden.
2. Serveren bekrefter TCP-segmentet fra klienten.
3. Når klienten får dette segmentet går den inn i neste tilstand, FIN_WAIT_2. Den venter på et segment fra serveren med *FIN-biten* satt til *1*.
4. Server sender TCP-segment med *FIN-bit* satt til *1*. Klient acknowledger dette segmentet. Klienten går i TIME_WAIT-tilstanden i tilfelle segmentet ikke kom frem. 

Gjennom livet til en TCP-koblingen, har koblingen flere **TCP-tilstander**.  Her er typiske tilstander en TCP-tilkobling har i levetiden sin: 

![tcp_states](https://i.imgur.com/5PvqNl2.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

### Congestion Control - Approaches to Congestion Control

Vi skal se på to store tilnærminger for congestion control, som er blitt tatt i bruk og diskutere spesifikke nettverksarkitekturer og congestion-control protokoler som bruker disse metodene. 

På det bredeste nivået kan vi skille mellom fremgangsmåter for congestion control ved om nettverkslaget gir noen eksplisitt hjelp til transportlaget for overbelastningsstyringsformål:

* *Ende-til-ende congestion control.* I en ende-til-ende tilnærming for congestion control, gir nettverkslaget *ingen eksplisitt støtte* til transportlaget for congestion-control-formål. 
Om det er overbelastning i nettverket eller ikke må utledes av endesystemene, som bare er basert på nettverksadferd (pakketap og forsinkelse).
	* For eksempel på TCP ta denne ende-til-ende-tilnærmingen, siden IP-laget ikke gir noen tilbakemelding til endesystemene angående nettverksbelastning. TCP-segmenttap (timeout eller 3 * duplikat ACK) er brukt som indikasjon for nettverksoverbelastning (*eng. network congestion*). 


* *Nettverksassistert congestion control.* Med nettverksassistert congestion control (*eng. network-assisted*), gir nettverklagskomponentene (dvs. rutere) eksplisitt tilbakemelding til senderen angående nettverkbelastningen (*congestion*)
	* Denne tilbakemeldingen kan være så enkel som en enkelt bit som indikerer overbelastning ved en link

I nettverksassistert congestion control, sier ruteren ifra på en av to måter. Enten sende en **choke-pakke**, som essensielt sier at den er opptatt, eller å legge på en indikator på pakken, slik at mottakeren kan si ifra til senderen om at overbelastningen/*congestion*


### TCP Congestion Control

TCP må bruke ende-til-ende congestion control istedet for nettwork-assisted congestion control, siden IP-laget ikke tilbyr noen eksplisitt feedback til endesystemene angående nettverksbelastning. 

Tilnærmingen til TCP er å ha hver avsender begrense hastigheten som den sender trafikk til forbindelsen sin, som en funksjon av oppfattet nettverksbelastning.

Vi så i forrige delkapittel at begge sidene av TCP-koblingen hadde buffere, og flere variabler (*LastByteRead*, *rwnd* m.m.). TCP congestion-control-mekanismen hos senderen holder på en ekstra variabel, **congestion window**. Overbelastningsvinduet / congestion window, betegnet *cwnd*, setter en begrensning på hastigheten der en TCP-avsender kan sende trafikk til nettverket. Spesifikt kan mengden av ubekreftede data ved en avsender ikke overstige minimum cwnd og rwnd, det vil si

* *LastByteSent* – *LastByteAcked*   *min*{*cwnd*, *rwnd*}

For å ikke fokusere på flytkontroll, så antar vi at mottakervinduet er så stort at størrelsen dens kan ignoreres. Dermed er mengden av ubekreftede data ved avsenderen kun begrenset av *cwnd*. 

DVed  begynnelsen av hver RTT, tillater begrensningen at avsenderen sender *cwnd* bytes data inn i forbindelsen. På slutten av RTT mottar avsenderen bekreftelser for dataene. Dermed er avsenderens sendehastighet omtrent:

* *cwnd* bytes /*RTT* sec
	* Ved å **justere** verdien av *cwnd*, kan avsenderen derfor **justere** frekvensen der den sender data til sin forbindelse.

	
La oss se nærmere på hvordan en TCP-avsender oppfatter at det er overbelastning på veien mellom seg selv og destinasjonen. La oss definere en "*tapshendelse*" på en TCP-avsender som forekomsten av enten en *timeout* eller mottak av *tre* *dupliserte* *ACKer* fra mottakeren.

> Ettersom TCP bruker acknowledgements for å trigge sin økning i *"congestion window size"*, sier TCP å være **self-clocking**.


TCP følger følgende retningslinjer:

* *Et tapt segment innebærer overbelastning, og TCP-avsenderens hastighet bør derfor reduseres når et segment går tapt.* Husk at en time-out-hendelse eller kvittering av fire bekreftelser for et gitt segment (en original ACK og deretter tre dupliserte ACKs) tolkes som en implisitt "tapshendelse" -indikasjon av segmentet som følger fireganger ACKed-segment, utløser en re-sending av det tapte segmentet.

* *Et bekreftet segment indikerer at nettverket leverer avsenderens segmenter til mottakeren, og følgelig kan avsenderens hastighet økes når en ACK kommer for et tidligere ubekreftet segment.* Mottakelsen av bekreftelser er tatt som en implisitt indikasjon på at alt er bra - Segmenter blir vellykket levert fra avsender til mottaker, og nettverket er ikke overbelastet. Congestion window-et kan økes. 

* *Båndbreddeundersøkelse (eng. Bandwith probing)*. Gitt ACK-er som indikerer en overbelastningsfri kilde-til-destinasjon-vei og tapshendelser som indikerer en overbelastet vei, er TCPs strategi for å justere overføringshastigheten å øke frekvensen som følge av mottatte ACKs inntil det oppstår en tapshendelse, da blir overføringsrate redusert. Hver TCP-avsender virker på lokal informasjon asynkront fra andre TCP-sendere.


#### TCP Congestion Control Algorithm

Algoritmen har 3 store komponenter: (1) slow start, (2) congestion avoidance og (3) fast recovery

1. **Slow start:** Når en TCP-kobling begynner, er verdien til *cwnd* initiellt en liten verdi på 1M MSS, som gir en sendingsrate på MSS/RTT. Deretter vil *cwnd* øke med 1 MSS for hvert bekreftede segment. Det vil se ut som figuren under. 
	*	Dersom det indikeres at en pakke er blitt mistet blir *cwnd* satt til 1 	MSS, og det lagres en verdi *ssthresh* = *cwnd*/2. 
	* Når *cwnd* = *ssthresh*, avslutter slow start, og TCP går inn i *congestion* *avoidance*-tilstanden
	* Dersom man finner 3 duplikate ACKer, så utfører TCP en *fast* *retransmit* 	(kjapp re-sending), og går inn i *fast* *recovery*-tilstanden.

![slowstart](https://i.imgur.com/7uG0xx1.png)

2. **Congestion aviodance:**  Ved inngang til congestion aviodance-tilstanden er verdien av *cwnd* omtrent halvparten av verdien når congestion sist oppsto - congestion kan ligge rett rundt hjørnet! Så i stedet for å fordoble verdien av hver RTT, så øker TCP verdien av *cwnd* med bare 1 MSS hver RTT. Men når skal congestion-ens lineære økning (med 1 MSS per RTT) ende? 
	* TCPs congestion-algoritme oppfører seg det samme når en timeout oppstår: 	Setter verdien til *cwnd* og *ssthresh* og *slow start*.
	* Ved tredobbelt duplikat ACK, så fortsettes det å sende segmenter, halverer *cwnd* og legger til 3 MSS for de tre ACK-ene. Går så inn i* fast recovery*. 


3. **Fast recovery:** Ved fast recovery økes verdien av *cwnd* med 1 MSS for hver duplikat ACK mottatt for det manglende segmentet som forårsaket at TCP kommer inn i fast recovery. Til slutt, når en ACK kommer for det manglende segmentet, går TCP inn i congestion-avoidance-tilstanden etter å ha deflatert *cwnd*.
	* Hvis en **timeout** skjer, går over til slow-start-tilstand etter å utføre 	de samme handlingene som i slow start og congestion-avoidance: Verdien av 	cwnd er satt til 1 MSS, og verdien av ssthresh er satt til halvparten av 	verdien av *cwnd* da tapshendelsen skjedde.

> TCP Congestion Control blir ofte referert til som en **additive-increase, multiplicative- decrease (AIMD)** form for congestion control. 


#### Fairness

Figuren under viser gjennomstrømingen til to connections gjennom en flaskehals. Punktene A, B, .. viser hvordan fordelingen av gjennomstrømning fordeler seg for hver endringene TCP Congestion Control gjør på congestion-vinduene deres.
 
![fairness](https://i.imgur.com/WoZ2HqM.png)

##### Fairness and UDP

Fra TCP sitt synspunkt er det urettferdig at mutlimedia-applikasjoner bruker UDP, da de kan sende så mye data de vil og i noen tilfeller miste pakker, istedet for å sette sendingsraten deres på et "fair" nivå, og hjelpe hverandre. Dermed er det mulig for UDP å overkjøre TCP-trafikk.

#### Fairness and Parallel TCP Connections

Selvom vi kunne ha tvunget UDP-trafikken til å oppføre seg "fair", har vi ikke løst "fairness" problemet helt. Ingenting stopper TCP-baserte applikasjoner fra å kjøre paralelle koblinger, som gir dem en større andel av båndbredden på linken. 


## Chapter 4 - The Network Layer

