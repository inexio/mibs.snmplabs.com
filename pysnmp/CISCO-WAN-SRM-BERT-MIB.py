#
# PySNMP MIB module CISCO-WAN-SRM-BERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-SRM-BERT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter64, Counter32, Gauge32, Unsigned32, ModuleIdentity, Integer32, IpAddress, Bits, iso, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter64", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "IpAddress", "Bits", "iso", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanSrmBertMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 31))
ciscoWanSrmBertMIB.setRevisions(('2002-08-26 00:00',))
if mibBuilder.loadTexts: ciscoWanSrmBertMIB.setLastUpdated('200208260000Z')
if mibBuilder.loadTexts: ciscoWanSrmBertMIB.setOrganization('Cisco Systems, Inc.')
bert = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 1))
bertControl = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("acquireBert", 1), ("releaseBert", 2), ("cnfBert", 3), ("startBert", 4), ("modBert", 5), ("delBert", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertControl.setStatus('current')
bertResourceStatus = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("free", 1), ("inUse", 2), ("cleanupPending", 3))).clone('free')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertResourceStatus.setStatus('current')
bertOwner = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertOwner.setStatus('current')
bertUserId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertUserId.setStatus('current')
bertStatus = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inactive", 1), ("bertInSync", 2), ("bertOutOfSync", 3), ("searchingDDSCommands", 4), ("farEndInLoop", 5), ("facilityInLoop", 6), ("portFacilityFifoFault", 7), ("portFacilityFifoOutOfSync", 8), ("metallicInLoop", 9), ("bertFailed", 10))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertStatus.setStatus('current')
bertSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertSlotNumber.setStatus('current')
bertTestMedium = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("line", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertTestMedium.setStatus('current')
bertPort = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertPort.setStatus('current')
bertLine = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertLine.setStatus('current')
bertMode = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bertPatternTest", 1), ("ddsSeek", 2), ("loopback", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertMode.setStatus('current')
bertDeviceToLoop = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("noLatchOCUwith1", 1), ("noLatchOCUwitout1", 2), ("noLatchCSU", 3), ("noLatchDSU", 4), ("latchDS0Drop", 5), ("latchDS0Line", 6), ("latchOCU", 7), ("latchCSU", 8), ("latchDSU", 9), ("latchHL96", 10), ("v54Polynomial", 11), ("inband", 12), ("esf", 13), ("metallic", 14), ("noDevice", 15), ("smartJackInband", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertDeviceToLoop.setStatus('current')
bertDS0DPIterationCount = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertDS0DPIterationCount.setStatus('current')
bertPattern = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("allZeros", 1), ("allOnes", 2), ("alternateONeZero", 3), ("doubleOneZero", 4), ("fifteenBit", 5), ("twentyBit", 6), ("twentyBitQRSS", 7), ("twentythreeBit", 8), ("oneInEight", 9), ("threeIntwentyfour", 10), ("dds-1", 11), ("dds-2", 12), ("dds-3", 13), ("dds-4", 14), ("dds-5", 15), ("nineBit", 16), ("elevenBit", 17)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertPattern.setStatus('current')
bertLoopback = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("farEndLoopback", 1), ("facilityLoopback", 2), ("metallicLoopback", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertLoopback.setStatus('current')
bertLoopbackOperation = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopUp", 1), ("loopDown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bertLoopbackOperation.setStatus('current')
bertDS0Speed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("speed56k", 1), ("speed64k", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertDS0Speed.setStatus('current')
bertTimeSlots = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertTimeSlots.setStatus('current')
bertStartTime = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertStartTime.setStatus('current')
bertStartDate = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertStartDate.setStatus('current')
bertBitCount = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertBitCount.setStatus('current')
bertBitErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertBitErrorCount.setStatus('current')
bertErrorInjectCount = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertErrorInjectCount.setStatus('current')
bertCleanupAction = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("noAction", 1), ("smCleanup", 2), ("latchDS0DropLoopdown", 3), ("latchDS0LineLoopdown", 4), ("latchOCULoopdown", 5), ("latchCSULoopdown", 6), ("latchDSULoopdown", 7), ("latchHL96Loopdown", 8), ("v54PolynomialLoopdown", 9), ("inbandLoopdown", 10), ("esfLoopdown", 11), ("facilityLoopdown", 12), ("metallicLoopdown", 13), ("smartJackInbandLoopdown", 14))).clone('noAction')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertCleanupAction.setStatus('current')
bertAbortReason = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ascStateChange", 1), ("smStateChange", 2), ("srmStateChange", 3), ("coreCardSwitch", 4), ("smRedundancySwitch", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertAbortReason.setStatus('current')
bertDDSSeekResultsTableFirstIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertDDSSeekResultsTableFirstIndex.setStatus('current')
bertDDSSeekResultsTableLastIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertDDSSeekResultsTableLastIndex.setStatus('current')
bertDDSSeekResultsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27), )
if mibBuilder.loadTexts: bertDDSSeekResultsTable.setStatus('current')
bertDDSSeekResultsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27, 1), ).setIndexNames((0, "CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableIndex"))
if mibBuilder.loadTexts: bertDDSSeekResultsTableEntry.setStatus('current')
bertDDSSeekResultsTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertDDSSeekResultsTableIndex.setStatus('current')
bertDDSCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(30, 10, 40, 44, 90, 126, 86, 114, 26, 42, 120, 28, 108, 58, 24, 50))).clone(namedValues=NamedValues(("abnormalStationCondition", 30), ("block", 10), ("channelLoopback", 40), ("dsuLoopback", 44), ("farEndVoice", 90), ("idle", 126), ("loopbackEnable", 86), ("mjuAlert", 114), ("muxOutOfSync", 26), ("ocuLoopback", 42), ("release", 120), ("test", 28), ("testAlert", 108), ("transitionInProgress", 58), ("unassignedMuxChannel", 24), ("unnamed", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertDDSCode.setStatus('current')
bertSupportedTestsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28), )
if mibBuilder.loadTexts: bertSupportedTestsTable.setStatus('current')
bertSupportedTestsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1), ).setIndexNames((0, "CISCO-WAN-SRM-BERT-MIB", "bertSupportedTestsTableIndex"))
if mibBuilder.loadTexts: bertSupportedTestsTableEntry.setStatus('current')
bertSupportedTestsTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertSupportedTestsTableIndex.setStatus('current')
bertSupportFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertSupportFlag.setStatus('current')
bertTestMediumMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertTestMediumMask.setStatus('current')
bertModeMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertModeMask.setStatus('current')
bertDeviceToLoopMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertDeviceToLoopMask.setStatus('current')
bertPatternMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertPatternMask.setStatus('current')
bertLoopbackMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertLoopbackMask.setStatus('current')
bertCardT1E1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t1", 1), ("e1", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bertCardT1E1Type.setStatus('current')
ciscoWanSrmBertMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 31, 2))
ciscoWanSrmBertMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1))
ciscoWanSrmBertMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 2))
ciscoWanSrmBertCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 2, 1)).setObjects(("CISCO-WAN-SRM-BERT-MIB", "ciscoWanSrmBertConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmBertCompliance = ciscoWanSrmBertCompliance.setStatus('current')
ciscoWanSrmBertConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1, 1)).setObjects(("CISCO-WAN-SRM-BERT-MIB", "bertControl"), ("CISCO-WAN-SRM-BERT-MIB", "bertResourceStatus"), ("CISCO-WAN-SRM-BERT-MIB", "bertOwner"), ("CISCO-WAN-SRM-BERT-MIB", "bertUserId"), ("CISCO-WAN-SRM-BERT-MIB", "bertStatus"), ("CISCO-WAN-SRM-BERT-MIB", "bertSlotNumber"), ("CISCO-WAN-SRM-BERT-MIB", "bertTestMedium"), ("CISCO-WAN-SRM-BERT-MIB", "bertPort"), ("CISCO-WAN-SRM-BERT-MIB", "bertLine"), ("CISCO-WAN-SRM-BERT-MIB", "bertMode"), ("CISCO-WAN-SRM-BERT-MIB", "bertDeviceToLoop"), ("CISCO-WAN-SRM-BERT-MIB", "bertDS0DPIterationCount"), ("CISCO-WAN-SRM-BERT-MIB", "bertPattern"), ("CISCO-WAN-SRM-BERT-MIB", "bertLoopback"), ("CISCO-WAN-SRM-BERT-MIB", "bertLoopbackOperation"), ("CISCO-WAN-SRM-BERT-MIB", "bertDS0Speed"), ("CISCO-WAN-SRM-BERT-MIB", "bertTimeSlots"), ("CISCO-WAN-SRM-BERT-MIB", "bertStartTime"), ("CISCO-WAN-SRM-BERT-MIB", "bertStartDate"), ("CISCO-WAN-SRM-BERT-MIB", "bertBitCount"), ("CISCO-WAN-SRM-BERT-MIB", "bertBitErrorCount"), ("CISCO-WAN-SRM-BERT-MIB", "bertErrorInjectCount"), ("CISCO-WAN-SRM-BERT-MIB", "bertCleanupAction"), ("CISCO-WAN-SRM-BERT-MIB", "bertAbortReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmBertConfGroup = ciscoWanSrmBertConfGroup.setStatus('current')
ciscoWanSrmBertTestResultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1, 2)).setObjects(("CISCO-WAN-SRM-BERT-MIB", "bertSupportedTestsTableIndex"), ("CISCO-WAN-SRM-BERT-MIB", "bertSupportFlag"), ("CISCO-WAN-SRM-BERT-MIB", "bertTestMediumMask"), ("CISCO-WAN-SRM-BERT-MIB", "bertModeMask"), ("CISCO-WAN-SRM-BERT-MIB", "bertDeviceToLoopMask"), ("CISCO-WAN-SRM-BERT-MIB", "bertPatternMask"), ("CISCO-WAN-SRM-BERT-MIB", "bertLoopbackMask"), ("CISCO-WAN-SRM-BERT-MIB", "bertCardT1E1Type"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmBertTestResultsGroup = ciscoWanSrmBertTestResultsGroup.setStatus('current')
ciscoWanSrmBertDDSResultsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1, 3)).setObjects(("CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableFirstIndex"), ("CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableLastIndex"), ("CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableIndex"), ("CISCO-WAN-SRM-BERT-MIB", "bertDDSCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanSrmBertDDSResultsGroup = ciscoWanSrmBertDDSResultsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-SRM-BERT-MIB", bertAbortReason=bertAbortReason, bertDDSSeekResultsTableIndex=bertDDSSeekResultsTableIndex, bertDDSSeekResultsTableFirstIndex=bertDDSSeekResultsTableFirstIndex, bertLoopbackOperation=bertLoopbackOperation, bertLine=bertLine, bertDDSSeekResultsTable=bertDDSSeekResultsTable, bertDDSCode=bertDDSCode, ciscoWanSrmBertConfGroup=ciscoWanSrmBertConfGroup, ciscoWanSrmBertTestResultsGroup=ciscoWanSrmBertTestResultsGroup, ciscoWanSrmBertCompliance=ciscoWanSrmBertCompliance, bertDS0DPIterationCount=bertDS0DPIterationCount, bertModeMask=bertModeMask, bertTestMedium=bertTestMedium, bertPattern=bertPattern, bertMode=bertMode, bertBitCount=bertBitCount, bertOwner=bertOwner, bertTestMediumMask=bertTestMediumMask, bertLoopback=bertLoopback, ciscoWanSrmBertMIBGroups=ciscoWanSrmBertMIBGroups, bertBitErrorCount=bertBitErrorCount, ciscoWanSrmBertDDSResultsGroup=ciscoWanSrmBertDDSResultsGroup, bertStartTime=bertStartTime, ciscoWanSrmBertMIB=ciscoWanSrmBertMIB, bertSupportFlag=bertSupportFlag, bertCleanupAction=bertCleanupAction, bertPort=bertPort, ciscoWanSrmBertMIBCompliances=ciscoWanSrmBertMIBCompliances, bertTimeSlots=bertTimeSlots, bertSlotNumber=bertSlotNumber, bertErrorInjectCount=bertErrorInjectCount, bertStatus=bertStatus, bertDDSSeekResultsTableLastIndex=bertDDSSeekResultsTableLastIndex, PYSNMP_MODULE_ID=ciscoWanSrmBertMIB, bertUserId=bertUserId, bertDeviceToLoopMask=bertDeviceToLoopMask, bertResourceStatus=bertResourceStatus, bertStartDate=bertStartDate, bertDDSSeekResultsTableEntry=bertDDSSeekResultsTableEntry, bertDS0Speed=bertDS0Speed, bertSupportedTestsTableEntry=bertSupportedTestsTableEntry, bertCardT1E1Type=bertCardT1E1Type, bertSupportedTestsTableIndex=bertSupportedTestsTableIndex, bertSupportedTestsTable=bertSupportedTestsTable, bertControl=bertControl, ciscoWanSrmBertMIBConformance=ciscoWanSrmBertMIBConformance, bertPatternMask=bertPatternMask, bert=bert, bertLoopbackMask=bertLoopbackMask, bertDeviceToLoop=bertDeviceToLoop)