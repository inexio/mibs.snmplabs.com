#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-OBSERVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-OBSERVE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:17:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, CiscoNetworkAddress, TimeIntervalSec, CiscoInetAddressMask, Unsigned64 = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity", "CiscoNetworkAddress", "TimeIntervalSec", "CiscoInetAddressMask", "Unsigned64")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectId, CucsManagedObjectDn = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId", "CucsManagedObjectDn")
CucsMoMoClassId, CucsObserveObservedFsmTaskItem, CucsFsmFsmStageStatus, CucsFsmFlags, CucsObserveObservedFsmCurrentFsm, CucsObserveObservedFsmStageName, CucsFsmCompletion, CucsConditionRemoteInvRslt = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsMoMoClassId", "CucsObserveObservedFsmTaskItem", "CucsFsmFsmStageStatus", "CucsFsmFlags", "CucsObserveObservedFsmCurrentFsm", "CucsObserveObservedFsmStageName", "CucsFsmCompletion", "CucsConditionRemoteInvRslt")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, iso, Counter32, Unsigned32, NotificationType, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "iso", "Counter32", "Unsigned32", "NotificationType", "IpAddress", "ModuleIdentity", "TimeTicks")
MacAddress, DisplayString, DateAndTime, TruthValue, RowPointer, TimeInterval, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "DateAndTime", "TruthValue", "RowPointer", "TimeInterval", "TimeStamp", "TextualConvention")
cucsObserveObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68))
if mibBuilder.loadTexts: cucsObserveObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsObserveObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsObserveObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsObserveObjects.setDescription('MIB representation of the Cisco Unified Computing System OBSERVE management information model package')
cucsObserveFilterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1), )
if mibBuilder.loadTexts: cucsObserveFilterTable.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterTable.setDescription('Cisco UCS observe:Filter managed object table')
cucsObserveFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveFilterInstanceId"))
if mibBuilder.loadTexts: cucsObserveFilterEntry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterEntry.setDescription('Entry for the cucsObserveFilterTable table.')
cucsObserveFilterInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsObserveFilterInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterInstanceId.setDescription('Instance identifier of the managed object.')
cucsObserveFilterDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterDn.setDescription('Cisco UCS observe:Filter:dn managed object property')
cucsObserveFilterRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterRn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterRn.setDescription('Cisco UCS observe:Filter:rn managed object property')
cucsObserveFilterAndOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterAndOperation.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterAndOperation.setDescription('Cisco UCS observe:Filter:andOperation managed object property')
cucsObserveFilterChildClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 5), CucsMoMoClassId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterChildClassId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterChildClassId.setDescription('Cisco UCS observe:Filter:childClassId managed object property')
cucsObserveFilterFilterClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 6), CucsMoMoClassId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterClassId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterClassId.setDescription('Cisco UCS observe:Filter:filterClassId managed object property')
cucsObserveFilterFilterPropId1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterPropId1.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterPropId1.setDescription('Cisco UCS observe:Filter:filterPropId1 managed object property')
cucsObserveFilterFilterPropId2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterPropId2.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterPropId2.setDescription('Cisco UCS observe:Filter:filterPropId2 managed object property')
cucsObserveFilterFilterPropId3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterPropId3.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterPropId3.setDescription('Cisco UCS observe:Filter:filterPropId3 managed object property')
cucsObserveFilterFilterPropValue1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterPropValue1.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterPropValue1.setDescription('Cisco UCS observe:Filter:filterPropValue1 managed object property')
cucsObserveFilterFilterPropValue2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterPropValue2.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterPropValue2.setDescription('Cisco UCS observe:Filter:filterPropValue2 managed object property')
cucsObserveFilterFilterPropValue3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterFilterPropValue3.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterFilterPropValue3.setDescription('Cisco UCS observe:Filter:filterPropValue3 managed object property')
cucsObserveFilterHierarchical = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterHierarchical.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterHierarchical.setDescription('Cisco UCS observe:Filter:hierarchical managed object property')
cucsObserveFilterReplicateIfNoChild = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveFilterReplicateIfNoChild.setStatus('current')
if mibBuilder.loadTexts: cucsObserveFilterReplicateIfNoChild.setDescription('Cisco UCS observe:Filter:replicateIfNoChild managed object property')
cucsObserveObservedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2), )
if mibBuilder.loadTexts: cucsObserveObservedTable.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedTable.setDescription('Cisco UCS observe:Observed managed object table')
cucsObserveObservedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedInstanceId"))
if mibBuilder.loadTexts: cucsObserveObservedEntry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedEntry.setDescription('Entry for the cucsObserveObservedTable table.')
cucsObserveObservedInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsObserveObservedInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedInstanceId.setDescription('Instance identifier of the managed object.')
cucsObserveObservedDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedDn.setDescription('Cisco UCS observe:Observed:dn managed object property')
cucsObserveObservedRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedRn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedRn.setDescription('Cisco UCS observe:Observed:rn managed object property')
cucsObserveObservedDataSrcAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedDataSrcAppType.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedDataSrcAppType.setDescription('Cisco UCS observe:Observed:dataSrcAppType managed object property')
cucsObserveObservedDataSrcSysId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedDataSrcSysId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedDataSrcSysId.setDescription('Cisco UCS observe:Observed:dataSrcSysId managed object property')
cucsObserveObservedFsmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmDescr.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmDescr.setDescription('Cisco UCS observe:Observed:fsmDescr managed object property')
cucsObserveObservedFsmPrev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmPrev.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmPrev.setDescription('Cisco UCS observe:Observed:fsmPrev managed object property')
cucsObserveObservedFsmProgr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmProgr.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmProgr.setDescription('Cisco UCS observe:Observed:fsmProgr managed object property')
cucsObserveObservedFsmRmtInvErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtInvErrCode.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtInvErrCode.setDescription('Cisco UCS observe:Observed:fsmRmtInvErrCode managed object property')
cucsObserveObservedFsmRmtInvErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtInvErrDescr.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtInvErrDescr.setDescription('Cisco UCS observe:Observed:fsmRmtInvErrDescr managed object property')
cucsObserveObservedFsmRmtInvRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 11), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtInvRslt.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtInvRslt.setDescription('Cisco UCS observe:Observed:fsmRmtInvRslt managed object property')
cucsObserveObservedFsmStageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageDescr.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageDescr.setDescription('Cisco UCS observe:Observed:fsmStageDescr managed object property')
cucsObserveObservedFsmStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStamp.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStamp.setDescription('Cisco UCS observe:Observed:fsmStamp managed object property')
cucsObserveObservedFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStatus.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStatus.setDescription('Cisco UCS observe:Observed:fsmStatus managed object property')
cucsObserveObservedFsmTry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTry.setDescription('Cisco UCS observe:Observed:fsmTry managed object property')
cucsObserveObservedGenNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedGenNum.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedGenNum.setDescription('Cisco UCS observe:Observed:genNum managed object property')
cucsObserveObservedHierarchical = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedHierarchical.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedHierarchical.setDescription('Cisco UCS observe:Observed:hierarchical managed object property')
cucsObserveObservedId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedId.setDescription('Cisco UCS observe:Observed:id managed object property')
cucsObserveObservedIsDeleted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedIsDeleted.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedIsDeleted.setDescription('Cisco UCS observe:Observed:isDeleted managed object property')
cucsObserveObservedObservedDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 20), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedObservedDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedObservedDn.setDescription('Cisco UCS observe:Observed:observedDn managed object property')
cucsObserveObservedContTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3), )
if mibBuilder.loadTexts: cucsObserveObservedContTable.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedContTable.setDescription('Cisco UCS observe:ObservedCont managed object table')
cucsObserveObservedContEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedContInstanceId"))
if mibBuilder.loadTexts: cucsObserveObservedContEntry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedContEntry.setDescription('Entry for the cucsObserveObservedContTable table.')
cucsObserveObservedContInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsObserveObservedContInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedContInstanceId.setDescription('Instance identifier of the managed object.')
cucsObserveObservedContDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedContDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedContDn.setDescription('Cisco UCS observe:ObservedCont:dn managed object property')
cucsObserveObservedContRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedContRn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedContRn.setDescription('Cisco UCS observe:ObservedCont:rn managed object property')
cucsObserveObservedContIdCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedContIdCount.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedContIdCount.setDescription('Cisco UCS observe:ObservedCont:idCount managed object property')
cucsObserveObservedFsmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4), )
if mibBuilder.loadTexts: cucsObserveObservedFsmTable.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTable.setDescription('Cisco UCS observe:ObservedFsm managed object table')
cucsObserveObservedFsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedFsmInstanceId"))
if mibBuilder.loadTexts: cucsObserveObservedFsmEntry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmEntry.setDescription('Entry for the cucsObserveObservedFsmTable table.')
cucsObserveObservedFsmInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsObserveObservedFsmInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmInstanceId.setDescription('Instance identifier of the managed object.')
cucsObserveObservedFsmDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmDn.setDescription('Cisco UCS observe:ObservedFsm:dn managed object property')
cucsObserveObservedFsmRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRn.setDescription('Cisco UCS observe:ObservedFsm:rn managed object property')
cucsObserveObservedFsmCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmCompletionTime.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmCompletionTime.setDescription('Cisco UCS observe:ObservedFsm:completionTime managed object property')
cucsObserveObservedFsmCurrentFsm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 5), CucsObserveObservedFsmCurrentFsm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmCurrentFsm.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmCurrentFsm.setDescription('Cisco UCS observe:ObservedFsm:currentFsm managed object property')
cucsObserveObservedFsmDescrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmDescrData.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmDescrData.setDescription('Cisco UCS observe:ObservedFsm:descr managed object property')
cucsObserveObservedFsmFsmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 7), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmFsmStatus.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmFsmStatus.setDescription('Cisco UCS observe:ObservedFsm:fsmStatus managed object property')
cucsObserveObservedFsmProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmProgress.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmProgress.setDescription('Cisco UCS observe:ObservedFsm:progress managed object property')
cucsObserveObservedFsmRmtErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtErrCode.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtErrCode.setDescription('Cisco UCS observe:ObservedFsm:rmtErrCode managed object property')
cucsObserveObservedFsmRmtErrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtErrDescr.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtErrDescr.setDescription('Cisco UCS observe:ObservedFsm:rmtErrDescr managed object property')
cucsObserveObservedFsmRmtRslt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 11), CucsConditionRemoteInvRslt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtRslt.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmRmtRslt.setDescription('Cisco UCS observe:ObservedFsm:rmtRslt managed object property')
cucsObserveObservedFsmStageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5), )
if mibBuilder.loadTexts: cucsObserveObservedFsmStageTable.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageTable.setDescription('Cisco UCS observe:ObservedFsmStage managed object table')
cucsObserveObservedFsmStageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedFsmStageInstanceId"))
if mibBuilder.loadTexts: cucsObserveObservedFsmStageEntry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageEntry.setDescription('Entry for the cucsObserveObservedFsmStageTable table.')
cucsObserveObservedFsmStageInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsObserveObservedFsmStageInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageInstanceId.setDescription('Instance identifier of the managed object.')
cucsObserveObservedFsmStageDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageDn.setDescription('Cisco UCS observe:ObservedFsmStage:dn managed object property')
cucsObserveObservedFsmStageRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageRn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageRn.setDescription('Cisco UCS observe:ObservedFsmStage:rn managed object property')
cucsObserveObservedFsmStageDescrData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageDescrData.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageDescrData.setDescription('Cisco UCS observe:ObservedFsmStage:descr managed object property')
cucsObserveObservedFsmStageLastUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageLastUpdateTime.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageLastUpdateTime.setDescription('Cisco UCS observe:ObservedFsmStage:lastUpdateTime managed object property')
cucsObserveObservedFsmStageName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 6), CucsObserveObservedFsmStageName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageName.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageName.setDescription('Cisco UCS observe:ObservedFsmStage:name managed object property')
cucsObserveObservedFsmStageOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageOrder.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageOrder.setDescription('Cisco UCS observe:ObservedFsmStage:order managed object property')
cucsObserveObservedFsmStageRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageRetry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageRetry.setDescription('Cisco UCS observe:ObservedFsmStage:retry managed object property')
cucsObserveObservedFsmStageStageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 9), CucsFsmFsmStageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmStageStageStatus.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmStageStageStatus.setDescription('Cisco UCS observe:ObservedFsmStage:stageStatus managed object property')
cucsObserveObservedFsmTaskTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6), )
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskTable.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskTable.setDescription('Cisco UCS observe:ObservedFsmTask managed object table')
cucsObserveObservedFsmTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedFsmTaskInstanceId"))
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskEntry.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskEntry.setDescription('Entry for the cucsObserveObservedFsmTaskTable table.')
cucsObserveObservedFsmTaskInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskInstanceId.setDescription('Instance identifier of the managed object.')
cucsObserveObservedFsmTaskDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskDn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskDn.setDescription('Cisco UCS observe:ObservedFsmTask:dn managed object property')
cucsObserveObservedFsmTaskRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskRn.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskRn.setDescription('Cisco UCS observe:ObservedFsmTask:rn managed object property')
cucsObserveObservedFsmTaskCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 4), CucsFsmCompletion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskCompletion.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskCompletion.setDescription('Cisco UCS observe:ObservedFsmTask:completion managed object property')
cucsObserveObservedFsmTaskFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 5), CucsFsmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskFlags.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskFlags.setDescription('Cisco UCS observe:ObservedFsmTask:flags managed object property')
cucsObserveObservedFsmTaskItem = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 6), CucsObserveObservedFsmTaskItem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskItem.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskItem.setDescription('Cisco UCS observe:ObservedFsmTask:item managed object property')
cucsObserveObservedFsmTaskSeqId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskSeqId.setStatus('current')
if mibBuilder.loadTexts: cucsObserveObservedFsmTaskSeqId.setDescription('Cisco UCS observe:ObservedFsmTask:seqId managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", cucsObserveObservedFsmStageRn=cucsObserveObservedFsmStageRn, cucsObserveObservedFsmCurrentFsm=cucsObserveObservedFsmCurrentFsm, cucsObserveObservedContRn=cucsObserveObservedContRn, cucsObserveObservedGenNum=cucsObserveObservedGenNum, cucsObserveFilterFilterPropId3=cucsObserveFilterFilterPropId3, cucsObserveFilterReplicateIfNoChild=cucsObserveFilterReplicateIfNoChild, cucsObserveObservedContIdCount=cucsObserveObservedContIdCount, cucsObserveObservedFsmStageLastUpdateTime=cucsObserveObservedFsmStageLastUpdateTime, cucsObserveFilterDn=cucsObserveFilterDn, cucsObserveObservedFsmStageInstanceId=cucsObserveObservedFsmStageInstanceId, cucsObserveObservedFsmRmtRslt=cucsObserveObservedFsmRmtRslt, cucsObserveObservedFsmProgr=cucsObserveObservedFsmProgr, cucsObserveFilterChildClassId=cucsObserveFilterChildClassId, cucsObserveObservedIsDeleted=cucsObserveObservedIsDeleted, cucsObserveObservedFsmRn=cucsObserveObservedFsmRn, cucsObserveObservedFsmStageRetry=cucsObserveObservedFsmStageRetry, cucsObserveFilterFilterClassId=cucsObserveFilterFilterClassId, cucsObserveObservedDataSrcSysId=cucsObserveObservedDataSrcSysId, cucsObserveObservedContInstanceId=cucsObserveObservedContInstanceId, cucsObserveObservedFsmEntry=cucsObserveObservedFsmEntry, cucsObserveFilterRn=cucsObserveFilterRn, cucsObserveObservedFsmTaskTable=cucsObserveObservedFsmTaskTable, cucsObserveObservedFsmStageStageStatus=cucsObserveObservedFsmStageStageStatus, cucsObserveObservedFsmDescr=cucsObserveObservedFsmDescr, cucsObserveObservedFsmRmtErrCode=cucsObserveObservedFsmRmtErrCode, cucsObserveObservedFsmRmtInvErrCode=cucsObserveObservedFsmRmtInvErrCode, cucsObserveFilterEntry=cucsObserveFilterEntry, cucsObserveObservedContEntry=cucsObserveObservedContEntry, cucsObserveObservedFsmTaskSeqId=cucsObserveObservedFsmTaskSeqId, cucsObserveObservedContDn=cucsObserveObservedContDn, cucsObserveFilterAndOperation=cucsObserveFilterAndOperation, cucsObserveFilterHierarchical=cucsObserveFilterHierarchical, cucsObserveObservedFsmTaskEntry=cucsObserveObservedFsmTaskEntry, cucsObserveFilterFilterPropValue2=cucsObserveFilterFilterPropValue2, cucsObserveObservedInstanceId=cucsObserveObservedInstanceId, cucsObserveObservedFsmFsmStatus=cucsObserveObservedFsmFsmStatus, cucsObserveObservedFsmDn=cucsObserveObservedFsmDn, cucsObserveObservedFsmTaskInstanceId=cucsObserveObservedFsmTaskInstanceId, cucsObserveObservedFsmTaskItem=cucsObserveObservedFsmTaskItem, cucsObserveFilterInstanceId=cucsObserveFilterInstanceId, cucsObserveObservedFsmStageEntry=cucsObserveObservedFsmStageEntry, cucsObserveObjects=cucsObserveObjects, cucsObserveObservedFsmStageDescrData=cucsObserveObservedFsmStageDescrData, cucsObserveObservedFsmProgress=cucsObserveObservedFsmProgress, cucsObserveFilterFilterPropId2=cucsObserveFilterFilterPropId2, cucsObserveObservedObservedDn=cucsObserveObservedObservedDn, cucsObserveObservedRn=cucsObserveObservedRn, cucsObserveObservedFsmTaskDn=cucsObserveObservedFsmTaskDn, cucsObserveFilterFilterPropValue1=cucsObserveFilterFilterPropValue1, cucsObserveObservedFsmRmtInvErrDescr=cucsObserveObservedFsmRmtInvErrDescr, cucsObserveObservedFsmTable=cucsObserveObservedFsmTable, cucsObserveObservedTable=cucsObserveObservedTable, cucsObserveFilterTable=cucsObserveFilterTable, cucsObserveObservedFsmStageTable=cucsObserveObservedFsmStageTable, cucsObserveObservedId=cucsObserveObservedId, cucsObserveObservedContTable=cucsObserveObservedContTable, cucsObserveObservedFsmDescrData=cucsObserveObservedFsmDescrData, cucsObserveFilterFilterPropId1=cucsObserveFilterFilterPropId1, cucsObserveFilterFilterPropValue3=cucsObserveFilterFilterPropValue3, cucsObserveObservedFsmInstanceId=cucsObserveObservedFsmInstanceId, cucsObserveObservedHierarchical=cucsObserveObservedHierarchical, cucsObserveObservedFsmCompletionTime=cucsObserveObservedFsmCompletionTime, PYSNMP_MODULE_ID=cucsObserveObjects, cucsObserveObservedDn=cucsObserveObservedDn, cucsObserveObservedFsmStageName=cucsObserveObservedFsmStageName, cucsObserveObservedFsmStageDescr=cucsObserveObservedFsmStageDescr, cucsObserveObservedFsmTaskCompletion=cucsObserveObservedFsmTaskCompletion, cucsObserveObservedFsmTaskFlags=cucsObserveObservedFsmTaskFlags, cucsObserveObservedFsmStageDn=cucsObserveObservedFsmStageDn, cucsObserveObservedFsmRmtInvRslt=cucsObserveObservedFsmRmtInvRslt, cucsObserveObservedDataSrcAppType=cucsObserveObservedDataSrcAppType, cucsObserveObservedFsmStageOrder=cucsObserveObservedFsmStageOrder, cucsObserveObservedFsmTry=cucsObserveObservedFsmTry, cucsObserveObservedFsmPrev=cucsObserveObservedFsmPrev, cucsObserveObservedFsmRmtErrDescr=cucsObserveObservedFsmRmtErrDescr, cucsObserveObservedFsmStamp=cucsObserveObservedFsmStamp, cucsObserveObservedEntry=cucsObserveObservedEntry, cucsObserveObservedFsmStatus=cucsObserveObservedFsmStatus, cucsObserveObservedFsmTaskRn=cucsObserveObservedFsmTaskRn)
