#
# PySNMP MIB module CISCO-SWITCH-NETFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-NETFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalDescr = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalDescr")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, Counter32, TimeTicks, iso, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "TimeTicks", "iso", "Unsigned32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSwitchNetflowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 737))
ciscoSwitchNetflowMIB.setRevisions(('2010-05-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchNetflowMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchNetflowMIB.setLastUpdated('201005260000Z')
if mibBuilder.loadTexts: ciscoSwitchNetflowMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchNetflowMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchNetflowMIB.setDescription('This MIB module defines management objects for the Netflow features on Cisco Layer 2 and Layer 3 devices.')
ciscoSwitchNetflowMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 0))
ciscoSwitchNetflowMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1))
ciscoSwitchNetflowMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 2))
csnAccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1))
csnAccGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 1))
csnAccNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 2))
cshAccUsageThresh = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3))
csnAccUtilization = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4))
csnAccNetflowTableSize = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5))
csnAccSampler = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 6))
class CsnNetflowDirectionTypes(TextualConvention, Integer32):
    description = "Defines the various Netflow direction types. 'none' - no Netflow direction is supported. 'ingress' - Netflow direction is ingress. 'egress' - Netflow direction is egress. 'ingressAndEgress' - Netflow direction is both ingress and egress."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ingress", 2), ("egress", 3), ("ingressAndEgress", 4))

