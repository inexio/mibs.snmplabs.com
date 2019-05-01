#
# PySNMP MIB module CISCO-DIAMETER-SG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIAMETER-SG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, ModuleIdentity, Unsigned32, iso, Integer32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, NotificationType, Bits, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Unsigned32", "iso", "Integer32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "NotificationType", "Bits", "TimeTicks", "MibIdentifier")
StorageType, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TextualConvention", "RowStatus")
ciscoDiameterSGMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 132))
ciscoDiameterSGMIB.setRevisions(('2006-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDiameterSGMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDiameterSGMIB.setLastUpdated('200609060000Z')
if mibBuilder.loadTexts: ciscoDiameterSGMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDiameterSGMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoDiameterSGMIB.setDescription("The MIB module for Cisco's Diameter Server Group Entities. This MIB describes the SNMP MIB objects that are supported in order to provide the ability to fetch/configure the Diameter Server Groups.")
ciscoDiameterSGMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 132, 0))
ciscoDiameterSGMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 132, 1))
ciscoDiameterSGMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 132, 2))
cdsgHostCfgs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1))
cdsgServerGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1), )
if mibBuilder.loadTexts: cdsgServerGroupTable.setStatus('current')
if mibBuilder.loadTexts: cdsgServerGroupTable.setDescription('The table listing the Diameter server group information. Entries are added to this table via cdsgServerGroupRowStatus in accordance with the RowStatus convention.')
cdsgServerGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAMETER-SG-MIB", "cdsgServerGroupIndex"))
if mibBuilder.loadTexts: cdsgServerGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cdsgServerGroupEntry.setDescription('A row entry representing a Diameter server group entry.')
cdsgServerGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cdsgServerGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cdsgServerGroupIndex.setDescription('A number uniquely identifying each Diameter Server Group. An index that uniquely represents a Server Group. This index is assigned arbitrarily by the SNMP engine and is not saved over reloads.')
cdsgServerGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdsgServerGroupName.setStatus('current')
if mibBuilder.loadTexts: cdsgServerGroupName.setDescription('The Server Group Name. It has to be unique and not an empty string.')
cdsgServerGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdsgServerGroupStorageType.setReference('Textual Conventions for SMIv2, Section 2.')
if mibBuilder.loadTexts: cdsgServerGroupStorageType.setStatus('current')
if mibBuilder.loadTexts: cdsgServerGroupStorageType.setDescription('The storage type for this conceptual row. An agent implementing the table must allow adding cdsgServerGroupName into the table. None of the columnar objects is writable when the conceptual row is permanent.')
cdsgServerGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdsgServerGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cdsgServerGroupRowStatus.setDescription("The status of this conceptual row. To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5). Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the cdsgServerGroupRowStatus column is 'notReady'. In particular, a newly created row cannot be made active until the corresponding cdsgServerGroupName has been set. cdsgServerGroupName may not be modified while the value of this object is active(1): An attempt to set these objects while the value of cdsgServerGroupRowStatus is active(1) will result in an inconsistentValue error. Entries in this table with cdsgServerGroupRowStatus equal to active(1) remain in the table until destroyed. Entries in this table with cdsgServerGroupRowStatus equal to values other than active(1) will be destroyed after timeout (5 minutes). Upon reload, cdsgServerGroupIndex values may be changed.")
cdsgServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2), )
if mibBuilder.loadTexts: cdsgServerTable.setStatus('current')
if mibBuilder.loadTexts: cdsgServerTable.setDescription('The table listing information regarding the server which are part of the Diameter server groups. Entries are added to this table via cdsgServerRowStatus in accordance with the RowStatus convention. ')
cdsgServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DIAMETER-SG-MIB", "cdsgServerGroupIndex"), (0, "CISCO-DIAMETER-SG-MIB", "cdsgServerIndex"))
if mibBuilder.loadTexts: cdsgServerEntry.setStatus('current')
if mibBuilder.loadTexts: cdsgServerEntry.setDescription('A row entry representing a Diameter server group.')
cdsgServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cdsgServerIndex.setStatus('current')
if mibBuilder.loadTexts: cdsgServerIndex.setDescription('A number uniquely identifying each Diameter Server. An index that uniquely represents a Server within a Server Group. This index is assigned arbitrarily by the SNMP engine and is not saved over reloads.')
cdsgServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdsgServerName.setStatus('current')
if mibBuilder.loadTexts: cdsgServerName.setDescription('The Server Name. It has to be unique and not an empty string.')
cdsgServerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdsgServerStorageType.setReference('Textual Conventions for SMIv2, Section 2.')
if mibBuilder.loadTexts: cdsgServerStorageType.setStatus('current')
if mibBuilder.loadTexts: cdsgServerStorageType.setDescription('The storage type for this conceptual row. An agent implementing the table must allow adding cdsgServerName into the table. None of the columnar objects is writable when the conceptual row is permanent.')
cdsgServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 132, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdsgServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: cdsgServerRowStatus.setDescription("The status of this conceptual row. To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5). This table is an extended table to the cdsgServerGroupTable and so an entry here must have a corresponding parent entry in the cdsgServerGroupTable as well. This would map all such entries with the same cdsgServerEntry under one single cdsgServerGroupEntry i.e these servers are under the server group represented by the cdsgServerGroupEntry. Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the cdsgServerRowStatus column is 'notReady'. In particular, a newly created row cannot be made active until the corresponding cdsgServerName has been set. cdsgServerName may not be modified while the value of this object is active(1): An attempt to set these objects while the value of cdsgServerRowStatus is active(1) will result in an inconsistentValue error. Entries in this table with cdsgServerRowStatus equal to active(1) remain in the table until destroyed. Entries in this table with cdsgServerRowStatus equal to values other than active(1) will be destroyed after timeout (5 minutes). Upon reload, cdsgServerIndex values may be changed.")
ciscoDiameterSGMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 1))
ciscoDiameterSGMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 2))
ciscoDiameterSGMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 1, 1)).setObjects(("CISCO-DIAMETER-SG-MIB", "ciscoDiameterSGHostCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterSGMIBCompliance = ciscoDiameterSGMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterSGMIBCompliance.setDescription('The compliance statement for Diameter Server Group entities.')
ciscoDiameterSGHostCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 132, 2, 2, 1)).setObjects(("CISCO-DIAMETER-SG-MIB", "cdsgServerGroupName"), ("CISCO-DIAMETER-SG-MIB", "cdsgServerGroupRowStatus"), ("CISCO-DIAMETER-SG-MIB", "cdsgServerGroupStorageType"), ("CISCO-DIAMETER-SG-MIB", "cdsgServerName"), ("CISCO-DIAMETER-SG-MIB", "cdsgServerRowStatus"), ("CISCO-DIAMETER-SG-MIB", "cdsgServerStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterSGHostCfgGroup = ciscoDiameterSGHostCfgGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDiameterSGHostCfgGroup.setDescription('A collection of objects providing configuration common to the server.')
mibBuilder.exportSymbols("CISCO-DIAMETER-SG-MIB", cdsgServerStorageType=cdsgServerStorageType, cdsgServerTable=cdsgServerTable, cdsgServerEntry=cdsgServerEntry, cdsgServerGroupStorageType=cdsgServerGroupStorageType, cdsgServerGroupRowStatus=cdsgServerGroupRowStatus, cdsgServerGroupEntry=cdsgServerGroupEntry, ciscoDiameterSGMIBCompliances=ciscoDiameterSGMIBCompliances, cdsgServerRowStatus=cdsgServerRowStatus, ciscoDiameterSGMIBNotifs=ciscoDiameterSGMIBNotifs, ciscoDiameterSGMIBGroups=ciscoDiameterSGMIBGroups, ciscoDiameterSGHostCfgGroup=ciscoDiameterSGHostCfgGroup, cdsgServerGroupName=cdsgServerGroupName, ciscoDiameterSGMIBConform=ciscoDiameterSGMIBConform, cdsgServerGroupIndex=cdsgServerGroupIndex, PYSNMP_MODULE_ID=ciscoDiameterSGMIB, ciscoDiameterSGMIBObjects=ciscoDiameterSGMIBObjects, ciscoDiameterSGMIBCompliance=ciscoDiameterSGMIBCompliance, cdsgServerGroupTable=cdsgServerGroupTable, ciscoDiameterSGMIB=ciscoDiameterSGMIB, cdsgServerIndex=cdsgServerIndex, cdsgHostCfgs=cdsgHostCfgs, cdsgServerName=cdsgServerName)
