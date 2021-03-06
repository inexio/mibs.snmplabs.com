#
# PySNMP MIB module VERTICAL15-1600ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERTICAL15-1600ROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity, Counter64, Bits, iso, Gauge32, Integer32, NotificationType, MibIdentifier, enterprises, NotificationType, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "iso", "Gauge32", "Integer32", "NotificationType", "MibIdentifier", "enterprises", "NotificationType", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vertical = MibIdentifier((1, 3, 6, 1, 4, 1, 2338))
v1600Router = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 15))
v1600InstalledSlot = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600InstalledSlot.setStatus('mandatory')
if mibBuilder.loadTexts: v1600InstalledSlot.setDescription('The slot number in which the 1600-Router Card is installed.')
v1600Ser0ChannelWidth = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600Ser0ChannelWidth.setStatus('mandatory')
if mibBuilder.loadTexts: v1600Ser0ChannelWidth.setDescription('The number of channels used by the internal interface (S0) to connect to T1.')
v1600Ser0T1InterfaceSlot = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600Ser0T1InterfaceSlot.setStatus('mandatory')
if mibBuilder.loadTexts: v1600Ser0T1InterfaceSlot.setDescription('Slot number of T1 card configured for the WAN interface.')
v1600Ser0T1InterfacePort = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600Ser0T1InterfacePort.setStatus('mandatory')
if mibBuilder.loadTexts: v1600Ser0T1InterfacePort.setDescription('Port number of the T1 card configured for WAN interface.')
v1600Ser0T1InterfaceStartChan = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600Ser0T1InterfaceStartChan.setStatus('mandatory')
if mibBuilder.loadTexts: v1600Ser0T1InterfaceStartChan.setDescription('Starting channel used by the internal interface (S0) to T1.')
v1600FlashCardReady = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ready", 0), ("notReady", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600FlashCardReady.setStatus('mandatory')
if mibBuilder.loadTexts: v1600FlashCardReady.setDescription('Ready = Flash card inserted , Not Ready = Flash card removed.')
v1600CardReadyLED = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600CardReadyLED.setStatus('mandatory')
if mibBuilder.loadTexts: v1600CardReadyLED.setDescription('On= 1600-Router Card is fully operational, Off=1600-Router Card is not Ready.')
v1600CardErrorLED = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600CardErrorLED.setStatus('mandatory')
if mibBuilder.loadTexts: v1600CardErrorLED.setDescription('On= 1600-Router Card is not ready, Off=1600-Router Card is Ready.')
v1600RouterOKLED = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600RouterOKLED.setStatus('mandatory')
if mibBuilder.loadTexts: v1600RouterOKLED.setDescription('Router OK LED Status. This variable is no longer used and will be deprecated in the next release.')
v1600ExtSerial1ConnOK = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("on", 1), ("off", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600ExtSerial1ConnOK.setStatus('mandatory')
if mibBuilder.loadTexts: v1600ExtSerial1ConnOK.setDescription('Shows whether a cable is connected to the 5-in-1 External Serial(S1) Connector. on=Connected , off=Not Connected')
v1600ExtSerial1DCD = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600ExtSerial1DCD.setStatus('mandatory')
if mibBuilder.loadTexts: v1600ExtSerial1DCD.setDescription('Shows the status of 5-in-1 External Serial(S1) DCD LED. on=Link is up, off=Link is down')
v1600SwitchSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600SwitchSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: v1600SwitchSlotNum.setDescription('Switch port Slot number. This variable is no longer used and will be deprecated in the next release.')
v1600EthSwitchedPorts = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600EthSwitchedPorts.setStatus('mandatory')
if mibBuilder.loadTexts: v1600EthSwitchedPorts.setDescription('Number of Swithced Ethernet ports on 1600-Router Card.')
v1600SwitchStat = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600SwitchStat.setStatus('mandatory')
if mibBuilder.loadTexts: v1600SwitchStat.setDescription('More Information about Switch Port statistics. This variable is no longer used and will be deprecated in the next release.')
v1600IntSerial0ConnOK = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600IntSerial0ConnOK.setStatus('mandatory')
if mibBuilder.loadTexts: v1600IntSerial0ConnOK.setDescription('Internal WAN interface (S0) connection to T1 LED status.')
v1600IntSerial0DCD = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600IntSerial0DCD.setStatus('mandatory')
if mibBuilder.loadTexts: v1600IntSerial0DCD.setDescription('Internal WAN interface (S0) Link LED status. on=Link is up, off=Link is down.')
v1600RouterEthLinkOK = MibScalar((1, 3, 6, 1, 4, 1, 2338, 15, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("on", 0), ("off", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: v1600RouterEthLinkOK.setStatus('mandatory')
if mibBuilder.loadTexts: v1600RouterEthLinkOK.setDescription('Shows status of internal Ethernet Interface (E0) LED. on=Link is up , off=Link is down')
v1600CardNotReady = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,68)).setObjects(("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot"))
if mibBuilder.loadTexts: v1600CardNotReady.setDescription('Notification sent when the 1600-Router card is not ready at boot time.')
v1600FlashCardNotReady = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,69)).setObjects(("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot"))
if mibBuilder.loadTexts: v1600FlashCardNotReady.setDescription('The Flash card on the 1600-Router Card is either removed or not inserted properly. Please insert the Flash Card after you power down the system.')
v1600FlashCardReadyTrap = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,76)).setObjects(("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot"))
if mibBuilder.loadTexts: v1600FlashCardReadyTrap.setDescription('The Flash card on the 1600-Router Card has been re-inserted.')
v1600RouterReady = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,77)).setObjects(("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot"))
if mibBuilder.loadTexts: v1600RouterReady.setDescription('The Router is ready and has booted from the image on the Flash Card.')
v1600RouterNotReady = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,78)).setObjects(("VERTICAL15-1600ROUTER-MIB", "v1600InstalledSlot"))
if mibBuilder.loadTexts: v1600RouterNotReady.setDescription('The Router is has not booted from the image on the Flash Card or the system is still booting. Please open the 1600-Router console and make sure that the Router boots from the image on the Flash Card for normal operation of the system.')
mibBuilder.exportSymbols("VERTICAL15-1600ROUTER-MIB", v1600RouterReady=v1600RouterReady, v1600EthSwitchedPorts=v1600EthSwitchedPorts, v1600CardReadyLED=v1600CardReadyLED, v1600Ser0T1InterfaceStartChan=v1600Ser0T1InterfaceStartChan, v1600CardErrorLED=v1600CardErrorLED, v1600Ser0T1InterfaceSlot=v1600Ser0T1InterfaceSlot, v1600FlashCardReady=v1600FlashCardReady, v1600ExtSerial1DCD=v1600ExtSerial1DCD, v1600IntSerial0DCD=v1600IntSerial0DCD, v1600SwitchSlotNum=v1600SwitchSlotNum, v1600Router=v1600Router, v1600FlashCardReadyTrap=v1600FlashCardReadyTrap, v1600FlashCardNotReady=v1600FlashCardNotReady, v1600CardNotReady=v1600CardNotReady, v1600Ser0ChannelWidth=v1600Ser0ChannelWidth, v1600InstalledSlot=v1600InstalledSlot, v1600RouterNotReady=v1600RouterNotReady, v1600RouterEthLinkOK=v1600RouterEthLinkOK, vertical=vertical, v1600RouterOKLED=v1600RouterOKLED, v1600SwitchStat=v1600SwitchStat, v1600IntSerial0ConnOK=v1600IntSerial0ConnOK, v1600Ser0T1InterfacePort=v1600Ser0T1InterfacePort, v1600ExtSerial1ConnOK=v1600ExtSerial1ConnOK)
