#
# PySNMP MIB module Fore-tp25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-tp25-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Integer32, iso, NotificationType, Gauge32, IpAddress, TimeTicks, ObjectIdentity, Bits, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Integer32", "iso", "NotificationType", "Gauge32", "IpAddress", "TimeTicks", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreTP25Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9))
if mibBuilder.loadTexts: foreTP25Module.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreTP25Module.setOrganization('FORE')
if mibBuilder.loadTexts: foreTP25Module.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreTP25Module.setDescription(' The foreTP25 Module supports all switchs that have the 25.6Mbps UTP/STP port module.')
tp25ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1))
tp25StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2))
tp25ConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1), )
if mibBuilder.loadTexts: tp25ConfTable.setStatus('current')
if mibBuilder.loadTexts: tp25ConfTable.setDescription('A table of TP25(25.6Mbps UTP/STP switch port configuration information.')
tp25ConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1), ).setIndexNames((0, "Fore-tp25-MIB", "tp25ConfBoard"), (0, "Fore-tp25-MIB", "tp25ConfModule"), (0, "Fore-tp25-MIB", "tp25ConfPort"))
if mibBuilder.loadTexts: tp25ConfEntry.setStatus('current')
if mibBuilder.loadTexts: tp25ConfEntry.setDescription('A table entry containing TP25 configuration information for each port.')
tp25ConfBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ConfBoard.setStatus('current')
if mibBuilder.loadTexts: tp25ConfBoard.setDescription("The index of this port's switch board.")
tp25ConfModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ConfModule.setStatus('current')
if mibBuilder.loadTexts: tp25ConfModule.setDescription('The network module of this port.')
tp25ConfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ConfPort.setStatus('current')
if mibBuilder.loadTexts: tp25ConfPort.setDescription('The number of this port.')
tp25MediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp25UTP", 1), ("tp25STP", 2), ("tp25FTP", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25MediaType.setStatus('current')
if mibBuilder.loadTexts: tp25MediaType.setDescription('This variable represents the type of the physical medium connected to the TP25 interface: tp25UTP (1) means physical media is UTP tp25STP (2) means physical media is STP tp25FTP (3) means physical media is FTP.')
tp25LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp25NoLoop", 1), ("tp25DiagLoop", 2), ("tp25LineLoop", 3))).clone('tp25NoLoop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tp25LoopbackConfig.setStatus('current')
if mibBuilder.loadTexts: tp25LoopbackConfig.setDescription('This variable represents the loopback configuration of the TP25 interface. tp25NoLoop (1) means that the interface is not in a loopback state. tp25DiagLoop (2) means that the transmit data stream is looped back to the receiver. tp25LineLoop (3) also known as remote loopback, in this state received data is transfered to upstream system as well as looped back to the transmitter.')
tp25RxTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tp25NoTimingPresent", 1), ("tp25TimingPresent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25RxTiming.setStatus('current')
if mibBuilder.loadTexts: tp25RxTiming.setDescription('This variable represents the type of the physical medium connected to the TP25 interface: tp25NoTimingPresent (1) means port is not receiving sync pulses. tp25TimingPresent (2) means port is receiving sync pulses.')
tp25ErrorTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1), )
if mibBuilder.loadTexts: tp25ErrorTable.setStatus('current')
if mibBuilder.loadTexts: tp25ErrorTable.setDescription('A table of TP25 error counters.')
tp25ErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1), ).setIndexNames((0, "Fore-tp25-MIB", "tp25ErrorBoard"), (0, "Fore-tp25-MIB", "tp25ErrorModule"), (0, "Fore-tp25-MIB", "tp25ErrorPort"))
if mibBuilder.loadTexts: tp25ErrorEntry.setStatus('current')
if mibBuilder.loadTexts: tp25ErrorEntry.setDescription('A table entry containing TP25 error counters.')
tp25ErrorBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ErrorBoard.setStatus('current')
if mibBuilder.loadTexts: tp25ErrorBoard.setDescription("The index of this port's switch board.")
tp25ErrorModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ErrorModule.setStatus('current')
if mibBuilder.loadTexts: tp25ErrorModule.setDescription('The network module of this port.')
tp25ErrorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ErrorPort.setStatus('current')
if mibBuilder.loadTexts: tp25ErrorPort.setDescription('The number of this port.')
tp25ErrorSymbol = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25ErrorSymbol.setStatus('current')
if mibBuilder.loadTexts: tp25ErrorSymbol.setDescription('The number of all undefined 5 bit symbols received.')
tp25AtmTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2), )
if mibBuilder.loadTexts: tp25AtmTable.setStatus('current')
if mibBuilder.loadTexts: tp25AtmTable.setDescription('A table of TP25 ATM statistics information.')
tp25AtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1), ).setIndexNames((0, "Fore-tp25-MIB", "tp25AtmBoard"), (0, "Fore-tp25-MIB", "tp25AtmModule"), (0, "Fore-tp25-MIB", "tp25AtmPort"))
if mibBuilder.loadTexts: tp25AtmEntry.setStatus('current')
if mibBuilder.loadTexts: tp25AtmEntry.setDescription('A table entry containing TP25 ATM statistics information.')
tp25AtmBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25AtmBoard.setStatus('current')
if mibBuilder.loadTexts: tp25AtmBoard.setDescription("The index of this port's switch board.")
tp25AtmModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25AtmModule.setStatus('current')
if mibBuilder.loadTexts: tp25AtmModule.setDescription('The network module of this port.')
tp25AtmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25AtmPort.setStatus('current')
if mibBuilder.loadTexts: tp25AtmPort.setDescription('The number of this port.')
tp25AtmHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25AtmHCSs.setStatus('current')
if mibBuilder.loadTexts: tp25AtmHCSs.setDescription('Number of header check sequence (HCS) error events. The HCS is a CRC-8 calculation over the first 4 octets of the ATM cell header.')
tp25AtmRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25AtmRxCells.setStatus('current')
if mibBuilder.loadTexts: tp25AtmRxCells.setDescription('Number of ATM cells that were received.')
tp25AtmTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 9, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tp25AtmTxCells.setStatus('current')
if mibBuilder.loadTexts: tp25AtmTxCells.setDescription('Number of non-null ATM cells that were transmitted.')
mibBuilder.exportSymbols("Fore-tp25-MIB", tp25LoopbackConfig=tp25LoopbackConfig, tp25ErrorSymbol=tp25ErrorSymbol, tp25ConfModule=tp25ConfModule, tp25AtmBoard=tp25AtmBoard, tp25AtmPort=tp25AtmPort, foreTP25Module=foreTP25Module, tp25AtmRxCells=tp25AtmRxCells, tp25AtmModule=tp25AtmModule, tp25AtmTable=tp25AtmTable, tp25RxTiming=tp25RxTiming, tp25ErrorTable=tp25ErrorTable, tp25ErrorBoard=tp25ErrorBoard, tp25AtmEntry=tp25AtmEntry, tp25MediaType=tp25MediaType, tp25ErrorPort=tp25ErrorPort, tp25ConfTable=tp25ConfTable, tp25ErrorModule=tp25ErrorModule, tp25ErrorEntry=tp25ErrorEntry, tp25ConfEntry=tp25ConfEntry, tp25AtmHCSs=tp25AtmHCSs, tp25ConfPort=tp25ConfPort, tp25StatsGroup=tp25StatsGroup, tp25ConfBoard=tp25ConfBoard, tp25AtmTxCells=tp25AtmTxCells, tp25ConfGroup=tp25ConfGroup, PYSNMP_MODULE_ID=foreTP25Module)
