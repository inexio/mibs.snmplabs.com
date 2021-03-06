#
# PySNMP MIB module CISCO-SERVICE-CONTROL-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SERVICE-CONTROL-LINK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:11:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
PhysicalIndex, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, iso, ModuleIdentity, Unsigned32, Counter32, MibIdentifier, Counter64, IpAddress, Gauge32, ObjectIdentity, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoServiceControlLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 631))
ciscoServiceControlLinkMIB.setRevisions(('2007-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setLastUpdated('200706260000Z')
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-excelsior-dev@cisco.com')
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setDescription('This MIB module provides information about the status and configuration of links used by service control entities. The link on a service control entity is a contained entity that joins subscriber side port(s) to network side port(s).')
ciscoSCLinkMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 0))
ciscoSCLinkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 1))
ciscoSCLinkMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2))
class CsceLinkModeType(TextualConvention, Integer32):
    description = "An enumerated value which identifies the various modes of a link. 'other' None of the following. 'bypass' The traffic is forwarded from one port to the other using an internal splitter. 'forwarding' The traffic is forwarded through the internal hardware and software modules of the system. 'cutoff' The traffic is dropped by the system. 'sniffing' The traffic is passed in the same manner as in 'bypass' mode, however a copy of the traffic is made and analyzed internally in the box."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("bypass", 2), ("forwarding", 3), ("cutoff", 4), ("sniffing", 5))

cscLinkNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkNotifsEnabled.setStatus('current')
if mibBuilder.loadTexts: cscLinkNotifsEnabled.setDescription("This object controls whether the cServiceLinkModeChange notification is generated. A 'false' value will prevent notifications from being generated.")
cscLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2), )
if mibBuilder.loadTexts: cscLinkStatusTable.setStatus('current')
if mibBuilder.loadTexts: cscLinkStatusTable.setDescription("This table provides information regarding the configuration and status of the links that pass through the service control entity and carry inband traffic. The link is an entity and has an entry in the entPhysicalTable of the ENTITY-MIB with entPhysicalClass of 'other' and is contained in entity 'chassis' or 'module'. A link entity contains entities from the entPhysicalTable of entPhysicalClass 'port'. The number of entries in this table is determined by the number of service control entities in the entPhysicalTable and the number of links supported by each. Each Link entity contains at least a subscriber side port entity and a network side port entity.")
cscLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cscLinkStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cscLinkStatusEntry.setDescription("An entry (conceptual row) in the cscLinkStatusTable created by the agent for every link entity contained in the service control entity after initilization. entPhysicalIndex is index for this table which represents entities of 'other' entPhysicalClass.")
cscLinkAdminModeOnActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 1), CsceLinkModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminModeOnActive.setStatus('current')
if mibBuilder.loadTexts: cscLinkAdminModeOnActive.setDescription('This object indicates the desired mode of the link when the entity that contains this link has the operating status of active and the entity is not in boot or failure state.')
cscLinkAdminModeOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 2), CsceLinkModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminModeOnFailure.setStatus('current')
if mibBuilder.loadTexts: cscLinkAdminModeOnFailure.setDescription('This object indicates the desired mode of the link when the entity that contains this link has the operational status of failure.')
cscLinkOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 3), CsceLinkModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkOperMode.setStatus('current')
if mibBuilder.loadTexts: cscLinkOperMode.setDescription('This object reflects the operational mode of the link.')
cscLinkAdminReflectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reflectionEnabled", 1), ("reflectionOnAllPortsEnabled", 2), ("reflectionDisabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminReflectionEnable.setStatus('current')
if mibBuilder.loadTexts: cscLinkAdminReflectionEnable.setDescription("This object indicates how the failure status of the physical link on one port should be reflected to the other port(s) of the link. 'reflectionEnabled' : Failure is reflected on the other port of the link. 'reflectionOnAllPortsEnabled': Failure of Physical Link is reflected on all other ports on all links. 'reflectionDisabled' : Port status is not reflected on the link.")
cscLinkSubscriberSidePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 5), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkSubscriberSidePortIndex.setStatus('current')
if mibBuilder.loadTexts: cscLinkSubscriberSidePortIndex.setDescription('This object specifies the entPhysicalIndex value that uniquely identifies the port entity contained in this link entity in the entPhysicalTable. This port entity is connected to the subscriber side.')
cscLinkNetworkSidePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 6), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkNetworkSidePortIndex.setStatus('current')
if mibBuilder.loadTexts: cscLinkNetworkSidePortIndex.setDescription('This object specifies the entPhysicalIndex value that uniquely identifies the port entity contained in this link entity in the entPhysicalTable. This port entity is connected to the network side.')
cscLinkAdminReflectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noLinkReflection", 1), ("reflectingFailureToNetwork", 2), ("reflectingFailureToSubscriber", 3), ("reflectingFailureToBoth", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminReflectionState.setStatus('current')
if mibBuilder.loadTexts: cscLinkAdminReflectionState.setDescription("This object indicates how the link propagates the failure state between the ports on each end of the link. 'noLinkReflection' : No failure is currently being reflected. 'reflectingFailureToNetwork' : Link failure on subscriber side is reflected to the network side. 'reflectingFailureToSubscriber': Link failure on network side is reflected to the subscriber side. 'reflectingFailureToBoth' : Failure reflected to both sides of the link.")
ciscoServiceControlLinkModeChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 631, 0, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"))
if mibBuilder.loadTexts: ciscoServiceControlLinkModeChange.setStatus('current')
if mibBuilder.loadTexts: ciscoServiceControlLinkModeChange.setDescription('This notification signifies that the agent entity has detected that the cscLinkOperMode object in this MIB has changed.')
ciscoSCLinkMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1))
ciscoSCLinkMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2))
cServiceLinkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkMIBObjectGroup"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkMIBNotificationGroup"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceLinkMIBCompliance = cServiceLinkMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cServiceLinkMIBCompliance.setDescription('The compliance statement for SNMP Agents which implement this MIB.')
cSCLinkMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnActive"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnFailure"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionEnable"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkSubscriberSidePortIndex"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNetworkSidePortIndex"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkMIBObjectGroup = cSCLinkMIBObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cSCLinkMIBObjectGroup.setDescription('Collection of objects for link status.')
cSCLinkMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 2)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "ciscoServiceControlLinkModeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkMIBNotificationGroup = cSCLinkMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cSCLinkMIBNotificationGroup.setDescription('This group contains notifications of this MIB.')
cSCLinkNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 3)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkNotifControlGroup = cSCLinkNotifControlGroup.setStatus('current')
if mibBuilder.loadTexts: cSCLinkNotifControlGroup.setDescription('This is a collection of objects that controls the enable/disable of notifications defined in this MIB.')
mibBuilder.exportSymbols("CISCO-SERVICE-CONTROL-LINK-MIB", cSCLinkMIBNotificationGroup=cSCLinkMIBNotificationGroup, ciscoServiceControlLinkMIB=ciscoServiceControlLinkMIB, ciscoServiceControlLinkModeChange=ciscoServiceControlLinkModeChange, cscLinkAdminReflectionState=cscLinkAdminReflectionState, cscLinkNetworkSidePortIndex=cscLinkNetworkSidePortIndex, cServiceLinkMIBCompliance=cServiceLinkMIBCompliance, cSCLinkNotifControlGroup=cSCLinkNotifControlGroup, ciscoSCLinkMIBNotifs=ciscoSCLinkMIBNotifs, cscLinkSubscriberSidePortIndex=cscLinkSubscriberSidePortIndex, ciscoSCLinkMIBCompliances=ciscoSCLinkMIBCompliances, cSCLinkMIBObjectGroup=cSCLinkMIBObjectGroup, cscLinkNotifsEnabled=cscLinkNotifsEnabled, cscLinkAdminReflectionEnable=cscLinkAdminReflectionEnable, ciscoSCLinkMIBObjectGroups=ciscoSCLinkMIBObjectGroups, cscLinkStatusEntry=cscLinkStatusEntry, cscLinkOperMode=cscLinkOperMode, CsceLinkModeType=CsceLinkModeType, ciscoSCLinkMIBObjects=ciscoSCLinkMIBObjects, cscLinkStatusTable=cscLinkStatusTable, ciscoSCLinkMIBConform=ciscoSCLinkMIBConform, cscLinkAdminModeOnFailure=cscLinkAdminModeOnFailure, PYSNMP_MODULE_ID=ciscoServiceControlLinkMIB, cscLinkAdminModeOnActive=cscLinkAdminModeOnActive)
