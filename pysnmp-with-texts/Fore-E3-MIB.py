#
# PySNMP MIB module Fore-E3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-E3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Counter64, Integer32, NotificationType, Unsigned32, Gauge32, ModuleIdentity, IpAddress, iso, MibIdentifier, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Counter64", "Integer32", "NotificationType", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "iso", "MibIdentifier", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
foreE3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5))
if mibBuilder.loadTexts: foreE3.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreE3.setOrganization('FORE')
if mibBuilder.loadTexts: foreE3.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreE3.setDescription('write something interesting here')
e3ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1))
e3StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2))
e3ConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1), )
if mibBuilder.loadTexts: e3ConfTable.setStatus('current')
if mibBuilder.loadTexts: e3ConfTable.setDescription('A table of E3 switch port configuration information.')
e3ConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1), ).setIndexNames((0, "Fore-E3-MIB", "e3ConfBoard"), (0, "Fore-E3-MIB", "e3ConfModule"), (0, "Fore-E3-MIB", "e3ConfPort"))
if mibBuilder.loadTexts: e3ConfEntry.setStatus('current')
if mibBuilder.loadTexts: e3ConfEntry.setDescription('A table entry containing E3 configuration information for each port. Not all RFC1407 configuration table variables are included, and some are modified.')
e3ConfBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3ConfBoard.setStatus('current')
if mibBuilder.loadTexts: e3ConfBoard.setDescription("The index of this port's switch board.")
e3ConfModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3ConfModule.setStatus('current')
if mibBuilder.loadTexts: e3ConfModule.setDescription('The network module of this port.')
e3ConfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3ConfPort.setStatus('current')
if mibBuilder.loadTexts: e3ConfPort.setDescription('The number of this port.')
e3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("e3OtherLineType", 1), ("e3Framed", 2), ("e3Plcp", 3))).clone('e3Framed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3LineType.setStatus('current')
if mibBuilder.loadTexts: e3LineType.setDescription('This variable indicates the type of cell delineation being used. The e3Plcp(3) value indicates cell delineation according to CCITT G.751 using PLCP (Physical Layer Converhence Protocol) framing, while e3Framed(2) indicates HCS (Header Check Sequence) based framing. This variable is defined in the rfc1407 configuration table as dsx3LineType. According to RFC1407, the different values are: e3Framed(2) specification: CCITT G.751 e3Plcp(3) specification: ETSI T/NA(91)18.')
e3LineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("e3OtherLineCoding", 1), ("e3HDB3", 2))).clone('e3HDB3')).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3LineCoding.setStatus('current')
if mibBuilder.loadTexts: e3LineCoding.setDescription('This variable describes the variety of Zero Code suppression used on this interface, which in turn affects a number of its characteristics. e3HDB3 (1) refers to the use of specified pattern of normal bits and bipolar violations which are used to replaced sequences of zero bits of specified length. This variable is defined in the rfc1407 configuration table as dsx3LineCoding.')
e3SendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("e3SendNoCode", 1), ("e3SendLineCode", 2), ("e3SendPayloadCode", 3), ("e3SendResetCode", 4), ("e3SendDS1LoopCode", 5), ("e3SendTestPattern", 6))).clone('e3SendNoCode')).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3SendCode.setStatus('current')
if mibBuilder.loadTexts: e3SendCode.setDescription('This variable indicates what type of code is being sent across the E3/E3 interface by the device. The values mean: e3SendNoCode sending looped or normal data e3SendLineCode sending request for a line loopback e3SendPayloadCode sending a request for a payload loopback (i.e. all DS1/E1 in a E3/E3 frame) e3SendResetCode sending a loopback deactivation request e3SendDS1LoopCode requesting to loopback a particular DS1/E1 within a E3/E3 frame e3SendTestPattern sending a test pattern.')
e3ReceiveCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("e3ReceiveNoCode", 1), ("e3ReceiveLineCode", 2), ("e3ReceivePayloadCode", 3), ("e3ReceiveResetCode", 4), ("e3ReceiveDS1LoopCode", 5), ("e3ReceiveTestPattern", 6))).clone('e3ReceiveNoCode')).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3ReceiveCode.setStatus('current')
if mibBuilder.loadTexts: e3ReceiveCode.setDescription('This variable indicates the type of code that was received across the E3/E3 interface. The values mean: e3ReceiveNoCode receiving looped or normal data e3ReceiveLineCode receiving request for a line loopback e3ReceivePayloadCode receiving a request for a payload loopback (i.e. all DS1/E1 in a E3/E3 frame) e3ReceiveResetCode receiving a loopback deactivation request e3ReceiveDS1LoopCode receiving a request to loopback a particular DS1/E1 within a E3/E3 frame e3ReceiveTestPattern receiving a test pattern.')
e3LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("e3NoLoop", 1), ("e3CellLoop", 2), ("e3PayloadLoop", 3), ("e3DiagLoop", 4), ("e3LineLoop", 5), ("e3OtherLoop", 6))).clone('e3NoLoop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3LoopbackConfig.setStatus('current')
if mibBuilder.loadTexts: e3LoopbackConfig.setDescription("This variable represents the loopback configuration of the E3 interface. This variable is defined in the rfc1407 configuration table as dsx3LoopbackConfig, with slightly different values. e3NoLoop (1) means that the interface is not in a loopback state. e3CellLoop (2) means that cells that are processed by the receiving component are not written into the receive FIFO, but into the transmit FIFO for retransmission. e3PayloadLoop (3) means that the receive signal is looped back for retransmission after it has passed through the port's reframing function. e3DiagLoop (4) means that the transmit data stream is looped back to the receiver. e3LineLoop (5) means that the received data stream is reflected back to the sender. e3OtherLoop (6) means that the interface is in a loopback that is not defined here.")
e3TxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rxTiming", 1), ("localTiming", 2))).clone('localTiming')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3TxClockSource.setStatus('current')
if mibBuilder.loadTexts: e3TxClockSource.setDescription('The source of the transmit clock.')
e3RxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("descrambling", 1), ("noDescrambling", 2))).clone('noDescrambling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3RxScrambling.setStatus('current')
if mibBuilder.loadTexts: e3RxScrambling.setDescription('This variable indicates whether the information is being descrambled on receiving. It should be set the same as the transmitting side.')
e3TxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scrambling", 1), ("noScrambling", 2))).clone('noScrambling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3TxScrambling.setStatus('current')
if mibBuilder.loadTexts: e3TxScrambling.setDescription('This variable indicates whether the information (48 octet payload) is being scrambled before transmitting. It should be set the same as the receiving side.')
e3LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3LineStatus.setStatus('current')
if mibBuilder.loadTexts: e3LineStatus.setDescription('This variable indicates the Line Status of the interface. A similar object is defined in the rfc1407 configuration table as dsx3LineStatus (the e3RxFERF bit is not defined in rfc1407) . The variable contains loopback state information and failure state information. It is a bit map represented as a sum. The e3NoAlarm should be set if and only if no other flag is set. The various bit positions are: 1 e3NoAlarm 2 e3RxAIS Receiving AIS failure state 4 e3TxAIS Transmitting AIS (Not used) 8 e3PLCPLOF Receiving PLCP LOF failure state 16 e3LOS Receiving LOS failure state 32 e3LoopbackState Looping the received signal 64 e3HcsLCD Loss of Cell Delineation (Not used) 128 e3RxFERF Receiving Far End Receive Failure 256 e3OtherFailure any line status not defined here. 512 e3RxPLCPYellow Receiving PLCP Yellow 1024 e3TxPLCPYellow Transmitting PLCP Yellow 2048 e3RxLOF Receving LOF alarm. 4096 e3TxFERF Transmitting FERF 32768 e3RxLCD Receiving LCD failure indication')
e3IdleUnassignedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e3IdleUnassignedCells.setStatus('current')
if mibBuilder.loadTexts: e3IdleUnassignedCells.setDescription("This variable indicates the types of cells that should be sent in case there is no real data to send. According to the ATM Forum, Unassigned cells should be sent (octet 1-3 are 0's, octet 4 is 0000xxx0, where x is 'don't care'). According to the CCITT specifications, Idle cells should be sent (everything is '0' except for the CLP bit which is '1'). By default, unassigned cells are transmitted is case there is no data to send.")
e3FramingTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1), )
if mibBuilder.loadTexts: e3FramingTable.setStatus('current')
if mibBuilder.loadTexts: e3FramingTable.setDescription('A table of E3 framing statistics information.')
e3FramingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1), ).setIndexNames((0, "Fore-E3-MIB", "e3FramingBoard"), (0, "Fore-E3-MIB", "e3FramingModule"), (0, "Fore-E3-MIB", "e3FramingPort"))
if mibBuilder.loadTexts: e3FramingEntry.setStatus('current')
if mibBuilder.loadTexts: e3FramingEntry.setDescription('A table entry containing E3 framing statistics information.')
e3FramingBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingBoard.setStatus('current')
if mibBuilder.loadTexts: e3FramingBoard.setDescription("The index of this port's switch board.")
e3FramingModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingModule.setStatus('current')
if mibBuilder.loadTexts: e3FramingModule.setDescription('The network module of this port.')
e3FramingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingPort.setStatus('current')
if mibBuilder.loadTexts: e3FramingPort.setDescription('The number of this port.')
e3FramingLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingLOSs.setStatus('current')
if mibBuilder.loadTexts: e3FramingLOSs.setDescription('The number of seconds in which Loss Of Signal (LOS) errors were detected by the E3 Receive Framer block.')
e3FramingLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingLCVs.setStatus('current')
if mibBuilder.loadTexts: e3FramingLCVs.setDescription('The number of Line Code Violations (LCV) that were detected by the E3 Receive Framer block.')
e3FramingFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingFERRs.setStatus('current')
if mibBuilder.loadTexts: e3FramingFERRs.setDescription('Number of E3 framing error (FERR) events.')
e3FramingOOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingOOFs.setStatus('current')
if mibBuilder.loadTexts: e3FramingOOFs.setDescription('Number of seconds when E3 Out Of Frame (OOF) error events.')
e3FramingFERFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingFERFs.setStatus('current')
if mibBuilder.loadTexts: e3FramingFERFs.setDescription('In a G.832 (e3LineType == e3Framed) configured port, this variable relects the number of seconds when Far End Receive Failures were experienced. In G.751 (e3LineType == e3Plcp) it is the number of Remote Alarm Indications.')
e3FramingAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingAISs.setStatus('current')
if mibBuilder.loadTexts: e3FramingAISs.setDescription('The number of seconds in which Alarm Indication Signals (AIS) were detected by the E3 Receive Framer block. AIS indicates that an upstream failure has been detected by the far end.')
e3FramingBIP8s = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingBIP8s.setStatus('current')
if mibBuilder.loadTexts: e3FramingBIP8s.setDescription('The number of E3 G.832 BIP-8 errors. This counter is only valid in G.832.')
e3FramingFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3FramingFEBEs.setStatus('current')
if mibBuilder.loadTexts: e3FramingFEBEs.setDescription('Number of E3 far end block error (FEBE) events.')
e3PlcpTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2), )
if mibBuilder.loadTexts: e3PlcpTable.setStatus('current')
if mibBuilder.loadTexts: e3PlcpTable.setDescription('A table of E3 Physical Layer Convergence Protocol (PLCP) statistics information. These statistics are only valid when the G.751 (PLCP) based framing is being used by the E3. They are not meaningful when G.832 HCS-based framing is being used. Check e3LineType for the current framing option.')
e3PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1), ).setIndexNames((0, "Fore-E3-MIB", "e3PlcpBoard"), (0, "Fore-E3-MIB", "e3PlcpModule"), (0, "Fore-E3-MIB", "e3PlcpPort"))
if mibBuilder.loadTexts: e3PlcpEntry.setStatus('current')
if mibBuilder.loadTexts: e3PlcpEntry.setDescription('A table entry containing E3 PLCP statistics information.')
e3PlcpBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpBoard.setStatus('current')
if mibBuilder.loadTexts: e3PlcpBoard.setDescription("The index of this port's switch board.")
e3PlcpModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpModule.setStatus('current')
if mibBuilder.loadTexts: e3PlcpModule.setDescription('The network module of this port.')
e3PlcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpPort.setStatus('current')
if mibBuilder.loadTexts: e3PlcpPort.setDescription('The number of this port.')
e3PlcpFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpFERRs.setStatus('current')
if mibBuilder.loadTexts: e3PlcpFERRs.setDescription('Number of Physical Layer Convergence Protocol (PLCP) octet error events.')
e3PlcpLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpLOFs.setStatus('current')
if mibBuilder.loadTexts: e3PlcpLOFs.setDescription('The number of seconds in which Loss Of Frame (LOF) errors were detected by the PLCP (Physical Layer Convergence Protocol) receiver. LOF is declared when an Out-Of-Frame state persists for more than 1ms. LOF is removed when in-frame state persists for more than 12ms.')
e3PlcpBIP8s = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpBIP8s.setStatus('current')
if mibBuilder.loadTexts: e3PlcpBIP8s.setDescription('Number of BIP-8 (Bit Interleaved Parity - 8) error events. The BIP-8 is calculated over the Path Overhead field and the associated ATM cell of the previous frame. A BIP-N is a method of error monitoring. An N bit code is generated by the transmitting equipment in such a manner that the first bit of the code provides even parity over the first bit of all N-bit sequences in the previous VT SPE, the second bit provides even parity over the second bits of all N-bit sequences within the specified portion, etc.')
e3PlcpFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpFEBEs.setStatus('current')
if mibBuilder.loadTexts: e3PlcpFEBEs.setDescription('Number of ATM Far End Block Error (FEBE) events.')
e3PlcpYellows = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3PlcpYellows.setStatus('current')
if mibBuilder.loadTexts: e3PlcpYellows.setDescription('The number of seconds in which Yellow alarm errors were detected by the PLCP (Physical Layer Convergence Protocol) receiver. Yellow alarm is asserted when 10 consecutive yellow signal bits are set to logical 1. Yellow signals are used to alert upstream terminals of a downstream failure in order to initiate trunk conditioning on the failure circuit.')
e3AtmTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3), )
if mibBuilder.loadTexts: e3AtmTable.setStatus('current')
if mibBuilder.loadTexts: e3AtmTable.setDescription('A table of E3 ATM statistics information.')
e3AtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1), ).setIndexNames((0, "Fore-E3-MIB", "e3AtmBoard"), (0, "Fore-E3-MIB", "e3AtmModule"), (0, "Fore-E3-MIB", "e3AtmPort"))
if mibBuilder.loadTexts: e3AtmEntry.setStatus('current')
if mibBuilder.loadTexts: e3AtmEntry.setDescription('A table entry containing E3 ATM statistics information.')
e3AtmBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmBoard.setStatus('current')
if mibBuilder.loadTexts: e3AtmBoard.setDescription("The index of this port's switch board.")
e3AtmModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmModule.setStatus('current')
if mibBuilder.loadTexts: e3AtmModule.setDescription('The network module of this port.')
e3AtmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmPort.setStatus('current')
if mibBuilder.loadTexts: e3AtmPort.setDescription('The number of this port.')
e3AtmHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmHCSs.setStatus('current')
if mibBuilder.loadTexts: e3AtmHCSs.setDescription('Number of header check sequence (HCS) error events. The HCS is a CRC-8 calculation over the first 4 octets of the ATM cell header.')
e3AtmRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmRxCells.setStatus('current')
if mibBuilder.loadTexts: e3AtmRxCells.setDescription('Number of ATM cells that were received.')
e3AtmTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmTxCells.setStatus('current')
if mibBuilder.loadTexts: e3AtmTxCells.setDescription('Number of non-null ATM cells that were transmitted.')
e3AtmLCDs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 5, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e3AtmLCDs.setStatus('current')
if mibBuilder.loadTexts: e3AtmLCDs.setDescription('The number of seconds in which Loss of Cell Delineation (LCD) has occurred. An LCD defect is detected when an out of cell delination state has persisted for 4ms. An LCD defect is cleared when the sync state has been maintained for 4ms.')
mibBuilder.exportSymbols("Fore-E3-MIB", e3AtmBoard=e3AtmBoard, e3ConfEntry=e3ConfEntry, e3SendCode=e3SendCode, e3StatsGroup=e3StatsGroup, e3FramingFERRs=e3FramingFERRs, e3FramingTable=e3FramingTable, e3FramingFEBEs=e3FramingFEBEs, e3AtmEntry=e3AtmEntry, e3FramingBIP8s=e3FramingBIP8s, e3TxClockSource=e3TxClockSource, e3FramingModule=e3FramingModule, foreE3=foreE3, e3LineCoding=e3LineCoding, e3AtmLCDs=e3AtmLCDs, PYSNMP_MODULE_ID=foreE3, e3AtmTxCells=e3AtmTxCells, e3AtmRxCells=e3AtmRxCells, e3TxScrambling=e3TxScrambling, e3FramingOOFs=e3FramingOOFs, e3ConfGroup=e3ConfGroup, e3FramingEntry=e3FramingEntry, e3LoopbackConfig=e3LoopbackConfig, e3AtmTable=e3AtmTable, e3ConfBoard=e3ConfBoard, e3LineStatus=e3LineStatus, e3LineType=e3LineType, e3PlcpModule=e3PlcpModule, e3PlcpBIP8s=e3PlcpBIP8s, e3ConfPort=e3ConfPort, e3FramingBoard=e3FramingBoard, e3FramingLCVs=e3FramingLCVs, e3ConfTable=e3ConfTable, e3ReceiveCode=e3ReceiveCode, e3FramingAISs=e3FramingAISs, e3PlcpEntry=e3PlcpEntry, e3FramingPort=e3FramingPort, e3PlcpBoard=e3PlcpBoard, e3AtmHCSs=e3AtmHCSs, e3AtmModule=e3AtmModule, e3AtmPort=e3AtmPort, e3ConfModule=e3ConfModule, e3PlcpFERRs=e3PlcpFERRs, e3PlcpFEBEs=e3PlcpFEBEs, e3PlcpYellows=e3PlcpYellows, e3FramingFERFs=e3FramingFERFs, e3RxScrambling=e3RxScrambling, e3PlcpTable=e3PlcpTable, e3PlcpPort=e3PlcpPort, e3PlcpLOFs=e3PlcpLOFs, e3IdleUnassignedCells=e3IdleUnassignedCells, e3FramingLOSs=e3FramingLOSs)
