#
# PySNMP MIB module HPICF-SAVI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPICF-SAVI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hpSwitchExperimental, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitchExperimental")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetVersion, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetVersion", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, TimeTicks, iso, ModuleIdentity, Gauge32, Counter32, MibIdentifier, Bits, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "TimeTicks", "iso", "ModuleIdentity", "Gauge32", "Counter32", "MibIdentifier", "Bits", "Unsigned32", "Counter64")
RowStatus, TextualConvention, TimeInterval, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeInterval", "MacAddress", "DisplayString")
hpicfSaviMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1))
hpicfSaviMIB.setRevisions(('2017-11-08 00:00',))
if mibBuilder.loadTexts: hpicfSaviMIB.setLastUpdated('201711080000Z')
if mibBuilder.loadTexts: hpicfSaviMIB.setOrganization('HP Networking')
hpicfSaviObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1))
hpicfSaviObjectsPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfSaviObjectsPortTable.setStatus('current')
hpicfSaviObjectsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1), ).setIndexNames((0, "HPICF-SAVI-MIB", "hpicfSaviObjectsPortIPVersion"), (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsPortIfIndex"))
if mibBuilder.loadTexts: hpicfSaviObjectsPortEntry.setStatus('current')
hpicfSaviObjectsPortIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 1), InetVersion())
if mibBuilder.loadTexts: hpicfSaviObjectsPortIPVersion.setStatus('current')
hpicfSaviObjectsPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: hpicfSaviObjectsPortIfIndex.setStatus('current')
hpicfSaviObjPortDhcpTrustAttr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSaviObjPortDhcpTrustAttr.setStatus('current')
hpicfSaviObjectsPortFilteringNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSaviObjectsPortFilteringNum.setStatus('current')
hpicfSaviObjectsBindingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfSaviObjectsBindingTable.setStatus('current')
hpicfSaviObjectsBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1), ).setIndexNames((0, "HPICF-SAVI-MIB", "hpicfSaviObjBindingIpAddrType"), (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsBindingType"), (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsBindingIfIndex"), (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsBindingIpAddress"))
if mibBuilder.loadTexts: hpicfSaviObjectsBindingEntry.setStatus('current')
hpicfSaviObjBindingIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfSaviObjBindingIpAddrType.setStatus('current')
hpicfSaviObjectsBindingType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("manual", 1), ("slaac", 2), ("dhcp", 3), ("send", 4))))
if mibBuilder.loadTexts: hpicfSaviObjectsBindingType.setStatus('current')
hpicfSaviObjectsBindingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: hpicfSaviObjectsBindingIfIndex.setStatus('current')
hpicfSaviObjectsBindingIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 4), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: hpicfSaviObjectsBindingIpAddress.setStatus('current')
hpicfSaviObjectsBindingMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSaviObjectsBindingMacAddr.setStatus('current')
hpicfSaviObjectsBindingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSaviObjectsBindingLifetime.setStatus('current')
hpicfSaviObjectsBindingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSaviObjectsBindingRowStatus.setStatus('current')
hpicfSaviObjectsFilteringTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfSaviObjectsFilteringTable.setStatus('current')
hpicfSaviObjectsFilteringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1), ).setIndexNames((0, "HPICF-SAVI-MIB", "hpicfSaviObjFilteringIpAddrType"), (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsFilteringIfIndex"), (0, "HPICF-SAVI-MIB", "hpicfSaviObjFilteringIpAddr"))
if mibBuilder.loadTexts: hpicfSaviObjectsFilteringEntry.setStatus('current')
hpicfSaviObjFilteringIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfSaviObjFilteringIpAddrType.setStatus('current')
hpicfSaviObjectsFilteringIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: hpicfSaviObjectsFilteringIfIndex.setStatus('current')
hpicfSaviObjFilteringIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: hpicfSaviObjFilteringIpAddr.setStatus('current')
hpicfSaviObjectsFilteringMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSaviObjectsFilteringMacAddr.setStatus('current')
hpicfSaviConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2))
hpicfSaviCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 1))
hpicfSaviCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 1, 1)).setObjects(("HPICF-SAVI-MIB", "hpicfSaviportGroup"), ("HPICF-SAVI-MIB", "hpicfSavibindingGroup"), ("HPICF-SAVI-MIB", "hpicfSavifilteringGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSaviCompliance = hpicfSaviCompliance.setStatus('current')
hpicfSaviGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2))
hpicfSaviportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2, 1)).setObjects(("HPICF-SAVI-MIB", "hpicfSaviObjPortDhcpTrustAttr"), ("HPICF-SAVI-MIB", "hpicfSaviObjectsPortFilteringNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSaviportGroup = hpicfSaviportGroup.setStatus('current')
hpicfSavibindingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2, 2)).setObjects(("HPICF-SAVI-MIB", "hpicfSaviObjectsBindingMacAddr"), ("HPICF-SAVI-MIB", "hpicfSaviObjectsBindingLifetime"), ("HPICF-SAVI-MIB", "hpicfSaviObjectsBindingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavibindingGroup = hpicfSavibindingGroup.setStatus('current')
hpicfSavifilteringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2, 3)).setObjects(("HPICF-SAVI-MIB", "hpicfSaviObjectsFilteringMacAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSavifilteringGroup = hpicfSavifilteringGroup.setStatus('current')
mibBuilder.exportSymbols("HPICF-SAVI-MIB", hpicfSaviObjectsBindingLifetime=hpicfSaviObjectsBindingLifetime, hpicfSaviObjectsFilteringIfIndex=hpicfSaviObjectsFilteringIfIndex, hpicfSaviObjectsPortIPVersion=hpicfSaviObjectsPortIPVersion, hpicfSaviObjectsFilteringEntry=hpicfSaviObjectsFilteringEntry, hpicfSaviObjectsPortFilteringNum=hpicfSaviObjectsPortFilteringNum, hpicfSaviObjectsPortTable=hpicfSaviObjectsPortTable, hpicfSaviObjectsBindingRowStatus=hpicfSaviObjectsBindingRowStatus, hpicfSaviObjects=hpicfSaviObjects, hpicfSaviObjFilteringIpAddrType=hpicfSaviObjFilteringIpAddrType, hpicfSaviObjectsBindingMacAddr=hpicfSaviObjectsBindingMacAddr, hpicfSaviObjectsPortIfIndex=hpicfSaviObjectsPortIfIndex, hpicfSaviObjFilteringIpAddr=hpicfSaviObjFilteringIpAddr, hpicfSaviObjectsBindingIpAddress=hpicfSaviObjectsBindingIpAddress, hpicfSaviportGroup=hpicfSaviportGroup, hpicfSaviObjectsFilteringMacAddr=hpicfSaviObjectsFilteringMacAddr, hpicfSaviObjectsBindingIfIndex=hpicfSaviObjectsBindingIfIndex, hpicfSavibindingGroup=hpicfSavibindingGroup, hpicfSaviObjPortDhcpTrustAttr=hpicfSaviObjPortDhcpTrustAttr, hpicfSaviObjectsBindingTable=hpicfSaviObjectsBindingTable, hpicfSavifilteringGroup=hpicfSavifilteringGroup, hpicfSaviObjBindingIpAddrType=hpicfSaviObjBindingIpAddrType, hpicfSaviCompliance=hpicfSaviCompliance, hpicfSaviConformance=hpicfSaviConformance, hpicfSaviObjectsBindingEntry=hpicfSaviObjectsBindingEntry, PYSNMP_MODULE_ID=hpicfSaviMIB, hpicfSaviObjectsBindingType=hpicfSaviObjectsBindingType, hpicfSaviCompliances=hpicfSaviCompliances, hpicfSaviGroups=hpicfSaviGroups, hpicfSaviObjectsPortEntry=hpicfSaviObjectsPortEntry, hpicfSaviObjectsFilteringTable=hpicfSaviObjectsFilteringTable, hpicfSaviMIB=hpicfSaviMIB)
