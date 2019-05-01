#
# PySNMP MIB module E5-110-AS-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/E5-110-AS-ATM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:58:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
accessSwitchCommonATM, = mibBuilder.importSymbols("E5-110-MIB", "accessSwitchCommonATM")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, ObjectIdentity, Bits, Counter64, TimeTicks, IpAddress, ModuleIdentity, MibIdentifier, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "ObjectIdentity", "Bits", "Counter64", "TimeTicks", "IpAddress", "ModuleIdentity", "MibIdentifier", "iso", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
asMaxNumOfChannels = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asMaxNumOfChannels.setStatus('mandatory')
if mibBuilder.loadTexts: asMaxNumOfChannels.setDescription('The maximum number of virtual channels which can be created on a port.')
asChannelTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2), )
if mibBuilder.loadTexts: asChannelTable.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelTable.setDescription('This table includes the configuration of the virtual channel.')
asChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "E5-110-AS-ATM-MIB", "asChannelVpi"), (0, "E5-110-AS-ATM-MIB", "asChannelVci"))
if mibBuilder.loadTexts: asChannelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelEntry.setDescription('An entry in asChannelTable.')
asChannelVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: asChannelVpi.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelVpi.setDescription('VPI of the channel.')
asChannelVci = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: asChannelVci.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelVci.setDescription('VCI of the channel.')
asChannelPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 3), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelPvid.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelPvid.setDescription('The default VID of the channel.')
asChannelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelPriority.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelPriority.setDescription('The 802.1p default priority of the channel.')
asChannelProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfile.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfile.setDescription('The value of this object identifies the row in the asChannelProfileTable, which applies for this channel.')
asChannelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table.')
asMaxNumOfChannelProfiles = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asMaxNumOfChannelProfiles.setStatus('mandatory')
if mibBuilder.loadTexts: asMaxNumOfChannelProfiles.setDescription('The maximum number of channel profiles which the system supports.')
asChannelProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6), )
if mibBuilder.loadTexts: asChannelProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileTable.setDescription('This table contains information on the virtual channel configuration. One entry in this table reflects a profile which can be used to configure the virtual channel.')
asChannelProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1), ).setIndexNames((1, "E5-110-AS-ATM-MIB", "asChannelProfileName"))
if mibBuilder.loadTexts: asChannelProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileEntry.setDescription('An entry in asChannelProfileTable.')
asChannelProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: asChannelProfileName.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileName.setDescription('This object is used by the channel profile table in order to identify a row of this table.')
asChannelProfileEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llc", 1), ("vc", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileEncap.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileEncap.setDescription('RFC1483 encapsulation.')
asChannelProfileAAL = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileAAL.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileAAL.setDescription('ATM Adaptation Layer policy.')
asChannelProfileClass = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cbr", 1), ("rt-vbr", 2), ("nrt-vbr", 3), ("ubr", 4), ("abr", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileClass.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileClass.setDescription('ATM traffic class, including constant bit rate, real-time variable bit rate, non real-time variable bit rate, unspecified bit rate, and available bit rate.')
asChannelProfilePcr = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfilePcr.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfilePcr.setDescription('Peak cell rate (cells/sec).')
asChannelProfileCdvt = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileCdvt.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileCdvt.setDescription('Cell delay variation tolerance.')
asChannelProfileScrMcr = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileScrMcr.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileScrMcr.setDescription('Sustain cell rate for vbr traffic class, or minimum cell rate for abr traffic class. The unit is the number of cells per second.')
asChannelProfileBt = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileBt.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileBt.setDescription('Burst tolerance for vbr traffic class.')
asChannelProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 6, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asChannelProfileRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelProfileRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table.')
asChannelStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7), )
if mibBuilder.loadTexts: asChannelStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelStatusTable.setDescription('This table includes the status of the virtual channel.')
asChannelStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "E5-110-AS-ATM-MIB", "asChannelVpi"), (0, "E5-110-AS-ATM-MIB", "asChannelVci"))
if mibBuilder.loadTexts: asChannelStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelStatusEntry.setDescription('An entry in asChannelStatusTable.')
asChannelTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelTxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelTxPackets.setDescription('Count of channel Tx packets.')
asChannelRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelRxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelRxPackets.setDescription('Count of channel Rx packets.')
asChannelTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelTxCells.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelTxCells.setDescription('Count of channel Tx cells.')
asChannelRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asChannelRxCells.setStatus('mandatory')
if mibBuilder.loadTexts: asChannelRxCells.setDescription('Count of channel Rx cells.')
asMaxNumOfIpqosProfiles = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asMaxNumOfIpqosProfiles.setStatus('mandatory')
if mibBuilder.loadTexts: asMaxNumOfIpqosProfiles.setDescription('The maximum number of ipqos profiles which the system supports.')
asIpqosProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9), )
if mibBuilder.loadTexts: asIpqosProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileTable.setDescription('This table contains information on the ipqos profile configuration. One entry in this table reflects a profile which can be used to configure the virtual channel.')
asIpqosProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1), ).setIndexNames((1, "E5-110-AS-ATM-MIB", "asIpqosProfileName"))
if mibBuilder.loadTexts: asIpqosProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileEntry.setDescription('An entry in asIpqosProfileTable.')
asIpqosProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpqosProfileName.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileName.setDescription('This object is used by the ipqos profile table in order to identify a row of this table.')
asIpqosProfileEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llc", 1), ("vc", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileEncap.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileEncap.setDescription('RFC1483 encapsulation.')
asIpqosProfileQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("four", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileQueueNumber.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileQueueNumber.setDescription('Number of Ipqos profile egress queue.')
asIpqosProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asIpqosProfileRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table.')
asIpqosProfileQueueTable = MibTable((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10), )
if mibBuilder.loadTexts: asIpqosProfileQueueTable.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileQueueTable.setDescription('This table contains information on the ipqos profile queue configuration.')
asIpqosProfileQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1), ).setIndexNames((0, "E5-110-AS-ATM-MIB", "asIpqosProfileName"), (1, "E5-110-AS-ATM-MIB", "asIpqosProfileQueueIndex"))
if mibBuilder.loadTexts: asIpqosProfileQueueEntry.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileQueueEntry.setDescription('An entry in asIpqosProfileTable.')
asIpqosProfileQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asIpqosProfileQueueIndex.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileQueueIndex.setDescription('The index of a ipqos profile egress queue.')
asIpqosProfileAAL = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileAAL.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileAAL.setDescription('ATM Adaptation Layer policy.')
asIpqosProfileLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ubr", 0), ("nrt-vbr", 1), ("rt-vbr", 2), ("cbr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileLevel.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileLevel.setDescription('ATM traffic class, including constant bit rate, real-time variable bit rate, non real-time variable bit rate, and unspecified bit rate.')
asIpqosProfileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 10, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asIpqosProfileRate.setStatus('mandatory')
if mibBuilder.loadTexts: asIpqosProfileRate.setDescription('Peak cell rate (cells/sec).')
asShapingMode = MibScalar((1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 1, 99, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("atm", 1), ("packet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asShapingMode.setStatus('mandatory')
if mibBuilder.loadTexts: asShapingMode.setDescription('The two types of shaping mechanism can not co-exist, and this variable is used to switch between these two types of shaping mechanism. To change to new shaping mode, E5-11x will remove all configured PVC, save current configuration and reboot automatically. After reboot, the new shaping mode can take effect.')
mibBuilder.exportSymbols("E5-110-AS-ATM-MIB", asChannelProfileScrMcr=asChannelProfileScrMcr, asIpqosProfileQueueIndex=asIpqosProfileQueueIndex, asChannelRxCells=asChannelRxCells, asChannelRowStatus=asChannelRowStatus, asChannelProfileName=asChannelProfileName, asIpqosProfileAAL=asIpqosProfileAAL, asChannelEntry=asChannelEntry, asIpqosProfileTable=asIpqosProfileTable, asChannelTxPackets=asChannelTxPackets, asChannelProfilePcr=asChannelProfilePcr, asChannelProfileBt=asChannelProfileBt, asChannelRxPackets=asChannelRxPackets, asChannelProfile=asChannelProfile, asIpqosProfileQueueEntry=asIpqosProfileQueueEntry, asShapingMode=asShapingMode, asChannelTable=asChannelTable, asChannelStatusTable=asChannelStatusTable, asChannelStatusEntry=asChannelStatusEntry, asIpqosProfileRowStatus=asIpqosProfileRowStatus, asChannelProfileEncap=asChannelProfileEncap, asChannelProfileAAL=asChannelProfileAAL, asIpqosProfileQueueTable=asIpqosProfileQueueTable, asMaxNumOfChannelProfiles=asMaxNumOfChannelProfiles, asMaxNumOfChannels=asMaxNumOfChannels, asChannelProfileEntry=asChannelProfileEntry, asChannelPvid=asChannelPvid, asChannelProfileCdvt=asChannelProfileCdvt, asChannelTxCells=asChannelTxCells, asChannelProfileClass=asChannelProfileClass, asChannelPriority=asChannelPriority, asIpqosProfileRate=asIpqosProfileRate, asChannelProfileTable=asChannelProfileTable, asChannelVpi=asChannelVpi, asIpqosProfileName=asIpqosProfileName, asChannelProfileRowStatus=asChannelProfileRowStatus, asIpqosProfileEncap=asIpqosProfileEncap, asChannelVci=asChannelVci, asIpqosProfileEntry=asIpqosProfileEntry, asIpqosProfileLevel=asIpqosProfileLevel, asIpqosProfileQueueNumber=asIpqosProfileQueueNumber, asMaxNumOfIpqosProfiles=asMaxNumOfIpqosProfiles)
