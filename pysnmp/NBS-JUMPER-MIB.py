#
# PySNMP MIB module NBS-JUMPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-JUMPER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nbs, InterfaceIndex = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbs", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Unsigned32, Gauge32, TimeTicks, Counter64, MibIdentifier, ModuleIdentity, NotificationType, Counter32, Bits, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "TimeTicks", "Counter64", "MibIdentifier", "ModuleIdentity", "NotificationType", "Counter32", "Bits", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsJumperMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 210))
if mibBuilder.loadTexts: nbsJumperMib.setLastUpdated('201007140000Z')
if mibBuilder.loadTexts: nbsJumperMib.setOrganization('NBS')
nbsJumperGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 210, 1))
if mibBuilder.loadTexts: nbsJumperGrp.setStatus('current')
nbsJumperTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 210, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperTableSize.setStatus('current')
nbsJumperTable = MibTable((1, 3, 6, 1, 4, 1, 629, 210, 1, 2), )
if mibBuilder.loadTexts: nbsJumperTable.setStatus('current')
nbsJumperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1), ).setIndexNames((0, "NBS-JUMPER-MIB", "nbsJumperIfIndex"), (0, "NBS-JUMPER-MIB", "nbsJumperIndex"))
if mibBuilder.loadTexts: nbsJumperEntry.setStatus('current')
nbsJumperIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsJumperIfIndex.setStatus('current')
nbsJumperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsJumperIndex.setStatus('current')
nbsJumperPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("off", 2), ("on", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperPosition.setStatus('current')
nbsJumperInterpret = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperInterpret.setStatus('current')
nbsJumperSilkScreen = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperSilkScreen.setStatus('current')
nbsJumperDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperDescription.setStatus('current')
mibBuilder.exportSymbols("NBS-JUMPER-MIB", nbsJumperTable=nbsJumperTable, nbsJumperGrp=nbsJumperGrp, PYSNMP_MODULE_ID=nbsJumperMib, nbsJumperIfIndex=nbsJumperIfIndex, nbsJumperInterpret=nbsJumperInterpret, nbsJumperSilkScreen=nbsJumperSilkScreen, nbsJumperDescription=nbsJumperDescription, nbsJumperPosition=nbsJumperPosition, nbsJumperEntry=nbsJumperEntry, nbsJumperIndex=nbsJumperIndex, nbsJumperTableSize=nbsJumperTableSize, nbsJumperMib=nbsJumperMib)