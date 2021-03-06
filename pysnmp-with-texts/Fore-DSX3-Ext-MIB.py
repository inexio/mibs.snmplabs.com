#
# PySNMP MIB module Fore-DSX3-Ext-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-DSX3-Ext-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dsx3LineIndex, = mibBuilder.importSymbols("DS3-MIB", "dsx3LineIndex")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
trapLogIndex, = mibBuilder.importSymbols("Fore-TrapLog-MIB", "trapLogIndex")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Counter64, Bits, ObjectIdentity, Unsigned32, iso, Integer32, Counter32, ModuleIdentity, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Counter64", "Bits", "ObjectIdentity", "Unsigned32", "iso", "Integer32", "Counter32", "ModuleIdentity", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
foreDsx3Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15))
if mibBuilder.loadTexts: foreDsx3Mib.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreDsx3Mib.setOrganization('FORE')
if mibBuilder.loadTexts: foreDsx3Mib.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreDsx3Mib.setDescription('This mib module implements extensions to the standard DS3 mib to support extra configuration, statistics, and diagnostic capabilities of Fore Systems equipment.')
foreDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1), )
if mibBuilder.loadTexts: foreDsx3ConfigTable.setStatus('current')
if mibBuilder.loadTexts: foreDsx3ConfigTable.setDescription('A table of configuration options, statistics, and diagnostics supported by DS3 interfaces on Fore Systems ATM Switches.')
foreDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1), ).setIndexNames((0, "DS3-MIB", "dsx3LineIndex"))
if mibBuilder.loadTexts: foreDsx3ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: foreDsx3ConfigEntry.setDescription('A table entry containing Fore specific extensions to the standard DS3 MIB tables.')
foreDsx3ConfigReceiveCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds3ReceiveNoCode", 1), ("ds3ReceiveLineCode", 2), ("ds3ReceivePayloadCode", 3), ("ds3ReceiveResetCode", 4), ("ds3ReceiveDS1LoopCode", 5), ("ds3ReceiveTestPattern", 6))).clone('ds3ReceiveNoCode')).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3ConfigReceiveCode.setStatus('current')
if mibBuilder.loadTexts: foreDsx3ConfigReceiveCode.setDescription('This variable indicates the type of code that was received across the DS3/E3 interface. The values mean: ds3ReceiveNoCode receiving looped or normal data ds3ReceiveLineCode receiving request for a line loopback ds3ReceivePayloadCode receiving a request for a payload loopback (i.e. all DS1/E1 in a DS3/E3 frame) ds3ReceiveResetCode receiving a loopback deactivation request ds3ReceiveDS1LoopCode receiving a request to loopback a particular DS1/E1 within a DS3/E3 frame ds3ReceiveTestPattern receiving a test pattern.')
foreDsx3ConfigLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ds3LineLt225", 1), ("ds3LineGt225", 2))).clone('ds3LineGt225')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3ConfigLineLength.setStatus('current')
if mibBuilder.loadTexts: foreDsx3ConfigLineLength.setDescription('This variable represents the length of the physical cable connected to the ds3 port. The user has to set this object to match the physical cable in order to get the netmod to receive the signal on the cable. The different values are: ds3LineLt225 (1) means the line is shorter than 225 ft, ds1LineGt225 (2) means the line length is greater than 220 ft. This value is not settable for Series A netmods and the value for these netmods is Gt225')
foreDsx3ConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 3), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3ConfigStatus.setStatus('current')
if mibBuilder.loadTexts: foreDsx3ConfigStatus.setDescription('This variable represents the current status of the Dsx3 interface. This variable is a bit map represented as a sum. The various bit positions are: 1 dsx3NoDefect True if no other defects are present 2 dsx3RxFERF Receiving a Far End Receive Failure 4 dsx3TxFERF Sending a Far End Receive Failure 8 dsx3RxAIS Receiving Alarm Indication 16 dsx3TxAIS Transmitting Alarm Indication 32 dsx3LOF Loss Of Frame 64 dsx3LOS Loss Of Signal 128 dsx3Loopback Remotly Initiatiated Loopback Operational 256 dsx3RxTest Receiving Test Pattern 512 dsx3Other Other, non specific falure.')
foreDsx3LineTypeFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("e3G751", 1), ("e3G832", 2))).clone('e3G832')).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3LineTypeFraming.setStatus('current')
if mibBuilder.loadTexts: foreDsx3LineTypeFraming.setDescription("This variable extends the 'dsx3LineType' variable from rfc1407. When dsx3LineType == e3Framed, this variable determines whether G.751 or G.832 framing is used. When dsx3LineType == e3Plcp, the value of this variable will be 1, indicating G.751 framing.")
foreDsx3PbitPerrThrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 5), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3PbitPerrThrSeconds.setStatus('current')
if mibBuilder.loadTexts: foreDsx3PbitPerrThrSeconds.setDescription('This variable represents the consecutive number of BAD/GOOD seconds to detect/clear an Excessive P-bit Parity Error Defect. The range of values it can take is between 2 and 10 inclusive.')
foreDsx3PbitPerrThrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3PbitPerrThrErrors.setStatus('current')
if mibBuilder.loadTexts: foreDsx3PbitPerrThrErrors.setDescription('This variable is a threshold for the number of P-bit Parity Errors per second and is used as a parameter to the Excessive P-bit Parity Error Defect. If the number of errors exceeds the threshold, the particular second is declared BAD, otherwise it is declared GOOD.')
foreDsx3PbitPerrFailEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3PbitPerrFailEnable.setStatus('current')
if mibBuilder.loadTexts: foreDsx3PbitPerrFailEnable.setDescription("This variable controls whether declaration of an Excessive P-bit Parity Error Defect forces the port's operState to Down.")
foreDsx3SignalDegradeBer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3SignalDegradeBer.setStatus('current')
if mibBuilder.loadTexts: foreDsx3SignalDegradeBer.setDescription('This is the exponent of 10 for the current signal degrade bit error rate (BER) threshold for this port. The value -7, for example, represents a BER of 1E-7. This variable is only applicable when dsx3BerErrorModel is set to errorModelRandom.')
foreDsx3SignalFailBer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3SignalFailBer.setStatus('current')
if mibBuilder.loadTexts: foreDsx3SignalFailBer.setDescription('This is the exponent of 10 for the current signal fail bit error rate (BER) threshold for this port. The value -4, for example, represents a BER of 1E-4. This variable is only applicable when dsx3BerErrorModel is set to errorModelRandom.')
foreDsx3BerErrorModel = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("errorModelNone", 0), ("errorModelRandom", 1), ("errorModelBurst", 2))).clone('errorModelRandom')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreDsx3BerErrorModel.setStatus('current')
if mibBuilder.loadTexts: foreDsx3BerErrorModel.setDescription('This is the error distribution model to be used to identify signal degrade and signal fail conditions. errorModelRandom selects a random error distribution and declares signal conditions based on the thresholds set in dsx3SignalDegradeBer and dsx3SignalFailBer. errorModelBurst selects a burst error model and declares signal degrade conditions based on the thresholds set in dsx3BipThrSeconds and dsx3BipThrErrors. errorModelNone disables detection of signal conditions.')
foreDsx3BerState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("berStateOk", 0), ("berStateSigDegrade", 1), ("berStateSigFail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3BerState.setStatus('current')
if mibBuilder.loadTexts: foreDsx3BerState.setDescription('This value describes the current state of the port as determined through bit error rate analysis.')
foreDsx3TotalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2), )
if mibBuilder.loadTexts: foreDsx3TotalTable.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalTable.setDescription('A table of statistics, supported by DS3 interfaces on Fore Systems Equipment.')
foreDsx3TotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1), ).setIndexNames((0, "DS3-MIB", "dsx3LineIndex"))
if mibBuilder.loadTexts: foreDsx3TotalEntry.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalEntry.setDescription('A table entry containing Fore specific extensions to the standard DS3 MIB tables.')
foreDsx3TotalFramingLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingLOSs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingLOSs.setDescription('The number of seconds in which Loss Of Signal (LOS) errors were detected by the DS3 Receive Framer block.')
foreDsx3TotalFramingLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingLCVs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingLCVs.setDescription('The number of Line Code Violations (LCV) that were detected by the DS3 Receive Framer block.')
foreDsx3TotalFramingSumLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingSumLCVs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingSumLCVs.setDescription('The number of DS3 information blocks (85 bits) which contain one or more Line Code Violations (LCV).')
foreDsx3TotalFramingFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingFERRs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingFERRs.setDescription('Number of DS3 framing error (FERR) events.')
foreDsx3TotalFramingOOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingOOFs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingOOFs.setDescription('Number of seconds DS3 Out Of Frame (OOF) error events were experienced.')
foreDsx3TotalFramingFERFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingFERFs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingFERFs.setDescription('The number of seconds in which Far End Receive Failure (FERF) state has been detected by the DS3 Receive Framer block. FERF signal alerts the upstream terminal that a failure has been detected along the downstream line.')
foreDsx3TotalFramingAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingAISs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingAISs.setDescription('The number of seconds in which Alarm Indication Signals (AIS) were detected by the DS3 Receive Framer block. AIS indicates that an upstream failure has been detected by the far end.')
foreDsx3TotalFramingPbitPERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingPbitPERRs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingPbitPERRs.setDescription('Number of P-bit parity error (PERR) events or the number of BIP-8 errors in case of E3 G.832.')
foreDsx3TotalFramingCbitPERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingCbitPERRs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingCbitPERRs.setDescription('Number of C-bit parity error (PERR) events.')
foreDsx3TotalFramingFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingFEBEs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingFEBEs.setDescription('Number of DS3 far end block error (FEBE) events.')
foreDsx3TotalFramingIDLEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreDsx3TotalFramingIDLEs.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TotalFramingIDLEs.setDescription('The number of seconds in which IDLE signal was detected by the DS3 Receive Framer block.')
foreDsx3LOFDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 1)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3LOFDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3LOFDetected.setDescription('This trap indicates that Loss Of Frame(LOF) is detected on the incoming signal.')
foreDsx3LOFCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 2)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3LOFCleared.setStatus('current')
if mibBuilder.loadTexts: foreDsx3LOFCleared.setDescription('This trap indicates that Loss Of Frame is cleared on the incoming signal.')
foreDsx3AISDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 3)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3AISDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3AISDetected.setDescription('This trap indicates that AIS Alarm is detected on the incoming signal.')
foreDsx3AISCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 4)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3AISCleared.setStatus('current')
if mibBuilder.loadTexts: foreDsx3AISCleared.setDescription('This trap indicates that AIS Alarm is cleared on the incoming signal.')
foreDsx3FERFDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 5)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3FERFDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3FERFDetected.setDescription('This trap indicates that FERF Alarm or DS3 Yellow Alarm is detected on the incoming signal.')
foreDsx3FERFCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 6)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3FERFCleared.setStatus('current')
if mibBuilder.loadTexts: foreDsx3FERFCleared.setDescription('This trap indicates that FERF Alarm or DS3 Yellow Alarm is cleared on the incoming signal.')
foreDsx3LOSDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 7)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3LOSDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3LOSDetected.setDescription('This trap indicates that the specified DS3 port has detected incoming LOS Alarm.')
foreDsx3LOSCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 8)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3LOSCleared.setStatus('current')
if mibBuilder.loadTexts: foreDsx3LOSCleared.setDescription('This trap indicates that the incoming LOS Alarm has been cleared on the specified DS3 port.')
foreDsx3IdleDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 9)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3IdleDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3IdleDetected.setDescription('This trap indicates that an Idle Maintenance Signal (IDLE) is detected on the incoming signal.')
foreDsx3IdleCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 10)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3IdleCleared.setStatus('current')
if mibBuilder.loadTexts: foreDsx3IdleCleared.setDescription('This trap indicates that an Idle Maintenance Signal (IDLE) is cleared on the incoming signal.')
foreDsx3TrailChangeDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 11)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3TrailChangeDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3TrailChangeDetected.setDescription('This trap indicates that a Trail Trace Mismatch was detected on the incoming signal.')
foreDsx3PbitPerrDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 12)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3PbitPerrDetected.setStatus('current')
if mibBuilder.loadTexts: foreDsx3PbitPerrDetected.setDescription('This trap indicates that the specified DSX3 port is experiencing P-bit Parity errors. A P-bit Parity Error failure is declared when the P-bit Parity Error persists for a period of 2.5 +/- 0.5 seconds.')
foreDsx3PbitPerrCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 15, 0, 13)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreDsx3PbitPerrCleared.setStatus('current')
if mibBuilder.loadTexts: foreDsx3PbitPerrCleared.setDescription('This trap indicates that the P-bit Parity Error failure identified by trap asxDS3PbitPerrDetected has been cleared. A P-bit Parity Error failure is cleared when the P-bit Parity Error defect is absent for 10 +/- 0.5 seconds.')
mibBuilder.exportSymbols("Fore-DSX3-Ext-MIB", foreDsx3PbitPerrCleared=foreDsx3PbitPerrCleared, foreDsx3AISDetected=foreDsx3AISDetected, foreDsx3LOFCleared=foreDsx3LOFCleared, foreDsx3FERFDetected=foreDsx3FERFDetected, foreDsx3ConfigTable=foreDsx3ConfigTable, foreDsx3BerErrorModel=foreDsx3BerErrorModel, foreDsx3TotalFramingPbitPERRs=foreDsx3TotalFramingPbitPERRs, foreDsx3TotalFramingAISs=foreDsx3TotalFramingAISs, PYSNMP_MODULE_ID=foreDsx3Mib, foreDsx3TrailChangeDetected=foreDsx3TrailChangeDetected, foreDsx3LineTypeFraming=foreDsx3LineTypeFraming, foreDsx3PbitPerrThrSeconds=foreDsx3PbitPerrThrSeconds, foreDsx3TotalFramingSumLCVs=foreDsx3TotalFramingSumLCVs, foreDsx3ConfigReceiveCode=foreDsx3ConfigReceiveCode, foreDsx3TotalFramingOOFs=foreDsx3TotalFramingOOFs, foreDsx3TotalTable=foreDsx3TotalTable, foreDsx3TotalFramingLOSs=foreDsx3TotalFramingLOSs, foreDsx3FERFCleared=foreDsx3FERFCleared, foreDsx3PbitPerrThrErrors=foreDsx3PbitPerrThrErrors, foreDsx3LOFDetected=foreDsx3LOFDetected, foreDsx3TotalEntry=foreDsx3TotalEntry, foreDsx3PbitPerrFailEnable=foreDsx3PbitPerrFailEnable, foreDsx3ConfigEntry=foreDsx3ConfigEntry, foreDsx3BerState=foreDsx3BerState, foreDsx3TotalFramingIDLEs=foreDsx3TotalFramingIDLEs, foreDsx3PbitPerrDetected=foreDsx3PbitPerrDetected, foreDsx3ConfigLineLength=foreDsx3ConfigLineLength, foreDsx3TotalFramingFERRs=foreDsx3TotalFramingFERRs, foreDsx3TotalFramingLCVs=foreDsx3TotalFramingLCVs, foreDsx3IdleCleared=foreDsx3IdleCleared, foreDsx3Mib=foreDsx3Mib, foreDsx3LOSDetected=foreDsx3LOSDetected, foreDsx3TotalFramingCbitPERRs=foreDsx3TotalFramingCbitPERRs, foreDsx3TotalFramingFEBEs=foreDsx3TotalFramingFEBEs, foreDsx3SignalDegradeBer=foreDsx3SignalDegradeBer, foreDsx3ConfigStatus=foreDsx3ConfigStatus, foreDsx3AISCleared=foreDsx3AISCleared, foreDsx3LOSCleared=foreDsx3LOSCleared, foreDsx3SignalFailBer=foreDsx3SignalFailBer, foreDsx3TotalFramingFERFs=foreDsx3TotalFramingFERFs, foreDsx3IdleDetected=foreDsx3IdleDetected)
