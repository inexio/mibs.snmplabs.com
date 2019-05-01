#
# PySNMP MIB module Wellfleet-HWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-HWF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, Counter64, Bits, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, NotificationType, Integer32, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Counter64", "Bits", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfHwFGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfHwFGroup")
wfHwfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1), )
if mibBuilder.loadTexts: wfHwfTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfTable.setDescription('The following table will contain information about a collection of Hardware Filter (HWF) driver records. Only one HWF driver may be spawned, by the loader, on a given slot. Hence, only the slot number is used as the instance identifier into the table.')
wfHwfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1), ).setIndexNames((0, "Wellfleet-HWF-MIB", "wfHwfSlot"))
if mibBuilder.loadTexts: wfHwfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfEntry.setDescription('Slot number used as instance identifier.')
wfHwfDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHwfDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfDelete.setDescription('Create/delete parameter.')
wfHwfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHwfEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfEnable.setDescription('Enable/disable parameter.')
wfHwfState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfState.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfState.setDescription('Driver state variable.')
wfHwfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfSlot.setDescription('Slot number -- instance ID.')
wfHwfAvailableLines = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfAvailableLines.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfAvailableLines.setDescription('Number of available lines on module.')
wfHwfLineTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2), )
if mibBuilder.loadTexts: wfHwfLineTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineTable.setDescription('The following table will contain information about a collection of Hardware Filter (HWF) line records.')
wfHwfLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1), ).setIndexNames((0, "Wellfleet-HWF-MIB", "wfHwfLineSlot"), (0, "Wellfleet-HWF-MIB", "wfHwfLineNumber"))
if mibBuilder.loadTexts: wfHwfLineEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineEntry.setDescription('Slot number and line number used as instance identifier.')
wfHwfLineState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operational", 1), ("disabled", 2), ("full", 3))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineState.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineState.setDescription('State of filtering hardware on a per line basis.')
wfHwfLineSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineSlot.setDescription('Slot number -- instance ID.')
wfHwfLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineNumber.setDescription('Line number -- instance ID.')
wfHwfLineCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineCct.setDescription('Circuit number associated with a line.')
wfHwfLineCapableMaxTblSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineCapableMaxTblSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineCapableMaxTblSize.setDescription('This attribute specifies the maximum number of table entries capable of being used by a line based upon actual hardware filter devices present and available.')
wfHwfLineCurrentTblSize = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineCurrentTblSize.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineCurrentTblSize.setDescription('Current capacity of the hardware filter table. Hardware filter table resources are dynamically allocated (in increments of 256) on an as-needed basis up to the available table size.')
wfHwfLineCurrentUsedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineCurrentUsedEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineCurrentUsedEntries.setDescription('Number of hardware filter table entries used.')
wfHwfLineDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 6, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHwfLineDroppedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: wfHwfLineDroppedFrames.setDescription('Number of frames dropped because of hardware filter match.')
mibBuilder.exportSymbols("Wellfleet-HWF-MIB", wfHwfLineState=wfHwfLineState, wfHwfLineEntry=wfHwfLineEntry, wfHwfEnable=wfHwfEnable, wfHwfLineSlot=wfHwfLineSlot, wfHwfLineNumber=wfHwfLineNumber, wfHwfLineCurrentTblSize=wfHwfLineCurrentTblSize, wfHwfTable=wfHwfTable, wfHwfDelete=wfHwfDelete, wfHwfAvailableLines=wfHwfAvailableLines, wfHwfLineDroppedFrames=wfHwfLineDroppedFrames, wfHwfSlot=wfHwfSlot, wfHwfLineCct=wfHwfLineCct, wfHwfEntry=wfHwfEntry, wfHwfLineCapableMaxTblSize=wfHwfLineCapableMaxTblSize, wfHwfLineTable=wfHwfLineTable, wfHwfState=wfHwfState, wfHwfLineCurrentUsedEntries=wfHwfLineCurrentUsedEntries)
