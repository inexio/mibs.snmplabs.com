#
# PySNMP MIB module HUAWEI-BRAS-RUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-RUI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, Bits, Unsigned32, MibIdentifier, ObjectIdentity, ModuleIdentity, NotificationType, Counter64, Gauge32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "Bits", "Unsigned32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "iso", "Integer32")
DisplayString, TextualConvention, RowStatus, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue", "MacAddress")
hwBRASRui = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19))
if mibBuilder.loadTexts: hwBRASRui.setLastUpdated('200504181334Z')
if mibBuilder.loadTexts: hwBRASRui.setOrganization(' NanJing Institute,Huawei Technologies Co.,Ltd. HuiHong Mansion,No.91 BaiXia Rd. NanJing, P.R. of China Zipcode:210001 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwBRASRui.setContactInfo('The MIB contains objects of module RUI.')
if mibBuilder.loadTexts: hwBRASRui.setDescription('Description.')
hwPeerBackupObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1))
hwPeerBackupEnableTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1))
hwPeerBackupEnableEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1))
hwPeerBackupEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("hotEnable", 2), ("warmEnable", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPeerBackupEnable.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupEnable.setDescription('Peer backup enable. ')
hwPeerBackupServerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2), )
if mibBuilder.loadTexts: hwPeerBackupServerTable.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerTable.setDescription('Peer backup server table. ')
hwPeerBackupServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1), ).setIndexNames((0, "HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerPeerIp"))
if mibBuilder.loadTexts: hwPeerBackupServerEntry.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerEntry.setDescription('Peer backup server table. ')
hwPeerBackupServerPeerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPeerBackupServerPeerIp.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerPeerIp.setDescription('IP address of the peer backup server. ')
hwPeerBackupServerLocalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPeerBackupServerLocalIp.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerLocalIp.setDescription('IP address of the local backup server. ')
hwPeerBackupServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 55535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPeerBackupServerPort.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerPort.setDescription('Port of the TCP connection. ')
hwPeerBackupServerDetectRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 12)).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPeerBackupServerDetectRetransmit.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerDetectRetransmit.setDescription('Number of events re-transmitting the detect packet,default is 8. ')
hwPeerBackupServerDetectInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 60)).clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPeerBackupServerDetectInterval.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerDetectInterval.setDescription('The interval of detecting tcp connection,default is 20 seconds. ')
hwPeerBackupServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPeerBackupServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerRowStatus.setDescription('Row admin status,only Add or Del. ')
hwRemoteBackupProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3), )
if mibBuilder.loadTexts: hwRemoteBackupProfileTable.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileTable.setDescription('Remote backup profile configuration table. ')
hwRemoteBackupProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1), ).setIndexNames((0, "HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIndex"))
if mibBuilder.loadTexts: hwRemoteBackupProfileEntry.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileEntry.setDescription('Remote backup profile configuration table. ')
hwRemoteBackupProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRemoteBackupProfileIndex.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileIndex.setDescription('Remote backup profile index. ')
hwRemoteBackupProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileName.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileName.setDescription('Remote backup profile name. ')
hwRemoteBackupProfilePeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfilePeerIP.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfilePeerIP.setDescription('Configure peer IP address in remote backup profile. ')
hwRemoteBackupProfileVrrpID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileVrrpID.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileVrrpID.setDescription('Configure VrrpID in remote backup profile. ')
hwRemoteBackupProfileBackupID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 4095), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileBackupID.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileBackupID.setDescription('Configure BackupID in remote backup proflie ,need configure PeerIP first. ')
hwRemoteBackupProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileRowStatus.setDescription('Row admin status,only Add or Del. ')
hwRemoteBackupProfileExtTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4), )
if mibBuilder.loadTexts: hwRemoteBackupProfileExtTable.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileExtTable.setDescription('Remote backup profile configuration extend table. ')
hwRemoteBackupProfileExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1), ).setIndexNames((0, "HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIndex"), (0, "HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIPPoolBindIndex"))
if mibBuilder.loadTexts: hwRemoteBackupProfileExtEntry.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileExtEntry.setDescription('Remote backup profile configuration extend table. ')
hwRemoteBackupProfileIPPoolBindIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRemoteBackupProfileIPPoolBindIndex.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileIPPoolBindIndex.setDescription('Ip pool bound Index. ')
hwRemoteBackupProfileIPPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 4096), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileIPPoolIndex.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileIPPoolIndex.setDescription('Ip pool bound by remote backup profile. ')
hwRemoteBackupProfileDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileDomainName.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileDomainName.setDescription('Domain bound by remote backup profile, need bind ip pool first. ')
hwRemoteBackupProfileExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRemoteBackupProfileExtRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileExtRowStatus.setDescription('Row admin status,only Add or Del. ')
hwRuiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2))
hwRuiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 1))
hwRuiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 1, 1)).setObjects(("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupEnableGroup"), ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerGroup"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileGroup"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRuiCompliance = hwRuiCompliance.setStatus('current')
if mibBuilder.loadTexts: hwRuiCompliance.setDescription('The compliance statement for systems supporting the this module.')
hwRuiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2))
hwPeerBackupEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 1)).setObjects(("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPeerBackupEnableGroup = hwPeerBackupEnableGroup.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupEnableGroup.setDescription('The RUI peer backup enable group.')
hwPeerBackupServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 2)).setObjects(("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerPeerIp"), ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerLocalIp"), ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerPort"), ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerDetectRetransmit"), ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerDetectInterval"), ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPeerBackupServerGroup = hwPeerBackupServerGroup.setStatus('current')
if mibBuilder.loadTexts: hwPeerBackupServerGroup.setDescription('The peer backup server group.')
hwRemoteBackupProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 3)).setObjects(("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIndex"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileName"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfilePeerIP"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileVrrpID"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileBackupID"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRemoteBackupProfileGroup = hwRemoteBackupProfileGroup.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileGroup.setDescription('The remote backup profile group.')
hwRemoteBackupProfileExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 4)).setObjects(("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIPPoolBindIndex"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIPPoolIndex"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileDomainName"), ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileExtRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwRemoteBackupProfileExtGroup = hwRemoteBackupProfileExtGroup.setStatus('current')
if mibBuilder.loadTexts: hwRemoteBackupProfileExtGroup.setDescription('The RUI peer backup enable extern group.')
mibBuilder.exportSymbols("HUAWEI-BRAS-RUI-MIB", hwRemoteBackupProfileIPPoolIndex=hwRemoteBackupProfileIPPoolIndex, hwRemoteBackupProfilePeerIP=hwRemoteBackupProfilePeerIP, hwPeerBackupServerLocalIp=hwPeerBackupServerLocalIp, hwRemoteBackupProfileIndex=hwRemoteBackupProfileIndex, hwBRASRui=hwBRASRui, hwPeerBackupEnableEntry=hwPeerBackupEnableEntry, hwRemoteBackupProfileIPPoolBindIndex=hwRemoteBackupProfileIPPoolBindIndex, hwRemoteBackupProfileVrrpID=hwRemoteBackupProfileVrrpID, hwPeerBackupEnableGroup=hwPeerBackupEnableGroup, hwPeerBackupServerEntry=hwPeerBackupServerEntry, hwPeerBackupServerDetectRetransmit=hwPeerBackupServerDetectRetransmit, hwRemoteBackupProfileExtEntry=hwRemoteBackupProfileExtEntry, hwRemoteBackupProfileDomainName=hwRemoteBackupProfileDomainName, hwRuiCompliances=hwRuiCompliances, hwRuiConformance=hwRuiConformance, hwRuiCompliance=hwRuiCompliance, hwPeerBackupServerGroup=hwPeerBackupServerGroup, hwPeerBackupEnable=hwPeerBackupEnable, hwRemoteBackupProfileBackupID=hwRemoteBackupProfileBackupID, hwPeerBackupServerRowStatus=hwPeerBackupServerRowStatus, hwRemoteBackupProfileExtTable=hwRemoteBackupProfileExtTable, hwPeerBackupEnableTable=hwPeerBackupEnableTable, hwRemoteBackupProfileEntry=hwRemoteBackupProfileEntry, hwRemoteBackupProfileRowStatus=hwRemoteBackupProfileRowStatus, hwRemoteBackupProfileExtGroup=hwRemoteBackupProfileExtGroup, hwPeerBackupServerTable=hwPeerBackupServerTable, hwPeerBackupServerDetectInterval=hwPeerBackupServerDetectInterval, PYSNMP_MODULE_ID=hwBRASRui, hwRemoteBackupProfileName=hwRemoteBackupProfileName, hwPeerBackupObject=hwPeerBackupObject, hwRemoteBackupProfileExtRowStatus=hwRemoteBackupProfileExtRowStatus, hwPeerBackupServerPort=hwPeerBackupServerPort, hwRemoteBackupProfileGroup=hwRemoteBackupProfileGroup, hwRemoteBackupProfileTable=hwRemoteBackupProfileTable, hwRuiGroups=hwRuiGroups, hwPeerBackupServerPeerIp=hwPeerBackupServerPeerIp)
