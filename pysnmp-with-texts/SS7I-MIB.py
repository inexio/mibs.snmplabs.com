#
# PySNMP MIB module SS7I-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SS7I-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, IpAddress, ModuleIdentity, TimeTicks, Bits, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, experimental, NotificationType, Unsigned32, iso, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "IpAddress", "ModuleIdentity", "TimeTicks", "Bits", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "experimental", "NotificationType", "Unsigned32", "iso", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
nas = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1))
ss7i = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35))
ss7iCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35, 1))
ss7iCfgTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1), )
if mibBuilder.loadTexts: ss7iCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgTable.setDescription('The Configuration Table contains an entry for each of the manageable HiPer SS7i cards in the chassis. It contains objects that reflect the current configuration of parameters that affect the operation of all the entities that reside on the given card.')
ss7iCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1), ).setIndexNames((0, "SS7I-MIB", "ss7iCfgIndex"))
if mibBuilder.loadTexts: ss7iCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgEntry.setDescription('There is one Configuration Table entry per HiPer SS7i Card in the chassis.')
ss7iCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iCfgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgIndex.setDescription('A unique value for each HiPer SS7i card in the chassis. The value of ss7iCfgIndex matches the value of the index for the corresponding HiPer SS7i card entity in the entity table of the chassis MIB.')
ss7iCfgIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgIpAddr.setDescription('The IP address on interface 0 of the HiPer SS7i.')
ss7iCfgNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgNetmask.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgNetmask.setDescription('The netmask on interface 0 of the HiPer SS7i.')
ss7iCfgDfltGwIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgDfltGwIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgDfltGwIpAddr.setDescription('The IP address of the default IP routing gateway.')
ss7iCfgProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("slapV2", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgProtocol.setDescription('The external signaling protocol running over the TCP/IP connection with the external signaling gateway. Default = hss7iSlapV2(1).')
ss7iCfgGwConnStartMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lsAuto", 1), ("lsManual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgGwConnStartMethod.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgGwConnStartMethod.setDescription('The method used by the HiPer SS7i to bring up the TCP/IP connection to the external signaling gateway at boot time.')
ss7iCfgGwIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgGwIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgGwIpAddr.setDescription('The primary external SS7 gateway IP address. Valid for SLAP only.')
ss7iCfgGwPort = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgGwPort.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgGwPort.setDescription('The primary external SS7 gateway port number. Valid for SLAP only.')
ss7iCfgSecGwIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgSecGwIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgSecGwIpAddr.setDescription('The secondary external SS7 gateway IP address. Valid for SLAP only.')
ss7iCfgSecGwPort = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgSecGwPort.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgSecGwPort.setDescription('The secondary external SS7 gateway port number. Valid for SLAP only.')
ss7iCfgHrtbtTimerNearEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgHrtbtTimerNearEnd.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgHrtbtTimerNearEnd.setDescription('The HiPer SS7i heartbeat timer. Upon expiration, the HiPer SS7i will send a heartbeat message to the external SS7 gateway. The time should be less than what the gateway expects. Valid for SLAP only. Default = 15000 msec.')
ss7iCfgHrtbtTimerFarEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgHrtbtTimerFarEnd.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgHrtbtTimerFarEnd.setDescription('The external SS7 gateway heartbeat timer. Upon expiration it causes the HiPer SS7i to commence the connection re-establishment procedure to the external SS7 gateway. The time should be longer than what the external SS7 gateway is set to. Valid for SLAP only. Default = 15000 msec.')
ss7iCfgChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgChassisId.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgChassisId.setDescription('This uniquely identifies logical Chassis under the control of the HiPer SS7I, valid for SLAP only. The OCTET STRING format must be FF FF FF FF .')
ss7iCfgGwConnRetryCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgGwConnRetryCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgGwConnRetryCnt.setDescription('The number of times the HiPer SS7i will attempt to re-establish the TCP/IP connection to the external SS7 gateway after the initial failure was detected. Valid for SLAP only. Default = 3.')
ss7iCfgGwConnRetryIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgGwConnRetryIntvl.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgGwConnRetryIntvl.setDescription('The time interval between attempts of the HiPer SS7i to re-establish the TCP/IP connection to the external SS7 gateway. Valid for SLAP only. Default = 2 sec.')
ss7iCfgGwMssdHrtbtThrsh = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 1, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCfgGwMssdHrtbtThrsh.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCfgGwMssdHrtbtThrsh.setDescription('The number of external SS7 gateway heartbeat timeouts allowed before the connection to the gateway is considered lost. A setting of 0 means no attempt will be made to re-establish the connection. Default = 1.')
ss7iCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35, 2))
ss7iCmdTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1), )
if mibBuilder.loadTexts: ss7iCmdTable.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdTable.setDescription('The Command table contains an entry for each of the manageable HiPer SS7i cards in the chassis. It provides a means through which to take specific actions on them.')
ss7iCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1), ).setIndexNames((0, "SS7I-MIB", "ss7iCmdIndex"))
if mibBuilder.loadTexts: ss7iCmdEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdEntry.setDescription('There is one Command Table entry per HiPer SS7i card in the chassis.')
ss7iCmdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iCmdIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdIndex.setDescription("A unique value for each HiPer SS7i card in the chassis. The value of this object matches the value of the index of the corresponding HiPer SS7i card's entry in the entity table of the chassis MIB.")
ss7iCmdMgtStationId = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCmdMgtStationId.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdMgtStationId.setDescription('This object is a generic read-write variable that a Management Station (MS) can use to guarantee that the results from a given command are the results of a command issued by that specific MS. Each MS must SET a unique value to this object when doing commands and GET the value of this object together with ss7iCmdReqId and ss7iCmdResult to detect interference from other MSs.')
ss7iCmdReqId = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iCmdReqId.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdReqId.setDescription('This object contains the value of the request-id field in the SNMP PDU which invoked the current or most recent command or test on this HiPer SS7i card. If the request-id is unknown or undefined, this object contains the value zero.')
ss7iCmdFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("noCommand", 1), ("saveToNVRAM", 2), ("restoreFromNVRAM", 3), ("restoreFromDefault", 4), ("softwareReset", 5), ("startSS7GwConn", 6), ("shutDownSS7GwConn", 7), ("resetSS7Counters", 8), ("resetPbusCounters", 9), ("startPbusConnToAll", 10), ("stopPbusConnToAll", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCmdFunction.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdFunction.setDescription('This object contains a value which describes the command which is being invoked.')
ss7iCmdForce = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("force", 1), ("noForce", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCmdForce.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdForce.setDescription('In some cases, the HiPer SS7i card may be in a state such that certain commands could adversely affect connections. In such cases, a command request with this object not present or set to noForce will result in a warning. If the operator elects to ignore such warnings, this object can be set to force in a subsequent issue of the command to cause the command to be carried out regardless of its potentially hazzardous effects.')
ss7iCmdParam = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iCmdParam.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdParam.setDescription('This object contains parameters that are specific to the particular command being issued. In some cases, there will be no aditional parameters required.')
ss7iCmdResult = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("notSupported", 4), ("unAbleToRun", 5), ("aborted", 6), ("failed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iCmdResult.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdResult.setDescription('This object contains the result of the most recently requested command or test, or the value none(1) if no commands have been requested since the last reset.')
ss7iCmdCode = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 6, 8, 12, 20, 22, 25, 58, 73))).clone(namedValues=NamedValues(("noError", 1), ("unable", 2), ("unrecognizedCommand", 6), ("slotEmpty", 8), ("noResponse", 12), ("unsupportedCommand", 20), ("deviceDisabled", 22), ("testFailed", 25), ("userInterfaceActive", 58), ("pendingSoftwareDownload", 73)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iCmdCode.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iCmdCode.setDescription('The value of this object upon command completion indicates a further description of what went wrong if the command was unsuccessful. In the case of tests, a bit mapped result of each of the sub-tests performed can be found in the status table.')
ss7iTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35, 3))
ss7iTrapTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1), )
if mibBuilder.loadTexts: ss7iTrapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapTable.setDescription('Table containing objects to enable traps on the HiPer SS7i cards in the chassis.')
ss7iTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1), ).setIndexNames((0, "SS7I-MIB", "ss7iTrapIndex"))
if mibBuilder.loadTexts: ss7iTrapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapEntry.setDescription('There is one entry for each HiPer SS7i card in the chassis.')
ss7iTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iTrapIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapIndex.setDescription('A unique index identifying the HiPer SS7i card to which the trap enable objects pertain.')
ss7iTrapPbusLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iTrapPbusLinkUp.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapPbusLinkUp.setDescription('Enables reporting of a trap and/or log message when the ENFAS packet bus signaling link to the HiPer Dsp comes up. Default = disableAll(2).')
ss7iTrapPbusLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iTrapPbusLinkDown.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapPbusLinkDown.setDescription('Enables reporting of a trap and/or log message when the ENFAS packet bus signaling link to the HiPer Dsp goes down. Default = disableAll(2).')
ss7iTrapGwConnUp = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iTrapGwConnUp.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapGwConnUp.setDescription('Enables reporting of a trap and/or log message when the TCP/IP signaling connection to the SS7 (or media) gateway comes up. Default = disableAll(2).')
ss7iTrapGwConnDown = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iTrapGwConnDown.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iTrapGwConnDown.setDescription('Enables reporting of a trap and/or log message when the TCP/IP signaling connection to the SS7 (or media) gateway goes down. Default = disableAll(2).')
ss7iStat = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35, 4))
ss7iStatTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1), )
if mibBuilder.loadTexts: ss7iStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatTable.setDescription('The Statistics table contains an entry for each of the manageable HiPer SS7i cards in the chassis. It contains objects that reflect the current status of the card.')
ss7iStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1), ).setIndexNames((0, "SS7I-MIB", "ss7iStatIndex"))
if mibBuilder.loadTexts: ss7iStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatEntry.setDescription('There is one Statistics table entry for each HiPer SS7i card in the chassis.')
ss7iStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatIndex.setDescription('A unique value for each HiPer SS7i card in the chassis. The value of ss7iStatIndex matches the value of the index for the corresponding Hiper SS7i card entity in the entity table of the chassis MIB.')
ss7iStatGwConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwConnStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwConnStatus.setDescription('Status of the TCP/IP connection with the external signaling gateway. Valid for SLAP only.')
ss7iStatGwNumMsgsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwNumMsgsRcvd.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwNumMsgsRcvd.setDescription('The number of messages received from the external SS7 gateway or the Media Gateway Controller.')
ss7iStatGwNumBytesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwNumBytesRcvd.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwNumBytesRcvd.setDescription('The number of bytes received from the external SS7 gateway or the Media Gateway Controller.')
ss7iStatGwNumMsgsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwNumMsgsSent.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwNumMsgsSent.setDescription('The number of messages sent to the external SS7 gateway or the Media Gateway Controller.')
ss7iStatGwNumBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwNumBytesSent.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwNumBytesSent.setDescription('The number of bytes sent to the external SS7 gateway or the Media Gateway Controller.')
ss7iStatGwMssdHrtbtCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwMssdHrtbtCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwMssdHrtbtCnt.setDescription('The accumulated number of missed heartbeat messages expected to arrive from the external SS7 gateway.')
ss7iStatGwLinkLostCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwLinkLostCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwLinkLostCnt.setDescription('The accumulated number of times the physical Ethernet connection is unplugged or severed.')
ss7iStatGwLinkErrCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwLinkErrCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwLinkErrCnt.setDescription('The accumulated number of errors encountered sending to or receiving from the external SS7 gateway when the TCP/IP connection is believed to be healthy.')
ss7iStatGwLinkDownCause = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("heartbeatTimeout", 2), ("socketSndRcvError", 3), ("physicalLinkSevered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iStatGwLinkDownCause.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iStatGwLinkDownCause.setDescription('The reason the signaling connection to the external SS7 gateway went down.')
ss7iHdm = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35, 5))
ss7iHdmTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1), )
if mibBuilder.loadTexts: ss7iHdmTable.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmTable.setDescription('The ss7iHdm table contains objects for all of the HiPer Dsp cards in the chassis.')
ss7iHdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1), ).setIndexNames((0, "SS7I-MIB", "ss7iHdmIndex"), (0, "SS7I-MIB", "ss7iHdmIndex2"))
if mibBuilder.loadTexts: ss7iHdmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmEntry.setDescription('There is one entry for each HiPer Dsp Card in the chassis.')
ss7iHdmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmIndex.setDescription('A unique value for each HiPer SS7i card in the chassis. The value of ss7iHdmIndex matches the value of the index for the corresponding HiPer SS7i card entity in the entity table of the chassis MIB.')
ss7iHdmIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmIndex2.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmIndex2.setDescription('The secondary index into the ss7iHdm table. There is one entry for each Hiper Dsp in the chassis. The value of the index is equal to the chassis slot number of a HiPer Dsp card.')
ss7iHdmConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("closed", 1), ("opening", 2), ("opened", 3), ("configuring", 4), ("ready", 5), ("closing", 6), ("loopback", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmConnState.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmConnState.setDescription('The state of the signaling packet bus connection to the HiPer Dsp. There is one connection from the HiPer SS7i card to each HiPer Dsp in the chassis.')
ss7iHdmSndPktsOkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmSndPktsOkCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmSndPktsOkCnt.setDescription('The number of packets successfully transmitted over the signaling packet bus connection.')
ss7iHdmSndPktsFailCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmSndPktsFailCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmSndPktsFailCnt.setDescription('The number of packets failing to transmit over the signaling packet bus connection.')
ss7iHdmRcvPktsOkCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmRcvPktsOkCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmRcvPktsOkCnt.setDescription('The number of packets sucessfully received over the signaling packet bus connection.')
ss7iHdmRcvPktsFailCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmRcvPktsFailCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmRcvPktsFailCnt.setDescription('The number of signaling packet bus connection packets rejected by the HiPer SS7i message handler.')
ss7iHdmLinkDownCause = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("missingHdm", 2), ("ss7GwLinkDown", 3), ("pbusSndRcvError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iHdmLinkDownCause.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iHdmLinkDownCause.setDescription('The reason the packet bus ENFAS signaling link to the HiPer Dsp went down.')
ss7iSigPb = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 35, 6))
ss7iSigPbTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1), )
if mibBuilder.loadTexts: ss7iSigPbTable.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iSigPbTable.setDescription('The ss7iSigPb table contains objects for managing the signaling packet bus connections to all of the HiPer Dsp cards in the chassis.')
ss7iSigPbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1), ).setIndexNames((0, "SS7I-MIB", "ss7iSigPbIndex"), (0, "SS7I-MIB", "ss7iSigPbIndex2"))
if mibBuilder.loadTexts: ss7iSigPbEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iSigPbEntry.setDescription('There is one entry for each HiPer Dsp Card in the chassis.')
ss7iSigPbIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iSigPbIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iSigPbIndex.setDescription('A unique value for each HiPer SS7i card in the chassis. The value of ss7iSigPbIndex matches the value of the index for the corresponding HiPer SS7i card entity in the entity table of the chassis MIB.')
ss7iSigPbIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ss7iSigPbIndex2.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iSigPbIndex2.setDescription('The secondary index into the ss7iSigPb table. There is one entry for each Hiper Dsp in the chassis. The value of the index is equal to the chassis slot number of a HiPer Dsp card.')
ss7iSigPbConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iSigPbConnection.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iSigPbConnection.setDescription('The means to enable or disable a signaling packet bus connection between the HiPer SS7i and a Hiper Dsp. Default = disable(1).')
ss7iSigPbLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 35, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ss7iSigPbLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: ss7iSigPbLoopback.setDescription('The means to enable or disable the loopback state on the signaling packet bus connection between the HiPer SS7i and a Hiper Dsp. Default = disable(1).')
mibBuilder.exportSymbols("SS7I-MIB", ss7iCmdCode=ss7iCmdCode, ss7iCfgSecGwIpAddr=ss7iCfgSecGwIpAddr, ss7iCfgSecGwPort=ss7iCfgSecGwPort, ss7iTrapGwConnUp=ss7iTrapGwConnUp, ss7iCfgGwConnRetryCnt=ss7iCfgGwConnRetryCnt, ss7iStat=ss7iStat, ss7iCfgTable=ss7iCfgTable, ss7iCmdTable=ss7iCmdTable, ss7iTrapIndex=ss7iTrapIndex, ss7iTrapTable=ss7iTrapTable, ss7iStatEntry=ss7iStatEntry, ss7iHdmRcvPktsOkCnt=ss7iHdmRcvPktsOkCnt, ss7iSigPbTable=ss7iSigPbTable, ss7iStatGwConnStatus=ss7iStatGwConnStatus, ss7iCfgIpAddr=ss7iCfgIpAddr, ss7iSigPbEntry=ss7iSigPbEntry, ss7iCfgChassisId=ss7iCfgChassisId, ss7iCmdEntry=ss7iCmdEntry, ss7iStatGwLinkLostCnt=ss7iStatGwLinkLostCnt, ss7iCfgEntry=ss7iCfgEntry, ss7iTrapGwConnDown=ss7iTrapGwConnDown, ss7iHdmTable=ss7iHdmTable, ss7iSigPb=ss7iSigPb, ss7iStatGwNumBytesRcvd=ss7iStatGwNumBytesRcvd, ss7iHdmIndex2=ss7iHdmIndex2, ss7iStatIndex=ss7iStatIndex, ss7iCfgGwMssdHrtbtThrsh=ss7iCfgGwMssdHrtbtThrsh, ss7iCmdForce=ss7iCmdForce, ss7iCfgProtocol=ss7iCfgProtocol, nas=nas, ss7iCmdParam=ss7iCmdParam, ss7iCmdResult=ss7iCmdResult, ss7i=ss7i, ss7iHdmConnState=ss7iHdmConnState, ss7iCfgHrtbtTimerFarEnd=ss7iCfgHrtbtTimerFarEnd, ss7iHdmSndPktsOkCnt=ss7iHdmSndPktsOkCnt, ss7iStatTable=ss7iStatTable, ss7iCfgGwPort=ss7iCfgGwPort, ss7iCfg=ss7iCfg, ss7iCmd=ss7iCmd, ss7iCmdReqId=ss7iCmdReqId, ss7iTrapPbusLinkUp=ss7iTrapPbusLinkUp, ss7iTrapEntry=ss7iTrapEntry, ss7iCfgGwConnStartMethod=ss7iCfgGwConnStartMethod, ss7iCfgHrtbtTimerNearEnd=ss7iCfgHrtbtTimerNearEnd, ss7iStatGwNumMsgsRcvd=ss7iStatGwNumMsgsRcvd, ss7iSigPbIndex=ss7iSigPbIndex, ss7iCfgNetmask=ss7iCfgNetmask, ss7iCfgDfltGwIpAddr=ss7iCfgDfltGwIpAddr, ss7iCfgIndex=ss7iCfgIndex, ss7iStatGwNumBytesSent=ss7iStatGwNumBytesSent, ss7iStatGwNumMsgsSent=ss7iStatGwNumMsgsSent, ss7iHdmSndPktsFailCnt=ss7iHdmSndPktsFailCnt, ss7iHdm=ss7iHdm, ss7iStatGwMssdHrtbtCnt=ss7iStatGwMssdHrtbtCnt, ss7iHdmIndex=ss7iHdmIndex, ss7iStatGwLinkDownCause=ss7iStatGwLinkDownCause, ss7iHdmEntry=ss7iHdmEntry, ss7iSigPbConnection=ss7iSigPbConnection, ss7iCmdIndex=ss7iCmdIndex, ss7iTrap=ss7iTrap, usr=usr, ss7iCfgGwIpAddr=ss7iCfgGwIpAddr, ss7iStatGwLinkErrCnt=ss7iStatGwLinkErrCnt, ss7iHdmRcvPktsFailCnt=ss7iHdmRcvPktsFailCnt, ss7iCfgGwConnRetryIntvl=ss7iCfgGwConnRetryIntvl, ss7iHdmLinkDownCause=ss7iHdmLinkDownCause, ss7iTrapPbusLinkDown=ss7iTrapPbusLinkDown, ss7iCmdMgtStationId=ss7iCmdMgtStationId, ss7iSigPbIndex2=ss7iSigPbIndex2, ss7iSigPbLoopback=ss7iSigPbLoopback, ss7iCmdFunction=ss7iCmdFunction)
