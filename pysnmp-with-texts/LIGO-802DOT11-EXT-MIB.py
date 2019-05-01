#
# PySNMP MIB module LIGO-802DOT11-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGO-802DOT11-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:07:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, ifPhysAddress, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifPhysAddress", "ifIndex")
ligoMgmt, = mibBuilder.importSymbols("LIGOWAVE-MIB", "ligoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Integer32, Gauge32, iso, NotificationType, Counter64, Unsigned32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Integer32", "Gauge32", "iso", "NotificationType", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity")
MacAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TruthValue")
ligo802dot11ExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750, 3, 5))
ligo802dot11ExtMIB.setRevisions(('2010-03-31 00:00', '2009-05-15 00:00', '2008-12-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ligo802dot11ExtMIB.setRevisionsDescriptions(('Added ligoDot11IfAssocNodeCount.', 'Added ligoDot11RemoteNodeStatsTable and ligoRemoteNodeConnected, ligoRemoteNodeDisconnected notifications.', 'First revision.',))
if mibBuilder.loadTexts: ligo802dot11ExtMIB.setLastUpdated('201003310000Z')
if mibBuilder.loadTexts: ligo802dot11ExtMIB.setOrganization('LigoWave')
if mibBuilder.loadTexts: ligo802dot11ExtMIB.setContactInfo(' LigoWave Customer Support E-mail: support@ligowave.com')
if mibBuilder.loadTexts: ligo802dot11ExtMIB.setDescription('The LigoWave 802.11 Extension MIB.')
ligo802dot11ExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1))
ligoDot11Notifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0))
ligoDot11Info = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 1))
ligoDot11Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2))
ligoDot11Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3))
ligoDot11IfConfTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1), )
if mibBuilder.loadTexts: ligoDot11IfConfTable.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfConfTable.setDescription('Wireless interface configuration table.')
ligoDot11IfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ligoDot11IfConfEntry.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfConfEntry.setDescription('Wireless interface configuration table entry.')
ligoDot11IfParentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfParentIndex.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfParentIndex.setDescription("Wireless interface's parent index, which corresponds to ifIndex in MIB-II interfaces table. This is only applicable if the interface is virtual and it is created under some other interface, like it is for Atheros cards when using MadWiFi driver, where parent interfaces are wifi0, wifi1, etc.")
ligoDot11IfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfProtocol.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfProtocol.setDescription("Protocol string, for example 'IEEE 802.11g'.")
ligoDot11IfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("adhoc", 1), ("managed", 2), ("master", 3), ("repeater", 4), ("secondary", 5), ("monitor", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfMode.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfMode.setDescription('Wireless interface operation mode')
ligoDot11IfESSID = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfESSID.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfESSID.setDescription('ESSID')
ligoDot11IfAccessPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfAccessPoint.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfAccessPoint.setDescription("Access point's MAC address if working in managed mode and connected. Current interface's MAC address, when working in master mode.")
ligoDot11IfCountryCode = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfCountryCode.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfCountryCode.setDescription('Country code.')
ligoDot11IfFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 7), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfFrequency.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfFrequency.setDescription('Current frequency as reported by driver.')
ligoDot11IfChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfChannel.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfChannel.setDescription('Channel number.')
ligoDot11IfChannelBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 9), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfChannelBandwidth.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfChannelBandwidth.setDescription('Channel bandwidth.')
ligoDot11IfTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 10), Gauge32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfTxPower.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfTxPower.setDescription('Transmit power in dBm.')
ligoDot11IfBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 11), Gauge32()).setUnits('kbit/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfBitRate.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfBitRate.setDescription('Transmission bitrate.')
ligoDot11IfLinkQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfLinkQuality.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfLinkQuality.setDescription('Link quality value.')
ligoDot11IfMaxLinkQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfMaxLinkQuality.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfMaxLinkQuality.setDescription('Maximum possible link quality value for current wireless card.')
ligoDot11IfSignalLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 14), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfSignalLevel.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfSignalLevel.setDescription('Signal level.')
ligoDot11IfNoiseLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 15), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfNoiseLevel.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfNoiseLevel.setDescription('Noise level.')
ligoDot11IfAssocNodeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfAssocNodeCount.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfAssocNodeCount.setDescription('Number of associated nodes when working in access point mode. 1 - if associated to remote access point in client mode.')
ligoDot11IfErrStatsTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1), )
if mibBuilder.loadTexts: ligoDot11IfErrStatsTable.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfErrStatsTable.setDescription('Wireless interface statistics table.')
ligoDot11IfErrStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ligoDot11IfErrStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfErrStatsEntry.setDescription('Wireless interface statistics table entry.')
ligoDot11IfRxInvalidNWID = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfRxInvalidNWID.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfRxInvalidNWID.setDescription('Number of received packets with invalid NWID/ESSID. Increasing value usually means that there are other stations transmitting on the same channel or adjacent channels.')
ligoDot11IfRxInvalidCrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfRxInvalidCrypt.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfRxInvalidCrypt.setDescription('Number of received packets the hardware was unable to decrypt.')
ligoDot11IfRxInvalidFrag = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfRxInvalidFrag.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfRxInvalidFrag.setDescription('Number of received packets that were missing link layer fragments for complete re-assembly.')
ligoDot11IfTxExcessiveRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfTxExcessiveRetries.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfTxExcessiveRetries.setDescription('Number of packets hardware failed to deliver.')
ligoDot11IfInvalidMisc = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfInvalidMisc.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfInvalidMisc.setDescription('Other packets lost in relation with specific wireless operations.')
ligoDot11IfMissedBeacons = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11IfMissedBeacons.setStatus('current')
if mibBuilder.loadTexts: ligoDot11IfMissedBeacons.setDescription('Number of beacons that should have been sent by remote access point but were not received. Increasing number usually means that communicating peers moved out of range.')
ligoDot11RemoteNodeStatsTable = MibTable((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2), )
if mibBuilder.loadTexts: ligoDot11RemoteNodeStatsTable.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RemoteNodeStatsTable.setDescription('Remote node statistics table. This table shows statistics for associated or already disconnected clients on wireless interfaces which are operating in access point mode. For interfaces operating in client mode and associated to remote access point information about access point is shown.')
ligoDot11RemoteNodeStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "LIGO-802DOT11-EXT-MIB", "ligoDot11RmtNodeMacAddress"))
if mibBuilder.loadTexts: ligoDot11RemoteNodeStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RemoteNodeStatsEntry.setDescription('Wireless remote node statistics table entry.')
ligoDot11RmtNodeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11RmtNodeMacAddress.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RmtNodeMacAddress.setDescription('Remote node MAC address.')
ligoDot11RmtNodeAssociated = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11RmtNodeAssociated.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RmtNodeAssociated.setDescription('Remote node is currently associated.')
ligoDot11RmtNodeTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 3), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11RmtNodeTxBytes.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RmtNodeTxBytes.setDescription('Bytes transmitted to remote node. This object is optional.')
ligoDot11RmtNodeRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11RmtNodeRxBytes.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RmtNodeRxBytes.setDescription('Bytes received from remote node. This object is optional.')
ligoDot11RmtNodeAssocTime = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11RmtNodeAssocTime.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RmtNodeAssocTime.setDescription('UNIX timestamp of the association. This object is optional.')
ligoDot11RmtNodeDisassocTime = MibTableColumn((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ligoDot11RmtNodeDisassocTime.setStatus('current')
if mibBuilder.loadTexts: ligoDot11RmtNodeDisassocTime.setDescription('UNIX timestamp of the disassociation (if remote node recently dissasociated). This object is optional.')
ligoFrequencyChange = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-802DOT11-EXT-MIB", "ligoDot11IfFrequency"))
if mibBuilder.loadTexts: ligoFrequencyChange.setStatus('current')
if mibBuilder.loadTexts: ligoFrequencyChange.setDescription('This notification is sent on frequency change.')
ligoNoiseThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-802DOT11-EXT-MIB", "ligoDot11IfNoiseLevel"))
if mibBuilder.loadTexts: ligoNoiseThresholdReached.setStatus('current')
if mibBuilder.loadTexts: ligoNoiseThresholdReached.setDescription('This notification is sent when noise becomes bigger than threshold.')
ligoRemoteNodeConnected = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 3)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifPhysAddress"), ("IF-MIB", "ifIndex"), ("LIGO-802DOT11-EXT-MIB", "ligoDot11RmtNodeMacAddress"))
if mibBuilder.loadTexts: ligoRemoteNodeConnected.setStatus('current')
if mibBuilder.loadTexts: ligoRemoteNodeConnected.setDescription('This notification is sent when remote node associates.')
ligoRemoteNodeDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 4)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifPhysAddress"), ("IF-MIB", "ifIndex"), ("LIGO-802DOT11-EXT-MIB", "ligoDot11RmtNodeMacAddress"))
if mibBuilder.loadTexts: ligoRemoteNodeDisconnected.setStatus('current')
if mibBuilder.loadTexts: ligoRemoteNodeDisconnected.setDescription('This notification is sent when remote node dissasociates.')
ligoLinkQualThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 5)).setObjects(("SNMPv2-MIB", "sysLocation"), ("IF-MIB", "ifIndex"), ("LIGO-802DOT11-EXT-MIB", "ligoDot11IfLinkQuality"))
if mibBuilder.loadTexts: ligoLinkQualThresholdReached.setStatus('current')
if mibBuilder.loadTexts: ligoLinkQualThresholdReached.setDescription('This notification is sent when link quality crosses the specified threshold.')
mibBuilder.exportSymbols("LIGO-802DOT11-EXT-MIB", ligo802dot11ExtMIB=ligo802dot11ExtMIB, ligoDot11RmtNodeAssociated=ligoDot11RmtNodeAssociated, ligoDot11IfErrStatsEntry=ligoDot11IfErrStatsEntry, ligoDot11IfMode=ligoDot11IfMode, ligoRemoteNodeConnected=ligoRemoteNodeConnected, ligoDot11IfParentIndex=ligoDot11IfParentIndex, ligoDot11RemoteNodeStatsTable=ligoDot11RemoteNodeStatsTable, ligoDot11IfChannel=ligoDot11IfChannel, ligo802dot11ExtMIBObjects=ligo802dot11ExtMIBObjects, ligoDot11Notifs=ligoDot11Notifs, ligoDot11IfConfTable=ligoDot11IfConfTable, ligoDot11RmtNodeTxBytes=ligoDot11RmtNodeTxBytes, ligoNoiseThresholdReached=ligoNoiseThresholdReached, ligoDot11IfCountryCode=ligoDot11IfCountryCode, ligoDot11RemoteNodeStatsEntry=ligoDot11RemoteNodeStatsEntry, ligoDot11IfConfEntry=ligoDot11IfConfEntry, PYSNMP_MODULE_ID=ligo802dot11ExtMIB, ligoDot11IfRxInvalidCrypt=ligoDot11IfRxInvalidCrypt, ligoDot11IfAccessPoint=ligoDot11IfAccessPoint, ligoDot11IfESSID=ligoDot11IfESSID, ligoDot11IfChannelBandwidth=ligoDot11IfChannelBandwidth, ligoDot11IfMaxLinkQuality=ligoDot11IfMaxLinkQuality, ligoDot11IfFrequency=ligoDot11IfFrequency, ligoDot11IfProtocol=ligoDot11IfProtocol, ligoLinkQualThresholdReached=ligoLinkQualThresholdReached, ligoDot11Info=ligoDot11Info, ligoDot11RmtNodeDisassocTime=ligoDot11RmtNodeDisassocTime, ligoDot11IfSignalLevel=ligoDot11IfSignalLevel, ligoDot11IfBitRate=ligoDot11IfBitRate, ligoDot11RmtNodeAssocTime=ligoDot11RmtNodeAssocTime, ligoFrequencyChange=ligoFrequencyChange, ligoDot11Stats=ligoDot11Stats, ligoDot11IfAssocNodeCount=ligoDot11IfAssocNodeCount, ligoDot11IfTxExcessiveRetries=ligoDot11IfTxExcessiveRetries, ligoDot11IfNoiseLevel=ligoDot11IfNoiseLevel, ligoDot11IfTxPower=ligoDot11IfTxPower, ligoDot11IfMissedBeacons=ligoDot11IfMissedBeacons, ligoDot11IfRxInvalidNWID=ligoDot11IfRxInvalidNWID, ligoDot11IfErrStatsTable=ligoDot11IfErrStatsTable, ligoDot11RmtNodeMacAddress=ligoDot11RmtNodeMacAddress, ligoDot11IfRxInvalidFrag=ligoDot11IfRxInvalidFrag, ligoRemoteNodeDisconnected=ligoRemoteNodeDisconnected, ligoDot11RmtNodeRxBytes=ligoDot11RmtNodeRxBytes, ligoDot11Conf=ligoDot11Conf, ligoDot11IfInvalidMisc=ligoDot11IfInvalidMisc, ligoDot11IfLinkQuality=ligoDot11IfLinkQuality)
