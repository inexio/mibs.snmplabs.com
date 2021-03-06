#
# PySNMP MIB module Dell-LAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-LAN-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
dellLan, dellLanCommon = mibBuilder.importSymbols("Dell-Vendor-MIB", "dellLan", "dellLanCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, ModuleIdentity, Bits, ObjectIdentity, NotificationType, Counter32, MibIdentifier, Gauge32, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "Bits", "ObjectIdentity", "NotificationType", "Counter32", "MibIdentifier", "Gauge32", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
dellAlarmGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1))
if mibBuilder.loadTexts: dellAlarmGroup.setLastUpdated('200504260000Z')
if mibBuilder.loadTexts: dellAlarmGroup.setOrganization('Dell.')
dellTrapInfo = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellTrapInfo.setStatus('current')
dellTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("clear", 0), ("info", 1), ("minor", 2), ("major", 3), ("critical", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellTrapSeverity.setStatus('current')
dellTrapSource = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellTrapSource.setStatus('current')
dellTrapSeqNum = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellTrapSeqNum.setStatus('current')
dellTrapTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellTrapTimeStamp.setStatus('current')
hwResourceOverflow = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 500)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: hwResourceOverflow.setStatus('current')
swResourceOverflow = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 510)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: swResourceOverflow.setStatus('current')
configChanged = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 520)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: configChanged.setStatus('current')
resetRequired = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 530)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: resetRequired.setStatus('current')
endTftp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 540)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: endTftp.setStatus('current')
abortTftp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 550)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: abortTftp.setStatus('current')
startTftp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 560)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: startTftp.setStatus('current')
linkFailure = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 570)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: linkFailure.setStatus('current')
linkFailureSwitchBackUp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 580)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: linkFailureSwitchBackUp.setStatus('current')
mainLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 590)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: mainLinkUp.setStatus('current')
errorsDuringInit = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 600)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: errorsDuringInit.setStatus('current')
vlanDynPortAdded = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 610)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vlanDynPortAdded.setStatus('current')
vlanDynPortRemoved = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 620)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vlanDynPortRemoved.setStatus('current')
ipZhrReqStaticConnNotAccepted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 630)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: ipZhrReqStaticConnNotAccepted.setStatus('current')
ipZhrVirtualIpAsSource = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 640)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: ipZhrVirtualIpAsSource.setStatus('current')
ipZhrNotAllocVirtualIp = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 650)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: ipZhrNotAllocVirtualIp.setStatus('current')
stackMasterFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 660)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackMasterFailed.setStatus('current')
stackNewMasterElected = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 670)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackNewMasterElected.setStatus('current')
stackMemberUnitFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 680)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackMemberUnitFailed.setStatus('current')
stackNewMemberUnitAdded = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 690)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackNewMemberUnitAdded.setStatus('current')
stackMemberUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 700)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackMemberUnitRemoved.setStatus('current')
stackSplitMasterReport = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 710)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackSplitMasterReport.setStatus('current')
stackSplitNewMasterReport = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 720)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackSplitNewMasterReport.setStatus('current')
stackRejoined = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 730)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackRejoined.setStatus('current')
stackLinkFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 740)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stackLinkFailed.setStatus('current')
dhcpAllocationFailure = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 750)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: dhcpAllocationFailure.setStatus('current')
dot1dStpPortStateForwarding = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 760)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: dot1dStpPortStateForwarding.setStatus('current')
dot1dStpPortStateNotForwarding = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 770)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: dot1dStpPortStateNotForwarding.setStatus('current')
policyDropPacketTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 780)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: policyDropPacketTrap.setStatus('current')
policyForwardPacketTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 790)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: policyForwardPacketTrap.setStatus('current')
igmpV1MsgReceived = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 800)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: igmpV1MsgReceived.setStatus('current')
vrrpEntriesDeleted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 810)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vrrpEntriesDeleted.setStatus('current')
trunkPortAddedTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 820)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: trunkPortAddedTrap.setStatus('current')
trunkPortRemovedTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 830)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: trunkPortRemovedTrap.setStatus('current')
lockPortTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 840)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: lockPortTrap.setStatus('current')
vlanDynVlanAdded = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 850)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vlanDynVlanAdded.setStatus('current')
vlanDynVlanRemoved = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 860)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vlanDynVlanRemoved.setStatus('current')
vlanDynamicToStatic = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 870)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vlanDynamicToStatic.setStatus('current')
vlanStaticToDynamic = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 880)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: vlanStaticToDynamic.setStatus('current')
envMonFanStateChange = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 890)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: envMonFanStateChange.setStatus('current')
envMonPowerSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 900)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: envMonPowerSupplyStateChange.setStatus('current')
envMonTemperatureRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 910)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: envMonTemperatureRisingAlarm.setStatus('current')
copyFinished = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 920)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: copyFinished.setStatus('current')
copyFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 930)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: copyFailed.setStatus('current')
dot1xPortStatusAuthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 940)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: dot1xPortStatusAuthorizedTrap.setStatus('current')
dot1xPortStatusUnauthorizedTrap = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 950)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: dot1xPortStatusUnauthorizedTrap.setStatus('current')
broadcastStormDetected = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 960)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: broadcastStormDetected.setStatus('current')
stpElectedAsRoot = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 970)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stpElectedAsRoot.setStatus('current')
stpNewRootElected = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 980)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: stpNewRootElected.setStatus('current')
igmpElectedAsQuerier = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 990)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: igmpElectedAsQuerier.setStatus('current')
invalidUserLoginAttempted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 1000)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: invalidUserLoginAttempted.setStatus('current')
managementACLViolation = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 1010)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: managementACLViolation.setStatus('current')
sfpInserted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 1020)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: sfpInserted.setStatus('current')
sfpRemoved = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 1030)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: sfpRemoved.setStatus('current')
xfpInserted = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 1040)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: xfpInserted.setStatus('current')
xfpRemoved = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 1050)).setObjects(("Dell-LAN-TRAP-MIB", "dellTrapTimeStamp"), ("Dell-LAN-TRAP-MIB", "dellTrapSeqNum"), ("Dell-LAN-TRAP-MIB", "dellTrapSource"), ("Dell-LAN-TRAP-MIB", "dellTrapSeverity"), ("Dell-LAN-TRAP-MIB", "dellTrapInfo"))
if mibBuilder.loadTexts: xfpRemoved.setStatus('current')
mibBuilder.exportSymbols("Dell-LAN-TRAP-MIB", dellTrapSource=dellTrapSource, policyDropPacketTrap=policyDropPacketTrap, trunkPortRemovedTrap=trunkPortRemovedTrap, xfpInserted=xfpInserted, stackMasterFailed=stackMasterFailed, vlanDynVlanRemoved=vlanDynVlanRemoved, vlanDynamicToStatic=vlanDynamicToStatic, PYSNMP_MODULE_ID=dellAlarmGroup, copyFailed=copyFailed, stpElectedAsRoot=stpElectedAsRoot, dellTrapTimeStamp=dellTrapTimeStamp, xfpRemoved=xfpRemoved, dot1dStpPortStateForwarding=dot1dStpPortStateForwarding, copyFinished=copyFinished, startTftp=startTftp, invalidUserLoginAttempted=invalidUserLoginAttempted, stackNewMasterElected=stackNewMasterElected, dellTrapInfo=dellTrapInfo, hwResourceOverflow=hwResourceOverflow, sfpRemoved=sfpRemoved, linkFailureSwitchBackUp=linkFailureSwitchBackUp, igmpV1MsgReceived=igmpV1MsgReceived, ipZhrVirtualIpAsSource=ipZhrVirtualIpAsSource, dellTrapSeqNum=dellTrapSeqNum, vlanDynPortAdded=vlanDynPortAdded, sfpInserted=sfpInserted, mainLinkUp=mainLinkUp, envMonPowerSupplyStateChange=envMonPowerSupplyStateChange, stackRejoined=stackRejoined, stackNewMemberUnitAdded=stackNewMemberUnitAdded, dot1xPortStatusUnauthorizedTrap=dot1xPortStatusUnauthorizedTrap, envMonFanStateChange=envMonFanStateChange, linkFailure=linkFailure, vlanDynPortRemoved=vlanDynPortRemoved, stackSplitNewMasterReport=stackSplitNewMasterReport, ipZhrReqStaticConnNotAccepted=ipZhrReqStaticConnNotAccepted, dot1dStpPortStateNotForwarding=dot1dStpPortStateNotForwarding, dellTrapSeverity=dellTrapSeverity, endTftp=endTftp, broadcastStormDetected=broadcastStormDetected, stpNewRootElected=stpNewRootElected, lockPortTrap=lockPortTrap, managementACLViolation=managementACLViolation, stackLinkFailed=stackLinkFailed, envMonTemperatureRisingAlarm=envMonTemperatureRisingAlarm, ipZhrNotAllocVirtualIp=ipZhrNotAllocVirtualIp, stackMemberUnitRemoved=stackMemberUnitRemoved, igmpElectedAsQuerier=igmpElectedAsQuerier, policyForwardPacketTrap=policyForwardPacketTrap, vrrpEntriesDeleted=vrrpEntriesDeleted, dot1xPortStatusAuthorizedTrap=dot1xPortStatusAuthorizedTrap, dellAlarmGroup=dellAlarmGroup, resetRequired=resetRequired, dhcpAllocationFailure=dhcpAllocationFailure, vlanStaticToDynamic=vlanStaticToDynamic, stackMemberUnitFailed=stackMemberUnitFailed, vlanDynVlanAdded=vlanDynVlanAdded, stackSplitMasterReport=stackSplitMasterReport, swResourceOverflow=swResourceOverflow, abortTftp=abortTftp, trunkPortAddedTrap=trunkPortAddedTrap, configChanged=configChanged, errorsDuringInit=errorsDuringInit)
