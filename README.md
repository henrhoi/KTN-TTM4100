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

<a name="kap4"></a>
## Kapittel 4 - The Network Layer

#### Forwarding and routing

Rollen til nettverkslaget er enkelt - å flytte pakker fra den sendende verten til den mottakende verten. For å gjøre det så har nettverkslaget to viktige funksjoner:

* *Forwarding.* Når en pakke mottas ved en ruters input-linken, må ruteren flytte pakken til riktig utgangslink. 

* *Routing.* Nettverkslaget må bestemme ruten eller stien tatt av pakkene mens de flyter mellom sender og mottaker. Algoritmene som bestemmer disse stiene er kalt **routing algorithms**.

> *Forwarding* refererer til ruterens lokale handling for å overføre en pakke fra et inngangslinkgrensesnitt til riktig utgangslinkgrensesnitt. 
> 
> *Routing* refererer til den nettverksbrede prosessen som bestemmer slutt-til-ende-banene som pakker tar fra kilde til destinasjon.


Hver ruter har et **forwarding table**. En ruters videresender en pakke ved å se på verdien til et header-felt hos den mottatte pakken, og sammenlikner med indeksene i ruterens forwarding table. 

Når vi refererer til termet *packet switch* (*nor. pakkesvitsj*) mener vi en generell pakkesvitsje-enhet, som overfører en pakke fra input-link grensesnitt til output-link grensesnitt. 

* Noen pakkesvitsjer, som kalles **link-layer switches**, baserer deres videresendingsbeslutninger på verdier i feltene til linklagsrammen (*eng. frame*), og refereres til som *link-layer (layer 2) devices*. 

* Andre pakkesvitsjer, kalt **rutere**, baserer deres videresendingsbeslutningerpå verdien i nettverklagsfeltet, og er dermed  *network-layer (layer 3) devices*. 

#### Connecton Setup

Vi sa nettopp at nettverkslaget har to viktige funksjoner, videresending og ruting. Men vi ser snart at i enkelte datanettverk er det faktisk en tredje viktig nettverkslagsfunksjon, nemlig **tilkoblingsoppsett** (*eng. connection setup*). 

Husk at i TCP trengs det en treveishåndshake før data sendes. Dette gjør det mulig for avsenderen og mottakeren å sette opp nødvendig tilstandsinformasjon (for eksempel sekvensnummer og initiell flykontroll-vinduestørrelse). 

På en analogisk måte vil noen nettverkslagsarkitekturer, for eksempel ATM, fram relay og MPLS, kreve at ruterne langs den valgte banen fra sender til mottaker  *"handshaker"* med hverandre for å sette opp tilstander før nettverkslagdatapakker innenfor en gitt kilde-til-destinasjon-tilkoblignen kan begynne å strømme. I nettverkslaget kalles denne prosessen som tilkoblingsoppsett.


#### Network Service Models

**Network service model** definerer egenskapene for ende-til-ende transport av pakker mellom sende- og mottaker-endesystemer.

La oss nå vurdere noen mulige tjenester som nettverkslaget kan gi, etter at transportlaget har overført en pakke til nettverkslaget:

* *Garantert levering.* Denne tjenesten garanterer at en pakke etter hvert vil ankomme destinasjonen sin.

* *Garantert levering med maks. forsinkelse.* Denne tjenesten garanterer ikke bare at pakken kommer frem, men levering innen et spesifisert vert-til-vert-forsinkelse.
 
* *In-order pakkelevering.* Denne tjenesten garanterer at pakkene kommer hos destinasjonen i rekkefølgen de ble sendt.

* *Garantert minimal båndbredde.* Så lenge en sender kan overføre pakker under koblingens bitrate, kan tjenesten garantere ingen tap av pakker og at de kommer frem innen et spesifisert vert-til-vert-delay.
 
* *Garantert maksimal jitter.* Denne tjenesten garanterer at tiden mellom overføringen av to pakker hos senderen er lik tidsforskjellen på mottakelsen av pakkene (eller mindre enn et spesifisert delay).

* *Sikkerhetstjenester.* Ved å bruke en hemmelig nøkkel, kun kjent av kilde- og desnitasjonsvertene, kan man encrypte deler payloaden til datagrammet, og pakken er dermed konfidensiell mellom vertene. 

