#
# PySNMP MIB module CISCO-GGSN-GEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GGSN-GEO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:59:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Bits, NotificationType, iso, Counter32, Counter64, ModuleIdentity, TimeTicks, Unsigned32, Integer32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "NotificationType", "iso", "Counter32", "Counter64", "ModuleIdentity", "TimeTicks", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
cggsnGeoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 724))
cggsnGeoMIB.setRevisions(('2010-02-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cggsnGeoMIB.setRevisionsDescriptions(('Initial version of the MIB module.',))
if mibBuilder.loadTexts: cggsnGeoMIB.setLastUpdated('201002190000Z')
if mibBuilder.loadTexts: cggsnGeoMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cggsnGeoMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cggsnGeoMIB.setDescription('This MIB provide additional information for passive interface configured for each OSPF process, independent of object creation in the corresponding OSPF MIB.')
cggsnGeoPassiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 724, 1), )
if mibBuilder.loadTexts: cggsnGeoPassiveTable.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoPassiveTable.setDescription('This table contains information about passive interfaces configured in each OSPF process. Further this table provides information about passive interfaces either enabled(active) or in standby mode.')
cggsnGeoPassiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-GGSN-GEO-MIB", "cggsnGeoProcessNumber"))
if mibBuilder.loadTexts: cggsnGeoPassiveEntry.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoPassiveEntry.setDescription('An entry is created or removed whenever a interface related configuation operation is performed under the OSPF process. For Example : Ethernet1/0 interface has ifIndex value as 5. The ifIndex of 5 is a passive interface of particular OSPF process which copies the name of the particular interface to this object . Based on this example Ethernet1/0 is going copy to the object. Otherwise ifIndex is not a passive interface this object content will be NULL.')
cggsnGeoProcessNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cggsnGeoProcessNumber.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoProcessNumber.setDescription('Specifies the process identifier for each OSPF configured interface')
cggsnGeoPassiveStdbyIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveStdbyIfName.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoPassiveStdbyIfName.setDescription('This variable specfies name of the passive interface configured')
cggsnGeoPassiveIfOnStdby = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveIfOnStdby.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoPassiveIfOnStdby.setDescription("This object indicates whether the passive interface is configured in standby mode or not. The value of this object 'true' indicates, the standby mode is configured, otherwise the standby mode is not configured.")
cggsnGeoVRFEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cggsnGeoVRFEnabled.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoVRFEnabled.setDescription("This object indicates whether the Current OSPF process is bonded with VRF name of the router or not. The value of this object 'true' indicates OSPF process is bonded with VRF name of the router, otherwise the OSPF process is not bonded with VRF name of router.")
cggsnGeoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoRowStatus.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoRowStatus.setDescription("This object is used to manage creation and deletion of rows in this table. Objects in this row cannot be modified when this entry is 'active'.")
cggsnGeoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2))
cggsnGeogroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1))
cggsnGeoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2))
cggsnGeoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoCompliance = cggsnGeoCompliance.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoCompliance.setDescription('The Compilance Stament for the agent they support CISCO-GGSN-GEO-MIB')
cggsnGeoPassiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveStdbyIfName"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveIfOnStdby"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoVRFEnabled"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoPassiveGroup = cggsnGeoPassiveGroup.setStatus('current')
if mibBuilder.loadTexts: cggsnGeoPassiveGroup.setDescription('These objects are used to provide information about passive standby interface configuration in OSPF interface')
mibBuilder.exportSymbols("CISCO-GGSN-GEO-MIB", cggsnGeoProcessNumber=cggsnGeoProcessNumber, PYSNMP_MODULE_ID=cggsnGeoMIB, cggsnGeoMIB=cggsnGeoMIB, cggsnGeoVRFEnabled=cggsnGeoVRFEnabled, cggsnGeoRowStatus=cggsnGeoRowStatus, cggsnGeoConformance=cggsnGeoConformance, cggsnGeoCompliances=cggsnGeoCompliances, cggsnGeoCompliance=cggsnGeoCompliance, cggsnGeoPassiveGroup=cggsnGeoPassiveGroup, cggsnGeogroups=cggsnGeogroups, cggsnGeoPassiveEntry=cggsnGeoPassiveEntry, cggsnGeoPassiveIfOnStdby=cggsnGeoPassiveIfOnStdby, cggsnGeoPassiveStdbyIfName=cggsnGeoPassiveStdbyIfName, cggsnGeoPassiveTable=cggsnGeoPassiveTable)
