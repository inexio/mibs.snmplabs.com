#
# PySNMP MIB module ENTERASYS-NETFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-NETFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ObjectIdentity, Counter32, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Integer32, TimeTicks, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Counter32", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Integer32", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysNetflowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61))
etsysNetflowMIB.setRevisions(('2007-02-07 19:49', '2006-03-22 21:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysNetflowMIB.setRevisionsDescriptions(('Clarify that the translation provided by this MIB is only applicable to NetFlow Version 5 export frames.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysNetflowMIB.setLastUpdated('200702071949Z')
if mibBuilder.loadTexts: etsysNetflowMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: etsysNetflowMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysNetflowMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID pertaining to configuration of Netflow on a device.')
etsysNetflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1))
etsysNetflowInterfaceMap = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1))
etsysNetflowExportIntfMapTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1), )
if mibBuilder.loadTexts: etsysNetflowExportIntfMapTable.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowExportIntfMapTable.setDescription('A table of mappings from the Netflow version 5 export record interfaces to MIB-II ifIndex.')
etsysNetflowExportIntfMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-NETFLOW-MIB", "etsysNetflowExportIntf"))
if mibBuilder.loadTexts: etsysNetflowExportIntfMapEntry.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowExportIntfMapEntry.setDescription('An entry containing per interface mapping of Netflow version 5 export record interfaces to MIB-II ifIndex.')
etsysNetflowExportIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: etsysNetflowExportIntf.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowExportIntf.setDescription('The interface number used in the 16 bit interface fields of Netflow version 5 export records.')
etsysNetflowIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysNetflowIfIndex.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowIfIndex.setDescription('The MIB-II ifIndex of the interface bound to etsysNetflowExportIntf.')
etsysNetflowIfIndexMapTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2), )
if mibBuilder.loadTexts: etsysNetflowIfIndexMapTable.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowIfIndexMapTable.setDescription('A table of mappings from MIB-II ifIndex to Netflow export record interfaces.')
etsysNetflowIfIndexMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysNetflowIfIndexMapEntry.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowIfIndexMapEntry.setDescription('An entry containing per interface mapping of MIB-II ifIndex to Netflow version 5 export record interfaces.')
etsysNetflowExportInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysNetflowExportInterface.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowExportInterface.setDescription('The 16 bit interface number used in the interface fields of Netflow version 5 export records that is bound to the specified ifIndex.')
etsysNetflowConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2))
etsysNetflowGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 1))
etsysNetflowCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 2))
etsysNetflowIntfMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 1, 1)).setObjects(("ENTERASYS-NETFLOW-MIB", "etsysNetflowExportIntf"), ("ENTERASYS-NETFLOW-MIB", "etsysNetflowIfIndex"), ("ENTERASYS-NETFLOW-MIB", "etsysNetflowExportInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysNetflowIntfMapGroup = etsysNetflowIntfMapGroup.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowIntfMapGroup.setDescription('The interface mapping group for all devices supporting Netflow version 5 export records.')
etsysNetflowIntfMapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 2, 1)).setObjects(("ENTERASYS-NETFLOW-MIB", "etsysNetflowIntfMapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysNetflowIntfMapCompliance = etsysNetflowIntfMapCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysNetflowIntfMapCompliance.setDescription('The compliance statement for devices that support Netflow.')
mibBuilder.exportSymbols("ENTERASYS-NETFLOW-MIB", etsysNetflowIfIndexMapTable=etsysNetflowIfIndexMapTable, etsysNetflowObjects=etsysNetflowObjects, PYSNMP_MODULE_ID=etsysNetflowMIB, etsysNetflowInterfaceMap=etsysNetflowInterfaceMap, etsysNetflowIfIndexMapEntry=etsysNetflowIfIndexMapEntry, etsysNetflowGroups=etsysNetflowGroups, etsysNetflowExportInterface=etsysNetflowExportInterface, etsysNetflowConformance=etsysNetflowConformance, etsysNetflowExportIntfMapTable=etsysNetflowExportIntfMapTable, etsysNetflowIntfMapCompliance=etsysNetflowIntfMapCompliance, etsysNetflowExportIntf=etsysNetflowExportIntf, etsysNetflowCompliances=etsysNetflowCompliances, etsysNetflowIntfMapGroup=etsysNetflowIntfMapGroup, etsysNetflowExportIntfMapEntry=etsysNetflowExportIntfMapEntry, etsysNetflowIfIndex=etsysNetflowIfIndex, etsysNetflowMIB=etsysNetflowMIB)
