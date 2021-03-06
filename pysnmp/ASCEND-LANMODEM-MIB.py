#
# PySNMP MIB module ASCEND-LANMODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-LANMODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
lanModemGroup, slots = mibBuilder.importSymbols("ASCEND-MIB", "lanModemGroup", "slots")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, NotificationType, ModuleIdentity, IpAddress, MibIdentifier, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Integer32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Integer32", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

class ModemSpeedType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45))
    namedValues = NamedValues(("baud300", 1), ("baud600", 2), ("baud1200", 3), ("baud2400", 4), ("baud4800", 5), ("baud9600", 6), ("baud12000", 7), ("baud14400", 8), ("baud7200", 9), ("baud16800", 10), ("baud19200", 11), ("baud21600", 12), ("baud24000", 13), ("baud26400", 14), ("baud28800", 15), ("baud31200", 16), ("baud33600", 17), ("baud32000", 18), ("baud34000", 19), ("baud36000", 20), ("baud38000", 21), ("baud40000", 22), ("baud42000", 23), ("baud44000", 24), ("baud46000", 25), ("baud48000", 26), ("baud50000", 27), ("baud52000", 28), ("baud54000", 29), ("baud56000", 30), ("baud28000", 31), ("baud29333", 32), ("baud30667", 33), ("baud33333", 34), ("baud34667", 35), ("baud37333", 36), ("baud38667", 37), ("baud41333", 38), ("baud42667", 39), ("baud45333", 40), ("baud46667", 41), ("baud49333", 42), ("baud50667", 43), ("baud53333", 44), ("baud54667", 45))

