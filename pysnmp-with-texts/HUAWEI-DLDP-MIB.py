#
# PySNMP MIB module HUAWEI-DLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DLDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Bits, Gauge32, ModuleIdentity, NotificationType, iso, MibIdentifier, Counter32, Counter64, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Bits", "Gauge32", "ModuleIdentity", "NotificationType", "iso", "MibIdentifier", "Counter32", "Counter64", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue", "MacAddress")
hwDldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173))
if mibBuilder.loadTexts: hwDldpMIB.setLastUpdated('200807151430Z')
if mibBuilder.loadTexts: hwDldpMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwDldpMIB.setContactInfo('R&D NanJing, Huawei Technologies co.,Ltd. High hope mansion, Baixia road, Nanjing city Zip:100085 Http://www.huawei.com E-mail:support@huawei.com Zip:100000 ')
if mibBuilder.loadTexts: hwDldpMIB.setDescription('This file is a DLDP-MIB. It provides the functions such as globally enabling or disabling the DLDP protocol, enabling the global alarm, clearing statistics on ports and configuring work mode.')
class PortIndex(TextualConvention, Integer32):
    description = 'Each port is uniquely identified by a port number. The port number ranges from 0 to 575.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 575)

hwDldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1))
hwDldpPortTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2))
hwDldpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3))
hwDldpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4))
hwDldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1))
hwDldpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2))
hwDldpEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpEnable.setStatus('current')
if mibBuilder.loadTexts: hwDldpEnable.setDescription('Globally enable or disable the DLDP configuration. If the hwDldpEnable is 1, DLDP is enabled. If the hwDldpEnable is 2, DLDP is disabled. By default, DLDP is disabled.')
hwDldpUnidirectionalShutdown = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpUnidirectionalShutdown.setStatus('current')
if mibBuilder.loadTexts: hwDldpUnidirectionalShutdown.setDescription('When the device discovers a one-way link, the shutdown mode of port. The modes include auto and manual. By default, DLDP is auto.')
hwDldpWorkMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("enhance", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpWorkMode.setStatus('current')
if mibBuilder.loadTexts: hwDldpWorkMode.setDescription('It configures the work mode of the DLDP protocol, including normal and enhanced mode. By default, the mode is enhanced.')
hwDldpAdvertInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpAdvertInterval.setStatus('current')
if mibBuilder.loadTexts: hwDldpAdvertInterval.setDescription('Global interval for sending advertisement packets for the DLDP configuration. By default, the interval is 5s.')
hwDelayDownTimer = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDelayDownTimer.setStatus('current')
if mibBuilder.loadTexts: hwDelayDownTimer.setDescription('Global timeout of DelayDown timer. The value rangs from 1s to 5s, By default, the time is 1s.')
hwDldpAuthenMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("md5", 2), ("simple", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpAuthenMode.setStatus('current')
if mibBuilder.loadTexts: hwDldpAuthenMode.setDescription('Global authentication mode of the DLDP configuration. It has three authentication modes, including none, md5,and simple. By default the authentication mode is none.')
hwDldpMd5Password = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpMd5Password.setStatus('current')
if mibBuilder.loadTexts: hwDldpMd5Password.setDescription('Global md5 password for authentication when authentication is md5.')
hwDldpSimplePassword = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDldpSimplePassword.setStatus('current')
if mibBuilder.loadTexts: hwDldpSimplePassword.setDescription('Global simple password for authentication when authentication is simple.')
hwDldpPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9), )
if mibBuilder.loadTexts: hwDldpPortTable.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortTable.setDescription('DLDP port configuration table.')
hwDldpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1), ).setIndexNames((0, "HUAWEI-DLDP-MIB", "hwDldpPortIndex"))
if mibBuilder.loadTexts: hwDldpPortEntry.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortEntry.setDescription('Entries of the DLDP port configuration table.')
hwDldpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 1), PortIndex())
if mibBuilder.loadTexts: hwDldpPortIndex.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortIndex.setDescription('It describes enabled DLDP port index. Each port is uniquely identified by a port number. It ranges from 0 to 575.')
hwDldpPortStateReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDldpPortStateReset.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStateReset.setDescription('It describes the DLDP status of the reset port.')
hwDldpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("initial", 1), ("inactive", 2), ("active", 3), ("advertisement", 4), ("probe", 5), ("disable", 6), ("delayDown", 7), ("loop", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortState.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortState.setDescription('Port state has seven states, including initial, inactive, active, advertisement, probe, disable, and delayDown.')
hwDldpPortLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortLinkState.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortLinkState.setDescription('Port state has two modes, including up and down.')
hwDldpResetStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDldpResetStatistics.setStatus('current')
if mibBuilder.loadTexts: hwDldpResetStatistics.setDescription('It clears the statistics of packets received and sent on the current port.')
hwDldpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 9, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwDldpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwDldpRowStatus.setDescription(' Operation of CreateAndGo can be used to create a new instance, and operation of Destroy be used to destroy an existent index. But these operations will not take effect if they are not activated by running the command of activating or setting mib node of hwDldpEnable.')
hwDldpNeighbourTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10), )
if mibBuilder.loadTexts: hwDldpNeighbourTable.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourTable.setDescription('DLDP Neighbour configuration table.')
hwDldpNeighbourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1), ).setIndexNames((0, "HUAWEI-DLDP-MIB", "hwDldpPortIndex"), (0, "HUAWEI-DLDP-MIB", "hwDldpNeighbourMacAddr"), (0, "HUAWEI-DLDP-MIB", "hwDldpNeighbourPortIndex"))
if mibBuilder.loadTexts: hwDldpNeighbourEntry.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourEntry.setDescription('Entries of the DLDP Neighbour configuration table.')
hwDldpNeighbourMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 1), MacAddress())
if mibBuilder.loadTexts: hwDldpNeighbourMacAddr.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourMacAddr.setDescription('When the activated port detects a neighbor, it can record the neighbor information, including MAC address of neighbor. The port may detect multiple neighbors.')
hwDldpNeighbourPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hwDldpNeighbourPortIndex.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourPortIndex.setDescription('When the activated port detects a neighbor, it can record the port index of the neighbour.')
hwDldpNeighbourPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpNeighbourPortName.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourPortName.setDescription('When the activated port detects a neighbor, it can record the port name of the neighbour.')
hwDldpNeighbourState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("oneWay", 2), ("twoWay", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpNeighbourState.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourState.setDescription('When the activated port detects a neighbor, it can record the state of the neighbour, and its value includes unknown, one way, and two way.')
hwDldpNeighbourAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpNeighbourAgeTime.setStatus('current')
if mibBuilder.loadTexts: hwDldpNeighbourAgeTime.setDescription('When the activated port detects a neighbor, it can record the aging time of the neighbor. The aging time is three times the interval for sending advertisement packets.')
hwDldpPortStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1), )
if mibBuilder.loadTexts: hwDldpPortStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsTable.setDescription('DLDP port statics configuration table.')
hwDldpPortStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1), ).setIndexNames((0, "HUAWEI-DLDP-MIB", "hwDldpPortIndex"))
if mibBuilder.loadTexts: hwDldpPortStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsEntry.setDescription('Entries of the table of the packets sent or received on the DLDP port.')
hwDldpPortStatisticsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortStatisticsTx.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsTx.setDescription('It describes the number of packets sent on the activated port.')
hwDldpPortStatisticsRxTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortStatisticsRxTotal.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsRxTotal.setDescription('It describes the number of packets received on the activated port.')
hwDldpPortStatisticsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortStatisticsRxError.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsRxError.setDescription('It describes the number of error packets received on the activated port.')
hwDldpPortStatisticsRxLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortStatisticsRxLoop.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsRxLoop.setDescription('It describes the number of loop packets received on the activated port.')
hwDldpPortStatisticsRxValid = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortStatisticsRxValid.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsRxValid.setDescription('It describes the number of valid packets received on the activated port.')
hwDldpPortStatisticsRxAuthenFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDldpPortStatisticsRxAuthenFail.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortStatisticsRxAuthenFail.setDescription('It describes the number of authentication failure packets received on the activated port.')
hwDldpTrapInterfaceIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwDldpTrapInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: hwDldpTrapInterfaceIndex.setDescription('It describes the interface index of the activated port that detected one way or found that two way is resumed.')
hwDldpTrapIfName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwDldpTrapIfName.setStatus('current')
if mibBuilder.loadTexts: hwDldpTrapIfName.setDescription('It describes the interface name of the activated port that detected one way or found that two way is resumed.')
hwDldpTrapFaultReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwDldpTrapFaultReason.setStatus('current')
if mibBuilder.loadTexts: hwDldpTrapFaultReason.setDescription('It describes the reason interface fault.')
hwDldpUnidirectionalLink = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 1)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"), ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"), ("HUAWEI-DLDP-MIB", "hwDldpTrapFaultReason"))
if mibBuilder.loadTexts: hwDldpUnidirectionalLink.setStatus('current')
if mibBuilder.loadTexts: hwDldpUnidirectionalLink.setDescription('Notify the NMS that the DLDP detected one way. The hwDldpTrapInterfaceIndex node is the interface index.')
hwDldpLinkResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 2)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"), ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
if mibBuilder.loadTexts: hwDldpLinkResume.setStatus('current')
if mibBuilder.loadTexts: hwDldpLinkResume.setDescription('Notify the NMS that the DLDP detected that unidirectional link was resumed. The hwDldpTrapInterfaceIndex node is interface index.')
hwDldpLoopDetect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 3)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"), ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
if mibBuilder.loadTexts: hwDldpLoopDetect.setStatus('current')
if mibBuilder.loadTexts: hwDldpLoopDetect.setDescription('Notify the NMS that the DLDP detected Loop State. The hwDldpTrapInterfaceIndex node is the interface index.')
hwDldpLoopResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 3, 4)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"), ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
if mibBuilder.loadTexts: hwDldpLoopResume.setStatus('current')
if mibBuilder.loadTexts: hwDldpLoopResume.setDescription('Notify the NMS that the DLDP detected Loop State was resumed. The hwDldpTrapInterfaceIndex node is interface index.')
hwDldpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 1))
hwDldpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2))
hwDldpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 1, 1)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpConfigGroup"), ("HUAWEI-DLDP-MIB", "hwDldpStatisticsGroup"), ("HUAWEI-DLDP-MIB", "hwDldpPortGroup"), ("HUAWEI-DLDP-MIB", "hwDldpPortTrapGroup"), ("HUAWEI-DLDP-MIB", "hwDldpTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDldpCompliance = hwDldpCompliance.setStatus('current')
if mibBuilder.loadTexts: hwDldpCompliance.setDescription('The compliance statement for SNMP entities which implement the HUAWEI-DLDP-MIB.')
hwDldpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 1)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpEnable"), ("HUAWEI-DLDP-MIB", "hwDldpUnidirectionalShutdown"), ("HUAWEI-DLDP-MIB", "hwDldpWorkMode"), ("HUAWEI-DLDP-MIB", "hwDldpAdvertInterval"), ("HUAWEI-DLDP-MIB", "hwDelayDownTimer"), ("HUAWEI-DLDP-MIB", "hwDldpAuthenMode"), ("HUAWEI-DLDP-MIB", "hwDldpMd5Password"), ("HUAWEI-DLDP-MIB", "hwDldpSimplePassword"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDldpConfigGroup = hwDldpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hwDldpConfigGroup.setDescription('The collection of objects which are used to configure the DLDP implementation behavior. This group is mandatory for agents which implement the DLDP.')
hwDldpStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 2)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsTx"), ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxTotal"), ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxError"), ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxLoop"), ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxValid"), ("HUAWEI-DLDP-MIB", "hwDldpPortStatisticsRxAuthenFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDldpStatisticsGroup = hwDldpStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: hwDldpStatisticsGroup.setDescription('The collection of objects which are used to represent DLDP statistics. This group is mandatory for agents which implement the DLDP and have the capability of receiving and transmitting DLDP frames.')
hwDldpPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 3)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpPortStateReset"), ("HUAWEI-DLDP-MIB", "hwDldpPortState"), ("HUAWEI-DLDP-MIB", "hwDldpPortLinkState"), ("HUAWEI-DLDP-MIB", "hwDldpResetStatistics"), ("HUAWEI-DLDP-MIB", "hwDldpRowStatus"), ("HUAWEI-DLDP-MIB", "hwDldpNeighbourPortName"), ("HUAWEI-DLDP-MIB", "hwDldpNeighbourState"), ("HUAWEI-DLDP-MIB", "hwDldpNeighbourAgeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDldpPortGroup = hwDldpPortGroup.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortGroup.setDescription('The collection of objects indicates the information of port.')
hwDldpPortTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 4)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpTrapInterfaceIndex"), ("HUAWEI-DLDP-MIB", "hwDldpTrapIfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDldpPortTrapGroup = hwDldpPortTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwDldpPortTrapGroup.setDescription('The collection of objects indicates that the activated port index detected one way or found that two way is resumed.')
hwDldpTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 173, 4, 2, 5)).setObjects(("HUAWEI-DLDP-MIB", "hwDldpUnidirectionalLink"), ("HUAWEI-DLDP-MIB", "hwDldpLinkResume"), ("HUAWEI-DLDP-MIB", "hwDldpLoopDetect"), ("HUAWEI-DLDP-MIB", "hwDldpLoopResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDldpTrapGroup = hwDldpTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwDldpTrapGroup.setDescription('The collection of notifications used to indicate that the HUAWEI-DLDP-MIB data is consistent and indicate the general status information. This group is mandatory for agents which implement the DLDP and have the capability of receiving DLDP frames.')
mibBuilder.exportSymbols("HUAWEI-DLDP-MIB", hwDldpLoopResume=hwDldpLoopResume, hwDldpLoopDetect=hwDldpLoopDetect, hwDldpNeighbourMacAddr=hwDldpNeighbourMacAddr, hwDldpTraps=hwDldpTraps, hwDldpPortStatisticsRxLoop=hwDldpPortStatisticsRxLoop, hwDldpPortLinkState=hwDldpPortLinkState, hwDldpPortTrapGroup=hwDldpPortTrapGroup, hwDldpUnidirectionalLink=hwDldpUnidirectionalLink, hwDldpMd5Password=hwDldpMd5Password, hwDldpPortStatisticsRxError=hwDldpPortStatisticsRxError, hwDldpStatistics=hwDldpStatistics, PortIndex=PortIndex, hwDldpTrapInterfaceIndex=hwDldpTrapInterfaceIndex, hwDldpResetStatistics=hwDldpResetStatistics, hwDldpPortStatisticsRxTotal=hwDldpPortStatisticsRxTotal, hwDldpPortTable=hwDldpPortTable, hwDldpRowStatus=hwDldpRowStatus, hwDldpPortStateReset=hwDldpPortStateReset, hwDldpStatisticsGroup=hwDldpStatisticsGroup, hwDldpPortStatisticsEntry=hwDldpPortStatisticsEntry, hwDldpPortStatisticsRxValid=hwDldpPortStatisticsRxValid, hwDldpPortGroup=hwDldpPortGroup, hwDldpSimplePassword=hwDldpSimplePassword, hwDldpNeighbourPortIndex=hwDldpNeighbourPortIndex, hwDldpNeighbourTable=hwDldpNeighbourTable, hwDldpAuthenMode=hwDldpAuthenMode, hwDldpNeighbourAgeTime=hwDldpNeighbourAgeTime, hwDldpPortStatisticsTx=hwDldpPortStatisticsTx, hwDldpCompliance=hwDldpCompliance, hwDldpUnidirectionalShutdown=hwDldpUnidirectionalShutdown, hwDldpObjects=hwDldpObjects, hwDldpConfiguration=hwDldpConfiguration, hwDldpPortIndex=hwDldpPortIndex, hwDldpCompliances=hwDldpCompliances, hwDldpConformance=hwDldpConformance, hwDldpLinkResume=hwDldpLinkResume, hwDldpTrapFaultReason=hwDldpTrapFaultReason, hwDldpEnable=hwDldpEnable, hwDldpGroups=hwDldpGroups, hwDldpTrapGroup=hwDldpTrapGroup, hwDldpAdvertInterval=hwDldpAdvertInterval, hwDldpPortState=hwDldpPortState, hwDldpNeighbourPortName=hwDldpNeighbourPortName, hwDldpTrapIfName=hwDldpTrapIfName, hwDldpConfigGroup=hwDldpConfigGroup, hwDldpPortEntry=hwDldpPortEntry, hwDldpPortStatisticsRxAuthenFail=hwDldpPortStatisticsRxAuthenFail, PYSNMP_MODULE_ID=hwDldpMIB, hwDldpPortStatisticsTable=hwDldpPortStatisticsTable, hwDldpPortTrapObjects=hwDldpPortTrapObjects, hwDldpWorkMode=hwDldpWorkMode, hwDldpNeighbourEntry=hwDldpNeighbourEntry, hwDldpMIB=hwDldpMIB, hwDelayDownTimer=hwDelayDownTimer, hwDldpNeighbourState=hwDldpNeighbourState)