csnNetflowDirectionType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 1, 1), CsnNetflowDirectionTypes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csnNetflowDirectionType.setStatus('current')
if mibBuilder.loadTexts: csnNetflowDirectionType.setDescription('This object specifies the direction type of Netflow enabled on this system.')
csnUsageThreshExceedNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csnUsageThreshExceedNotifEnable.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshExceedNotifEnable.setDescription("This object specifies whether the system produces the csnUsageThreshExceededNotif. A 'false' value will prevent csnUsageThreshExceededNotif notifications from being generated by this system.")
csnUsageThreshTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1), )
if mibBuilder.loadTexts: csnUsageThreshTable.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshTable.setDescription('A table containing Netflow table usage monitoring configuration information.')
csnUsageThreshEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-SWITCH-NETFLOW-MIB", "csnUsageDirection"))
if mibBuilder.loadTexts: csnUsageThreshEntry.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshEntry.setDescription('A conceptual row of csnUsageThreshTable, containing the Netflow table usage monitoring configuration information.')
csnUsageDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1, 1), CsnNetflowDirectionTypes())
if mibBuilder.loadTexts: csnUsageDirection.setStatus('current')
if mibBuilder.loadTexts: csnUsageDirection.setDescription('This object specifies the direction of Netflow on the system.')
csnUsageThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1, 2), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csnUsageThreshold.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshold.setDescription('This object specifies the Netflow table usage threshold in percentage value. When the value of this object is set to zero, Netflow table usage monitoring is disabled. When the value of this object is set to greater than zero, Netflow table usage monitoring is enabled.')
csnUsageInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: csnUsageInterval.setStatus('current')
if mibBuilder.loadTexts: csnUsageInterval.setDescription('This object specifies the interval in seconds over which the Netflow table usage (the value of csnUtilization) will be compared against the threshold specified by csnUsageThreshold.')
csnUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4, 1), )
if mibBuilder.loadTexts: csnUtilizationTable.setStatus('current')
if mibBuilder.loadTexts: csnUtilizationTable.setDescription('A table containing Netflow table utilization information of each switching engine and a Newflow direction type.')
csnUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SWITCH-NETFLOW-MIB", "csnUsageDirection"))
if mibBuilder.loadTexts: csnUtilizationEntry.setStatus('current')
if mibBuilder.loadTexts: csnUtilizationEntry.setDescription('A conceptual row of csnUtilizationTable, containing the Netflow table utilization information for a particular switching engine and a particular Netflow type.')
csnUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4, 1, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csnUtilization.setStatus('current')
if mibBuilder.loadTexts: csnUtilization.setDescription('This object indicates the percentage of Netflow table utilization.')
csnNetflowTableSizeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5, 1), )
if mibBuilder.loadTexts: csnNetflowTableSizeTable.setStatus('current')
if mibBuilder.loadTexts: csnNetflowTableSizeTable.setDescription('A table containing Netflow table size information of each Netflow type supported in the system.')
csnNetflowTableSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-SWITCH-NETFLOW-MIB", "csnUsageDirection"))
if mibBuilder.loadTexts: csnNetflowTableSizeEntry.setStatus('current')
if mibBuilder.loadTexts: csnNetflowTableSizeEntry.setDescription('A conceptual row of csnNetflowTableSizeTable, containing the Netflow table size information for a particular Netflow type.')
csnNetflowTableTotalEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csnNetflowTableTotalEntries.setStatus('current')
if mibBuilder.loadTexts: csnNetflowTableTotalEntries.setDescription('This object indicates the total number of entries in the Netflow table for a particular Netflow direction type.')
csnSamplerTotal = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csnSamplerTotal.setStatus('current')
if mibBuilder.loadTexts: csnSamplerTotal.setDescription('This object indicates the total number of Netflow samplers in the device.')
csnSamplerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csnSamplerAvailable.setStatus('current')
if mibBuilder.loadTexts: csnSamplerAvailable.setDescription('This object indicates the number of Netflow samplers available in the system.')
csnUsageThreshExceededNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 737, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUtilization"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshold"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageInterval"))
if mibBuilder.loadTexts: csnUsageThreshExceededNotif.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshExceededNotif.setDescription('A csnUsageThreshExceededNotif is sent if the Netflow table usage has exceeded the configured threshold specified by csnUsageThreshold.')
csnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 1))
csnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2))
csnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 1, 1)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnGlobalGroup"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshNotifControlGroup"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshGroup"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUtilizationGroup"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshNotifGroup"), ("CISCO-SWITCH-NETFLOW-MIB", "csnNetflowTableSizeGroup"), ("CISCO-SWITCH-NETFLOW-MIB", "csnSamplerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnMIBCompliance = csnMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: csnMIBCompliance.setDescription('The compliance statement for CISCO-SWITCH-NETFLOW-MIB.')
csnGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 1)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnNetflowDirectionType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnGlobalGroup = csnGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: csnGlobalGroup.setDescription('A collection of objects providing global Netflow type configuration.')
csnUsageThreshNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 2)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshExceedNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnUsageThreshNotifControlGroup = csnUsageThreshNotifControlGroup.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshNotifControlGroup.setDescription('A collection of objects providing enabling/disabling of the Netflow table usage threshold notifications.')
csnUsageThreshGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 3)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshold"), ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnUsageThreshGroup = csnUsageThreshGroup.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshGroup.setDescription('A collection of objects providing Netflow table usage threshold information and configuration.')
csnUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 4)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnUtilizationGroup = csnUtilizationGroup.setStatus('current')
if mibBuilder.loadTexts: csnUtilizationGroup.setDescription('A collection of objects providing Netflow utilization information.')
csnUsageThreshNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 5)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshExceededNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnUsageThreshNotifGroup = csnUsageThreshNotifGroup.setStatus('current')
if mibBuilder.loadTexts: csnUsageThreshNotifGroup.setDescription('A collection of notifications providing Netflow table usage threshold exceeded notification.')
csnNetflowTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 6)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnNetflowTableTotalEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnNetflowTableSizeGroup = csnNetflowTableSizeGroup.setStatus('current')
if mibBuilder.loadTexts: csnNetflowTableSizeGroup.setDescription('A collection of objects providing Netflow table size information.')
csnSamplerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 7)).setObjects(("CISCO-SWITCH-NETFLOW-MIB", "csnSamplerTotal"), ("CISCO-SWITCH-NETFLOW-MIB", "csnSamplerAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnSamplerGroup = csnSamplerGroup.setStatus('current')
if mibBuilder.loadTexts: csnSamplerGroup.setDescription('A collection of objects providing Netflow sampler information.')
mibBuilder.exportSymbols("CISCO-SWITCH-NETFLOW-MIB", csnUsageThreshold=csnUsageThreshold, csnSamplerTotal=csnSamplerTotal, ciscoSwitchNetflowMIB=ciscoSwitchNetflowMIB, csnAccSampler=csnAccSampler, csnUsageInterval=csnUsageInterval, csnUtilizationTable=csnUtilizationTable, ciscoSwitchNetflowMIBNotifs=ciscoSwitchNetflowMIBNotifs, csnNetflowTableSizeGroup=csnNetflowTableSizeGroup, csnAccUtilization=csnAccUtilization, csnUtilizationEntry=csnUtilizationEntry, csnUtilizationGroup=csnUtilizationGroup, csnAccounting=csnAccounting, cshAccUsageThresh=cshAccUsageThresh, csnUsageThreshNotifGroup=csnUsageThreshNotifGroup, csnUsageDirection=csnUsageDirection, csnAccNotifControl=csnAccNotifControl, csnUsageThreshTable=csnUsageThreshTable, ciscoSwitchNetflowMIBConform=ciscoSwitchNetflowMIBConform, PYSNMP_MODULE_ID=ciscoSwitchNetflowMIB, ciscoSwitchNetflowMIBObjects=ciscoSwitchNetflowMIBObjects, csnAccNetflowTableSize=csnAccNetflowTableSize, csnNetflowDirectionType=csnNetflowDirectionType, csnNetflowTableSizeTable=csnNetflowTableSizeTable, csnUsageThreshExceededNotif=csnUsageThreshExceededNotif, csnGlobalGroup=csnGlobalGroup, CsnNetflowDirectionTypes=CsnNetflowDirectionTypes, csnUsageThreshExceedNotifEnable=csnUsageThreshExceedNotifEnable, csnNetflowTableSizeEntry=csnNetflowTableSizeEntry, csnMIBCompliances=csnMIBCompliances, csnAccGlobal=csnAccGlobal, csnSamplerGroup=csnSamplerGroup, csnUsageThreshGroup=csnUsageThreshGroup, csnMIBCompliance=csnMIBCompliance, csnUtilization=csnUtilization, csnSamplerAvailable=csnSamplerAvailable, csnMIBGroups=csnMIBGroups, csnUsageThreshNotifControlGroup=csnUsageThreshNotifControlGroup, csnNetflowTableTotalEntries=csnNetflowTableTotalEntries, csnUsageThreshEntry=csnUsageThreshEntry)
