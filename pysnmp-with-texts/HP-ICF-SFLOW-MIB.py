#
# PySNMP MIB module HP-ICF-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-SFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
sFlowRcvrEntry, sFlowFsInstance, sFlowFsDataSource = mibBuilder.importSymbols("SFLOW-MIB", "sFlowRcvrEntry", "sFlowFsInstance", "sFlowFsDataSource")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, TimeTicks, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ObjectIdentity, Counter64, ModuleIdentity, Gauge32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "ModuleIdentity", "Gauge32", "NotificationType", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hpicfSflowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92))
hpicfSflowMIB.setRevisions(('2012-08-22 00:00', '2012-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfSflowMIB.setRevisionsDescriptions(('Added mib object related to sFlow reciever over OOBM port.', 'This MIB module describes HP Sflow information.',))
if mibBuilder.loadTexts: hpicfSflowMIB.setLastUpdated('201208220000Z')
if mibBuilder.loadTexts: hpicfSflowMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfSflowMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfSflowMIB.setDescription('This MIB module describes HP Sflow information.')
hpicfSflowNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 0))
hpicfSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1))
hpicfSflowInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1))
hpicfSflowPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfSflowPortInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowPortInfoTable.setDescription('A table of objects that contains sflow port Information.')
hpicfSflowPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1), ).setIndexNames((0, "SFLOW-MIB", "sFlowFsDataSource"), (0, "SFLOW-MIB", "sFlowFsInstance"))
if mibBuilder.loadTexts: hpicfSflowPortInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowPortInfoEntry.setDescription('A set of objects that contains information of a sflow port.')
hpicfSflowPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("determine", 2), ("random", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSflowPortMode.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowPortMode.setDescription("This object indicates port's sflow mode.")
hpicfSflowPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSflowPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowPortStatus.setDescription("This object indicates port's sflow status.")
hpicfSflowRcvrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfSflowRcvrTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowRcvrTable.setDescription('Extensions to the table that contains SFLOW specific information.')
hpicfSflowRcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2, 1), )
sFlowRcvrEntry.registerAugmentions(("HP-ICF-SFLOW-MIB", "hpicfSflowRcvrEntry"))
hpicfSflowRcvrEntry.setIndexNames(*sFlowRcvrEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfSflowRcvrEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowRcvrEntry.setDescription('A list of extensions to the information maintained for an SFLOW receiver.')
hpicfSflowRcvrOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSflowRcvrOobm.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowRcvrOobm.setDescription('This object specifies whether to use OOBM port to send sflow data or not. This mib object will be applicable only if there is a physical OOBM port on the device ')
hpicfSflowConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2))
hpicfSflowGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1))
hpicfSflowInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1, 1)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowPortMode"), ("HP-ICF-SFLOW-MIB", "hpicfSflowPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowInfoGroup = hpicfSflowInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowInfoGroup.setDescription('A collection of objects representing the sflow information.')
hpicfSflowInfoGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1, 2)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowRcvrOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowInfoGroup1 = hpicfSflowInfoGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowInfoGroup1.setDescription('A collection of objects representing the sflow receiver information.')
hpicfSflowCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2))
hpicfSflowCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2, 1)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowCompliance = hpicfSflowCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowCompliance.setDescription('Describes the requirements for conformance to the sflow MIB.')
hpicfSflowCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2, 2)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowInfoGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowCompliance1 = hpicfSflowCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfSflowCompliance1.setDescription('Describes the requirements for conformance to the sflow MIB.')
mibBuilder.exportSymbols("HP-ICF-SFLOW-MIB", hpicfSflowRcvrTable=hpicfSflowRcvrTable, hpicfSflowPortInfoEntry=hpicfSflowPortInfoEntry, hpicfSflowCompliance1=hpicfSflowCompliance1, hpicfSflowGroups=hpicfSflowGroups, hpicfSflowPortStatus=hpicfSflowPortStatus, hpicfSflowMIB=hpicfSflowMIB, hpicfSflowConformance=hpicfSflowConformance, hpicfSflowRcvrEntry=hpicfSflowRcvrEntry, hpicfSflowInfoGroup=hpicfSflowInfoGroup, hpicfSflowObjects=hpicfSflowObjects, hpicfSflowCompliances=hpicfSflowCompliances, hpicfSflowCompliance=hpicfSflowCompliance, hpicfSflowRcvrOobm=hpicfSflowRcvrOobm, hpicfSflowPortMode=hpicfSflowPortMode, hpicfSflowNotifications=hpicfSflowNotifications, hpicfSflowPortInfoTable=hpicfSflowPortInfoTable, hpicfSflowInfoGroup1=hpicfSflowInfoGroup1, PYSNMP_MODULE_ID=hpicfSflowMIB, hpicfSflowInfo=hpicfSflowInfo)
