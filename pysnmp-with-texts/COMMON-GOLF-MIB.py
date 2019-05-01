#
# PySNMP MIB module COMMON-GOLF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COMMON-GOLF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Gauge32, Counter64, enterprises, Bits, Unsigned32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Gauge32", "Counter64", "enterprises", "Bits", "Unsigned32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "IpAddress", "ModuleIdentity")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
fore = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
edge = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
edgecommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
fore_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("fore-mgmt")
agentMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1))
agentBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1))
agentRuntimeSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRuntimeSwVersion.setStatus('mandatory')
if mibBuilder.loadTexts: agentRuntimeSwVersion.setDescription("This is a textual description for the runtime software version and revision. If the version number is one and revision number is zero agentRuntimeSwVersion would be 'Ver. 1.0'")
agentPromFwVersion = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPromFwVersion.setStatus('mandatory')
if mibBuilder.loadTexts: agentPromFwVersion.setDescription("This is a textual description of the agent PROM firmware version and revision. If the version number is one and revision number is zero agentPromFwVersion would be 'Ver. 1.0'")
agentHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentHwRevision.setStatus('mandatory')
if mibBuilder.loadTexts: agentHwRevision.setDescription('This is a integer number for the hardware revision.')
agentMgmtProtocolCapability = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmp-ip", 2), ("snmp-ipx", 3), ("snmp-ip-ipx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMgmtProtocolCapability.setStatus('mandatory')
if mibBuilder.loadTexts: agentMgmtProtocolCapability.setDescription('The network management protocol(s) supported by this agent.')
agentMibCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5), )
if mibBuilder.loadTexts: agentMibCapabilityTable.setStatus('mandatory')
if mibBuilder.loadTexts: agentMibCapabilityTable.setDescription('A list of MIB capability entries supported by this agent.')
agentMibCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1), ).setIndexNames((0, "COMMON-GOLF-MIB", "agentMibCapabilityIndex"))
if mibBuilder.loadTexts: agentMibCapabilityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: agentMibCapabilityEntry.setDescription('A MIB capability entry contains objects describing a particular MIB supported by this agent.')
agentMibCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityIndex.setStatus('mandatory')
if mibBuilder.loadTexts: agentMibCapabilityIndex.setDescription('A list of agentMibCapabilityDescr entries.')
agentMibCapabilityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityDescr.setStatus('mandatory')
if mibBuilder.loadTexts: agentMibCapabilityDescr.setDescription('The name of the MIB supported by the agent.')
agentMibCapabilityVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityVersion.setStatus('mandatory')
if mibBuilder.loadTexts: agentMibCapabilityVersion.setDescription('The version of the MIB specified in this entry.')
agentMibCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("proprietary", 3), ("experiment", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityType.setStatus('mandatory')
if mibBuilder.loadTexts: agentMibCapabilityType.setDescription('The type of the MIB specified in this entry.')
agentStatusConsoleInUse = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("in-use", 2), ("not-in-use", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusConsoleInUse.setStatus('mandatory')
if mibBuilder.loadTexts: agentStatusConsoleInUse.setDescription('This indicates whether console is currently in-use.')
agentStatusSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("proceeding", 2), ("completed", 3), ("changed-not-save", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusSaveCfg.setStatus('mandatory')
if mibBuilder.loadTexts: agentStatusSaveCfg.setDescription('This indicates the status of the device configuration. other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. proceeding(2) - the device configuration is being currently saved into the NV-RAM. completed(3) V all of the device configuration parameters have been saved into NV-RAM. changed-not-save(4)V some of the device configuration parameters have been changed but not saved into NV-RAM. failed(5) - The process to save device configuration is failed.')
agentBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2))
agentUpdateSource = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("network-load", 2), ("out-of-band-load", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentUpdateSource.setStatus('mandatory')
if mibBuilder.loadTexts: agentUpdateSource.setDescription('The source of the runtime software or configuration file to be downloaded by the system.')
agentCfgUpdateCtrl = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentCfgUpdateCtrl.setStatus('mandatory')
if mibBuilder.loadTexts: agentCfgUpdateCtrl.setDescription('This object provides the user to download configuration file. The setting will take effect when the system is restart.')
agentCfgUpdateFile = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentCfgUpdateFile.setStatus('mandatory')
if mibBuilder.loadTexts: agentCfgUpdateFile.setDescription('The name of the configuration file to be downloaded from the TFTP server when agentCfgUpdateCtrl is set to enabled.')
agentSoftwareUpdateCtrl = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSoftwareUpdateCtrl.setStatus('mandatory')
if mibBuilder.loadTexts: agentSoftwareUpdateCtrl.setDescription('This object provides the user to download runtime software. The setting will take effect when the system is restart.')
agentSoftwareUdateFile = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSoftwareUdateFile.setStatus('mandatory')
if mibBuilder.loadTexts: agentSoftwareUdateFile.setDescription('The name of the runtime software to be downloaded from the TFTP server when agentSoftwareUpdateCtrl is set to enabled.')
agentSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("cold-start", 2), ("warm-start", 3), ("no-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemReset.setStatus('mandatory')
if mibBuilder.loadTexts: agentSystemReset.setDescription('This object indicates the agent system reset state. Setting this object to no-reset(4) has no effect. Setting this object to cold-start(2) or warm-start(3) will reset the agent. The agent always returns no-reset(4) when this object is read.')
agentRs232PortConfig = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("console", 2), ("out-of-band", 3), ("notAvail", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRs232PortConfig.setStatus('mandatory')
if mibBuilder.loadTexts: agentRs232PortConfig.setDescription('This object indicates the RS-232C mode while device restart.')
agentOutOfBandBaudRateConfig = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutOfBandBaudRateConfig.setStatus('mandatory')
if mibBuilder.loadTexts: agentOutOfBandBaudRateConfig.setDescription('This object allows user to specify out_of_band baud rate. It will take effect when the system is restart.')
agentSaveCfg = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 9), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: agentSaveCfg.setStatus('mandatory')
if mibBuilder.loadTexts: agentSaveCfg.setDescription('As the object is set, the current device configuration will be saved into to NV-RAM.')
agentIpProtoConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3))
agentIpNumOfIf = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpNumOfIf.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpNumOfIf.setDescription('The total number of IP interfaces supported by this agent.')
agentIpIfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2), )
if mibBuilder.loadTexts: agentIpIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfTable.setDescription('A list of IP interface entries supported by the agent.')
agentIpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1), ).setIndexNames((0, "COMMON-GOLF-MIB", "agentIpIfIndex"))
if mibBuilder.loadTexts: agentIpIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfEntry.setDescription('An agentIPIfEntry contains information about a particular IP interface.')
agentIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfIndex.setDescription('This object uniquely identifies the IP interface number in the agentIpIfTable. This value should never greater than agentIpNumOfIf')
agentIpIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfAddress.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfAddress.setDescription('The IP address of the interface.')
agentIpIfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfNetMask.setDescription('The IP net mask for this interface.')
agentIpIfDefaultRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpIfDefaultRouter.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfDefaultRouter.setDescription('The default gateway for this IP interface.')
agentIpIfMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfMacAddr.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfMacAddr.setDescription('The MAC address of this IP interface. For interfaces which do not have such an address. (e.g., a serial line), this object should contain an octet string of zero length.')
agentIpIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 28))).clone(namedValues=NamedValues(("other", 1), ("ethernet-csmacd", 6), ("slip", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfType.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpIfType.setDescription('The physical layer interface of the IP interface.')
agentIpBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpBootServerAddr.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpBootServerAddr.setDescription('The IP Address of the Boot Server.')
agentIpGetIpFromBootpServer = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("manual", 2), ("from-bootp", 3), ("from-dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpGetIpFromBootpServer.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpGetIpFromBootpServer.setDescription('This object indicates whether the agent should get its system IP address from Bootp server at start up.')
agentIpUnauthAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpUnauthAddr.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpUnauthAddr.setDescription('The IP address of an unauthorized SNMP packet.')
agentIpUnauthComm = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpUnauthComm.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpUnauthComm.setDescription('The community string of an unauthorized SNMP packet.')
agentIpLastBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpLastBootServerAddr.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpLastBootServerAddr.setDescription('The last IP address used by the agent as Boot server IP address.')
agentIpLastIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpLastIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpLastIpAddr.setDescription('The last IP address used by the agent as system IP address.')
agentIpTrapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9), )
if mibBuilder.loadTexts: agentIpTrapManagerTable.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpTrapManagerTable.setDescription('A list of trap managers to which SNMP traps will be sent.')
agentIpTrapManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1), ).setIndexNames((0, "COMMON-GOLF-MIB", "agentIpTrapManagerIpAddr"))
if mibBuilder.loadTexts: agentIpTrapManagerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpTrapManagerEntry.setDescription('Each entry contains the particular trap manager settings.')
agentIpTrapManagerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpTrapManagerIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpTrapManagerIpAddr.setDescription('The IP address where SNMP traps will be destined for')
agentIpTrapManagerComm = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerComm.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpTrapManagerComm.setDescription('The community string used to encode SNMP trap packet to be sent to the trap manager.')
agentIpTrapManagerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpTrapManagerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: agentIpTrapManagerStatus.setDescription('This object indicates whether or not the trap should be sent to this trap manager.')
mibBuilder.exportSymbols("COMMON-GOLF-MIB", agentIpUnauthAddr=agentIpUnauthAddr, agentIpIfIndex=agentIpIfIndex, agentIpIfDefaultRouter=agentIpIfDefaultRouter, agentIpTrapManagerStatus=agentIpTrapManagerStatus, agentMibCapabilityEntry=agentMibCapabilityEntry, agentMibCapabilityType=agentMibCapabilityType, edgecommon=edgecommon, agentUpdateSource=agentUpdateSource, agentCfgUpdateFile=agentCfgUpdateFile, agentSoftwareUpdateCtrl=agentSoftwareUpdateCtrl, agentSaveCfg=agentSaveCfg, ethernet=ethernet, agentOutOfBandBaudRateConfig=agentOutOfBandBaudRateConfig, agentRs232PortConfig=agentRs232PortConfig, agentStatusSaveCfg=agentStatusSaveCfg, agentPromFwVersion=agentPromFwVersion, agentIpTrapManagerTable=agentIpTrapManagerTable, agentSystemReset=agentSystemReset, golfcommon=golfcommon, agentIpTrapManagerIpAddr=agentIpTrapManagerIpAddr, agentBasicInfo=agentBasicInfo, agentIpGetIpFromBootpServer=agentIpGetIpFromBootpServer, fore_mgmt=fore_mgmt, agentMgmtProtocolCapability=agentMgmtProtocolCapability, agentIpLastBootServerAddr=agentIpLastBootServerAddr, agentCfgUpdateCtrl=agentCfgUpdateCtrl, agentRuntimeSwVersion=agentRuntimeSwVersion, agentMibCapabilityDescr=agentMibCapabilityDescr, agentIpProtoConfig=agentIpProtoConfig, golf=golf, agentBasicConfig=agentBasicConfig, agentHwRevision=agentHwRevision, agentIpIfMacAddr=agentIpIfMacAddr, agentMibCapabilityVersion=agentMibCapabilityVersion, agentIpUnauthComm=agentIpUnauthComm, fore=fore, agentIpTrapManagerComm=agentIpTrapManagerComm, agentIpIfEntry=agentIpIfEntry, agentIpBootServerAddr=agentIpBootServerAddr, agentIpIfNetMask=agentIpIfNetMask, golfproducts=golfproducts, agentSoftwareUdateFile=agentSoftwareUdateFile, agentStatusConsoleInUse=agentStatusConsoleInUse, agentIpNumOfIf=agentIpNumOfIf, agentMibCapabilityTable=agentMibCapabilityTable, agentIpTrapManagerEntry=agentIpTrapManagerEntry, agentMibCapabilityIndex=agentMibCapabilityIndex, agentIpIfTable=agentIpIfTable, agentIpIfType=agentIpIfType, agentIpLastIpAddr=agentIpLastIpAddr, agentIpIfAddress=agentIpIfAddress, systems=systems, edge=edge, agentMgmt=agentMgmt)
