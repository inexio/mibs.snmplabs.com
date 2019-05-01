#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-REG
# Produced by pysmi-0.3.4 at Wed May  1 13:54:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Integer32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, enterprises, NotificationType, Unsigned32, IpAddress, TimeTicks, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "enterprises", "NotificationType", "Unsigned32", "IpAddress", "TimeTicks", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
multiFlexServerRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 1))
multiFlexServerRegModule.setRevisions(('2007-10-01 18:20', '2007-08-21 17:00', '2007-08-16 13:30', '2007-05-30 10:30', '2007-03-06 10:30', '2007-02-22 17:00', '2006-11-29 15:30', '2006-11-01 10:00', '2006-10-02 12:00', '2006-09-28 17:32',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: multiFlexServerRegModule.setRevisionsDescriptions(('Removed remaining references to OEMs', 'Renamed eventPolicyId to eventId', 'Reordered Revision to reverse chronological as some browsers choke, cleaned up some other simple nit-picky errors Added eventPolicyId to the notification group', 'Moved components to { multiFlexServer 2 } Added notificationInfo for bogus nodes used in event notification', "Dumped several nodes that really aren't relevant or going to be used: generic profiles requirements (experiments has been moved) conformance compliance", 'Renamed MIB file and updated internal relevance to formal product name Multi-Flex Server', 'Added regChassis & regControllers. Renumbered registry to put less likely 3rd party supplied components toward the end. Added three known new components to registry (multiFlexServer1, esm1 and scm1 which should be renamed later).', "Made several changes: old 'chassis' is now 'modularsystems' removed 'typeOfchassis' (thus entire tree moved up)", 'Moved mib, conformance, groups, & compliance definitions here. Heavily cleaned up module definitions.', "Removed code-name references and 'global prefixing.' Changed smb to typeOfChassis.",))
if mibBuilder.loadTexts: multiFlexServerRegModule.setLastUpdated('200710011820Z')
if mibBuilder.loadTexts: multiFlexServerRegModule.setOrganization('Intel Corporation')
if mibBuilder.loadTexts: multiFlexServerRegModule.setContactInfo('Brian Kurle Intel Corporation JF5-2-C3 Tel: 503-712-5032 E-Mail: brianx.j.kurle@intel.com')
if mibBuilder.loadTexts: multiFlexServerRegModule.setDescription('Registry module definitions for entire Multi-Flex Server MIB system')
intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2))
modularsystems = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19))
multiFlexServer = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1))
notifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 0))
if mibBuilder.loadTexts: notifications.setStatus('current')
if mibBuilder.loadTexts: notifications.setDescription("All the Multi-Flex Server notifications will reside under this branch as specified in RFC2578 'Structure of Management Information Version 2 (SMIv2)' 8.5")
registry = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1))
components = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2))
notificationInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3))
regModule = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1))
regComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2))
regChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 1))
regSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 2))
regScms = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 3))
regBlades = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 4))
regPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 5))
regFans = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 6))
multiFlexServer1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 1, 1))
if mibBuilder.loadTexts: multiFlexServer1.setStatus('current')
if mibBuilder.loadTexts: multiFlexServer1.setDescription('Multi-Flex Server rev1 chassis.')
esm1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 2, 1))
if mibBuilder.loadTexts: esm1.setStatus('current')
if mibBuilder.loadTexts: esm1.setDescription('Switch')
scm1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 3, 1))
if mibBuilder.loadTexts: scm1.setStatus('current')
if mibBuilder.loadTexts: scm1.setDescription('Storage Controller')
mib = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2))
groups = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2))
component = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: component.setStatus('current')
if mibBuilder.loadTexts: component.setDescription('Name of device reporting the event')
severity = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 0), ("neutral", 1), ("good", 2), ("info", 3), ("warning", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severity.setStatus('current')
if mibBuilder.loadTexts: severity.setDescription('Severity of the event being reported')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('current')
if mibBuilder.loadTexts: eventType.setDescription(' ... ')
user = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: user.setStatus('current')
if mibBuilder.loadTexts: user.setDescription(' ... ')
instanceId = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: instanceId.setStatus('current')
if mibBuilder.loadTexts: instanceId.setDescription(' ... ')
detail = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: detail.setStatus('current')
if mibBuilder.loadTexts: detail.setDescription(' ... ')
eventId = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventId.setStatus('current')
if mibBuilder.loadTexts: eventId.setDescription(' ... ')
chassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 1)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "component"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "severity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventType"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "user"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "instanceId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "detail"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisGroup = chassisGroup.setStatus('current')
if mibBuilder.loadTexts: chassisGroup.setDescription('Bogus Nodes (not really readable) for event notification')
mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", registry=registry, eventId=eventId, regSwitches=regSwitches, regPowerSupplies=regPowerSupplies, notificationInfo=notificationInfo, products=products, multiFlexServer=multiFlexServer, mib=mib, component=component, regBlades=regBlades, chassisGroup=chassisGroup, PYSNMP_MODULE_ID=multiFlexServerRegModule, regModule=regModule, regScms=regScms, detail=detail, user=user, instanceId=instanceId, notifications=notifications, intel=intel, groups=groups, multiFlexServer1=multiFlexServer1, eventType=eventType, multiFlexServerRegModule=multiFlexServerRegModule, modularsystems=modularsystems, components=components, regComponents=regComponents, regChassis=regChassis, esm1=esm1, scm1=scm1, severity=severity, regFans=regFans)
