#
# PySNMP MIB module ZYXEL-PROWIRELESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-PROWIRELESS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, ModuleIdentity, iso, enterprises, IpAddress, Bits, TimeTicks, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "iso", "enterprises", "IpAddress", "Bits", "TimeTicks", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter64", "NotificationType")
DisplayString, DateAndTime, TextualConvention, PhysAddress, TruthValue, RowStatus, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "PhysAddress", "TruthValue", "RowStatus", "RowPointer")
class DisplayString(OctetString):
    pass

zyxel = MibIdentifier((1, 3, 6, 1, 4, 1, 890))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1))
proWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9))
pwCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 1))
pwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2))
pwStations = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 3))
pwAPDetect = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 4))
pwWlanControl = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 5))
pwWlanExtControl = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 6))
pwSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwSwVersion.setStatus('mandatory')
if mibBuilder.loadTexts: pwSwVersion.setDescription('The current software version.')
pwCfgVersion = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwCfgVersion.setStatus('mandatory')
if mibBuilder.loadTexts: pwCfgVersion.setDescription('The current WLAN configuration version.')
pwTftpServer = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpServer.setStatus('mandatory')
if mibBuilder.loadTexts: pwTftpServer.setDescription('TFTP download server IP Address.')
pwTftpFileName = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpFileName.setStatus('mandatory')
if mibBuilder.loadTexts: pwTftpFileName.setDescription('TFTP file name in TFTP server.')
pwTftpFileType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("software", 1), ("romfile", 2), ("textconfig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpFileType.setStatus('mandatory')
if mibBuilder.loadTexts: pwTftpFileType.setDescription('File type in TFTP server.')
pwTftpOpStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 0), ("inprogress", 1), ("failed", 2), ("success", 3), ("timeout", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwTftpOpStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pwTftpOpStatus.setDescription('TFTP Operation Status.')
pwTftpOpCommand = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upload", 1), ("download", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTftpOpCommand.setStatus('mandatory')
if mibBuilder.loadTexts: pwTftpOpCommand.setDescription('TFTP Operation Command.')
pwSystemReboot = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("running", 0), ("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwSystemReboot.setStatus('mandatory')
if mibBuilder.loadTexts: pwSystemReboot.setDescription('System Reboot.')
pwAutoCfgMessage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAutoCfgMessage.setStatus('mandatory')
if mibBuilder.loadTexts: pwAutoCfgMessage.setDescription('The last error massage of Auto Configuration process.')
pwStationTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2), )
if mibBuilder.loadTexts: pwStationTable.setStatus('current')
if mibBuilder.loadTexts: pwStationTable.setDescription('This table lists the associated stations.')
pwStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1), ).setIndexNames((0, "ZYXEL-PROWIRELESS-MIB", "pwStationIndex"))
if mibBuilder.loadTexts: pwStationEntry.setStatus('current')
if mibBuilder.loadTexts: pwStationEntry.setDescription('An entry describing the station information.')
pwStationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pwStationIndex.setStatus('current')
if mibBuilder.loadTexts: pwStationIndex.setDescription('Index of stations.')
pwStationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 2), OctetString().clone('public')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwStationMacAddress.setStatus('current')
if mibBuilder.loadTexts: pwStationMacAddress.setDescription('The MAC Addresss of the station.')
pwStationAssociateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwStationAssociateTime.setStatus('current')
if mibBuilder.loadTexts: pwStationAssociateTime.setDescription('The associated time of the station.')
pwStationSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwStationSSID.setStatus('current')
if mibBuilder.loadTexts: pwStationSSID.setDescription('The associated ssid.')
pwStationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwStationStatus.setStatus('current')
if mibBuilder.loadTexts: pwStationStatus.setDescription('Controls and reflects the status of rows in this the row is active.')
pwAPDetectInterval = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwAPDetectInterval.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectInterval.setDescription('AP Detection Interval, time unit is minute. Minimum value is 3 minutes.')
pwAPDetectTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2), )
if mibBuilder.loadTexts: pwAPDetectTable.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectTable.setDescription('This table lists the neighbor AP.')
pwAPDetectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1), ).setIndexNames((0, "ZYXEL-PROWIRELESS-MIB", "pwAPDetectIndex"))
if mibBuilder.loadTexts: pwAPDetectEntry.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectEntry.setDescription('An entry describing the neighbor AP information.')
pwAPDetectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectIndex.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectIndex.setDescription('The index of neighbor AP table.')
pwAPDetectSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectSSID.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectSSID.setDescription("The SSID. If SSID of the AP is hidden, it will be displayed as '(Hidden SSID)'.")
pwAPDetectMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectMacAddress.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectMacAddress.setDescription('The MAC address.')
pwAPDetectChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectChannel.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectChannel.setDescription('The frequency channel ID.')
pwAPDetectSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectSignal.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectSignal.setDescription('The received signal strength, which represented as a percetage.')
pwAPDetectNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("infra", 0), ("adhoc", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectNetwork.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectNetwork.setDescription('The network mode.')
pwAPDetectSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("wep", 1), ("wpa", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwAPDetectSecurity.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectSecurity.setDescription('The data security mode.')
pwAPDetectStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAPDetectStatus.setStatus('current')
if mibBuilder.loadTexts: pwAPDetectStatus.setDescription('Controls and reflects the status of rows in this the row is active.')
pwMacFilterActive = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwMacFilterActive.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterActive.setDescription('Enable/Disable MAC Filter.')
pwMacFilterAction = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accept", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwMacFilterAction.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterAction.setDescription('Accept or discard the matched packets.')
pwMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3), )
if mibBuilder.loadTexts: pwMacFilterTable.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterTable.setDescription('This table lists the Mac Filter.')
pwMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1), ).setIndexNames((0, "ZYXEL-PROWIRELESS-MIB", "pwMacFilterIndex"))
if mibBuilder.loadTexts: pwMacFilterEntry.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterEntry.setDescription('An entry describing the Mac Filter information.')
pwMacFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwMacFilterIndex.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterIndex.setDescription('The index of MAC Filter table.')
pwMacFilterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwMacFilterMacAddress.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterMacAddress.setDescription('The MAC address.')
pwMacFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwMacFilterStatus.setStatus('current')
if mibBuilder.loadTexts: pwMacFilterStatus.setDescription('Controls and reflects the status of rows in this the row is active.')
pwWlanTxPower = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("disabled", 0), ("full", 1), ("half", 2), ("quarter", 4), ("eighth", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwWlanTxPower.setStatus('current')
if mibBuilder.loadTexts: pwWlanTxPower.setDescription('To specify the RF transmission power.')
pwTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1))
pwTrapVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2))
pwTrapTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3))
pwWirelessTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1))
pwSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 2))
pwTFTPTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 3))
pwTrapWirelessStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTrapWirelessStatus.setStatus('current')
if mibBuilder.loadTexts: pwTrapWirelessStatus.setDescription('Controls wireless group traps enable or disable.')
pwTrapSecurityStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTrapSecurityStatus.setStatus('current')
if mibBuilder.loadTexts: pwTrapSecurityStatus.setDescription('Controls security group traps enable or disable.')
pwTrapTFTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwTrapTFTPStatus.setStatus('current')
if mibBuilder.loadTexts: pwTrapTFTPStatus.setDescription('Controls TFTP group traps enable or disable.')
pwTrapGenericMessage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pwTrapGenericMessage.setStatus('current')
if mibBuilder.loadTexts: pwTrapGenericMessage.setDescription('Provide generic information on traps.')
pwTrapMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pwTrapMACAddress.setStatus('current')
if mibBuilder.loadTexts: pwTrapMACAddress.setDescription('Represents MAC address of the device or the host which triggers the trap.')
pwTrapWlanSSID = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pwTrapWlanSSID.setStatus('current')
if mibBuilder.loadTexts: pwTrapWlanSSID.setDescription('The SSID name which the wireless client associates.')
pwWlanStaAssociation = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1, 1))
if mibBuilder.loadTexts: pwWlanStaAssociation.setStatus('current')
if mibBuilder.loadTexts: pwWlanStaAssociation.setDescription('Wireless client assocication notification.')
pwWlanStaDisassociation = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1, 2))
if mibBuilder.loadTexts: pwWlanStaDisassociation.setStatus('current')
if mibBuilder.loadTexts: pwWlanStaDisassociation.setDescription('Wireless client disassocication notification.')
pwWlanStaAuthFail = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 2, 1))
if mibBuilder.loadTexts: pwWlanStaAuthFail.setStatus('current')
if mibBuilder.loadTexts: pwWlanStaAuthFail.setDescription('Wireless client authentication failed.')
pwTFTPStatus = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 3, 1)).setObjects(("ZYXEL-PROWIRELESS-MIB", "pwTrapGenericMessage"), ("ZYXEL-PROWIRELESS-MIB", "pwTftpOpStatus"), ("ZYXEL-PROWIRELESS-MIB", "pwTftpServer"), ("ZYXEL-PROWIRELESS-MIB", "pwTftpFileName"), ("ZYXEL-PROWIRELESS-MIB", "pwTftpFileType"), ("ZYXEL-PROWIRELESS-MIB", "pwTftpOpCommand"))
if mibBuilder.loadTexts: pwTFTPStatus.setStatus('current')
if mibBuilder.loadTexts: pwTFTPStatus.setDescription('Send when TFTP operation completed, or stopped due to some reason. For example, timeout or wrong configuration.')
mibBuilder.exportSymbols("ZYXEL-PROWIRELESS-MIB", pwMacFilterIndex=pwMacFilterIndex, pwTrapGenericMessage=pwTrapGenericMessage, pwTftpServer=pwTftpServer, proWireless=proWireless, pwWlanStaAssociation=pwWlanStaAssociation, pwTftpFileName=pwTftpFileName, pwTrapTFTPStatus=pwTrapTFTPStatus, pwTftpFileType=pwTftpFileType, pwTftpOpStatus=pwTftpOpStatus, pwTrapVariables=pwTrapVariables, pwSecurityTraps=pwSecurityTraps, pwWlanControl=pwWlanControl, pwAPDetectSSID=pwAPDetectSSID, pwAPDetectNetwork=pwAPDetectNetwork, pwCfgVersion=pwCfgVersion, pwAPDetectTable=pwAPDetectTable, pwAPDetectSecurity=pwAPDetectSecurity, pwTraps=pwTraps, pwAPDetectChannel=pwAPDetectChannel, pwMacFilterEntry=pwMacFilterEntry, pwStationStatus=pwStationStatus, pwStationIndex=pwStationIndex, products=products, pwStationSSID=pwStationSSID, zyxel=zyxel, pwStationAssociateTime=pwStationAssociateTime, pwMacFilterTable=pwMacFilterTable, pwTrapSecurityStatus=pwTrapSecurityStatus, pwTFTPStatus=pwTFTPStatus, pwTrapWlanSSID=pwTrapWlanSSID, pwTrapMACAddress=pwTrapMACAddress, pwMacFilterMacAddress=pwMacFilterMacAddress, pwTrapControl=pwTrapControl, DisplayString=DisplayString, pwSystemReboot=pwSystemReboot, pwAutoCfgMessage=pwAutoCfgMessage, pwMacFilterActive=pwMacFilterActive, pwCommon=pwCommon, pwStationEntry=pwStationEntry, pwAPDetectMacAddress=pwAPDetectMacAddress, pwAPDetectInterval=pwAPDetectInterval, pwMacFilterAction=pwMacFilterAction, pwWlanExtControl=pwWlanExtControl, pwStationTable=pwStationTable, pwSwVersion=pwSwVersion, pwWlanTxPower=pwWlanTxPower, pwAPDetectEntry=pwAPDetectEntry, pwAPDetectStatus=pwAPDetectStatus, pwStations=pwStations, pwTrapTypes=pwTrapTypes, pwWirelessTraps=pwWirelessTraps, pwMacFilterStatus=pwMacFilterStatus, pwTFTPTraps=pwTFTPTraps, pwWlanStaDisassociation=pwWlanStaDisassociation, pwTrapWirelessStatus=pwTrapWirelessStatus, pwTftpOpCommand=pwTftpOpCommand, pwStationMacAddress=pwStationMacAddress, pwAPDetectSignal=pwAPDetectSignal, pwAPDetectIndex=pwAPDetectIndex, pwWlanStaAuthFail=pwWlanStaAuthFail, pwAPDetect=pwAPDetect)