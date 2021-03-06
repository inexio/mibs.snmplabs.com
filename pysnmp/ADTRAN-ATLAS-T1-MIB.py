#
# PySNMP MIB module ADTRAN-ATLAS-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-T1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adATLASModuleInfoFPStatus, = mibBuilder.importSymbols("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus")
adATLASUnitSlotAddress, adATLASUnitFPStatus, adATLASUnitPortAddress = mibBuilder.importSymbols("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress", "adATLASUnitFPStatus", "adATLASUnitPortAddress")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
dsx1LineStatus, = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ModuleIdentity, TimeTicks, Gauge32, MibIdentifier, Integer32, Counter32, Bits, ObjectIdentity, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154))
adGenATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1))
adATLAST1mg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9))
adATLAST1IfNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfNumber.setStatus('mandatory')
adATLAST1IfTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2), )
if mibBuilder.loadTexts: adATLAST1IfTable.setStatus('mandatory')
adATLAST1IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1), ).setIndexNames((0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfIndex"))
if mibBuilder.loadTexts: adATLAST1IfEntry.setStatus('mandatory')
adATLAST1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfIndex.setStatus('mandatory')
adATLAST1IfSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfSlotNum.setStatus('mandatory')
adATLAST1IfPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfPortNum.setStatus('mandatory')
adATLAST1IfAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfAlarmStatus.setStatus('mandatory')
adATLAST1IfRxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("zerodb", 1), ("neg7pt5db", 2), ("neg15db", 3), ("neg22pt5db", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfRxLevel.setStatus('mandatory')
adATLAST1IfCurrentLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfCurrentLOFC.setStatus('mandatory')
adATLAST1IfTotalLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfTotalLOFC.setStatus('mandatory')
adATLAST1IfResetPRMStats = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAST1IfResetPRMStats.setStatus('mandatory')
adATLAST1IfIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3), )
if mibBuilder.loadTexts: adATLAST1IfIntervalTable.setStatus('mandatory')
adATLAST1IfIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1), ).setIndexNames((0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfIntervalIndex"), (0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfIntervalNumber"))
if mibBuilder.loadTexts: adATLAST1IfIntervalEntry.setStatus('mandatory')
adATLAST1IfIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfIntervalIndex.setStatus('mandatory')
adATLAST1IfIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfIntervalNumber.setStatus('mandatory')
adATLAST1IfIntervalLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfIntervalLOFC.setStatus('mandatory')
adATLAST1IfDS0Table = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4), )
if mibBuilder.loadTexts: adATLAST1IfDS0Table.setStatus('mandatory')
adATLAST1IfDS0Entry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1), ).setIndexNames((0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfDS0Index"))
if mibBuilder.loadTexts: adATLAST1IfDS0Entry.setStatus('mandatory')
adATLAST1IfDS0Index = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0Index.setStatus('mandatory')
adATLAST1IfDS0Status = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0Status.setStatus('mandatory')
adATLAST1IfDS0Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0Alarm.setStatus('mandatory')
adATLAST1IfDS0RxSignalStatusA = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0RxSignalStatusA.setStatus('mandatory')
adATLAST1IfDS0RxSignalStatusB = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0RxSignalStatusB.setStatus('mandatory')
adATLAST1IfDS0TxSignalStatusA = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0TxSignalStatusA.setStatus('mandatory')
adATLAST1IfDS0TxSignalStatusB = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1IfDS0TxSignalStatusB.setStatus('mandatory')
adATLAST1TstTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5), )
if mibBuilder.loadTexts: adATLAST1TstTable.setStatus('mandatory')
adATLAST1TstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1), ).setIndexNames((0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1TstIndex"))
if mibBuilder.loadTexts: adATLAST1TstEntry.setStatus('mandatory')
adATLAST1TstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstIndex.setStatus('mandatory')
adATLAST1TstLocalLpBk = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("payload", 2), ("line", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAST1TstLocalLpBk.setStatus('mandatory')
adATLAST1TstRemoteLpBk = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("attInbandLine", 2), ("ansiFDLLine", 3), ("ansiFDLPayload", 4), ("inbandNIU", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAST1TstRemoteLpBk.setStatus('mandatory')
adATLAST1TstRemoteLpBkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noRemoteLoops", 1), ("remLpUpStarted", 2), ("remLpUpInProgress", 3), ("remLpUpTimeout", 4), ("remLpUpDone", 5), ("remLpDwnStarted", 6), ("remLpDwnInProgress", 7), ("remLpDwnDone", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstRemoteLpBkStatus.setStatus('mandatory')
adATLAST1TstPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("allOnes", 2), ("allZeros", 3), ("qRSS", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAST1TstPattern.setStatus('mandatory')
adATLAST1TstPatternSync = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("synced", 1), ("noSync", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstPatternSync.setStatus('mandatory')
adATLAST1TstPatternSyncLost = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("syncLost", 1), ("syncNotLost", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstPatternSyncLost.setStatus('mandatory')
adATLAST1TstPatternESs = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstPatternESs.setStatus('mandatory')
adATLAST1TstPatternBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstPatternBESs.setStatus('mandatory')
adATLAST1TstPatternSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAST1TstPatternSESs.setStatus('mandatory')
adATLAST1TstClearResults = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAST1TstClearResults.setStatus('mandatory')
adATLAST1TstInjectError = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("inject", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLAST1TstInjectError.setStatus('mandatory')
adATLAST1RxYellowActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400900)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1RxYellowInActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400901)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1RxAISActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400902)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1RxAISInActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400903)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1RedAlarmActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400904)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1RedAlarmInActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400905)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1LOSActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400906)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1LOSInActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400907)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TxAISActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400908)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TxAISInActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400909)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TxYellowActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400910)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TxYellowInActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400911)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentES = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400912)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentSES = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400913)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentSEFS = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400914)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentUAS = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400915)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentCSS = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400916)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentPCV = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400917)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentLES = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400918)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1CurrentLCV = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400919)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalES = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400920)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalSES = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400921)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalSEFS = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400922)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalUAS = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400923)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalCSS = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400924)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalPCV = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400925)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalLES = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400926)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
adATLAST1TotalLCV = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400927)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"), ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"), ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"), ("RFC1406-MIB", "dsx1LineStatus"))
mibBuilder.exportSymbols("ADTRAN-ATLAS-T1-MIB", adATLAST1IfNumber=adATLAST1IfNumber, adATLAST1mg=adATLAST1mg, adATLAST1RedAlarmActive=adATLAST1RedAlarmActive, adATLAST1TstIndex=adATLAST1TstIndex, adATLAST1TstInjectError=adATLAST1TstInjectError, adATLAST1IfCurrentLOFC=adATLAST1IfCurrentLOFC, adATLAST1TxAISActive=adATLAST1TxAISActive, adATLAST1CurrentUAS=adATLAST1CurrentUAS, adATLAST1TstRemoteLpBkStatus=adATLAST1TstRemoteLpBkStatus, adATLAST1TstPatternSync=adATLAST1TstPatternSync, adATLAST1TstTable=adATLAST1TstTable, adATLAST1TotalLCV=adATLAST1TotalLCV, adATLAST1TxAISInActive=adATLAST1TxAISInActive, adATLAST1LOSInActive=adATLAST1LOSInActive, adATLAST1TstClearResults=adATLAST1TstClearResults, adtran=adtran, adATLAST1IfRxLevel=adATLAST1IfRxLevel, adATLAST1IfDS0Index=adATLAST1IfDS0Index, adATLAST1IfDS0Alarm=adATLAST1IfDS0Alarm, adATLAST1IfDS0RxSignalStatusB=adATLAST1IfDS0RxSignalStatusB, adATLAST1CurrentCSS=adATLAST1CurrentCSS, adATLAST1TotalSES=adATLAST1TotalSES, adATLAST1TxYellowInActive=adATLAST1TxYellowInActive, adATLAST1IfIntervalEntry=adATLAST1IfIntervalEntry, adATLAST1IfDS0Entry=adATLAST1IfDS0Entry, adATLAST1IfDS0RxSignalStatusA=adATLAST1IfDS0RxSignalStatusA, adATLAST1TotalSEFS=adATLAST1TotalSEFS, adATLAST1RxYellowInActive=adATLAST1RxYellowInActive, adATLAST1IfIndex=adATLAST1IfIndex, adATLAST1CurrentLES=adATLAST1CurrentLES, adATLAST1TstPatternBESs=adATLAST1TstPatternBESs, adATLAST1TstLocalLpBk=adATLAST1TstLocalLpBk, adATLAST1IfIntervalTable=adATLAST1IfIntervalTable, adATLAST1TotalES=adATLAST1TotalES, adATLAST1TotalUAS=adATLAST1TotalUAS, adATLAST1IfIntervalIndex=adATLAST1IfIntervalIndex, adATLAST1IfDS0TxSignalStatusA=adATLAST1IfDS0TxSignalStatusA, adATLAST1IfTable=adATLAST1IfTable, adATLAST1IfResetPRMStats=adATLAST1IfResetPRMStats, adATLAST1IfDS0Table=adATLAST1IfDS0Table, adATLAST1IfDS0Status=adATLAST1IfDS0Status, adATLAST1TstRemoteLpBk=adATLAST1TstRemoteLpBk, adATLAST1RedAlarmInActive=adATLAST1RedAlarmInActive, adATLAST1CurrentPCV=adATLAST1CurrentPCV, adATLASmg=adATLASmg, adATLAST1IfSlotNum=adATLAST1IfSlotNum, adATLAST1RxAISActive=adATLAST1RxAISActive, adGenATLASmg=adGenATLASmg, adATLAST1IfPortNum=adATLAST1IfPortNum, adATLAST1IfIntervalLOFC=adATLAST1IfIntervalLOFC, adATLAST1TstPatternSyncLost=adATLAST1TstPatternSyncLost, adATLAST1CurrentES=adATLAST1CurrentES, adATLAST1CurrentLCV=adATLAST1CurrentLCV, adATLAST1RxAISInActive=adATLAST1RxAISInActive, adATLAST1TstEntry=adATLAST1TstEntry, adATLAST1IfAlarmStatus=adATLAST1IfAlarmStatus, adATLAST1TxYellowActive=adATLAST1TxYellowActive, adATLAST1TotalPCV=adATLAST1TotalPCV, adATLAST1LOSActive=adATLAST1LOSActive, adATLAST1IfIntervalNumber=adATLAST1IfIntervalNumber, adATLAST1TstPattern=adATLAST1TstPattern, adATLAST1TotalLES=adATLAST1TotalLES, adMgmt=adMgmt, adATLAST1IfEntry=adATLAST1IfEntry, adATLAST1TstPatternESs=adATLAST1TstPatternESs, adATLAST1CurrentSES=adATLAST1CurrentSES, adATLAST1TstPatternSESs=adATLAST1TstPatternSESs, adATLAST1IfTotalLOFC=adATLAST1IfTotalLOFC, adATLAST1IfDS0TxSignalStatusB=adATLAST1IfDS0TxSignalStatusB, adATLAST1CurrentSEFS=adATLAST1CurrentSEFS, adATLAST1TotalCSS=adATLAST1TotalCSS, adATLAST1RxYellowActive=adATLAST1RxYellowActive)
