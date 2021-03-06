#
# PySNMP MIB module ELS100-S24TX2M-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELS100-S24TX2M-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, ModuleIdentity, ObjectIdentity, Counter32, Integer32, IpAddress, internet, Counter64, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Counter32", "Integer32", "IpAddress", "internet", "Counter64", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpELS100S24TX2M = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7))
tpELS100S24TX2M.setRevisions(('2002-08-05 17:53', '2002-02-20 22:02', '1999-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpELS100S24TX2M.setRevisionsDescriptions(('Added switchOIDTable for identifying the individual switches in a stack of switches.', 'Pretty print.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: tpELS100S24TX2M.setLastUpdated('200202202202Z')
if mibBuilder.loadTexts: tpELS100S24TX2M.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: tpELS100S24TX2M.setContactInfo('Enterasys Networks, Inc. 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-5005 (603) 332-9400 support@enterasys.com http://www.enterasys.com')
if mibBuilder.loadTexts: tpELS100S24TX2M.setDescription('The MIB module for ELS100-S24TX2M.')
switchInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1))
switchPortMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2))
systemSTAMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 3))
tftpDownloadMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4))
restartMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5))
portMirrorMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6))
igmpMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7))
switchNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchNumber.setStatus('current')
if mibBuilder.loadTexts: switchNumber.setDescription('The total number of switches present on this system.')
switchInfoTable = MibTable((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2), )
if mibBuilder.loadTexts: switchInfoTable.setStatus('current')
if mibBuilder.loadTexts: switchInfoTable.setDescription('Table of descriptive and status information about switches in this system.')
switchInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1), ).setIndexNames((0, "ELS100-S24TX2M-MIB", "swUnitIndex"))
if mibBuilder.loadTexts: switchInfoEntry.setStatus('current')
if mibBuilder.loadTexts: switchInfoEntry.setDescription('An entry in the table, containing information about a single switch in this system. ')
swUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: swUnitIndex.setStatus('current')
if mibBuilder.loadTexts: swUnitIndex.setDescription('This object identifies the switch within the system for which this entry contains information. This value can never be greater than switchNumber.')
swMainBoardHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMainBoardHwVer.setStatus('current')
if mibBuilder.loadTexts: swMainBoardHwVer.setDescription('Hardware version of the main board.')
swMainBoardFwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMainBoardFwVer.setStatus('current')
if mibBuilder.loadTexts: swMainBoardFwVer.setDescription('Firmware version of the main board.')
swAgentBoardHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAgentBoardHwVer.setStatus('current')
if mibBuilder.loadTexts: swAgentBoardHwVer.setDescription('Hardware version of the agent board.')
swAgentBoardFwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAgentBoardFwVer.setStatus('current')
if mibBuilder.loadTexts: swAgentBoardFwVer.setDescription('Firmware version of the agent board.')
swAgentBoardPOSTCodeVer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swAgentBoardPOSTCodeVer.setStatus('current')
if mibBuilder.loadTexts: swAgentBoardPOSTCodeVer.setDescription('POST code version of the agent board.')
swPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortNumber.setStatus('current')
if mibBuilder.loadTexts: swPortNumber.setDescription('The total port number of this switch (including expansion slot).')
swPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internalPower", 1), ("redundantPower", 2), ("internalAndRedundantPower", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerStatus.setStatus('current')
if mibBuilder.loadTexts: swPowerStatus.setDescription('Indicates the switch using internalPower(1), redundantPower(2) or both(3)')
swExpansionSlot1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("hundredBaseFX2Port", 1), ("thousandBaseSX", 2), ("stackingModule4GB", 3), ("hundredBaseFX1Port", 4), ("thousandBaseLX", 5), ("thousandBaseT", 6), ("thousandBaseGBIC", 7), ("stackingModule2GB", 8), ("other", 9), ("notPresent", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swExpansionSlot1.setStatus('current')
if mibBuilder.loadTexts: swExpansionSlot1.setDescription('Type of expansion module in this switch slot 1.')
swExpansionSlot2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("hundredBaseFX2Port", 1), ("thousandBaseSX", 2), ("stackingModule4GB", 3), ("hundredBaseFX1Port", 4), ("thousandBaseLX", 5), ("thousandBaseT", 6), ("thousandBaseGBIC", 7), ("stackingModule2GB", 8), ("other", 9), ("notPresent", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swExpansionSlot2.setStatus('current')
if mibBuilder.loadTexts: swExpansionSlot2.setDescription('Type of expansion module in this switch slot 2.')
swRoleInSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("master", 1), ("backupMaster", 2), ("slave", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRoleInSystem.setStatus('current')
if mibBuilder.loadTexts: swRoleInSystem.setDescription('Indicates the switch is master(1), backupMaster(2) or slave(3) in this system.')
switchOIDTable = MibTable((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3), )
if mibBuilder.loadTexts: switchOIDTable.setStatus('current')
if mibBuilder.loadTexts: switchOIDTable.setDescription('Table of System Object Identifiers for switches in this system.')
switchOIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3, 1), ).setIndexNames((0, "ELS100-S24TX2M-MIB", "switchOIDIndex"))
if mibBuilder.loadTexts: switchOIDEntry.setStatus('current')
if mibBuilder.loadTexts: switchOIDEntry.setDescription('An entry in the table, containing System Object Identifier for a single switch in this system.')
switchOIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: switchOIDIndex.setStatus('current')
if mibBuilder.loadTexts: switchOIDIndex.setDescription('This object identifies the switch within the system for which this entry contains information. This value can never be greater than switchNumber. Index value 1 always represents the Master in a stacked configuration and the only device in a standalone configuration. Subsequent indices are sequential with the lowest number representing the Slave nearest the Master and so on.')
switchOIDValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 1, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchOIDValue.setStatus('current')
if mibBuilder.loadTexts: switchOIDValue.setDescription('This object contains the System Object Identifier that uniquely identifies the type of switch.')
switchPortMgtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1), )
if mibBuilder.loadTexts: switchPortMgtTable.setStatus('current')
if mibBuilder.loadTexts: switchPortMgtTable.setDescription('Table of descriptive and status information about configuration of each switch ports (including expansion slot) in this system.')
switchPortMgtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1), ).setIndexNames((0, "ELS100-S24TX2M-MIB", "swUnitIndex"), (0, "ELS100-S24TX2M-MIB", "swPortMgtIndex"))
if mibBuilder.loadTexts: switchPortMgtEntry.setStatus('current')
if mibBuilder.loadTexts: switchPortMgtEntry.setDescription('An entry in the table, containing information about configuration in one switch port of the switch.')
swPortMgtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: swPortMgtIndex.setStatus('current')
if mibBuilder.loadTexts: swPortMgtIndex.setDescription('This object identifies the port within the switch for which this entry contains information.')
swPortMgtPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hundredBaseTX", 1), ("hundredBaseFX", 2), ("thousandBaseSX", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMgtPortType.setStatus('current')
if mibBuilder.loadTexts: swPortMgtPortType.setDescription('Indicates the port type is tenBaseT/hundredBaseTX(1), hundredBaseFX(2) or thousandBaseSX(3).')
swPortMgtSpeedDpxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("halfDuplex10", 1), ("fullDuplex10", 2), ("halfDuplex100", 3), ("fullDuplex100", 4), ("halfDuplex1000", 5), ("fullDuplex1000", 6), ("autoNegotiation", 7))).clone('autoNegotiation')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortMgtSpeedDpxAdmin.setStatus('current')
if mibBuilder.loadTexts: swPortMgtSpeedDpxAdmin.setDescription('Set the port speed and duplex mode as follows: halfDuplex10(1) - 10Mbps and half duplex mode fullDuplex10(2) - 10Mbps and full duplex mode halfDuplex100(3) - 100Mbps and half duplex mode fullDuplex100(4) - 100Mbps and full duplex mode halfDuplex1000(5) - 1000Mbps and half duplex mode fullDuplex1000(6) - 1000Mbps and full duplex mode autoNegotiation(7) - let the switch to negotiate with the other end of connection. hundredBaseTX port can be set as halfDuplex10(1) fullDuplex10(2) halfDuplex100(3) fullDuplex100(4) autoNegotiation(7) hundredBaseFX port can be set as halfDuplex100(3) fullDuplex100(4) thousandBaseSX port can be set as halfDuplex1000(5) fullDuplex1000(6) autoNegotiation(7) The actual operating speed and duplex of the port is given by swPortMgtSpeedDpxInUse.')
swPortMgtSpeedDpxInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("halfDuplex10", 1), ("fullDuplex10", 2), ("halfDuplex100", 3), ("fullDuplex100", 4), ("halfDuplex1000", 5), ("fullDuplex1000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMgtSpeedDpxInUse.setStatus('current')
if mibBuilder.loadTexts: swPortMgtSpeedDpxInUse.setDescription('The operating speed and duplex mode of the switched port.')
swPortMgtFlowCtrlAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("backPressure", 3), ("dot3xFlowControl", 4))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPortMgtFlowCtrlAdmin.setStatus('current')
if mibBuilder.loadTexts: swPortMgtFlowCtrlAdmin.setDescription('(1) Flow control mechanism is enabled. If the port type is hundredBaseTX or thousandBaseSX: When the port is operating in halfDuplex mode, the port uses backPressure flow control mechanism. When the port is operating in fullDuplex mode, the port uses IEEE 802.3x flow control mechanism. If the port type is hundredBaseFX: When the port is operating in halfDuplex mode, the port uses backPressure flow control mechanism. When the port is operating in fullDuplex mode, Flow control mechanism will not function. (2) Flow control mechanism is disabled. (3) Flow control mechanism is backPressure. When the port is in fullDuplex mode this flow control mechanism will not function. (4) Flow control mechanism is IEEE 802.3x flow control. When the port is in halfDuplex mode this flow control mechanism will not function. hundredBaseTX and thousandBaseSX port can be set as: enabled(1), disabled(2), backPressure(3), dot3xFlowControl(4). hundredBaseFX port can be set as: enabled(1), disabled(2), backPressure(3). The actual flow control mechanism is used given by swPortMgtFlowCtrlInUse.')
swPortMgtFlowCtrlInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("backPressure", 1), ("dot3xFlowControl", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPortMgtFlowCtrlInUse.setStatus('current')
if mibBuilder.loadTexts: swPortMgtFlowCtrlInUse.setDescription('(1) BackPressure flow control mechanism is used. (2) IEEE 802.3 flow control mechanism is used. (3) Flow control mechanism is disabled. ')
systemSTAStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemSTAStatus.setStatus('current')
if mibBuilder.loadTexts: systemSTAStatus.setDescription('Global spanning tree status. (1) Spanning tree protocol is enabled. (2) Spanning tree protocol is disabled. ')
tftpDownloadServerIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpDownloadServerIP.setStatus('current')
if mibBuilder.loadTexts: tftpDownloadServerIP.setDescription('The IP address of a TFTP server from which a firmware image can be downloaded.')
tftpDownloadAgentBoardFwFileName = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80)).clone('es3526f.bin')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpDownloadAgentBoardFwFileName.setStatus('current')
if mibBuilder.loadTexts: tftpDownloadAgentBoardFwFileName.setDescription('')
tftpDownloadAgentBoardFwDownloadNode = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permanent", 1), ("temporary", 2))).clone('permanent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpDownloadAgentBoardFwDownloadNode.setStatus('current')
if mibBuilder.loadTexts: tftpDownloadAgentBoardFwDownloadNode.setDescription('Indicates whether a newly upgraded firmware version should write to flash. When this object is temporary(2), following a successful upgrade the system will switch to run the new firmware but will not upgrade the new firmware to flash. That means after a power cycle, system will run the firmware residing the flash. When this object is permanent(1), following a successful firmware upgrade, the flash will be upgraded and the system will automatically switch to run the new firmware.')
tftpDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("notActive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpDownloadStatus.setStatus('current')
if mibBuilder.loadTexts: tftpDownloadStatus.setDescription('Setting this object to active(1) trigger the TFTP download action. Setting this object to notActive(2) has no effect. The system always returns the value notActive(2) when this object is read.')
restartOptionPOST = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartOptionPOST.setStatus('current')
if mibBuilder.loadTexts: restartOptionPOST.setDescription('Setting this object as enabled. The system will do POST when it restart')
restartOptionReloadFactoryDefault = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartOptionReloadFactoryDefault.setStatus('current')
if mibBuilder.loadTexts: restartOptionReloadFactoryDefault.setDescription('Setting this object as enabled. The system will do factory reset when it restart')
restartOptionKeepIpSetting = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartOptionKeepIpSetting.setStatus('current')
if mibBuilder.loadTexts: restartOptionKeepIpSetting.setDescription('Setting this object as enabled. The system will keep IP setting when it do factory reset.')
restartOptionKeepUserAuthentication = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartOptionKeepUserAuthentication.setStatus('current')
if mibBuilder.loadTexts: restartOptionKeepUserAuthentication.setDescription('Setting this object as enabled. The system will keep user authentication setting when it do factory reset.')
restartAction = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("notActive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartAction.setStatus('current')
if mibBuilder.loadTexts: restartAction.setDescription('Setting this object to active(1) trigger the system restart. Setting this object to notActive(2) has no effect. The system always returns the value notActive(2) when this object is read.')
portMirrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMirrorStatus.setStatus('current')
if mibBuilder.loadTexts: portMirrorStatus.setDescription('Port mirroring function status. (1) mirroring function is enabled. (2) mirroring function is disabled.')
portMirrorSnifferPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMirrorSnifferPort.setStatus('current')
if mibBuilder.loadTexts: portMirrorSnifferPort.setDescription('Linear port number of sniffer port to which all frames to/from mirrored ports are sent. Frames are only mirrored if the portMirrorStatus object is set to enabled(1).')
portMirrorMirroredPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portMirrorMirroredPort.setStatus('current')
if mibBuilder.loadTexts: portMirrorMirroredPort.setDescription("Linear port number of mirrored port. The traffic of mirrored port will be 'copied' to sniffer port.")
igmpStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpStatus.setStatus('current')
if mibBuilder.loadTexts: igmpStatus.setDescription('Parameter to enable or disable IGMP snooping on the device. When enabled, the device will examine IGMP packets and set up filters for IGMP ports. The default is enabled.')
igmpQueryCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpQueryCount.setStatus('current')
if mibBuilder.loadTexts: igmpQueryCount.setDescription('Maximum number of queries that have not been heard on the system before the system starts taking action to solicit reports(default is 5).')
igmpReportDelay = MibScalar((1, 3, 6, 1, 4, 1, 52, 3, 9, 1, 10, 7, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpReportDelay.setStatus('current')
if mibBuilder.loadTexts: igmpReportDelay.setDescription('Timeout value(mins) between IGMP reports received on a port for an IP Multicast Address that can pass before the system sends an IGMP Query out the port and removes it from the list(default is 5 minutes).')
mibBuilder.exportSymbols("ELS100-S24TX2M-MIB", igmpReportDelay=igmpReportDelay, igmpMgt=igmpMgt, restartOptionKeepUserAuthentication=restartOptionKeepUserAuthentication, switchInfoEntry=switchInfoEntry, portMirrorMirroredPort=portMirrorMirroredPort, swAgentBoardPOSTCodeVer=swAgentBoardPOSTCodeVer, switchInfoTable=switchInfoTable, switchOIDTable=switchOIDTable, tftpDownloadAgentBoardFwFileName=tftpDownloadAgentBoardFwFileName, restartOptionPOST=restartOptionPOST, switchNumber=switchNumber, swAgentBoardHwVer=swAgentBoardHwVer, swPortMgtSpeedDpxAdmin=swPortMgtSpeedDpxAdmin, swPortMgtSpeedDpxInUse=swPortMgtSpeedDpxInUse, PYSNMP_MODULE_ID=tpELS100S24TX2M, switchOIDEntry=switchOIDEntry, tftpDownloadServerIP=tftpDownloadServerIP, switchPortMgt=switchPortMgt, swExpansionSlot2=swExpansionSlot2, swPowerStatus=swPowerStatus, switchOIDIndex=switchOIDIndex, switchPortMgtEntry=switchPortMgtEntry, tftpDownloadAgentBoardFwDownloadNode=tftpDownloadAgentBoardFwDownloadNode, swPortMgtFlowCtrlInUse=swPortMgtFlowCtrlInUse, swMainBoardHwVer=swMainBoardHwVer, systemSTAStatus=systemSTAStatus, restartMgt=restartMgt, swExpansionSlot1=swExpansionSlot1, igmpStatus=igmpStatus, swRoleInSystem=swRoleInSystem, systemSTAMgt=systemSTAMgt, igmpQueryCount=igmpQueryCount, swPortNumber=swPortNumber, portMirrorMgt=portMirrorMgt, switchPortMgtTable=switchPortMgtTable, swAgentBoardFwVer=swAgentBoardFwVer, tftpDownloadStatus=tftpDownloadStatus, restartOptionKeepIpSetting=restartOptionKeepIpSetting, portMirrorSnifferPort=portMirrorSnifferPort, restartOptionReloadFactoryDefault=restartOptionReloadFactoryDefault, tpELS100S24TX2M=tpELS100S24TX2M, swPortMgtPortType=swPortMgtPortType, swUnitIndex=swUnitIndex, switchOIDValue=switchOIDValue, switchInfo=switchInfo, swPortMgtIndex=swPortMgtIndex, swMainBoardFwVer=swMainBoardFwVer, restartAction=restartAction, swPortMgtFlowCtrlAdmin=swPortMgtFlowCtrlAdmin, portMirrorStatus=portMirrorStatus, tftpDownloadMgt=tftpDownloadMgt)
