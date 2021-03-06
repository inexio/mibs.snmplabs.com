#
# PySNMP MIB module Fore-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, iso, ObjectIdentity, Counter32, Integer32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "iso", "ObjectIdentity", "Counter32", "Integer32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
foreDs1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7))
if mibBuilder.loadTexts: foreDs1.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreDs1.setOrganization('FORE')
ds1ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1))
ds1StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2))
ds1ConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1), )
if mibBuilder.loadTexts: ds1ConfTable.setStatus('current')
ds1ConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1), ).setIndexNames((0, "Fore-DS1-MIB", "ds1ConfBoard"), (0, "Fore-DS1-MIB", "ds1ConfModule"), (0, "Fore-DS1-MIB", "ds1ConfPort"))
if mibBuilder.loadTexts: ds1ConfEntry.setStatus('current')
ds1ConfBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1ConfBoard.setStatus('current')
ds1ConfModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1ConfModule.setStatus('current')
ds1ConfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1ConfPort.setStatus('current')
ds1LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ds1Other", 1), ("ds1ESF", 2), ("ds1D4", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1LineType.setStatus('current')
ds1LineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds1Other", 1), ("ds1JBZS", 2), ("ds1B8ZS", 3), ("ds1HDB3", 4), ("ds1ZBTSI", 5), ("ds1AMI", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1LineCoding.setStatus('current')
ds1SendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ds1SendNoCode", 1), ("ds1SendLineCode", 2), ("ds1SendPayloadCode", 3), ("ds1SendResetCode", 4), ("ds1SendQRS", 5), ("ds1Send511Pattern", 6), ("ds1Send3in24Pattern", 7), ("ds1SendOtherTestPattern", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1SendCode.setStatus('current')
ds1ReceiveCode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ds1ReceiveNoCode", 1), ("ds1ReceiveLineCode", 2), ("ds1ReceivePayloadCode", 3), ("ds1ReceiveResetCode", 4), ("ds1SendQRS", 5), ("ds1Send511Pattern", 6), ("ds1Send3in24Pattern", 7), ("ds1SendOtherTestPattern", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1ReceiveCode.setStatus('current')
ds1LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ds1NoLoop", 1), ("ds1LineLoop", 2), ("ds1PayloadLoop", 3), ("ds1DiagLoop", 4), ("ds1OtherLoop", 5))).clone('ds1NoLoop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1LoopbackConfig.setStatus('current')
ds1TxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rxTiming", 1), ("localTiming", 2))).clone('localTiming')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1TxClockSource.setStatus('current')
ds1LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1LineStatus.setStatus('current')
ds1IdleUnassignedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1IdleUnassignedCells.setStatus('current')
ds1LineTypeFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ds1Hcs", 2), ("ds1Plcp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1LineTypeFraming.setStatus('current')
ds1LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("ds1LineLt110", 1), ("ds1Line110-220", 2), ("ds1Line220-330", 3), ("ds1Line330-440", 4), ("ds1Line440-550", 5), ("ds1Line550-660", 6), ("ds1LineGt655", 7), ("ds1LineLt110Alt", 9), ("ds1Line110-220Alt", 10), ("ds1Line220-330Alt", 11), ("ds1Line330-440Alt", 12), ("ds1Line440-550Alt", 13), ("ds1Line550-660Alt", 14), ("ds1LineGt655Alt", 15))).clone('ds1LineLt110')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1LineLength.setStatus('current')
ds1RxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("descrambling", 1), ("noDescrambling", 2))).clone('noDescrambling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1RxScrambling.setStatus('current')
ds1TxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scrambling", 1), ("noScrambling", 2))).clone('noScrambling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1TxScrambling.setStatus('current')
ds1TxPRBS = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("invert", 3))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1TxPRBS.setStatus('current')
ds1CRCErrThrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 19), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1CRCErrThrSeconds.setStatus('current')
ds1CRCErrThrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1CRCErrThrErrors.setStatus('current')
ds1CRCErrFailEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1CRCErrFailEnable.setStatus('current')
ds1SigFailBer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1SigFailBer.setStatus('current')
ds1SigDegradeBer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1SigDegradeBer.setStatus('current')
ds1BerErrorModel = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("errorModelNone", 0), ("errorModelRandom", 1), ("errorModelBurst", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1BerErrorModel.setStatus('current')
ds1BerState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("berStateOk", 0), ("berStateSigDegrade", 1), ("berStateSigFail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1BerState.setStatus('current')
ds1FramingTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1), )
if mibBuilder.loadTexts: ds1FramingTable.setStatus('current')
ds1FramingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1), ).setIndexNames((0, "Fore-DS1-MIB", "ds1FramingBoard"), (0, "Fore-DS1-MIB", "ds1FramingModule"), (0, "Fore-DS1-MIB", "ds1FramingPort"))
if mibBuilder.loadTexts: ds1FramingEntry.setStatus('current')
ds1FramingBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingBoard.setStatus('current')
ds1FramingModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingModule.setStatus('current')
ds1FramingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingPort.setStatus('current')
ds1FramingLOSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingLOSs.setStatus('current')
ds1FramingLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingLCVs.setStatus('current')
ds1FramingFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingFERRs.setStatus('current')
ds1FramingOOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingOOFs.setStatus('current')
ds1FramingAISs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingAISs.setStatus('current')
ds1FramingB8ZSPatterns = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingB8ZSPatterns.setStatus('deprecated')
ds1Framing8Zeros = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1Framing8Zeros.setStatus('deprecated')
ds1Framing16Zeros = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1Framing16Zeros.setStatus('deprecated')
ds1FramingYellowAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingYellowAlarms.setStatus('current')
ds1FramingRedAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingRedAlarms.setStatus('current')
ds1FramingBEEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingBEEs.setStatus('current')
ds1FramingPRBSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingPRBSs.setStatus('current')
ds1FramingBERs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1FramingBERs.setStatus('current')
ds1PlcpTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2), )
if mibBuilder.loadTexts: ds1PlcpTable.setStatus('current')
ds1PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1), ).setIndexNames((0, "Fore-DS1-MIB", "ds1PlcpBoard"), (0, "Fore-DS1-MIB", "ds1PlcpModule"), (0, "Fore-DS1-MIB", "ds1PlcpPort"))
if mibBuilder.loadTexts: ds1PlcpEntry.setStatus('current')
ds1PlcpBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpBoard.setStatus('current')
ds1PlcpModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpModule.setStatus('current')
ds1PlcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpPort.setStatus('current')
ds1PlcpBIP8s = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpBIP8s.setStatus('current')
ds1PlcpFERRs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpFERRs.setStatus('current')
ds1PlcpFEBEs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpFEBEs.setStatus('current')
ds1PlcpLOFs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpLOFs.setStatus('current')
ds1PlcpYellows = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1PlcpYellows.setStatus('current')
ds1AtmTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3), )
if mibBuilder.loadTexts: ds1AtmTable.setStatus('current')
ds1AtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1), ).setIndexNames((0, "Fore-DS1-MIB", "ds1AtmBoard"), (0, "Fore-DS1-MIB", "ds1AtmModule"), (0, "Fore-DS1-MIB", "ds1AtmPort"))
if mibBuilder.loadTexts: ds1AtmEntry.setStatus('current')
ds1AtmBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmBoard.setStatus('current')
ds1AtmModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmModule.setStatus('current')
ds1AtmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmPort.setStatus('current')
ds1AtmHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmHCSs.setStatus('current')
ds1AtmRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmRxCells.setStatus('current')
ds1AtmTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmTxCells.setStatus('current')
ds1AtmUHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmUHCSs.setStatus('current')
ds1AtmCHCSs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmCHCSs.setStatus('current')
ds1AtmLCDs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 7, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1AtmLCDs.setStatus('current')
mibBuilder.exportSymbols("Fore-DS1-MIB", ds1ReceiveCode=ds1ReceiveCode, ds1TxScrambling=ds1TxScrambling, ds1FramingBEEs=ds1FramingBEEs, ds1CRCErrFailEnable=ds1CRCErrFailEnable, ds1AtmPort=ds1AtmPort, ds1AtmCHCSs=ds1AtmCHCSs, ds1ConfBoard=ds1ConfBoard, ds1FramingModule=ds1FramingModule, ds1FramingLOSs=ds1FramingLOSs, ds1PlcpFERRs=ds1PlcpFERRs, ds1ConfGroup=ds1ConfGroup, ds1SendCode=ds1SendCode, ds1LoopbackConfig=ds1LoopbackConfig, ds1FramingPRBSs=ds1FramingPRBSs, ds1CRCErrThrErrors=ds1CRCErrThrErrors, ds1FramingBERs=ds1FramingBERs, ds1PlcpYellows=ds1PlcpYellows, ds1StatsGroup=ds1StatsGroup, ds1RxScrambling=ds1RxScrambling, ds1ConfEntry=ds1ConfEntry, ds1SigFailBer=ds1SigFailBer, ds1FramingTable=ds1FramingTable, ds1FramingEntry=ds1FramingEntry, ds1FramingBoard=ds1FramingBoard, ds1PlcpPort=ds1PlcpPort, ds1AtmModule=ds1AtmModule, ds1FramingPort=ds1FramingPort, ds1AtmEntry=ds1AtmEntry, ds1AtmBoard=ds1AtmBoard, ds1AtmRxCells=ds1AtmRxCells, ds1FramingOOFs=ds1FramingOOFs, ds1TxClockSource=ds1TxClockSource, ds1PlcpModule=ds1PlcpModule, ds1TxPRBS=ds1TxPRBS, ds1AtmLCDs=ds1AtmLCDs, ds1LineType=ds1LineType, ds1ConfPort=ds1ConfPort, ds1SigDegradeBer=ds1SigDegradeBer, ds1FramingAISs=ds1FramingAISs, ds1IdleUnassignedCells=ds1IdleUnassignedCells, ds1CRCErrThrSeconds=ds1CRCErrThrSeconds, ds1LineTypeFraming=ds1LineTypeFraming, ds1PlcpBoard=ds1PlcpBoard, ds1BerState=ds1BerState, ds1PlcpLOFs=ds1PlcpLOFs, ds1AtmHCSs=ds1AtmHCSs, ds1ConfTable=ds1ConfTable, ds1BerErrorModel=ds1BerErrorModel, ds1PlcpEntry=ds1PlcpEntry, ds1ConfModule=ds1ConfModule, foreDs1=foreDs1, ds1FramingFERRs=ds1FramingFERRs, ds1FramingB8ZSPatterns=ds1FramingB8ZSPatterns, ds1LineCoding=ds1LineCoding, ds1PlcpBIP8s=ds1PlcpBIP8s, ds1AtmTable=ds1AtmTable, ds1AtmTxCells=ds1AtmTxCells, ds1Framing8Zeros=ds1Framing8Zeros, ds1Framing16Zeros=ds1Framing16Zeros, ds1FramingRedAlarms=ds1FramingRedAlarms, ds1AtmUHCSs=ds1AtmUHCSs, ds1LineLength=ds1LineLength, ds1PlcpTable=ds1PlcpTable, ds1FramingLCVs=ds1FramingLCVs, ds1FramingYellowAlarms=ds1FramingYellowAlarms, ds1PlcpFEBEs=ds1PlcpFEBEs, ds1LineStatus=ds1LineStatus, PYSNMP_MODULE_ID=foreDs1)
