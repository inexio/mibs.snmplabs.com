#
# PySNMP MIB module FOUNDRY-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-LAG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
snTraps, snSwitch = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snTraps", "snSwitch")
InterfaceIndex, ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Counter32, IpAddress, iso, Counter64, Bits, NotificationType, Unsigned32, Integer32, MibIdentifier, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter32", "IpAddress", "iso", "Counter64", "Bits", "NotificationType", "Unsigned32", "Integer32", "MibIdentifier", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fdryLinkAggregationGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33))
fdryLinkAggregationGroupMIB.setRevisions(('2010-06-02 00:00', '2009-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryLinkAggregationGroupMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'convert from SMIv1 to SMIv2',))
if mibBuilder.loadTexts: fdryLinkAggregationGroupMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: fdryLinkAggregationGroupMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryLinkAggregationGroupMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryLinkAggregationGroupMIB.setDescription("Management Information Base module for link aggregate group configuration and statistics. Link aggregation group is a new concept of trunk and this MIB is replacing FOUNDRY-SN-LAG-MIB in MLX/XMR products starting release 4.1.0. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
fdryLinkAggregationGroupNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 0))
fdryLinkAggregationGroupTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1))
fdryLinkAggregationGroupPortTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2))
fdryLinkAggregationGroupTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1), )
if mibBuilder.loadTexts: fdryLinkAggregationGroupTable.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupTable.setDescription('LinkAggregationGroup table.')
fdryLinkAggregationGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1), ).setIndexNames((0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"))
if mibBuilder.loadTexts: fdryLinkAggregationGroupEntry.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupEntry.setDescription('An entry of the Link Aggregate Group table.')
fdryLinkAggregationGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: fdryLinkAggregationGroupName.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupName.setDescription('Name of a LinkAggregationGroup.')
fdryLinkAggregationGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("keepalive", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupType.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupType.setDescription('LinkAggregationGroup type.')
fdryLinkAggregationGroupAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("deploy", 1), ("deployPassive", 2), ("undeploy", 3), ("undeployForced", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupAdminStatus.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupAdminStatus.setDescription('The desired deplyed state of this LinkAggregationGroup entry. This is not the operational status. Refer to ifTable for the operational status. deploy(1).............deploy the LAG and set to LACP active if dynamic LAG. deployPassive(2)..deploy the LAG and set to LACP passive if dynamic LAG. undeploy(3).........undeploy the LAG if no more than 2 ports are enabled. undeployForced(4)..undeploy the LAG regardless number of ports enabled. This is a write-only value. In particular, a row cannot be deployed until the corresponding instances of fdryLinkAggregationGroupIfList has been set.')
fdryLinkAggregationGroupIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupIfList.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupIfList.setDescription('A list of interface indices which are the port membership of a trunk group. Each interface index is a 32-bit integer in big endian order.')
fdryLinkAggregationGroupPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupPrimaryPort.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupPrimaryPort.setDescription('The primary port for the Link Aggregation Group. This must be set before deploying the LinkAggregateGroup unless this is a keepalive LinkAggregateGroup.')
fdryLinkAggregationGroupTrunkType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hashBased", 1), ("perPacket", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupTrunkType.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupTrunkType.setDescription('The trunk connection type which specifies what the scheme of load-sharing among the trunk ports is.')
fdryLinkAggregationGroupTrunkThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupTrunkThreshold.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupTrunkThreshold.setDescription('The number of UP ports needed to keep the trunk up. Not applicable for keepalive LAG.')
fdryLinkAggregationGroupLacpTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("long", 2), ("short", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupLacpTimeout.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupLacpTimeout.setDescription('The LACP timeout value this LACP LAG will use. Applicable for dynamic and keepalive LAG only.')
fdryLinkAggregationGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryLinkAggregationGroupIfIndex.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupIfIndex.setDescription('After deployment the operation information of a LAG entry will be represented in an entry in ifTable. Use this variable as the ifIndex to access the entry in ifTable and ifXTable. Zero will be returned for LAGs not yet deployed.')
fdryLinkAggregationGroupPortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortCount.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortCount.setDescription('The number of member ports belong to this LAG.')
fdryLinkAggregationGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryLinkAggregationGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupRowStatus.setDescription('The status of this conceptual row. createAndWait(5) is not supported. To create a row in this table, a manager must set this object to createAndGo(4) together with the setting of fdryLinkAggregationGroupType. After that the row status becomes active(1) regardless the LAG entry is deployed or not. To deploy the LAG entry, set the corresponding instance of fdryLinkAggregationGroupAdminStatus to deployActive or deployPassive.')
fdryLinkAggregationGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryLinkAggregationGroupId.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupId.setDescription('The numeric identifier assigned to this LAG.')
fdryLinkAggregationGroupPortTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1), )
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortTable.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortTable.setDescription('A table that contains Link Aggregation Control configuration information about every Aggregation Port associated with this device. A row appears in this table for each physical port.')
fdryLinkAggregationGroupPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortEntry.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortEntry.setDescription('An entry of the Link Aggregate Group Port table.')
fdryLinkAggregationGroupPortLacpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortLacpPriority.setStatus('current')
if mibBuilder.loadTexts: fdryLinkAggregationGroupPortLacpPriority.setDescription('The LACP priority value assigned to this link aggregation port. Applicable for dynamic and keepalive LAG only.')
fdryLAGName = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 0, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fdryLAGName.setStatus('current')
if mibBuilder.loadTexts: fdryLAGName.setDescription('Name of a LinkAggregationGroup.')
fdryTrapLagDeployed = NotificationType((1, 3, 6, 1, 4, 1, 1991, 0, 1204)).setObjects(("FOUNDRY-LAG-MIB", "fdryLAGName"), ("FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupIfIndex"))
if mibBuilder.loadTexts: fdryTrapLagDeployed.setStatus('current')
if mibBuilder.loadTexts: fdryTrapLagDeployed.setDescription('The SNMP trap that is generated when a LAG is deployed.')
fdryTrapLagUndeployed = NotificationType((1, 3, 6, 1, 4, 1, 1991, 0, 1205)).setObjects(("FOUNDRY-LAG-MIB", "fdryLAGName"), ("FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupIfIndex"))
if mibBuilder.loadTexts: fdryTrapLagUndeployed.setStatus('current')
if mibBuilder.loadTexts: fdryTrapLagUndeployed.setDescription('The SNMP trap that is generated when a LAG is undeployed.')
mibBuilder.exportSymbols("FOUNDRY-LAG-MIB", fdryLinkAggregationGroupNotifyObjects=fdryLinkAggregationGroupNotifyObjects, PYSNMP_MODULE_ID=fdryLinkAggregationGroupMIB, fdryTrapLagDeployed=fdryTrapLagDeployed, fdryLinkAggregationGroupIfIndex=fdryLinkAggregationGroupIfIndex, fdryLinkAggregationGroupTableObjects=fdryLinkAggregationGroupTableObjects, fdryTrapLagUndeployed=fdryTrapLagUndeployed, fdryLinkAggregationGroupIfList=fdryLinkAggregationGroupIfList, fdryLinkAggregationGroupMIB=fdryLinkAggregationGroupMIB, fdryLinkAggregationGroupEntry=fdryLinkAggregationGroupEntry, fdryLAGName=fdryLAGName, fdryLinkAggregationGroupTable=fdryLinkAggregationGroupTable, fdryLinkAggregationGroupPortCount=fdryLinkAggregationGroupPortCount, fdryLinkAggregationGroupPortEntry=fdryLinkAggregationGroupPortEntry, fdryLinkAggregationGroupAdminStatus=fdryLinkAggregationGroupAdminStatus, fdryLinkAggregationGroupLacpTimeout=fdryLinkAggregationGroupLacpTimeout, fdryLinkAggregationGroupPortTableObjects=fdryLinkAggregationGroupPortTableObjects, fdryLinkAggregationGroupPrimaryPort=fdryLinkAggregationGroupPrimaryPort, fdryLinkAggregationGroupType=fdryLinkAggregationGroupType, fdryLinkAggregationGroupPortLacpPriority=fdryLinkAggregationGroupPortLacpPriority, fdryLinkAggregationGroupRowStatus=fdryLinkAggregationGroupRowStatus, fdryLinkAggregationGroupTrunkThreshold=fdryLinkAggregationGroupTrunkThreshold, fdryLinkAggregationGroupName=fdryLinkAggregationGroupName, fdryLinkAggregationGroupTrunkType=fdryLinkAggregationGroupTrunkType, fdryLinkAggregationGroupPortTable=fdryLinkAggregationGroupPortTable, fdryLinkAggregationGroupId=fdryLinkAggregationGroupId)
