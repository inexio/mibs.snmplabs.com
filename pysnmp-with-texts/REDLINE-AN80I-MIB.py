#
# PySNMP MIB module REDLINE-AN80I-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDLINE-AN80I-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
redlineSystem, = mibBuilder.importSymbols("REDLINE-MIB", "redlineSystem")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, NotificationType, iso, Integer32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "NotificationType", "iso", "Integer32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "ObjectIdentity", "Bits", "MibIdentifier")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
redlineAn80iMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3))
redlineAn80iMib.setRevisions(('2005-11-29 15:43',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: redlineAn80iMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: redlineAn80iMib.setLastUpdated('200511291543Z')
if mibBuilder.loadTexts: redlineAn80iMib.setOrganization('Redline Communications Inc.')
if mibBuilder.loadTexts: redlineAn80iMib.setContactInfo('Henryk Kijak email: hkijak@redlinecommunications.com')
if mibBuilder.loadTexts: redlineAn80iMib.setDescription('This MIB module contains object definitions applicable only to Redline AN80i switched device.')
redlineAn80iPtpPmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1))
redlineAn80iSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1))
an80iOptionsKeyTable = MibTable((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1), )
if mibBuilder.loadTexts: an80iOptionsKeyTable.setStatus('current')
if mibBuilder.loadTexts: an80iOptionsKeyTable.setDescription('This table contains options key information. The maximum number of configured options key is 2.')
an80iOptionsKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1), ).setIndexNames((0, "REDLINE-AN80I-MIB", "an80iOptionsKeyId"))
if mibBuilder.loadTexts: an80iOptionsKeyEntry.setStatus('current')
if mibBuilder.loadTexts: an80iOptionsKeyEntry.setDescription('This table provides one row for each option key defined in the AN80i system')
an80iOptionsKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: an80iOptionsKeyId.setStatus('current')
if mibBuilder.loadTexts: an80iOptionsKeyId.setDescription('The Options Key Identifier.')
an80iOptionsKey = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: an80iOptionsKey.setStatus('current')
if mibBuilder.loadTexts: an80iOptionsKey.setDescription('The options key value.')
an80iOptionsKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: an80iOptionsKeyStatus.setStatus('current')
if mibBuilder.loadTexts: an80iOptionsKeyStatus.setDescription('This object is used to ctivate and deactivate rows in the an80iOptionsKeyTable table. There will be only two rows in the table and only one will be active. When one row is active the other one will be notInService. The row can not be created or deleted')
an80iHardwareType = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iHardwareType.setStatus('current')
if mibBuilder.loadTexts: an80iHardwareType.setDescription('The type/version/revision of the hardware.')
an80iRadioType = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRadioType.setStatus('current')
if mibBuilder.loadTexts: an80iRadioType.setDescription('The radio type.')
an80iSaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("saveConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSaveConfig.setStatus('current')
if mibBuilder.loadTexts: an80iSaveConfig.setDescription('This object will save the configuration in the nonvolatile memory and will activate the new configuration.')
an80iActivateConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("activeConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iActivateConfig.setStatus('current')
if mibBuilder.loadTexts: an80iActivateConfig.setDescription('This object will activate the new configuration without saving it in the nonvolatile memory. If after this event it will elapse more than 5 minutes and no save configuration occurs, then system will restart with the configuration from the nonvolatile memory.')
redlineAn80iWirelesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2))
an80iAntennaAllignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("buzzer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iAntennaAllignmentMode.setStatus('current')
if mibBuilder.loadTexts: an80iAntennaAllignmentMode.setDescription('Specifies if the antenna alignment buzzer is enabled or not. In the future, new alignment methods may be added.')
an80iCurrTxPower = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iCurrTxPower.setStatus('current')
if mibBuilder.loadTexts: an80iCurrTxPower.setDescription('The actual Tx Power of the AN-80i Node.')
an80iChannelAutoScan = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iChannelAutoScan.setStatus('current')
if mibBuilder.loadTexts: an80iChannelAutoScan.setDescription('Specifies if the frequency auto-scanning feature is enabled')
an80iCurrFrequency = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 4), Integer32()).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iCurrFrequency.setStatus('current')
if mibBuilder.loadTexts: an80iCurrFrequency.setDescription('The central frequency on which the equipment operates. If the auto-scanning feature is enabled then this may be different than the an80iOPeratingFrequency. [KHz]')
an80iOPeratingFrequency = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 5), Integer32()).setUnits('KHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iOPeratingFrequency.setStatus('current')
if mibBuilder.loadTexts: an80iOPeratingFrequency.setDescription('Specifies the operating frequency of the system [KHz].')
an80iMaxTxPower = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iMaxTxPower.setStatus('current')
if mibBuilder.loadTexts: an80iMaxTxPower.setDescription('The Tx Power of the AN-80i. Specifies the power level of the system, which is preset at the factory and should not be altered. In the event that this parameter needs to be changed, please contact the Redline support team.')
an80iSystemMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ptpSlave", 1), ("ptpMaster", 2), ("pmpSlave", 3), ("pmpMaster", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSystemMode.setStatus('current')
if mibBuilder.loadTexts: an80iSystemMode.setDescription('1 = PMP Slave, 2 = PTP Master, 3 = PMP Slave, 4 = PMP Master')
an80iRFStatusCode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRFStatusCode.setStatus('current')
if mibBuilder.loadTexts: an80iRFStatusCode.setDescription('Specifies the Error Code for the RF Interface.')
an80iDFSAction = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("txDisabled", 2), ("changeFreq", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iDFSAction.setStatus('current')
if mibBuilder.loadTexts: an80iDFSAction.setDescription('Action taken when a radar is detected on the same frequency.')
an80iAntennaGain = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iAntennaGain.setStatus('current')
if mibBuilder.loadTexts: an80iAntennaGain.setDescription('The gain of the antenna attached to the system.')
an80iActiveRFLinks = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iActiveRFLinks.setStatus('current')
if mibBuilder.loadTexts: an80iActiveRFLinks.setDescription('The actual number of provisioned links.')
an80iAtpControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iAtpControl.setStatus('current')
if mibBuilder.loadTexts: an80iAtpControl.setDescription('Enable/disable the automatic Tx power control.')
an80iTurboModeControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iTurboModeControl.setStatus('current')
if mibBuilder.loadTexts: an80iTurboModeControl.setDescription('Enable/disable the turbo mode. In this mode the system uses a 40MHz channel (20 MHz in normal mode). ')
an80iChannelWidth = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(7, 6, 5))).clone(namedValues=NamedValues(("chWidth40MHz", 7), ("chWidth20MHz", 6), ("chWidth10MHz", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iChannelWidth.setStatus('current')
if mibBuilder.loadTexts: an80iChannelWidth.setDescription('The width of the channel. ')
redlineAn80iEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3))
an80iEtherPortConn = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("normal", 2), ("crossover", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEtherPortConn.setStatus('current')
if mibBuilder.loadTexts: an80iEtherPortConn.setDescription('Specifies Ethernet port connection auto(1), mdi(2) or mdix(3)')
an80iEtherPortMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("auto", 1), ("e10hd", 2), ("e10fd", 3), ("e100hd", 4), ("e100fd", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEtherPortMode.setStatus('current')
if mibBuilder.loadTexts: an80iEtherPortMode.setDescription('The attribute specifies the Ethernet LED status of the AN80i.')
an80iFlowControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iFlowControl.setStatus('current')
if mibBuilder.loadTexts: an80iFlowControl.setDescription('This object specifies if flow control is enabled or not.')
an80iLowLatencyMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iLowLatencyMode.setStatus('current')
if mibBuilder.loadTexts: an80iLowLatencyMode.setDescription('This object specifies if prioritized low latency mode is enabled or not.')
an80iEthernetFollowsWireless = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEthernetFollowsWireless.setStatus('current')
if mibBuilder.loadTexts: an80iEthernetFollowsWireless.setDescription('This object specifies if the Ethernet follows wireless mode is enabled or not.')
an80iEthernetFollowsWirelessTimeout = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEthernetFollowsWirelessTimeout.setStatus('current')
if mibBuilder.loadTexts: an80iEthernetFollowsWirelessTimeout.setDescription('This object specifies if the timeout (seconds) for the Ethernet follows wireless mode (0=infinite).')
redlineAn80iManagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4))
an80iHttpAccess = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iHttpAccess.setStatus('current')
if mibBuilder.loadTexts: an80iHttpAccess.setDescription('This object specifies if Http Access is enabled or not.')
an80iTelnetAccess = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iTelnetAccess.setStatus('current')
if mibBuilder.loadTexts: an80iTelnetAccess.setDescription('This object specifies if Telnet Access is enabled or not.')
an80iTelnetPort = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 3), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iTelnetPort.setStatus('current')
if mibBuilder.loadTexts: an80iTelnetPort.setDescription('This object specifies the Telnet port number.')
redlineAn80iSWUpgradeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5))
an80iSwDownloadTftpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadTftpAddressType.setStatus('current')
if mibBuilder.loadTexts: an80iSwDownloadTftpAddressType.setDescription('The INET address type of the software upgrade TFTP server. IPv4 type supported only.')
an80iSwDownloadTftpAddress = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadTftpAddress.setStatus('current')
if mibBuilder.loadTexts: an80iSwDownloadTftpAddress.setDescription('The INET address of the TFTP server.')
an80iSwDownloadTftpFile = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadTftpFile.setStatus('current')
if mibBuilder.loadTexts: an80iSwDownloadTftpFile.setDescription('The image file name as required by the TFTP server.')
an80iSwDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("download", 1), ("inProgress", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iSwDownloadStatus.setStatus('current')
if mibBuilder.loadTexts: an80iSwDownloadStatus.setDescription('The status of the current software download.')
an80iSwDownloadControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("startUpgrade", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadControl.setStatus('current')
if mibBuilder.loadTexts: an80iSwDownloadControl.setDescription('Trigger software upgrade')
redlineAn80iPmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2))
redlineAn80iPmpWirelesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1))
an80iRegistrationPeriod = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iRegistrationPeriod.setStatus('current')
if mibBuilder.loadTexts: an80iRegistrationPeriod.setDescription('Number of frames between two consecutive registration periods.')
an80iMaximumDistance = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iMaximumDistance.setStatus('current')
if mibBuilder.loadTexts: an80iMaximumDistance.setDescription('Maximum distance in km between the sector controller and one subscriber station.')
an80iRegisteredStations = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRegisteredStations.setStatus('current')
if mibBuilder.loadTexts: an80iRegisteredStations.setDescription('The number of registered stations on the sector controller.')
an80iRegisteredConnections = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRegisteredConnections.setStatus('current')
if mibBuilder.loadTexts: an80iRegisteredConnections.setDescription('The number of registered connections on the sector controller.')
an80iMaxId = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iMaxId.setStatus('current')
if mibBuilder.loadTexts: an80iMaxId.setDescription('The maximum number of ID used to identify links, connections and groups')
an80iNextAvailId = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iNextAvailId.setStatus('current')
if mibBuilder.loadTexts: an80iNextAvailId.setDescription("The next available ID from the ID pool which is not grater then that defined in 'an80iMaxId' ")
an80iLastModifId = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iLastModifId.setStatus('current')
if mibBuilder.loadTexts: an80iLastModifId.setDescription("The last modified ID from the ID pool which is not grater then that defined in 'an80iMaxId' ")
an80iSaveIdConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSaveIdConfiguration.setStatus('current')
if mibBuilder.loadTexts: an80iSaveIdConfiguration.setDescription('Save the ID table in the flash memory')
redlineAn80iPtpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3))
redlineAn80iPtpSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3, 1))
an80iResetStatistics = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iResetStatistics.setStatus('current')
if mibBuilder.loadTexts: an80iResetStatistics.setDescription('This object resets wireless and Ethernet counters')
redlineAn80iTrapDefinitions = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0))
an80iPswdChangeFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 1))
if mibBuilder.loadTexts: an80iPswdChangeFailTrap.setStatus('current')
if mibBuilder.loadTexts: an80iPswdChangeFailTrap.setDescription('An event to report the failure of a password change.')
an80iFirmwareConfigFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 2))
if mibBuilder.loadTexts: an80iFirmwareConfigFailTrap.setStatus('current')
if mibBuilder.loadTexts: an80iFirmwareConfigFailTrap.setDescription('An event to report the failure of a firmware config.')
an80iEepromCorruptedTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 3))
if mibBuilder.loadTexts: an80iEepromCorruptedTrap.setStatus('current')
if mibBuilder.loadTexts: an80iEepromCorruptedTrap.setDescription('An event to report the corruption of the EEPROM.')
an80iHardwareFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 4))
if mibBuilder.loadTexts: an80iHardwareFailTrap.setStatus('current')
if mibBuilder.loadTexts: an80iHardwareFailTrap.setDescription('An event to report the hardware failure.')
an80iSaveConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 5))
if mibBuilder.loadTexts: an80iSaveConfigTrap.setStatus('current')
if mibBuilder.loadTexts: an80iSaveConfigTrap.setDescription('An event to report the saving of configuration')
an80iDFSEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 6))
if mibBuilder.loadTexts: an80iDFSEventTrap.setStatus('current')
if mibBuilder.loadTexts: an80iDFSEventTrap.setDescription('An event to report the radar frequency detection')
an80iIdChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 7)).setObjects(("REDLINE-AN80I-MIB", "an80iLastModifId"))
if mibBuilder.loadTexts: an80iIdChangedTrap.setStatus('current')
if mibBuilder.loadTexts: an80iIdChangedTrap.setDescription('Event that reports the modification in the configuration of an ID.')
an80iSWUpgradeFailed = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 8)).setObjects(("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"))
if mibBuilder.loadTexts: an80iSWUpgradeFailed.setStatus('current')
if mibBuilder.loadTexts: an80iSWUpgradeFailed.setDescription('Event that reports the failure of a software upgrade opration.')
an80iSWUpgradeSuccess = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 9)).setObjects(("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"))
if mibBuilder.loadTexts: an80iSWUpgradeSuccess.setStatus('current')
if mibBuilder.loadTexts: an80iSWUpgradeSuccess.setDescription('Event that reports the success of a software upgrade opration.')
redlineAn80iConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5))
redlineAn80iGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1))
redlineAn80iCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 2))
redlineAn80iPtpPmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 1)).setObjects(("REDLINE-AN80I-MIB", "an80iOptionsKey"), ("REDLINE-AN80I-MIB", "an80iHardwareType"), ("REDLINE-AN80I-MIB", "an80iRadioType"), ("REDLINE-AN80I-MIB", "an80iSaveConfig"), ("REDLINE-AN80I-MIB", "an80iActivateConfig"), ("REDLINE-AN80I-MIB", "an80iAntennaAllignmentMode"), ("REDLINE-AN80I-MIB", "an80iCurrTxPower"), ("REDLINE-AN80I-MIB", "an80iChannelAutoScan"), ("REDLINE-AN80I-MIB", "an80iCurrFrequency"), ("REDLINE-AN80I-MIB", "an80iOPeratingFrequency"), ("REDLINE-AN80I-MIB", "an80iMaxTxPower"), ("REDLINE-AN80I-MIB", "an80iSystemMode"), ("REDLINE-AN80I-MIB", "an80iRFStatusCode"), ("REDLINE-AN80I-MIB", "an80iDFSAction"), ("REDLINE-AN80I-MIB", "an80iAntennaGain"), ("REDLINE-AN80I-MIB", "an80iActiveRFLinks"), ("REDLINE-AN80I-MIB", "an80iAtpControl"), ("REDLINE-AN80I-MIB", "an80iTurboModeControl"), ("REDLINE-AN80I-MIB", "an80iEtherPortConn"), ("REDLINE-AN80I-MIB", "an80iEtherPortMode"), ("REDLINE-AN80I-MIB", "an80iFlowControl"), ("REDLINE-AN80I-MIB", "an80iLowLatencyMode"), ("REDLINE-AN80I-MIB", "an80iEthernetFollowsWireless"), ("REDLINE-AN80I-MIB", "an80iEthernetFollowsWirelessTimeout"), ("REDLINE-AN80I-MIB", "an80iHttpAccess"), ("REDLINE-AN80I-MIB", "an80iTelnetAccess"), ("REDLINE-AN80I-MIB", "an80iTelnetPort"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"), ("REDLINE-AN80I-MIB", "an80iSwDownloadStatus"), ("REDLINE-AN80I-MIB", "an80iSwDownloadControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iPtpPmpGroup = redlineAn80iPtpPmpGroup.setStatus('current')
if mibBuilder.loadTexts: redlineAn80iPtpPmpGroup.setDescription('AN80i PTP/PMP objects.')
redlineAn80iPmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 2)).setObjects(("REDLINE-AN80I-MIB", "an80iRegistrationPeriod"), ("REDLINE-AN80I-MIB", "an80iMaximumDistance"), ("REDLINE-AN80I-MIB", "an80iRegisteredStations"), ("REDLINE-AN80I-MIB", "an80iRegisteredConnections"), ("REDLINE-AN80I-MIB", "an80iMaxId"), ("REDLINE-AN80I-MIB", "an80iNextAvailId"), ("REDLINE-AN80I-MIB", "an80iLastModifId"), ("REDLINE-AN80I-MIB", "an80iSaveIdConfiguration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iPmpGroup = redlineAn80iPmpGroup.setStatus('current')
if mibBuilder.loadTexts: redlineAn80iPmpGroup.setDescription('AN80i PMP objects.')
redlineAn80iPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 3)).setObjects(("REDLINE-AN80I-MIB", "an80iResetStatistics"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iPtpGroup = redlineAn80iPtpGroup.setStatus('current')
if mibBuilder.loadTexts: redlineAn80iPtpGroup.setDescription('AN80i PTP objects.')
redlineAn80iNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 4)).setObjects(("REDLINE-AN80I-MIB", "an80iPswdChangeFailTrap"), ("REDLINE-AN80I-MIB", "an80iFirmwareConfigFailTrap"), ("REDLINE-AN80I-MIB", "an80iEepromCorruptedTrap"), ("REDLINE-AN80I-MIB", "an80iHardwareFailTrap"), ("REDLINE-AN80I-MIB", "an80iSaveConfigTrap"), ("REDLINE-AN80I-MIB", "an80iDFSEventTrap"), ("REDLINE-AN80I-MIB", "an80iIdChangedTrap"), ("REDLINE-AN80I-MIB", "an80iSWUpgradeFailed"), ("REDLINE-AN80I-MIB", "an80iSWUpgradeSuccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iNotificationGroup = redlineAn80iNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: redlineAn80iNotificationGroup.setDescription('The notifications which indicate specific events within the AN80i unit.')
redlineAn80iCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 2, 1)).setObjects(("REDLINE-AN80I-MIB", "redlineAn80iPtpPmpGroup"), ("REDLINE-AN80I-MIB", "redlineAn80iPmpGroup"), ("REDLINE-AN80I-MIB", "redlineAn80iPtpGroup"), ("REDLINE-AN80I-MIB", "redlineAn80iNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iCompliance = redlineAn80iCompliance.setStatus('current')
if mibBuilder.loadTexts: redlineAn80iCompliance.setDescription('The compliance statement for AN80i entities that implement this MIB module.')
mibBuilder.exportSymbols("REDLINE-AN80I-MIB", redlineAn80iSystemObjects=redlineAn80iSystemObjects, an80iEtherPortConn=an80iEtherPortConn, an80iEthernetFollowsWireless=an80iEthernetFollowsWireless, an80iRegisteredStations=an80iRegisteredStations, an80iResetStatistics=an80iResetStatistics, an80iSaveConfig=an80iSaveConfig, an80iAtpControl=an80iAtpControl, an80iDFSAction=an80iDFSAction, an80iRFStatusCode=an80iRFStatusCode, an80iSwDownloadControl=an80iSwDownloadControl, an80iHttpAccess=an80iHttpAccess, an80iChannelAutoScan=an80iChannelAutoScan, an80iSwDownloadTftpFile=an80iSwDownloadTftpFile, an80iSwDownloadStatus=an80iSwDownloadStatus, an80iActivateConfig=an80iActivateConfig, redlineAn80iEthernetObjects=redlineAn80iEthernetObjects, redlineAn80iPtpSystemObjects=redlineAn80iPtpSystemObjects, redlineAn80iManagObjects=redlineAn80iManagObjects, an80iHardwareFailTrap=an80iHardwareFailTrap, an80iOptionsKey=an80iOptionsKey, redlineAn80iWirelesObjects=redlineAn80iWirelesObjects, an80iMaxTxPower=an80iMaxTxPower, redlineAn80iPtpPmpObjects=redlineAn80iPtpPmpObjects, an80iSwDownloadTftpAddress=an80iSwDownloadTftpAddress, an80iOptionsKeyTable=an80iOptionsKeyTable, an80iChannelWidth=an80iChannelWidth, an80iAntennaGain=an80iAntennaGain, redlineAn80iSWUpgradeObjects=redlineAn80iSWUpgradeObjects, an80iNextAvailId=an80iNextAvailId, an80iSaveIdConfiguration=an80iSaveIdConfiguration, an80iOptionsKeyStatus=an80iOptionsKeyStatus, an80iSWUpgradeSuccess=an80iSWUpgradeSuccess, redlineAn80iTrapDefinitions=redlineAn80iTrapDefinitions, redlineAn80iMib=redlineAn80iMib, redlineAn80iCompliance=redlineAn80iCompliance, redlineAn80iPmpWirelesObjects=redlineAn80iPmpWirelesObjects, an80iRegisteredConnections=an80iRegisteredConnections, an80iSaveConfigTrap=an80iSaveConfigTrap, redlineAn80iNotificationGroup=redlineAn80iNotificationGroup, redlineAn80iPtpObjects=redlineAn80iPtpObjects, an80iPswdChangeFailTrap=an80iPswdChangeFailTrap, an80iOptionsKeyId=an80iOptionsKeyId, an80iLastModifId=an80iLastModifId, an80iSystemMode=an80iSystemMode, an80iLowLatencyMode=an80iLowLatencyMode, an80iRadioType=an80iRadioType, an80iEthernetFollowsWirelessTimeout=an80iEthernetFollowsWirelessTimeout, redlineAn80iConformance=redlineAn80iConformance, an80iAntennaAllignmentMode=an80iAntennaAllignmentMode, an80iTelnetAccess=an80iTelnetAccess, an80iFlowControl=an80iFlowControl, an80iDFSEventTrap=an80iDFSEventTrap, redlineAn80iPtpPmpGroup=redlineAn80iPtpPmpGroup, an80iMaximumDistance=an80iMaximumDistance, an80iIdChangedTrap=an80iIdChangedTrap, an80iHardwareType=an80iHardwareType, an80iMaxId=an80iMaxId, an80iEepromCorruptedTrap=an80iEepromCorruptedTrap, PYSNMP_MODULE_ID=redlineAn80iMib, an80iEtherPortMode=an80iEtherPortMode, redlineAn80iPmpGroup=redlineAn80iPmpGroup, an80iSWUpgradeFailed=an80iSWUpgradeFailed, an80iTelnetPort=an80iTelnetPort, an80iTurboModeControl=an80iTurboModeControl, redlineAn80iGroups=redlineAn80iGroups, an80iCurrFrequency=an80iCurrFrequency, redlineAn80iPtpGroup=redlineAn80iPtpGroup, an80iActiveRFLinks=an80iActiveRFLinks, an80iSwDownloadTftpAddressType=an80iSwDownloadTftpAddressType, an80iFirmwareConfigFailTrap=an80iFirmwareConfigFailTrap, an80iOptionsKeyEntry=an80iOptionsKeyEntry, an80iOPeratingFrequency=an80iOPeratingFrequency, an80iRegistrationPeriod=an80iRegistrationPeriod, redlineAn80iCompls=redlineAn80iCompls, an80iCurrTxPower=an80iCurrTxPower, redlineAn80iPmpObjects=redlineAn80iPmpObjects)
