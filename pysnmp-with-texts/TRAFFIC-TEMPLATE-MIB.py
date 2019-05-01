#
# PySNMP MIB module TRAFFIC-TEMPLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAFFIC-TEMPLATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, TimeTicks, Counter32, Gauge32, MibIdentifier, Unsigned32, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
hpicfTrafficTemplateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72))
hpicfTrafficTemplateMIB.setRevisions(('2012-02-02 00:00', '2010-03-04 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfTrafficTemplateMIB.setRevisionsDescriptions(('Added hpSwitchTrafficGroupEgressDiscardThreshold, hpSwitchTrafficTemplateNumQueues, and hpSwitchTrafficTemplatePredefined. Updated description text.', 'Initial version.',))
if mibBuilder.loadTexts: hpicfTrafficTemplateMIB.setLastUpdated('201202020000Z')
if mibBuilder.loadTexts: hpicfTrafficTemplateMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfTrafficTemplateMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfTrafficTemplateMIB.setDescription('This MIB defines HP proprietary objects used to configure traffic templates for CoS (Class of Service) queuing.')
hpicfTrafficTemplateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1))
hpicfTrafficTemplateScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 1))
hpSwitchTrafficTemplateSystemDefaultName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficTemplateSystemDefaultName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateSystemDefaultName.setDescription('The name of the traffic template used as the system default when no name has been explicitly set. Limited to 40 characters on some devices.')
hpSwitchTrafficTemplate = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2))
hpSwitchTrafficTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1), )
if mibBuilder.loadTexts: hpSwitchTrafficTemplateTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateTable.setDescription('A table that contains information about traffic templates for CoS (class of service) queue configuration in the device.')
hpSwitchTrafficTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1), ).setIndexNames((0, "TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateName"))
if mibBuilder.loadTexts: hpSwitchTrafficTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateEntry.setDescription('Information about a single traffic template for CoS queue configuration in the device.')
hpSwitchTrafficTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80)))
if mibBuilder.loadTexts: hpSwitchTrafficTemplateName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateName.setDescription('A unique name by which this template is referenced. Limited to 40 characters on some devices.')
hpSwitchTrafficTemplateMappedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 2), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchTrafficTemplateMappedPorts.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateMappedPorts.setDescription('The set of ports to which this traffic template is mapped. The set of ports is identified by a PortList in which each port is represented by a bit. A port cannot be mapped to more than one traffic template. Not all devices support different traffic templates for different ports. The port map is ignored on devices that use a common template for all ports.')
hpSwitchTrafficTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchTrafficTemplateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateRowStatus.setDescription("The Row Status of this traffic template entry. To create a new traffic template, send a SET request with a RowStatus of 'createAndWait'. This will result in the creation of a template of that name and a new hpSwitchTrafficGroupTable entry with system default values. active - all traffic groups in the template row are valid and the template is applied to one or more interfaces. notReady - template is not valid or is undergoing modification. notInService - template is valid, but is not applied to any interface. createAndWait - create a new traffic template. delete - delete the traffic template. createAndGo - not valid for this table. A device reboot is required to apply updated templates to their interfaces.")
hpSwitchTrafficTemplateNumQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficTemplateNumQueues.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplateNumQueues.setDescription('The number of egress queues this template is valid for.')
hpSwitchTrafficTemplatePredefined = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchTrafficTemplatePredefined.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficTemplatePredefined.setDescription('Indicates that this template is factory predefined. Predefined templates may not be deleted and their queue configuration may not be modified.')
hpSwitchTrafficGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2), )
if mibBuilder.loadTexts: hpSwitchTrafficGroupTable.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupTable.setDescription('A table that contains the mapping of 802.1q packet priorities to CoS traffic queues in the device. Entries in this table define traffic class groups containing a queue number, an optional ID number, a set of priority values mapped to the queue, an optional name, and a lossless flag when Priority Flow Control is enabled for a port. A SET to an object in any row of this table causes the RowStatus of the parent template to change to notReady. Changes are temporary until the template RowStatus is successfully SET to active.')
hpSwitchTrafficGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1), ).setIndexNames((0, "TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateName"), (0, "TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficQueue"))
if mibBuilder.loadTexts: hpSwitchTrafficGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupEntry.setDescription('Traffic group configuration for a given queue.')
hpSwitchTrafficQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9000)))
if mibBuilder.loadTexts: hpSwitchTrafficQueue.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficQueue.setDescription('The internal number of the queue this entry will apply to.')
hpSwitchTrafficGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficGroupID.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupID.setDescription('The ID value of this traffic class group in the DCBX exchange. Only IDs 0-7 are allowed in a SET request. This setting is not supported on all devices.')
hpSwitchTrafficGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficGroupName.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupName.setDescription('An optional user-defined name for this traffic group. Limited to 40 characters on some devices.')
hpSwitchTrafficGroupPriorityMap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 4), Bits().clone(namedValues=NamedValues(("priority0", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3), ("priority4", 4), ("priority5", 5), ("priority6", 6), ("priority7", 7), ("priority8", 8), ("priority9", 9), ("priority10", 10), ("priority11", 11), ("priority12", 12), ("priority13", 13), ("priority14", 14), ("priority15", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficGroupPriorityMap.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupPriorityMap.setDescription('A bitmap of 802.1q priority values assigned to this traffic group. Each priority value 0-7 must be assigned to exactly one group for the template to be valid.')
hpSwitchTrafficGroupLossless = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficGroupLossless.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupLossless.setDescription("A flag indicating that this queue is to be configured for lossless behavior when Priority Flow Control (PFC) is enabled on a port. Designating a queue as lossless causes ingress thresholds to be set that will trigger PFC frames when this queue exceeds or falls below a specific threshold. The queue will also respond to PFC frames received from a neighbor. This flag may not be set if any queue in the template is configured for a 'medium' or 'low' discard threshold (see hpSwitchTrafficGroupEgressDiscardThreshold). This flag is not supported on all devices.")
hpSwitchTrafficGroupEgressDiscardThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchTrafficGroupEgressDiscardThreshold.setStatus('current')
if mibBuilder.loadTexts: hpSwitchTrafficGroupEgressDiscardThreshold.setDescription("The Egress Buffer Discard Threshold setting for this traffic group. This setting controls the maximum size of the group egress queue. When set to 'medium' or 'low', the maximum number of buffers permitted in the queue is reduced so packets are dropped sooner and their buffers made available for higher priority traffic. However, this also reduces the maximum traffic burst that can be absorbed without dropping packets. The default is 'high'. This setting may not be changed if any queue in the template is configured for lossless behavior (see hpSwitchTrafficGroupLossless). This setting is not supported on all devices.")
hpicfTrafficTempalteConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2))
hpicfTrafficTemplateGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1))
hpicfTrafficTemplateCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 2))
hpicfTrafficTemplateScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 1)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateSystemDefaultName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficTemplateScalarGroup = hpicfTrafficTemplateScalarGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfTrafficTemplateScalarGroup.setDescription('A collection of scalars related to traffic template configuration.')
hpicfTrafficTemplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 2)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateMappedPorts"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficTemplateGroup = hpicfTrafficTemplateGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTrafficTemplateGroup.setDescription('###DEPRECATED### A collection of objects providing configuration of traffic templates. This conformance is deprecated and replaced by hpicfTrafficTemplateGroup2.')
hpicfTrafficGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 3)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupID"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupName"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupPriorityMap"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupLossless"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficGroup = hpicfTrafficGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTrafficGroup.setDescription('###DEPRECATED### A collection of objects providing configuration of traffic groups in a template. This conformance is deprecated and replaced by hpicfTrafficGroup2.')
hpicfTrafficTemplateGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 4)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateMappedPorts"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateRowStatus"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateNumQueues"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplatePredefined"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficTemplateGroup2 = hpicfTrafficTemplateGroup2.setStatus('current')
if mibBuilder.loadTexts: hpicfTrafficTemplateGroup2.setDescription('A collection of objects providing configuration of traffic templates.')
hpicfTrafficGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 5)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupID"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupName"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupPriorityMap"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupLossless"), ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupEgressDiscardThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficGroup2 = hpicfTrafficGroup2.setStatus('current')
if mibBuilder.loadTexts: hpicfTrafficGroup2.setDescription('A collection of objects providing configuration of traffic groups in a template.')
hpicfTrafficTemplateCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 2, 1)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpicfTrafficTemplateScalarGroup"), ("TRAFFIC-TEMPLATE-MIB", "hpicfTrafficTemplateGroup"), ("TRAFFIC-TEMPLATE-MIB", "hpicfTrafficGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficTemplateCompliance = hpicfTrafficTemplateCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTrafficTemplateCompliance.setDescription('###DEPRECATED### The compliance statement for device support of TRAFFIC-TEMPLATE-MIB. This compliance is deprecated and replaced by hpicfTrafficTemplateCompliance2.')
hpicfTrafficTemplateCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 2, 2)).setObjects(("TRAFFIC-TEMPLATE-MIB", "hpicfTrafficTemplateScalarGroup"), ("TRAFFIC-TEMPLATE-MIB", "hpicfTrafficTemplateGroup2"), ("TRAFFIC-TEMPLATE-MIB", "hpicfTrafficGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTrafficTemplateCompliance2 = hpicfTrafficTemplateCompliance2.setStatus('current')
if mibBuilder.loadTexts: hpicfTrafficTemplateCompliance2.setDescription('The compliance statement for device support of TRAFFIC-TEMPLATE-MIB.')
mibBuilder.exportSymbols("TRAFFIC-TEMPLATE-MIB", hpicfTrafficTemplateGroup2=hpicfTrafficTemplateGroup2, hpicfTrafficTemplateGroups=hpicfTrafficTemplateGroups, hpicfTrafficTemplateScalarGroup=hpicfTrafficTemplateScalarGroup, hpicfTrafficTemplateCompliance=hpicfTrafficTemplateCompliance, hpicfTrafficTemplateScalars=hpicfTrafficTemplateScalars, hpicfTrafficTemplateObjects=hpicfTrafficTemplateObjects, hpicfTrafficTemplateMIB=hpicfTrafficTemplateMIB, hpSwitchTrafficTemplate=hpSwitchTrafficTemplate, hpicfTrafficTemplateGroup=hpicfTrafficTemplateGroup, hpSwitchTrafficGroupEntry=hpSwitchTrafficGroupEntry, hpicfTrafficTemplateCompliances=hpicfTrafficTemplateCompliances, hpSwitchTrafficGroupID=hpSwitchTrafficGroupID, hpicfTrafficTempalteConformance=hpicfTrafficTempalteConformance, hpSwitchTrafficTemplateNumQueues=hpSwitchTrafficTemplateNumQueues, hpicfTrafficGroup=hpicfTrafficGroup, hpSwitchTrafficGroupLossless=hpSwitchTrafficGroupLossless, hpSwitchTrafficGroupEgressDiscardThreshold=hpSwitchTrafficGroupEgressDiscardThreshold, hpicfTrafficTemplateCompliance2=hpicfTrafficTemplateCompliance2, PYSNMP_MODULE_ID=hpicfTrafficTemplateMIB, hpSwitchTrafficTemplateSystemDefaultName=hpSwitchTrafficTemplateSystemDefaultName, hpSwitchTrafficTemplateName=hpSwitchTrafficTemplateName, hpSwitchTrafficTemplateTable=hpSwitchTrafficTemplateTable, hpSwitchTrafficQueue=hpSwitchTrafficQueue, hpSwitchTrafficGroupName=hpSwitchTrafficGroupName, hpSwitchTrafficTemplateEntry=hpSwitchTrafficTemplateEntry, hpSwitchTrafficGroupTable=hpSwitchTrafficGroupTable, hpicfTrafficGroup2=hpicfTrafficGroup2, hpSwitchTrafficTemplateMappedPorts=hpSwitchTrafficTemplateMappedPorts, hpSwitchTrafficGroupPriorityMap=hpSwitchTrafficGroupPriorityMap, hpSwitchTrafficTemplatePredefined=hpSwitchTrafficTemplatePredefined, hpSwitchTrafficTemplateRowStatus=hpSwitchTrafficTemplateRowStatus)
