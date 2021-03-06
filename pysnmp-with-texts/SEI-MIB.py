#
# PySNMP MIB module SEI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SEI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Bits, NotificationType, NotificationType, TimeTicks, enterprises, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Bits", "NotificationType", "NotificationType", "TimeTicks", "enterprises", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MemAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sei = MibIdentifier((1, 3, 6, 1, 4, 1, 175))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1))
suminet = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1))
sumistation = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 2))
sn3500 = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1))
s35Products = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 1))
s35System = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2))
s35Model00 = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 1, 1))
s35Box = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1))
s35Board = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2))
s35BoardIf = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4))
s35BoxFor00 = MibIdentifier((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1))
s35BoxFor00PowerState = MibScalar((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoxFor00PowerState.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoxFor00PowerState.setDescription('')
s35BoxFor00FanState = MibScalar((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("working", 1), ("stopping", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoxFor00FanState.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoxFor00FanState.setDescription('')
s35BoxFor00StationID = MibScalar((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoxFor00StationID.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoxFor00StationID.setDescription('')
s35BoxFor00LedState = MibScalar((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoxFor00LedState.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoxFor00LedState.setDescription('The value is a sum. This value initially takes the value zero, then for each of the configuration policies currently enforced on the node, 2 raised to a power is added to the sum. The power are according to the following table: Policy Power TxBeacon 0 Wrap 1 RingOp 2 SubLan1 3 SubLan2 4 FddiError 5 SubLan1Error 6 SubLan2Error 7 ')
s35BoardNumber = MibScalar((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardNumber.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardNumber.setDescription('')
s35BoardTable = MibTable((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2), )
if mibBuilder.loadTexts: s35BoardTable.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardTable.setDescription('')
s35BoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1), ).setIndexNames((0, "SEI-MIB", "s35BoardIndex"))
if mibBuilder.loadTexts: s35BoardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardEntry.setDescription('')
s35BoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardIndex.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIndex.setDescription('The board number of the board for which this entry containes board information.')
s35BoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fddi-00-512K", 1), ("fddi-00-1M", 2), ("fddi-30-1M", 3), ("ethernet-30p-1M", 4), ("ethernet-noparity", 5), ("ethernet-parity", 6), ("tokenring-4M", 7), ("tokenring-16M", 8), ("v35", 9), ("hsds", 10), ("sn3200-vab", 11), ("accelerator", 12), ("memory-30p-12M", 13), ("fddi-LBR-30", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardType.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardType.setDescription('The type of board.')
s35BoardCpuType = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("nothing", 1), ("mc68000", 2), ("mc68030", 3), ("mc68302", 4), ("mc68010", 5), ("am29200", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardCpuType.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardCpuType.setDescription('')
s35BoardHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardHardwareRevision.setStatus('optional')
if mibBuilder.loadTexts: s35BoardHardwareRevision.setDescription('')
s35BoardLedState = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardLedState.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardLedState.setDescription('')
s35BoardDipInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardDipInformation.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardDipInformation.setDescription('')
s35BoardRomRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardRomRevision.setStatus('optional')
if mibBuilder.loadTexts: s35BoardRomRevision.setDescription('')
s35BoardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardSerialNumber.setStatus('optional')
if mibBuilder.loadTexts: s35BoardSerialNumber.setDescription('')
s35BoardIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIfNumber.setDescription('')
s35BoardIfTable = MibTable((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2), )
if mibBuilder.loadTexts: s35BoardIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIfTable.setDescription('')
s35BoardIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1), ).setIndexNames((0, "SEI-MIB", "s35BoardIfBoardIndex"), (0, "SEI-MIB", "s35BoardIfIndex"))
if mibBuilder.loadTexts: s35BoardIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIfEntry.setDescription('')
s35BoardIfBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardIfBoardIndex.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIfBoardIndex.setDescription('The board number of the board which this entry contains network interface information.')
s35BoardIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIfIndex.setDescription('The value of the instance of the ifIndex object defined in RFC1213, for the instance corresponding to this board.')
s35BoardIfInitialized = MibTableColumn((1, 3, 6, 1, 4, 1, 175, 1, 1, 1, 2, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("initialized", 1), ("uninitialized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s35BoardIfInitialized.setStatus('mandatory')
if mibBuilder.loadTexts: s35BoardIfInitialized.setDescription('')
mibBuilder.exportSymbols("SEI-MIB", s35BoardIfIndex=s35BoardIfIndex, sumistation=sumistation, MacAddress=MacAddress, s35Box=s35Box, s35BoardIndex=s35BoardIndex, s35BoardEntry=s35BoardEntry, s35Model00=s35Model00, s35BoxFor00StationID=s35BoxFor00StationID, MemAddress=MemAddress, s35BoardIfBoardIndex=s35BoardIfBoardIndex, s35BoxFor00LedState=s35BoxFor00LedState, s35BoardIfInitialized=s35BoardIfInitialized, s35Products=s35Products, products=products, s35BoxFor00FanState=s35BoxFor00FanState, s35BoardIfTable=s35BoardIfTable, s35BoardTable=s35BoardTable, s35BoardIfEntry=s35BoardIfEntry, s35BoardIfNumber=s35BoardIfNumber, s35BoardIf=s35BoardIf, s35BoardSerialNumber=s35BoardSerialNumber, s35BoardLedState=s35BoardLedState, s35Board=s35Board, s35BoardNumber=s35BoardNumber, suminet=suminet, s35BoxFor00=s35BoxFor00, s35BoxFor00PowerState=s35BoxFor00PowerState, sei=sei, s35BoardDipInformation=s35BoardDipInformation, s35BoardCpuType=s35BoardCpuType, s35BoardRomRevision=s35BoardRomRevision, s35BoardHardwareRevision=s35BoardHardwareRevision, sn3500=sn3500, s35BoardType=s35BoardType, s35System=s35System)