slotMdmTable = MibTable((1, 3, 6, 1, 4, 1, 529, 2, 5), )
if mibBuilder.loadTexts: slotMdmTable.setStatus('mandatory')
slotMdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 2, 5, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "slotMdmIndex"))
if mibBuilder.loadTexts: slotMdmEntry.setStatus('mandatory')
slotMdmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMdmIndex.setStatus('mandatory')
slotMdmSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMdmSlotIndex.setStatus('mandatory')
slotMdmItemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMdmItemIndex.setStatus('mandatory')
slotMdmItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("modemStateNonExist", 1), ("modemStateFailPost", 2), ("modemStateIdle", 3), ("modemStateAwaitingRlsd", 4), ("modemStateAwaitingCodes", 5), ("modemStateOnline", 6), ("modemStateInit", 7), ("modemStateInitOpenQueued", 8), ("modemStateInitOpenQueuedVc", 9), ("modemStateInitDialstr2", 10), ("modemStateInitDialstr3", 11), ("modemStateVirtualConnect", 12), ("modemStateDisabled", 13), ("modemStateDisabledChan", 14), ("modemStateDtrDrop", 15), ("modemStateDiag", 16), ("modemStateVcInitStr", 17), ("modemStateInitDialstr4", 18), ("modemStateCsum", 19), ("modemStateRedownloadFailed", 20), ("modemStateCsmxExtraDelay", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMdmItemStatus.setStatus('mandatory')
slotMdmItemStatusChar = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotMdmItemStatusChar.setStatus('mandatory')
slotMdmItemConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3), ("disableAndChannel", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotMdmItemConfig.setStatus('mandatory')
availLanModem = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availLanModem.setStatus('mandatory')
availLanModemTable = MibTable((1, 3, 6, 1, 4, 1, 529, 15, 2), )
if mibBuilder.loadTexts: availLanModemTable.setStatus('mandatory')
availLanModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 15, 2, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "availLanModemSlotIndex"), (0, "ASCEND-LANMODEM-MIB", "availLanModemPortIndex"))
if mibBuilder.loadTexts: availLanModemEntry.setStatus('mandatory')
availLanModemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availLanModemSlotIndex.setStatus('mandatory')
availLanModemPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availLanModemPortIndex.setStatus('mandatory')
availLanModemUsedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availLanModemUsedCount.setStatus('mandatory')
availLanModemBadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availLanModemBadCount.setStatus('mandatory')
availLanModemLast32 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: availLanModemLast32.setStatus('mandatory')
suspectLanModem = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: suspectLanModem.setStatus('mandatory')
suspectLanModemTable = MibTable((1, 3, 6, 1, 4, 1, 529, 15, 4), )
if mibBuilder.loadTexts: suspectLanModemTable.setStatus('mandatory')
suspectLanModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 15, 4, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "suspectLanModemSlotIndex"), (0, "ASCEND-LANMODEM-MIB", "suspectLanModemPortIndex"))
if mibBuilder.loadTexts: suspectLanModemEntry.setStatus('mandatory')
suspectLanModemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: suspectLanModemSlotIndex.setStatus('mandatory')
suspectLanModemPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: suspectLanModemPortIndex.setStatus('mandatory')
suspectLanModemUsedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: suspectLanModemUsedCount.setStatus('mandatory')
suspectLanModemBadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: suspectLanModemBadCount.setStatus('mandatory')
suspectLanModemLast32 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: suspectLanModemLast32.setStatus('mandatory')
disabledLanModem = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: disabledLanModem.setStatus('mandatory')
disabledLanModemTable = MibTable((1, 3, 6, 1, 4, 1, 529, 15, 6), )
if mibBuilder.loadTexts: disabledLanModemTable.setStatus('mandatory')
disabledLanModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 15, 6, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "disabledLanModemSlotIndex"), (0, "ASCEND-LANMODEM-MIB", "disabledLanModemPortIndex"))
if mibBuilder.loadTexts: disabledLanModemEntry.setStatus('mandatory')
disabledLanModemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: disabledLanModemSlotIndex.setStatus('mandatory')
disabledLanModemPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: disabledLanModemPortIndex.setStatus('mandatory')
disabledLanModemUsedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: disabledLanModemUsedCount.setStatus('mandatory')
disabledLanModemBadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: disabledLanModemBadCount.setStatus('mandatory')
disabledLanModemLast32 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: disabledLanModemLast32.setStatus('mandatory')
deadLanModem = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deadLanModem.setStatus('mandatory')
deadLanModemTable = MibTable((1, 3, 6, 1, 4, 1, 529, 15, 8), )
if mibBuilder.loadTexts: deadLanModemTable.setStatus('mandatory')
deadLanModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 15, 8, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "deadLanModemSlotIndex"), (0, "ASCEND-LANMODEM-MIB", "deadLanModemPortIndex"))
if mibBuilder.loadTexts: deadLanModemEntry.setStatus('mandatory')
deadLanModemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deadLanModemSlotIndex.setStatus('mandatory')
deadLanModemPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deadLanModemPortIndex.setStatus('mandatory')
deadLanModemState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("failedPost", 2), ("nonExistent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deadLanModemState.setStatus('mandatory')
busyLanModem = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyLanModem.setStatus('mandatory')
busyLanModemTable = MibTable((1, 3, 6, 1, 4, 1, 529, 15, 10), )
if mibBuilder.loadTexts: busyLanModemTable.setStatus('mandatory')
busyLanModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 15, 10, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "busyLanModemSlotIndex"), (0, "ASCEND-LANMODEM-MIB", "busyLanModemPortIndex"))
if mibBuilder.loadTexts: busyLanModemEntry.setStatus('mandatory')
busyLanModemSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyLanModemSlotIndex.setStatus('mandatory')
busyLanModemPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyLanModemPortIndex.setStatus('mandatory')
busyLanModemUsedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyLanModemUsedCount.setStatus('mandatory')
busyLanModemBadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyLanModemBadCount.setStatus('mandatory')
busyLanModemLast32 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyLanModemLast32.setStatus('mandatory')
busyDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("callUnknown", 1), ("callOriginated", 2), ("callAnswered", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyDirection.setStatus('mandatory')
suspectTrapState = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: suspectTrapState.setStatus('mandatory')
csmLanMdmDiagAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csmLanMdmDiagAdminStatus.setStatus('mandatory')
csmLanMdmDiagMaxNumberOfDiagEntries = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagMaxNumberOfDiagEntries.setStatus('mandatory')
csmLanMdmDiagFirstIndexNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagFirstIndexNumber.setStatus('mandatory')
csmLanMdmDiagLastIndexNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 15, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagLastIndexNumber.setStatus('mandatory')
csmLanMdmDiagTable = MibTable((1, 3, 6, 1, 4, 1, 529, 15, 16), )
if mibBuilder.loadTexts: csmLanMdmDiagTable.setStatus('mandatory')
csmLanMdmDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 15, 16, 1), ).setIndexNames((0, "ASCEND-LANMODEM-MIB", "csmLanMdmDiagIndexNumber"))
if mibBuilder.loadTexts: csmLanMdmDiagEntry.setStatus('mandatory')
csmLanMdmDiagIndexNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagIndexNumber.setStatus('mandatory')
csmLanMdmDiagCallReferenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCallReferenceNum.setStatus('mandatory')
csmLanMdmDiagSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagSlotIndex.setStatus('mandatory')
csmLanMdmDiagPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagPortIndex.setStatus('mandatory')
csmLanMdmDiagCurrentXmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 5), ModemSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCurrentXmitRate.setStatus('mandatory')
csmLanMdmDiagMinXmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 6), ModemSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagMinXmitRate.setStatus('mandatory')
csmLanMdmDiagMaxXmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 7), ModemSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagMaxXmitRate.setStatus('mandatory')
csmLanMdmDiagCurrentRecvRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 8), ModemSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCurrentRecvRate.setStatus('mandatory')
csmLanMdmDiagMinRcvRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 9), ModemSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagMinRcvRate.setStatus('mandatory')
csmLanMdmDiagMaxRcvRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 10), ModemSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagMaxRcvRate.setStatus('mandatory')
csmLanMdmDiagProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("lap-m", 2), ("mnp4", 3), ("mnp10", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagProtocol.setStatus('mandatory')
csmLanMdmDiagCompression = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("mnp5", 2), ("v42bis", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCompression.setStatus('mandatory')
csmLanMdmDiagModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("v90", 1), ("v34", 2), ("v17", 3), ("v23", 4), ("v21", 5), ("k56flex", 6), ("v22bis", 7), ("v32", 8), ("bell212", 9), ("bell103", 10), ("v22", 11), ("vFC", 12), ("v33", 13), ("bell208", 14), ("v29", 15), ("v27", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagModulation.setStatus('mandatory')
csmLanMdmDiagSymbolRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notApplicable", 1), ("sym2400", 2), ("sym2800", 3), ("sym3000", 4), ("sym3200", 5), ("sym3429", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagSymbolRate.setStatus('mandatory')
csmLanMdmDiagCurrentRcvLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCurrentRcvLevel.setStatus('mandatory')
csmLanMdmDiagCurrentXmitLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCurrentXmitLevel.setStatus('mandatory')
csmLanMdmDiagCurrentLineQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCurrentLineQuality.setStatus('mandatory')
csmLanMdmDiagCurrentSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagCurrentSNR.setStatus('mandatory')
csmLanMdmDiagSNRMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagSNRMinimum.setStatus('mandatory')
csmLanMdmDiagSNRMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagSNRMaximum.setStatus('mandatory')
csmLanMdmDiagLocalRetrainRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagLocalRetrainRequested.setStatus('mandatory')
csmLanMdmDiagRemoteRetrainRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagRemoteRetrainRequested.setStatus('mandatory')
csmLanMdmDiagHighestSPXRcvState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagHighestSPXRcvState.setStatus('mandatory')
csmLanMdmDiagHighestSPXTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagHighestSPXTxState.setStatus('mandatory')
csmLanMdmDiagNonlinearEncode = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagNonlinearEncode.setStatus('mandatory')
csmLanMdmDiagPrecode = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagPrecode.setStatus('mandatory')
csmLanMdmDiagShaping = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagShaping.setStatus('mandatory')
csmLanMdmDiagConnectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagConnectionTime.setStatus('mandatory')
csmLanMdmDiagDisconnectReason = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23))).clone(namedValues=NamedValues(("none", 1), ("localRequest", 2), ("callWaiting", 3), ("carrierLost", 4), ("noErrorCorrection", 6), ("incompatibleProtocol", 7), ("linkDisconnect", 12), ("excessiveRetransmissions", 13), ("noRemoteResponse", 15), ("gstnCleardown", 16), ("inactivityTimer", 17), ("incompatibleSpeeds", 18), ("breakDisconnect", 19), ("keyAbort", 20), ("noConnect", 22), ("retrainFailure", 23)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagDisconnectReason.setStatus('mandatory')
csmLanMdmDiagRetrainReason = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("none", 1), ("retrainOrRateRenegSuccess", 2), ("localRetrainDueToATO1", 3), ("localRetrainDueToHiEQM", 4), ("localRateRenegDueToHiEQM", 5), ("localRateRenegDueToLowEQM", 6), ("localRetrainDueTo2RateRenegs", 7), ("carrierLostButLineActive", 8), ("lostConnection", 9), ("fallbackToV34", 10), ("localRateRenegDueToMN10", 11), ("localRetrainDueToMN10", 12), ("remoteRetrain", 13), ("remoteRateReneg", 14), ("v34RetrainAt24K", 15), ("v42RetrainDueToExcessiveReTx", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csmLanMdmDiagRetrainReason.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-LANMODEM-MIB", csmLanMdmDiagModulation=csmLanMdmDiagModulation, csmLanMdmDiagSNRMinimum=csmLanMdmDiagSNRMinimum, slotMdmEntry=slotMdmEntry, suspectLanModemPortIndex=suspectLanModemPortIndex, csmLanMdmDiagCurrentRcvLevel=csmLanMdmDiagCurrentRcvLevel, csmLanMdmDiagCurrentRecvRate=csmLanMdmDiagCurrentRecvRate, csmLanMdmDiagTable=csmLanMdmDiagTable, ModemSpeedType=ModemSpeedType, busyLanModemLast32=busyLanModemLast32, disabledLanModemBadCount=disabledLanModemBadCount, csmLanMdmDiagRetrainReason=csmLanMdmDiagRetrainReason, disabledLanModemUsedCount=disabledLanModemUsedCount, availLanModemPortIndex=availLanModemPortIndex, busyLanModemSlotIndex=busyLanModemSlotIndex, deadLanModemState=deadLanModemState, availLanModemTable=availLanModemTable, DisplayString=DisplayString, csmLanMdmDiagSymbolRate=csmLanMdmDiagSymbolRate, csmLanMdmDiagMaxNumberOfDiagEntries=csmLanMdmDiagMaxNumberOfDiagEntries, availLanModemLast32=availLanModemLast32, busyLanModemTable=busyLanModemTable, csmLanMdmDiagCompression=csmLanMdmDiagCompression, suspectLanModemSlotIndex=suspectLanModemSlotIndex, disabledLanModemEntry=disabledLanModemEntry, suspectLanModem=suspectLanModem, disabledLanModemLast32=disabledLanModemLast32, deadLanModemEntry=deadLanModemEntry, csmLanMdmDiagEntry=csmLanMdmDiagEntry, csmLanMdmDiagCurrentLineQuality=csmLanMdmDiagCurrentLineQuality, suspectLanModemUsedCount=suspectLanModemUsedCount, deadLanModemSlotIndex=deadLanModemSlotIndex, csmLanMdmDiagMaxRcvRate=csmLanMdmDiagMaxRcvRate, csmLanMdmDiagPrecode=csmLanMdmDiagPrecode, csmLanMdmDiagMinRcvRate=csmLanMdmDiagMinRcvRate, csmLanMdmDiagCurrentXmitRate=csmLanMdmDiagCurrentXmitRate, csmLanMdmDiagProtocol=csmLanMdmDiagProtocol, csmLanMdmDiagRemoteRetrainRequested=csmLanMdmDiagRemoteRetrainRequested, csmLanMdmDiagHighestSPXTxState=csmLanMdmDiagHighestSPXTxState, busyLanModemEntry=busyLanModemEntry, slotMdmItemStatusChar=slotMdmItemStatusChar, availLanModemSlotIndex=availLanModemSlotIndex, slotMdmItemStatus=slotMdmItemStatus, csmLanMdmDiagSlotIndex=csmLanMdmDiagSlotIndex, availLanModem=availLanModem, csmLanMdmDiagAdminStatus=csmLanMdmDiagAdminStatus, disabledLanModem=disabledLanModem, suspectLanModemBadCount=suspectLanModemBadCount, slotMdmTable=slotMdmTable, csmLanMdmDiagLocalRetrainRequested=csmLanMdmDiagLocalRetrainRequested, csmLanMdmDiagFirstIndexNumber=csmLanMdmDiagFirstIndexNumber, csmLanMdmDiagCurrentXmitLevel=csmLanMdmDiagCurrentXmitLevel, busyLanModemUsedCount=busyLanModemUsedCount, busyLanModemPortIndex=busyLanModemPortIndex, csmLanMdmDiagHighestSPXRcvState=csmLanMdmDiagHighestSPXRcvState, deadLanModemPortIndex=deadLanModemPortIndex, suspectLanModemTable=suspectLanModemTable, csmLanMdmDiagSNRMaximum=csmLanMdmDiagSNRMaximum, busyLanModem=busyLanModem, csmLanMdmDiagLastIndexNumber=csmLanMdmDiagLastIndexNumber, slotMdmSlotIndex=slotMdmSlotIndex, slotMdmIndex=slotMdmIndex, deadLanModem=deadLanModem, csmLanMdmDiagPortIndex=csmLanMdmDiagPortIndex, suspectLanModemEntry=suspectLanModemEntry, deadLanModemTable=deadLanModemTable, availLanModemBadCount=availLanModemBadCount, availLanModemEntry=availLanModemEntry, csmLanMdmDiagConnectionTime=csmLanMdmDiagConnectionTime, slotMdmItemIndex=slotMdmItemIndex, suspectLanModemLast32=suspectLanModemLast32, csmLanMdmDiagDisconnectReason=csmLanMdmDiagDisconnectReason, csmLanMdmDiagIndexNumber=csmLanMdmDiagIndexNumber, slotMdmItemConfig=slotMdmItemConfig, disabledLanModemPortIndex=disabledLanModemPortIndex, suspectTrapState=suspectTrapState, disabledLanModemSlotIndex=disabledLanModemSlotIndex, csmLanMdmDiagCallReferenceNum=csmLanMdmDiagCallReferenceNum, csmLanMdmDiagShaping=csmLanMdmDiagShaping, csmLanMdmDiagNonlinearEncode=csmLanMdmDiagNonlinearEncode, busyDirection=busyDirection, csmLanMdmDiagMinXmitRate=csmLanMdmDiagMinXmitRate, busyLanModemBadCount=busyLanModemBadCount, csmLanMdmDiagMaxXmitRate=csmLanMdmDiagMaxXmitRate, disabledLanModemTable=disabledLanModemTable, availLanModemUsedCount=availLanModemUsedCount, csmLanMdmDiagCurrentSNR=csmLanMdmDiagCurrentSNR)
