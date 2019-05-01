#
# PySNMP MIB module ChrComPmAtmATM-CELL-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmAtmATM-CELL-Current-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmAtm, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmAtm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, Bits, iso, IpAddress, Integer32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, MibIdentifier, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Bits", "iso", "IpAddress", "Integer32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "MibIdentifier", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmAtmATM_CELL_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1), ).setLabel("chrComPmAtmATM-CELL-CurrentTable")
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_CurrentTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_CurrentTable.setDescription('')
chrComPmAtmATM_CELL_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1), ).setLabel("chrComPmAtmATM-CELL-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_CurrentEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_CurrentEntry.setDescription('')
chrComPmAtmSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setDescription('')
chrComPmAtmElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setDescription('')
chrComPmAtmSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setDescription('')
chrComPmAtmOCDS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmOCDS.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmOCDS.setDescription('')
chrComPmAtmHECCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmHECCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmHECCells.setDescription('')
chrComPmAtmCorrectableHECCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmCorrectableHECCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmCorrectableHECCells.setDescription('')
chrComPmAtmDiscardedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedCells.setDescription('')
chrComPmAtmReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setDescription('')
chrComPmAtmTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setDescription('')
chrComPmAtmDiscardedIngCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngCells.setDescription('')
chrComPmAtmDiscardedIngHighPrCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngHighPrCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngHighPrCells.setDescription('')
chrComPmAtmDiscardedEgCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgCells.setDescription('')
chrComPmAtmDiscardedEgHighPrCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgHighPrCells.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgHighPrCells.setDescription('')
chrComPmAtmDiscardedUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedUPC.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmDiscardedUPC.setDescription('')
chrComPmAtmTaggedUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTaggedUPC.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmTaggedUPC.setDescription('')
chrComPmAtmThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmAtmThresholdProfIndex.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmThresholdProfIndex.setDescription('')
chrComPmAtmResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 1, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmAtmResetPmCountersAction.setStatus('current')
if mibBuilder.loadTexts: chrComPmAtmResetPmCountersAction.setDescription('')
mibBuilder.exportSymbols("ChrComPmAtmATM-CELL-Current-MIB", chrComPmAtmSuppressedIntrvls=chrComPmAtmSuppressedIntrvls, chrComPmAtmDiscardedUPC=chrComPmAtmDiscardedUPC, chrComPmAtmDiscardedEgCells=chrComPmAtmDiscardedEgCells, chrComPmAtmThresholdProfIndex=chrComPmAtmThresholdProfIndex, chrComPmAtmATM_CELL_CurrentEntry=chrComPmAtmATM_CELL_CurrentEntry, chrComPmAtmDiscardedEgHighPrCells=chrComPmAtmDiscardedEgHighPrCells, chrComPmAtmATM_CELL_CurrentTable=chrComPmAtmATM_CELL_CurrentTable, chrComPmAtmHECCells=chrComPmAtmHECCells, chrComPmAtmReceivedCells=chrComPmAtmReceivedCells, chrComPmAtmTransmittedCells=chrComPmAtmTransmittedCells, chrComPmAtmElapsedTime=chrComPmAtmElapsedTime, chrComPmAtmResetPmCountersAction=chrComPmAtmResetPmCountersAction, chrComPmAtmOCDS=chrComPmAtmOCDS, chrComPmAtmDiscardedCells=chrComPmAtmDiscardedCells, chrComPmAtmDiscardedIngHighPrCells=chrComPmAtmDiscardedIngHighPrCells, chrComPmAtmCorrectableHECCells=chrComPmAtmCorrectableHECCells, chrComPmAtmDiscardedIngCells=chrComPmAtmDiscardedIngCells, chrComPmAtmTaggedUPC=chrComPmAtmTaggedUPC, chrComPmAtmSuspectedInterval=chrComPmAtmSuspectedInterval)
