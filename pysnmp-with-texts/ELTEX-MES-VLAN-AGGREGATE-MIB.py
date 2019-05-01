#
# PySNMP MIB module ELTEX-MES-VLAN-AGGREGATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-VLAN-AGGREGATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, TimeTicks, IpAddress, Gauge32, NotificationType, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Integer32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Integer32", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
eltMesIpUnnumbered = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7))
eltMesIpUnnumbered.setRevisions(('2014-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesIpUnnumbered.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: eltMesIpUnnumbered.setLastUpdated('201405230000Z')
if mibBuilder.loadTexts: eltMesIpUnnumbered.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesIpUnnumbered.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesIpUnnumbered.setDescription('This private MIB module defines End of Eltex private MIBs.')
eltIpUnnumberedInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1), )
if mibBuilder.loadTexts: eltIpUnnumberedInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedInterfaceTable.setDescription('A table contains ip unnumbered interfaces.')
eltIpUnnumberedInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1), ).setIndexNames((0, "ELTEX-MES-VLAN-AGGREGATE-MIB", "eltIpUnnumberedIfIndex"))
if mibBuilder.loadTexts: eltIpUnnumberedInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedInterfaceEntry.setDescription('The row definition for this table.')
eltIpUnnumberedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpUnnumberedIfIndex.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedIfIndex.setDescription("An index is entrie's sequence. The table contains only one static entry.")
eltIpUnnumberedAggrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltIpUnnumberedAggrIfIndex.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedAggrIfIndex.setDescription("An index is entrie's sequence. The table contains only one static entry.")
eltIpUnnumberedVlan1to1024 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpUnnumberedVlan1to1024.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedVlan1to1024.setDescription('A list of staticaly created vlans from 1 to 1024.')
eltIpUnnumberedVlan1025to2048 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpUnnumberedVlan1025to2048.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedVlan1025to2048.setDescription('A list of staticaly created vlans from 1025 to 2048.')
eltIpUnnumberedVlan2049to3072 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpUnnumberedVlan2049to3072.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedVlan2049to3072.setDescription('A list of staticaly created vlans from 2049 to 3072.')
eltIpUnnumberedVlan3073to4094 = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIpUnnumberedVlan3073to4094.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedVlan3073to4094.setDescription('A list of staticaly created vlans from 3073 to 4094.')
eltIpUnnumberedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltIpUnnumberedStatus.setStatus('current')
if mibBuilder.loadTexts: eltIpUnnumberedStatus.setDescription('This variable displays the status of the en- try.')
mibBuilder.exportSymbols("ELTEX-MES-VLAN-AGGREGATE-MIB", eltIpUnnumberedInterfaceEntry=eltIpUnnumberedInterfaceEntry, PYSNMP_MODULE_ID=eltMesIpUnnumbered, eltIpUnnumberedVlan1to1024=eltIpUnnumberedVlan1to1024, eltIpUnnumberedIfIndex=eltIpUnnumberedIfIndex, eltIpUnnumberedStatus=eltIpUnnumberedStatus, eltIpUnnumberedVlan2049to3072=eltIpUnnumberedVlan2049to3072, eltIpUnnumberedVlan3073to4094=eltIpUnnumberedVlan3073to4094, eltIpUnnumberedInterfaceTable=eltIpUnnumberedInterfaceTable, eltIpUnnumberedAggrIfIndex=eltIpUnnumberedAggrIfIndex, eltIpUnnumberedVlan1025to2048=eltIpUnnumberedVlan1025to2048, eltMesIpUnnumbered=eltMesIpUnnumbered)
