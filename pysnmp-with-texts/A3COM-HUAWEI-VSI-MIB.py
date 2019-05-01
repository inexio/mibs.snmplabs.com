#
# PySNMP MIB module A3COM-HUAWEI-VSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VSI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Bits, ModuleIdentity, Unsigned32, Counter32, Integer32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Bits", "ModuleIdentity", "Unsigned32", "Counter32", "Integer32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "iso", "NotificationType")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
h3cVsi = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105))
h3cVsi.setRevisions(('2009-08-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cVsi.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: h3cVsi.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: h3cVsi.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: h3cVsi.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3cVsi.setDescription('The MIB for VSI (Virtual Switch Instance).')
h3cVsiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1))
h3cVsiScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 1))
h3cVsiNextAvailableVsiIndex = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVsiNextAvailableVsiIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVsiNextAvailableVsiIndex.setDescription('Next available VSI entry index for creating VSI. Its value ranges from 0x1 to 0xFFFFFFFF.The invalid value 0xFFFFFFFF indicates that no VSI entry can be created.')
h3cVsiTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2), )
if mibBuilder.loadTexts: h3cVsiTable.setStatus('current')
if mibBuilder.loadTexts: h3cVsiTable.setDescription('A table for configuring VSI parameters.')
h3cVsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"))
if mibBuilder.loadTexts: h3cVsiEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVsiEntry.setDescription('An entry for configuring VSI parameters.')
h3cVsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cVsiIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVsiIndex.setDescription('Index of VSI. Its value ranges from 0x1 to 0xFFFFFFFE.')
h3cVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiName.setStatus('current')
if mibBuilder.loadTexts: h3cVsiName.setDescription('Name of VSI. Max string length of VSI name is 31.')
h3cVsiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("martini", 1), ("minm", 2), ("martiniAndMinm", 3), ("kompella", 4), ("kompellaAndMinm", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiMode.setStatus('current')
if mibBuilder.loadTexts: h3cVsiMode.setDescription('Mode of VSI. Martini mode indicated this VSI support VPLS service signalled using LDP, kompella indicated this VSI support VPLS service signalled using BGP, minm indicated this VSI support MAC-in-MAC service.')
h3cMinmIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMinmIsid.setStatus('current')
if mibBuilder.loadTexts: h3cMinmIsid.setDescription('The MAC-in-MAC I-SID of VSI in minm or martiniAndMinm mode. It must be different for every VSI. Its value ranges from 0x1 to 0xFFFFFF. In other VSI mode, its value is invalid value 0x0.')
h3cVsiId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiId.setStatus('current')
if mibBuilder.loadTexts: h3cVsiId.setDescription("Identifier of VSI in martini or martiniAndMinm mode, by default, it's the PW ID of this VSI. Its value ranges from 1 to 4294967295. In other VSI mode, its value is invalid value 0.")
h3cVsiTransMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiTransMode.setStatus('current')
if mibBuilder.loadTexts: h3cVsiTransMode.setDescription('Transit Mode of VSI.')
h3cVsiEnableHubSpoke = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiEnableHubSpoke.setStatus('current')
if mibBuilder.loadTexts: h3cVsiEnableHubSpoke.setDescription('Config HubSpoke property of this VSI.')
h3cVsiAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adminUp", 1), ("adminDown", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiAdminState.setStatus('current')
if mibBuilder.loadTexts: h3cVsiAdminState.setDescription('Set VSI admin state as adminUp or adminDown.')
h3cVsiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVsiRowStatus.setDescription('Operation status of this table entry.')
h3cVsiXconnectTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3), )
if mibBuilder.loadTexts: h3cVsiXconnectTable.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectTable.setDescription('A table for configuring xconnect parameters.')
h3cVsiXconnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiXconnectIfIndex"), (0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiXconnectEvcSrvInstId"))
if mibBuilder.loadTexts: h3cVsiXconnectEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectEntry.setDescription('An entry for configuring xconnect parameters. Each entry means connecting a service instance of a interface to a VSI.')
h3cVsiXconnectIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cVsiXconnectIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectIfIndex.setDescription('Index of the interface associated with the VSI.')
h3cVsiXconnectEvcSrvInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: h3cVsiXconnectEvcSrvInstId.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectEvcSrvInstId.setDescription('Index of the service instance associated with the VSI.')
h3cVsiXconnectVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiXconnectVsiName.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectVsiName.setDescription('Name of VSI. Max string length of VSI name is 31.')
h3cVsiXconnectAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiXconnectAccessMode.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectAccessMode.setDescription('Access mode of this service instance.')
h3cVsiXconnectHubSpoke = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("hub", 2), ("spoke", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiXconnectHubSpoke.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectHubSpoke.setDescription('Config HubSpoke property of this service instance.')
h3cVsiXconnectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 105, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVsiXconnectRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVsiXconnectRowStatus.setDescription('Operation status of this table entry.')
mibBuilder.exportSymbols("A3COM-HUAWEI-VSI-MIB", h3cVsiIndex=h3cVsiIndex, h3cVsiXconnectEntry=h3cVsiXconnectEntry, h3cVsiId=h3cVsiId, h3cVsiXconnectIfIndex=h3cVsiXconnectIfIndex, h3cVsiXconnectVsiName=h3cVsiXconnectVsiName, h3cVsiTable=h3cVsiTable, h3cVsiXconnectEvcSrvInstId=h3cVsiXconnectEvcSrvInstId, h3cVsiName=h3cVsiName, h3cVsiXconnectAccessMode=h3cVsiXconnectAccessMode, h3cVsiAdminState=h3cVsiAdminState, h3cVsiMode=h3cVsiMode, PYSNMP_MODULE_ID=h3cVsi, h3cVsiRowStatus=h3cVsiRowStatus, h3cVsiEntry=h3cVsiEntry, h3cVsiScalarGroup=h3cVsiScalarGroup, h3cMinmIsid=h3cMinmIsid, h3cVsiXconnectRowStatus=h3cVsiXconnectRowStatus, h3cVsiEnableHubSpoke=h3cVsiEnableHubSpoke, h3cVsiXconnectTable=h3cVsiXconnectTable, h3cVsiNextAvailableVsiIndex=h3cVsiNextAvailableVsiIndex, h3cVsiXconnectHubSpoke=h3cVsiXconnectHubSpoke, h3cVsiObjects=h3cVsiObjects, h3cVsiTransMode=h3cVsiTransMode, h3cVsi=h3cVsi)
