#
# PySNMP MIB module ChrComPmAtmATM-CELL-Day-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmAtmATM-CELL-Day-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmAtm, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmAtm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Unsigned32, Counter32, Counter64, Integer32, MibIdentifier, IpAddress, ModuleIdentity, iso, Bits, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Unsigned32", "Counter32", "Counter64", "Integer32", "MibIdentifier", "IpAddress", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmAtmATM_CELL_DayTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3), ).setLabel("chrComPmAtmATM-CELL-DayTable")
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_DayTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_DayTable.setDescription('')
chrComPmAtmATM_CELL_DayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1), ).setLabel("chrComPmAtmATM-CELL-DayEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmAtmATM-CELL-Day-MIB", "chrComPmAtmDayNumber"))
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_DayEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_DayEntry.setDescription('')
chrComPmAtmDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDayNumber.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDayNumber.setDescription('')
chrComPmAtmSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setDescription('')
chrComPmAtmElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setDescription('')
chrComPmAtmSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setDescription('')
chrComPmAtmOCDS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmOCDS.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmOCDS.setDescription('')
chrComPmAtmHECCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmHECCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmHECCells.setDescription('')
chrComPmAtmCorrectableHECCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmCorrectableHECCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmCorrectableHECCells.setDescription('')
chrComPmAtmDiscardedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedCells.setDescription('')
chrComPmAtmReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setDescription('')
chrComPmAtmTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setDescription('')
chrComPmAtmDiscardedIngCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngCells.setDescription('')
chrComPmAtmDiscardedIngHighPrCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngHighPrCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngHighPrCells.setDescription('')
chrComPmAtmDiscardedEgCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgCells.setDescription('')
chrComPmAtmDiscardedEgHighPrCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgHighPrCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgHighPrCells.setDescription('')
chrComPmAtmDiscardedUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedUPC.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedUPC.setDescription('')
chrComPmAtmTaggedUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTaggedUPC.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmTaggedUPC.setDescription('')
chrComPmAtmThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmAtmThresholdProfIndex.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmThresholdProfIndex.setDescription('')
chrComPmAtmResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 3, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmAtmResetPmCountersAction.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmResetPmCountersAction.setDescription('')
mibBuilder.exportSymbols("ChrComPmAtmATM-CELL-Day-MIB", chrComPmAtmDiscardedEgHighPrCells=chrComPmAtmDiscardedEgHighPrCells, chrComPmAtmDiscardedIngHighPrCells=chrComPmAtmDiscardedIngHighPrCells, chrComPmAtmATM_CELL_DayEntry=chrComPmAtmATM_CELL_DayEntry, chrComPmAtmReceivedCells=chrComPmAtmReceivedCells, chrComPmAtmHECCells=chrComPmAtmHECCells, chrComPmAtmOCDS=chrComPmAtmOCDS, chrComPmAtmDiscardedCells=chrComPmAtmDiscardedCells, chrComPmAtmDiscardedIngCells=chrComPmAtmDiscardedIngCells, chrComPmAtmDiscardedUPC=chrComPmAtmDiscardedUPC, chrComPmAtmDiscardedEgCells=chrComPmAtmDiscardedEgCells, chrComPmAtmResetPmCountersAction=chrComPmAtmResetPmCountersAction, chrComPmAtmSuspectedInterval=chrComPmAtmSuspectedInterval, chrComPmAtmTransmittedCells=chrComPmAtmTransmittedCells, chrComPmAtmCorrectableHECCells=chrComPmAtmCorrectableHECCells, chrComPmAtmTaggedUPC=chrComPmAtmTaggedUPC, chrComPmAtmSuppressedIntrvls=chrComPmAtmSuppressedIntrvls, chrComPmAtmATM_CELL_DayTable=chrComPmAtmATM_CELL_DayTable, chrComPmAtmElapsedTime=chrComPmAtmElapsedTime, chrComPmAtmThresholdProfIndex=chrComPmAtmThresholdProfIndex, chrComPmAtmDayNumber=chrComPmAtmDayNumber)