![IATMABRCBR](https://i.imgur.com/A00su7P.png)


Internettets nettverkslag er en såkalt *best effort* tjeneste, det vil egt si ingen tjeneste i det hele tatt. Med en best effort-tjeneste er ikke timingen mellom pakkene garantert, pakkenes rekkefølge ved ankommelse hos destinasjon eller heller ikke garantert, heller ikke om pakkene kommer frem i det hele tatt. 

> Av denne definisjonen så ville et nettverk som leverte ingen av pakkene til destinasjonen tilfredsstille definisjonen av en best effort-tjeneste.

To viktige ATM tjenestemodeller er *constant bit rate*- og *available bit rate*-tjenester:

* **Constant bit rate (CBR) ATM network service**. Dette var første ATM tjenestemodell som ble standardisert, og reflekterer telefonselskapene sin intersse i ATM. Målet med *CBR* tjeneste er å tilby en flyt av pakker (cells  ATM-terminoloi) med et virtuelt rør hvis egenskaper er det samme som om en dedikert fastbåndbredde-overføringskobling eksisterte mellom sending og mottak av verter. Med CBR-tjenesten blir en strøm av ATM-celler båret over nettverket på en slik måte at en celles ende-til-ende forsinkelse, variabiliteten i en celle ende-til-ende forsinkelse (det vil si jitteren) og brøkdelen av celler som er tapt eller levert sent, er alle garantert å være mindre enn angitte verdier.

* **Available bit rate (ABR) ATM network service**. Med Internett som tilbyr såkalt best-service-tjeneste, kan ATMs ABR best karakteriseres som en litt bedre enn best mulig service. Som med Internett-tjenestemodellen kan celler gå tapt under ABR-tjenesten. I motsetning til Internett, kan imidlertid ikke cellene ombestilles (selv om de kan gå tapt), og en minimums celleoverføringshastighet (MCR) garanteres til en tilkobling ved hjelp av ABR-tjenesten. 


### What's Inside a Router

En ruter har fire komponenter som kan bli identifisert:

* *Input porter:* En inngangsport utfører en rekke nøkkelfunksjoner. Den utfører den fysiske-lagsfunksjonen ved å avslutte en innkommende fysisk link ved en ruter; Dette vises i den venstre boksen til inngangsporten og den høyre boksen til utgangsporten i figur 4.6. En inngangsport utfører også link-layer-funksjoner som trengs for å samvirke med link-layer på den andre siden av innkommende linken. Dette er representert av mellomkassene i inngangs- og utgangsportene. Kanskje mest avgjørende, **oppslagsfunksjonen** utføres også ved inngangsporten; Dette vil skje i den høyre boksen til inngangsporten. Det er her at videresendingstabellen blir konsultert for å bestemme utgangsporten til ruteren som en pakke vil bli videresendt via *swtching fabric*-en. Kontrollpakker (for eksempel pakker som bærer rutingsprotokollinformasjon) videresendes fra en inngangsport til rutingsprosessoren. 

> Vær oppmerksom på at termen port her - som refererer til de fysiske inngangs- og utgangsrutergrensesnittene - er tydelig forskjellig fra programvareportene som er knyttet til nettverksapplikasjoner og socketsene som er omtalt i kapittel 2 og 3.

* *Switching fabric:* Switching fabric-en kobler sammen ruterens inngangsporter til dens utgangsporter. Denne er kun inne i ruteren - et nettverk i en nettverksruter.

* *Output porter:* En utgangsport lagrer pakker mottat fra switching fabric-et og sender disse pakkene til den utgående linken, ved å utføre nødvendige linklags- og fysisklags-funksjoner. 

* *Routing processor:* Ruterprosessoren utførerer ruter-protokoller, vedlikeholder *routing tables* og tilstandsinformasjon til tilkoblede linker, og regner ut *forwarding table*-et for ruteren.  

![ruterarkitektur](https://i.imgur.com/vk4V7mP.png)

En ruters inngangsporter, utgangsporter og switchingfabric implementerer sammen forwarding-funksjonen. Disse forwarding-funksjonene er kollektivt referert til som **router forwarding plane**, som er implementert inn i maskinvaren. Forwarding-planet opererer på nanosekund-skaane, mens ruterens controlfunksjoner - som utfører ruterprotokollene, svarer koblinger, og utfører management-funksjoner, opererer på millisekund- eller sekund-skala. Disse **router control plane** funksjonene er vanligvis implementert inn i programvaren, og kjører på routing prosessoren. 

#### Input-prosessering

Som nevnt over, inngangsportens linjeterminering og link-lags prosessering implementerer det fysiske- og link-laget or den individuelle input-linken. 

Inngangsporten skjekking (*eng. lookup*) er sentral for ruterens operasjoner - det er her ruteren bruker forwarding tabelen for å se opp hvilken utgangsport pakken skal bli forwardet til via switching fabricen. 

Forwarding table-et blir utregnet og oppdatert av routing-prosessoren, med en "skygge-kopi" liggende hos hver inputport. Forwarding table-et blir kopiert fra ruterprosessoren til linjekortene over en separat buss indikert av den stiplede linjen på Figur 4.6 over. Med en skygge-kopi kan forwarding-beslutninger gjøres lokalt hos hver inngangsport, uten å spørre den sentraliserte prosessoren på en per-pakke-basis. Dermes *slippes* en **sentralisert flaskehals**. 
 
![inputportprosessering](https://i.imgur.com/84pJ05T.png)

Når en pakkes utgangsport har blitt bestemt via lookup-en, kan pakken bli sendt inn i switching fabric-en. I noen design vil pakker bli blokkert fra å gå inn i fabric-en dersom noen andre pakker fra andre inputporter bruker den. En blokket pakke blir satt i en kø hos inputporten, og som planlegges å gå inn i switching fabric-en senere. 

Selvom denne *looku-en* er den viktigste aksjonen ved inputportprosessering, må mange andre handlinger bli gjort: (1) fysisk- og link-lagsprosessering må skjer, (2) pakkens versjonsnummer, checksum og time-to-live-felt må skjekkes, og de to sistnevnte må overskrives, og (3) tellere brukt til nettverksadministrering (som antall IP datagram motatt) må oppdateres. Denne inngangsportprosesseringen kan enkelt forklares med "match-and 


#### Switching

Switching fabric-en er hjertet til ruteren, det er gjennom dette stoffet at pakkene faktisk blir svitsjet (*altså forwardet*) fra inngangsport til utgangsport. Svitsjing kan bli utført på en rekke måter, vist i Figur 4.8.

![switching](https://i.imgur.com/d0e7YGU.png)


* *Switching via memory.* De enkelste, tidligste ruterne var tradisjonelle datamaskiner der svitsjingen mellom portene ble gjort under direkte kontroll av CPU-en. Inngang- og utgangsportene fungerte som tradisjonelle I/O enheter i et tradisjonelt operativsystem. 
	* Når en pakke ankom på inngangsporten, sendte det en *interrupt* til CPU-en som kopierte pakken over til prosessorminnet. Prosessoren hentet så destinasjonsadressen fra headeren, skjekket passende utgangsport og kopierte pakken til utgangsportens buffer. Dersom båndbredden til CPU-ens minne B, som er antall pakker i sekundet som kan leses, skrives eller sendes, så må den totale videresendingstrømmen (den totale hastigheten som pakker overføres fra inngangsporter til utgangsportene) være mindre enn B / 2.

* *Switching via a bus.* Ingangsporten overfører pakken direkte til utgangsporten over en *delt bus*, uten intervenering fra ruterprosessoren. Dette er vanligvis gjort ved å legge på en ekstra header-label som indikerer hvilken utgangsport den skal sendes fra. Pakken vil mottas av alle utgangsportene, men kun en port som matcher labelen, og beholder pakken. Label-en blir fjernet ved utgangsporten. Siden alle pakkene må over bussen, er ruterens svitsjing-hastighet begrenset av bussens hastighet.

* *Switching via an interconnection network.* En måte å overkomme båndbreddebegrensing av en enkel, delt buss er å bruke et litt mer sofistikert interkoblet nettverk. En *crossbar-switch* er en sammenkoblingsnettverk bestående av 2*N* busser, som kobler sammen *N* inputporter med *N* utgangsporter, som vist over. Når en pakke skal fra port A til port Y, så vil switch-fabric-controlleren lukke krysspunktet ved krysset til bussene A og Y. 



#### Output Processing

Utgangsprossesering, vist i Figur 4.9 tar pakkers om er lagret hos utgangsportens minne og sender dm over til utgangs-linken. Dette inkluderer å selektere og de-queue pakker for seding, og utføre nødvendig link-lags- og fysisk-lags-overføringsfunksjoner

![outputprocessing](https://i.imgur.com/1agYhop.png)


#### Where does Queueing Occur?

Som lett kan sees i Figur 3.8, er det klart at pakkekøer kan forme seg på både inngangsportene og utgangsportene - analogi kan være biler som kjører inn mot en rundkjøring. Plasseringen og omfanget av køen (enten ved inngangsportkøene eller i utgangskortkøene) vil avhenge av trafikkbelastningen, den relative hastigheten til koblingsmaterialet og linjens hastighet.

Dersom en kø blir veldig stor og det ikke er plass til flere pakker, vil det ikke være plass til å lagre innkommende pakker, og vi vil oppleve **packet loss**.

> Vi sier at pakken ble "mistet i nettverket" eller "sluppet hos ruteren"
> 
> Det er i disse ruterkøende at pakker blir droppet eller mistet.


* Anta at inngang- og utgangslinjenes hastighetene (transmission rates) alle har en identisk overføringsrate på *R<sub>line</sub>* pakker per sukund, og at det er N inngangs- og N utgangsporter.
* La oss definere switching fabric-ens overføringsrate *R<sub>switch</sub>* som raten av pakker som kan bli overført fra inngangsport til utgangsport. Dersom *R<sub>switch</sub>* er *N* ganger raskere enn *R<sub>line</sub>*, da vil det bare oppstå ubetydelig kø på inngangsportene, men det kan oppstå kø hos utgangsportene dersom mange av pakkene går til samme utgangsport. 


![outportqueueing](https://i.imgur.com/MyzfOwo.png)


> Tommelregelen for bufferstørrelse var i mangeår at mengde buffering (*B*) skulle være lik gjennomsnitts round-trip time (*RTT*) ganger linkens kapasitet (*C*). `B = RTT · C`


* En konsekvens med utgangsportkø er at en **packet scheduler** ved utgangsporten må velge en pakke blant de som er i køen for overføring. Denne seleksjonen kan gjøres enkelt, FIFO-scheduling, eller en mer sofistikert måte, som *weighted fair queueing (WFQ)*, som deler utgangslinken fairly blandt de forskjellige ende-til-ende-tilkoblingene. 
	* Packet scheduling spiller en viktig rolle for å tilby **quality-of-service guarantees**. 

* Dersom det ikke er nok minne i bufferen til en innkommende pakken, må et valg tas om man enten skal droppe den innkommende pakken (kalles **drop-tail**) eller fjerne en eller flere av allerede kø-ede pakker, for å lage plass til den nyankommede pakken. 
	* Vanlig er det vanlig å merke et header-felt om overbelastningssignal til senderen, *før* bufferen er full. Det finnes et antall pakke-dropping og -markeringspolicyer (kollektivt kjent som **active queue management (AQM) algoritmer**). 


En av de mest studerte og implemterte AQM-algortimenene er **Random Early Detection (RED)** algoritmen. Under RED lages et threshold-intervall [*min<sub>th</sub>*, *max<sub>th</sub>*]. 

*	Dersom den gjennomsnittlige kølengden er mindre enn *min<sub>th</sub>*, vil pakken legges i køen. 
* Dersom køen er full eller den gjennomsnittlige kølengden er større *max<sub>th</sub>*, vil pakken markeres eller droppes. 
* Dersom køen har en gjennomsnittskølengde i intervallet [*min<sub>th</sub>*, *max<sub>th</sub>*], vil pakken markeres eller droppes med en sannsynlighet som er en typsik funskjon av min- og max-thresholdet.

Figur 4.11 viser et eksempel hvor to pakker (mørkt blå) på forsiden av inngangskøene er bestemt for samme øvre høyre utgangsport. Anta at switch-fabric velger å overføre pakken fra fronten av øvre venstre kø. I dette tilfellet må den mørkeblå pakken i nedre venstre kø vente. Men ikke bare må denne mørkeblå pakken vente, så også må den lyseblå pakken som står i køen bak den pakken i nedre venstre kø, selv om det ikke er noen tvil for midt-høyre utgangsporten (målet for den lyseblå pakke)n. 

Dette fenomenet kalles **head-of-the-line-blokkering (HOL)** i en svitsj med inngangskø. 

* En kø-pakke i en inngangskø må vente på overføring gjennom switching-fabric (*selv om utgangsporten er ledig*) fordi den er blokkert av en annen pakke forrerst på linjen.


#### The Routing Control Plane

I vår diskusjon hittil og i Figur 4.6 har vi implisitt antatt at *routing control plane* fullt ut ligger og utfører i en ruter
prosessor innenfor ruteren. Det nettverksbrede *routing control plane*  er  desentralisert med forskjellige deler (for eksempel av en rutingsalgoritme) som utføres hos forskjellige rutere som interagerer med hvandre ved å sende kontrollmeldinger til hverandre. 


### The Internet Protocol (IP): Forwarding and Addressing in the Internet

Vi skal nå se at Internett adressering og forwarding er vitkige komponenter til Internet Protocol (IP). Det er to versjoner av IP i bruk idag. Vi skal først se på den mye brukte IP protokoll versjon 4, som refereres til som IPv4. vi skal se på IP versjon 6 (IPv6), som er blitt foreslått å erstatte IPv4, mot slutten av seksjonen. 

![Networklayerinside](https://i.imgur.com/QqHjnnt.png)

Vi ser at internettets nettverkslag har tre store komponenter. Den første komponenten er IP-protokollen. Den andre komponeneten er ruter-komponenteen, som bestemmer stien et datagram tar fra kilde til destinasjon. Den siste komponenten av nettverkslaget er et anlegg for å rapportere feil i datagrammer og svare på forespørsler om bestemt nettverkslagsinformasjon. Vi vil dekke internettets nettverkslagrings- og informasjonsrapporteringsprotokoll, ICMP (Internet Control Message Protocol) snart. 

#### Datagram Format

> Husk at en nettverkslagspakke refereres til som et *datagram*. 

![ipv4datagram](https://i.imgur.com/n9yJwFR.png)

IPv4 datagram-formatet er vist i Figur 4.13. Nøkkelfeltene i TPv4-datagrammet er:

* *Version number.* Disse 4 bitene spesifiserer IP-protokoll versjonen til datagrammet. Forskjellige versjoner av IP burker forskjellige datagramformater.
* *Header length.* Fordi et IPv4-datagram kan inneholde et variabelt antall med options, er disse 4 bitene trengt for å bestemme hvor dataen i datagrammet begynner. 
* *Type of service.* Type of service (TOS) bits er inkludert i headeren for å la forskjellige typer av IP datagrammer for å tillate forskjellige typer IP-datagrammer (f.eks. datagram som spesifikt krever low delay, high throughput eller reliability) for å skille de fra hverandre. 
* *Datagram length.* Dette er den totale lengden til et IP-datagram (header pluss data. Dette feltet er 16 bits, og derfor er den teoretiske maks.størrelsen til et IP datagram 65,535 bytes - selvom de sjeldent er større en 1,500 bytes.
* *Identifier, flafs, fragmentation offset.* Disse tre feltene har med den såkalte IP-fragmentasjonen, noe vi skal se på snart. IPv6 tilatter ikke fragmentering hos ruterne. 
* *Time-to-live*. Time-to-live-feltet (TTL) er inkludert for å forsikre at datagrammer ikke sirkulerer for alltid pga f.eks. en loop i nettverket. Dersom TTL-feltet er 0, må pakken droppes.
* *Protocol*. Dette fletet brukes kun når IP-datagrammet kommer frem til destinasjonen. Verdien til dette feltet indikerer hvilken spesifikk transportprotokoll som skal ta hånd om dataen i datagrammet. 
* *Header checksum.* Header-checksummen hjelper ruterer i å finne bit-feil i et mottat IP-datagram. Header-checksummen er regnet ut ved å behandle alle 16 byte bits ord i headeren som et tall og summe disse tallene sammen deretter å ta 1s komplement. Dersom man finner en feil pleier man å droppe datagrammet. 
	* Noter at man har slike bit-error-skjekker både på transport og nettverkslaget. Hvorfor vi trenger å skjekke begge steder? Legg merke til at det kun er IP-headeren som blir checksummet ved IP-laget, mens TCP/UDP checksum regnes ut over hele TCP/UDP segmentet. 
* *Source and destination IP addresses.* Når en kilde lager et datagram legger den til sin IP-adresse, og legger til mottakerens IP-adresse. Ofte bestemmer kilden destinasjonsadressen via en DNS-lookup. 
* *Options*. Options-feltet lar en IP-header til å bli utvidet. Siden man har opitons-felt vil IP-datagrammer har variabel størrelse, og man må regne ut hvor dataen starter i datagrammet. 
* *Data (payload)*. Til sist kommer vi til det viktigste feltet, nemlig dataen til datagrammet. Data-feltet til IP-datagrammet inneholder transportlags-segmentet (TCP / UDP) for å bli levert til destinasjonen. Datafeltet kan også holde andre typer data, som en ICMP melding. 


> IP-datagrammet har totalt 20 bytes med header (antar ingen options). Dersom et datagram bærer et TCP-segment, da vil hvert datagram bære totalt 40 bytes med header (20 bytes IP-header pluss 20 bytes TCP-header) sammen med applikasjonsmeldingen. 


##### IP Datagram Fragmentation

I neste kapittel skal vi se at ikke alle link-layer-protokollen kan bære netverkslagspakker på samme størrelse. Noen protokoller kan bære store datagrammer, andre kan bare ta små. Den maksimale mengden data en **link-layer-frame** kan bre kalles *maximum transmission unit (MTU). På grunn av at hvert IP-datagram er innkapslet i en linklagsramme for transport mellom en ruter til en annen, vil MTY-en til en linklagsprotokoll sette en streng grense på lengden til IP-datagrammet. 

Dersom man mottar et IP-datagram fra en inngående link, og den utgående linken har en mindre MTU enn lengden til IP-datagrammet. Hva gjør man da? 

Løsningen er å fragmentere dataen i IP-datagrammet til to mindre IP-datagram, og innkapsle hver av disse i hver sin linklagsramme. Hvert av disse mindre datagrammene er referert til som et **fragment**. Jobben om å defragmentere datagrammene er satt til å være hos endesystemene og ikkke hos ruterne. For å kunne tillate verten å defragmentere så putter man *identifikasjon flag*, og *fragmentation offset* feltene i IP-datagramheaderen. Når et datagram lages så legger den sendende verten på et identifikasjonsnummer. For å forsikre seg om at alle pakker kommer frem, så vil den siste pakken ha flagget satt til 0, mens de andre har den satt til 1. 

![fragment/defragment](https://i.imgur.com/BrOQmnn.png)

> Dersom en eller flere av fragmentene ikke ankommer til destinasjonen vil det ukomplette fragmentet droppet og ikke sendt til transportlaget. 


#### IPv4 Addressing

En vert har typisk en enkel link til nettverket - Når IP i verten ønsker å sende et datagram, gjør den det over denne linken. Grensen mellom verten og den fysiske-linken kalles et **interface**. Grensen mellom en ruter og en av dets linker kalles også et interface - en ruter har dog flere interfacer, et for hver link. 

Ettersom hver vert og ruter er kapable til å sende og motta IP-datagrammer, krever IP at hvert interface hos hver vert og ruter har sin egen IPadresse. En IP-adresse er dermed teknisk assosiert med en interface, istedet for med verten eller ruteren som inneholder interfacet. 

Hver IP-adresse er **32**-bits (4 bytes) lang. Det gir en total på 2<sup>32</sup> mulige IP-adresser (4 milliarder). Disse adressene er typisk skrevet i **dotted-decimal notation**, der hver byte i IP-adressen, i decimal, skilles fra hverandre med et punktum. 

> Adressen *193.32.216.9* i binær notasjon blir 11000001 00100000 11011000 00001001.


Hvert interface på hver eneste vert og ruter på internettet må ha en IP-adresse som er globalt unik. Disse adressene kan ikke bli valgt på en tilfeldig måte, men en del av interfacets IP-adresse er bestemt av subnettet som den er koblet på. 

![ipsubnet](https://i.imgur.com/2TaiQ8u.png)

Figur 4.15 over gir et eksempel på IP-adressering og interfacer. I bildet er det en ruter (med tre interfacer) som brukes til å sammenkoble seg med syv verter. Ta en titt på de tre vertene øverst til venstre. De har alle en IP-adresse på formen  *223.1.1.xxx* (som bestemmer de 24 bitene til venstre av IP-adressen). 

De fire interfacene er altså sammenkoblet med hverandre av et nettverk *som ikke har en ruter*. Dette nettverket kan være sammenkoblet av Ethernet LAN. På IP-term, kalles denne typen for nettverk med sammenkoblede vert-interfacer og et ruter-interface for et **subnet** (Et subnet kalles også et *IP-nettverk*). 

IP-adressering tilegner en adresse til dette subnettet: *223.1.1.0/24*, der */24* notasjonen, kalt en **subnet mask**, indikerer at de 24 mest venstre bit-ene av de 32-bitene definerer subnettets adresse. 


>To determine the subnets, detach each interface from its host or router, creating islands of isolated networks, with interfaces terminating the end points of the isolated networks. Each of these isolated networks is called a subnet.


Internettets adressetildelingsstrategi er kjent som **Classless Interdomain Routing (CIDR)**. CIDR generaliserer begrepet subnet adressering. Som med subnettadressering er 32-biters IP-adresse delt inn i to deler og har igjen den stiplede desimalformen *a.b.c.d / x*, hvor x angir antall biter i den første delen av adressen.

De *x* mest signifikante biter av en adresse på skjemaet *a.b.c.d / x* utgjør nettverksdelen av IP-adressen, og blir ofte referert til som **prefiks** (eller *network prefix*) til adressen.

> Før CIDR ble vedtatt, ble nettverksdelene av en IP-adresse begrenset til å være 8, 16 eller 24 bits i lengden, en adresseringsordning kjent som **classful addressing**, siden subnett med 8-, 16- og 24-biters subnett-adresser ble kjent som henholdsvis klasse A, B og C-nettverk. 

IP-broadcast-adressen 255.255.255.255. Når en vert sender et datagram med destinasjonsadresse 255.255.255.255, blir meldingen levert til alle verter på samme subnett. Rutere videresender eventuelt meldingen til nærliggende subnett også (selv om de vanligvis ikke gjør det).


#### Obtaining a Block of Addresses

For å få en *blokk* med IP-adresser for bruk i en organisasjonens subnett, kan en nettverksadministrator først kontakte sin *ISP*, som vil gi adresser fra en større adresseblokk som allerede er blitt tildelt ISP. For eksempel kan Internett-leverandøren selv ha blitt tildelt adresseblokken *200.23.16.0/20*. Internett-leverandøren kan i sin tur for eksempel dele sin adresseblokk inn i åtte like store sammenhengende adresseblokker og gi en av disse adresseblokkene til opptil åtte organisasjoner som støttes av denne Internett-leverandøren, som vist nedenfor. (Vi har understreket delnettdelen av disse adressene for enkelhets skyld.)

![ipblokker](https://i.imgur.com/QtyyOis.png)

##### Obtaining a Host Address: the Dynamic Host Configuration Protocol (DHCP)

Når en organisasjon har fått en blokk med adresser, kan de tildele individuelle IP-adresser til vert- og ruter-interfacer i organisasjonen sin.
En systemadministrator vil typisk manuelt konfiguere IP-adressene inn i ruteren. 

Vertadressene kan også konfigueres manuelt, denne oppgaven blir ofte gjort med **Dynamic Hot Configuration Protocol (DHCP)**. DHCP tillater en vert å få (tilordnet) en IP-adresse *automatisk*. En nettverksadministrator kan konfigurere DHCP slik at en gitt vert mottar *samme* IP-adresse hver gang den kobles til nettverket, eller en vert kan tilordnes en midlertidig IP-adresse som vil være *forskjellig* hver gang verten kobles til nettverket. I tillegg til vert-IP-adressetildeling tillater DHCP også at en vert lærer tilleggsinformasjon, for eksempel sin nettverksmaske, adressen til sin første hop-router (ofte kalt standard gateway) og adressen til den lokale DNS-serveren.

På grunn av DHCPs evne til å automatisere nettverksrelaterte aspekter ved å koble en vert til et nettverk, blir det ofte referert til som en plug-and-play-protokoll. Denne funksjonen gjør det veldig attraktivt for nettverksadministratoren som på annen måte må utføre disse oppgavene manuelt! 

DCHP er bra i nettverk der det er mange verter som kommer og forlater nettverket ofte.

* DHCP er en klient-server protokoll. En klent er typisk en nyankommen vert som ønsker å få nettverkskonfigureringsinformasjon, som IP-adresse for seg selv. I det enkelste tilfelle har hvert subnett en egen DHCP-server.

Når en ny vert kommer til nettverket og ønsker å koble seg til, skjer det fire steg i DHCP klient-server interaksjonen:

1. *DHCP server discovery.* Klienten sender en **DHCP discover message** med en UDP pakke på port 67, til IP-adresse *255.255.255.255*, og source (klientens) IP-adresse *0.0.0.0*
2. *DHCP server offer*. Når DHCP-serveren mottar requesten, vil den svare klienten med en **DHCP offer message**, som sendes til *255.255.255.255*, denne sendes til broadcast-adressen pga at det kan være flere DHCP-servere på subnettet. Hvert server offer-melding inneholder en transaksjons IS til det mottate discover-melding, den foreslåtte IP-adressen til klienten, nettverksmasken og en leasingtid for IP-adresser - hvor lang tid IP-adressen vil være gyldig for. 
3. *DHCP request*. Den nye klienten kan velge mellom en eller flere server-offere og respondere til det valgte tilbudet med en ***DHCP request message**, og ekkoer tilbake konfigurasjonsparametrene fra den forrige meldingen. 
4. *DHCP ACK*. Serveren respondere til DHCP request message-en med en **DHCP ACK message**, som bekrefter de forespurte parametrene. 

![DHCPinteraksjon](https://i.imgur.com/g6BC57G.png)


#### Network Address Translation (NAT)

Vi vet nå at alle IP-kapable enheter trenger en IP-adresse. Dersom man har brukt opp alle IP-adressene i adresseblokken fra ISP-en sin, hvordan skal man da allokere nye adresser? En tilnærming er med **network address translation (NAT)**. 

Figur 4.22 viser driften av en NAT-aktivert ruteren. Den NAT-aktiverte ruteren, bosatt i hjemmet, har et grensesnitt som er en del av hjemmenettverket til høyre i figur 4.22. Adressering i hjemmenettverket er akkurat som vi har sett ovenfor - alle fire grensesnittene i hjemmenettverket har samme subnettadresse på *10.0.0 / 24*. Adresseområdet *10.0.0.0/8* er en av tre deler av IP-adresseplassen som er reservert i for et privat nettverk eller et **rike** med private adresser, for eksempel hjemmenettverket i Figur 4.22. 

> Et rike med private adresser refererer til et nettverk hvis adresser bare har betydning for enheter innenfor det aktuelle nettverket. 


For å se hvorfor dette er viktig, bør du vurdere det faktum at det er hundretusenvis av hjemmenettverk, og mange bruker samme adresserom, *10.0.0.0/24*. Enheter innenfor et gitt hjemmenettverk kan sende pakker til hverandre ved hjelp av *10.0.0.0/24* adressering. Imidlertid kan pakker videresendt utover hjemmenettverket til det større globale Internett, tydeligvis ikke bruke disse adressene (som enten en kilde eller en destinasjonsadresse) fordi det er hundrevis av tusenvis av nettverk som bruker denne adresseblokken. 


Det vil si at *10.0.0.0/24* adressene bare kan ha betydning innenfor det oppgitte hjemmenettverket. Men hvis private adresser bare har mening innenfor et gitt nettverk, hvordan håndteres adressering når pakkene sendes til eller mottas fra det globale Internett, hvor adressene er nødvendigvis unike? Svaret ligger i å forstå NAT:


* Den NAT-aktiverte ruteren ser ikke ut som en ruter for omverdenen. I stedet oppfører NAT-ruteren seg til omverdenen som en enkelt enhet med en enkelt IP-adresse. I Figur 4.22 har all trafikk som forlater hjemme-ruteren for det større Internett en kilde-IP-adresse på *138.76.29.7*, og all trafikk som kommer inn i hjem-ruteren må ha en destinasjonsadresse på *138.76.29.7*. 

* I hovedsak skjuler den NAT-aktiverte ruteren detaljene i hjemmenettverket fra omverdenen. Kanskje du lure på hvor hjemmenettverkene får adressene deres, og hvor ruteren får sin eneste IP-adresse. Ofte er svaret det samme - DHCP! 
	* Ruteren får adressen fra Internett-leverandørens DHCP-server, og ruteren kjører en DHCP-server for å gi adresser til datamaskiner innenfor NAT-DHCP-ruter-styrte hjemmenettverkets adresseplass.



Hvis alle datagrammer som kommer til NAT-ruteren fra WAN, har *samme* destinasjons-IP-adresse, hvordan kjenner ruteren den **interne verten** som den skal videresende et gitt datagram?

Trikset er å bruke et **NAT-oversettelsestabell** på NAT-ruteren, og å inkludere *portnumre* samt *IP-adresser* i tabelloppføringene. Når en intern vert sender en pakke sendes det med intern IP-adresse samt et vilkårlig portnummer samt destinasjonsaddresse. Hos ruteren så lagres IP-adressen fra LAN-siden og WAN-siden og det interne portnummeret, samt et vilkårlig kildeportnummer for ruteren. Dette lagres i oversettelsestabellen.

Når datagrammet fra destinasjonsadressen ankommer NAT-ruteren, så vil ruteren indekserer ruteren NAT-oversettelsestabellen ved hjelp av destinasjonens IP-adresse og destinasjonsportnummer for å oppnå riktig IP-adresse (*10.0.0.1*) og destinasjonsportnummer (*3345*). 

> Har vært diskusjon rundt NAT-oversettelse da flere mener at portnummere skal brukes for å adressere prosesser, ikke adressere verter. 

* Problem ved P2P, dersom Vert A ønsker å etablere TCP-tilkobling til Vert B, fungerer ikke dette, da Vert B ikke kan oppføre seg som en server og akseptere TCP-tilkobligner. 
	* Mulig å unngå dette med **connection reversal / NAT traversal** ved at Vert A, spør Vert B gjennom en Vert C, som ikke er er bak en NAT, om å initiere en TCP-tilkobling direkte tilbake til Vert A. 



#### UPnP

*NAT-traversal* leveres i økende grad av **Universal Plug and Play** (*UPnP*), som er en protokoll som gjør at en vert kan oppdage og konfigurere et nærliggende NAT. UPnP krever at både verten og NATen er UPnP-kompatible. Med UPnP kan et program som kjører i en vert, be om en NAT-kartlegging mellom dens (private IP-adresse, privat portnummer) og (offentlig IP-adresse, offentlig portnummer) for noen forespurt offentlig portnummer. 

Hvis NAT aksepterer forespørselen og oppretter kartlegging, kan nodene fra utsiden initiere TCP-tilkoblinger til (offentlig IP-adresse, offentlig portnummer). 

Videre lar UPnP programmet vite verdien av (offentlig IP-adresse, offentlig portnummer), slik at søknaden kan annonsere den til omverdenen.

Oppsummert lar UPnP eksterne verter å initiere kommunikasjonsøkter til NAT-ede verter, ved hjelp av enten TCP eller UDP. NAT har lenge vært en *nemesis* for P2P applikasjoner - UPnP, som gir en effektiv og robust NAT-traversal løsning, kan være deres frelser.



#### Internet Control Message Protocol (ICMP)

ICMP brukes av verter og rutere til å kommunisere nettverkslagsinformasjon til hverandre. Den mest typiske bruken av ICMP er for *feilrapportering*. For eksempel, når du kjører en Telnet-, FTP- eller HTTP-økt, kan det hende du har oppdaget en feilmelding, for eksempel “Destination network unreachable”. 

Denne meldingen hadde sin opprinnelse i ICMP. På et tidspunkt kunne en IP-ruteren ikke finne en vei til verten spesifisert i Telnet-, FTP- eller HTTP-applikasjonen. Denne ruteren skapte og sendte en *type-3* ICMP melding til verten din som angir feilen.

ICMP er ofte ansett som en del av IP, men arkitektonisk ligger den like *over* IP, da ICMP-meldinger er ført inne i IP-datagrammer. Det vil si at ICMP-meldinger blir båret som IP-nyttelast, akkurat som TCP- eller UDP-segmenter blir båret som IP-nyttelast. 

På samme måte, når en vert mottar et IP datagram med ICMP spesifisert som den øverste lagprotokollen, demultiplekse datagrammets innhold til ICMP, akkurat som det ville demultiplekse datagrammets innhold til TCP eller UDP.


* ICMP-meldinger har en *type* og et *kodefelt*, og inneholder overskriften og de første 8 byte av IP-datagrammet som forårsaket at ICMP-meldingen genereres i utgangspunktet (slik at avsenderen kan bestemme datagrammet som forårsaket feilen). 
* Utvalgte ICMP-meldingstyper er vist i Figur 4.23. Merk at ICMP-meldinger ikke bare brukes til signalfeilforhold.
* Det velkjente pingprogrammet sender en *ICMP type 8 kode 0* melding til den angitte verten. Destinasjonsverten, ser ekkoforespørselen, sender tilbake en *type 0 kode 0 ICMP-ekko-svar*. 

**Traceroute:** Sender ICMP-meldinger i vanlige datagrammer med UDP-segmenter, med usannsynlige UDP portnumre. Det første datagrammet har TTL på 1, neste har 2, tredje har 3, osv. Kilden starter også timeren for hver av datagrammene. Når det *n*-te datagrammet kommer til den *n*-te ruteren, ovserverer den *n*-te ruteren at TTL-en til datagrammet har gått ut, og sender en ICMP-warning melding til verten. Slik kan Traceroute karlegge antall og identiteten til ruterne mellom seg og destinasjonen. 


#### IPv6

På 1990 begynte de å se på en etterfølger til IPv4-protokollen - i hovedsak fordi de 32-bit IP-adressene begynte å bli brukt opp. Det ble så utviklet en ny IP protokoll, IPv6. 


##### IPv6 Datagram Format

Formatet til IPv6-datagrammet er vist i Figur 4.24 under. De viktigste endringene i IPv6 er tydelige i datagramformatet:

* *Expanded addressing capabilities.* IPv6 øker størrelsen på IP-adresser fra 32 til 128 bits. Dette gør at verden ikke kommer til å gå tom for IP-adresser. Finnes også nå **anyone address**, som lar et datagram å bli levert til enhver av en gruppe av verter.
* *A streamlined 40-byted header.* Noen IPv4 felt har blitt droppet eller gjort valgfrie. Den resulterende 40-byte fast-lengde headeren tillater raskere prosessering av IP-datagrammet.
* *Flow labelng and priority.* IPv6 har en unnvikende definisjon av **flow** (*nor. flow*). Dette tillater merking av pakker som tilhører bestemte strømmer som avsenderen ønsker spesiell håndtering for, for eksempel en ikke-standardkvalitet-tjeneste eller sanntids-tjeneste. For eksempel kan lyd og videooverføring sannsynligvis bli behandlet som en strømning. På den annen side kan de mer tradisjonelle applikasjonene, for eksempel filoverføring og e-post, ikke behandles som strømmer.

Følgende felt er definert i IPv6:
* *Version.* Dette 4-bit-feltet identifiserer IP-versjonsnummeret, IPv6 bærer en verdi av 6 i dette feltet. 

* *Traffic class*. 8-bit felt som er nesten likt TOS-feltet hos IPv4

* *Flow label.* 20-bit felt som identifiserer flow-en til datagrammet.

* *Payload length*. 16-bit verdi som gir antall bytes som følger etter headeren.

* *Next header.* Feltet identifiserer protokollen som datafeltet i datagrammet skal bli levert til (f.eks. UDP eller TCP).

* *Hop limit*. Innholdet i dette feltet blir dekrementert med en hos hver ruter som videresender datagrammet. Dersom hoplimit-en blir 0, vil datagrammet bli kastet.

* *Source and destination addresses.* IPv6-adressene til kilde og destinasjon, to felt på 128-bit. 

* *Data*. Dette er payload-delen av IPv6 datagrammet.


Felt som har forsvunnet fra det vi så i IPv4:

* *Fragmentaton/Reassembly*: IPv6 tillater ikke fragmentering eller refragmentering hos mellomliggende rutere, dette kan kun bli gjort hos kilde eller destinasjon. Dersom en pakke kommer til en utgående link som har mindre kapasitet enn størrelsen til datagrammet, blir pakken droppet, og en ICMP-error-melding blir sendt tilbake. 
* *Header checksum*: I IPv4, måtte checksummen bli regnet ut på nytt for hver ruter, pga den endrende verdien TTL. Dette tok tid, og som med fragmentering, var dette en for dyr operasjon i IPv4. 
* *Options*. Et options-felt er ikke lenger en del av IP-headeren. Men er ikke borte, kan bruke *next headers*-feltet.


##### Overgangen fra IPv4 til IPv6:

*Alternativer:*

* Et alternativ ville være å erklære en flaggdag - en gitt tid og dato da alle Internett-maskiner ville bli slått av og oppgradert fra IPv4 til IPv6. 

* Sannsynligvis den enkleste måten å introdusere IPv6-kompatible noder på, er en **dual-stack**-tilnærming, hvor IPv6-noder også har en fullstendig IPv4-implementering. 
	* En slik knute, referert til som en IPv6 / IPv4 knutepunkt i RFC 4213, har evnen til å sende og motta både IPv4 og IPv6 datagrammer. Når du samarbeider med en IPv4-node, kan en IPv6 / IPv4-node bruke IPv4 datagrammer. Når du samarbeider med en IPv6-node, kan den snakke IPv6. 
	* IPv6 / IPv4-noder må ha både IPv6- og IPv4-adresser
	* Bruke DNS for å bestemme om noder er kompatible med IPv4 eller IPv6. 
	* *Problem:* Når et IPv6-datagram blir konvertert over til et IPv4-datagram, vil feltene hos IPv6-datagrammet som ikke har noen motpart i IPv4 forsvinne. 
	
* Et alternativ til dual stack-tilnærmingen er kjent som **tunneling**. Tunneling kan løse problemet som er nevnt ovenfor. Den grunnleggende ideen bak tunneling er følgende. Anta at to IPv6-noder vil interoperere ved hjelp av IPv6 datagrammer, men er koblet til hverandre med IPv4-rutere. Vi refererer til det settet med IPv4-rutere mellom to IPv6-rutere som en **tunnel**, som illustrert i figur 4.26. Ved tunneling tar IPv6-noden på senderens side av tunnelen hele IPv6 datagrammet og setter det i **data** (payload)-feltet til et IPv4 datagram, og sender det til den andre IPv6-ruteren.


![dualstack](https://i.imgur.com/rDI1FAy.png)

![tunnelling](https://i.imgur.com/fAjMYdK.png)

> **En viktig leksjon som vi kan lære av IPv6-opplevelsen er at det er enormt vanskelig å endre protokollene til nettverkslag**


#### Brief Introduction to IP Security

Med sikkerhet som en stor bekymring i dag, har Internettforskere flyttet videre til å designe nye protokoller for nettverkslag som gir en rekke sikkerhetstjenester. 

En av disse protokollene er *IPsec*, en av de mest populære sikre nettverkslagprotokollene og også distribuert i Virtual Private Networks (*VPN*). Selv om IPsec og dets kryptografiske underlag er dekket i detalj i kapittel 8, gir vi en kort introduksjon på høyt nivå til IPsec-tjenester i denne delen.

IPsec er designet for å være bakoverkompatibel med IPv4 og IPv6. Spesielt, for å høste fordelene med IPsec, trenger vi ikke å erstatte protokollstabler i alle rutere og verter på Internett. Hvis du for eksempel bruker transportmodusen (en av to IPsec "mode"-ene), hvis to verter vil kommunisere sikkert, må IPsec bare være tilgjengelig i de to vertene. Alle andre rutere og verter kan fortsette å kjøre "vanilla IPv4".

> Vanilla = Straight out of the box

Vi skal nå se på IPsec sin transportmodus. På sendingssiden sender transportlaget et segment til IPsec. IPsec krypterer deretter segmentet, legger til flere sikkerhetsfelt i segmentet, og inkapsulerer den resulterende nyttelasten i et vanlig IP datagram. (Det er faktisk litt mer komplisert enn dette, som vi ser i kapittel 8.) Senderverten sender deretter datagrammet til Internett, som overfører det til mottakerverten. Der, dekrypterer IPsec segmentet og sender det ukrypterte segmentet til transportlaget.


Tjenestene som tilbys av en IPsec-økt inkluderer:

* *Cryptographic agreement.* Kommuniserende verter kan bli enige om crypto-algoritmer og nøkler
* *Encrypting of IP datagram payloads*. IPsex krypterer payloaden til datagrammet. 
* *Data intergrity*. IPsex tillater mottakende vert å verifisere at datagrammet ikke har blitt modifisert.
* *Origin authentication*. Mottakende vert kan være sikker på at kilde IP-adressen i datagrammet er den faktiske kilden til datagrammet.


 
 <a name="kap5"></a>
## Kapittel 5 - The Link Layer: Links, Access Networks, and LANs




