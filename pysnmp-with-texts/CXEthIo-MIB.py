#
# PySNMP MIB module CXEthIo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXEthIo-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
Alias, cxEthIo = mibBuilder.importSymbols("CXProduct-SMI", "Alias", "cxEthIo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Unsigned32, Bits, NotificationType, MibIdentifier, IpAddress, TimeTicks, iso, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "iso", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ethSapOprTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1), )
if mibBuilder.loadTexts: ethSapOprTable.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprTable.setDescription('Provides configuration information for each Ethernet service access point and its associated hardware ports. It also provides statistical information about activity at the interface. Each row of the table (entry) contains information that corresponds to a particular service access point.')
ethSapOprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1), ).setIndexNames((0, "CXEthIo-MIB", "ethSapOprNumber"))
if mibBuilder.loadTexts: ethSapOprEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprEntry.setDescription('Provides the configuration of a particular Ethernet service access point and its associated hardware port. It also provides statistical information about activity at the interface.')
ethSapOprNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethSapOprNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprNumber.setDescription('Identifies the service access point by a numerical value. Each service access point is assigned a unique number. The number is assigned by the system.')
ethSapOprAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 2), Alias()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethSapOprAlias.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprAlias.setDescription('Identifies the textual name (Alias) of this service access point. Each service access point must have a unique name. Range of Values: 0-16 alphanumeric characters. (Note that the first character must be a letter and spaces are not allowed). Default Value: None')
ethSapOprConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("aui", 2), ("tbaset", 3), ("baset-100", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethSapOprConnectorType.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprConnectorType.setDescription('Identifies the connector type used for the hardware port. Options: auto (1): (connector type detected automatically) aui (2): tbaseT (3): 100baseT (4) 100 Mbs Ethernet Default Value: auto')
ethSapOprDataGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("enabled-verify", 3), ("retrigger", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapOprDataGenerator.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprDataGenerator.setDescription('Determines whether the Data Generator is enabled. The Data Generator is used for testing purposes. Options: disabled (1) enabled (2) enabled-verify(3): The data generator is enabled and it checks what it receives against what it has sent. The result of the test is displayed in ethStatOprRxGenErrors. If this option is selected ethSapOprLoobackType must be set to remote. retrigger (4): The data generator repeats the transmission as specified in ethSapOprGenFrames and ethSapOprGen. Default Value: disabled Configuration Changed: administrative The change cannot be saved.')
ethSapOprGenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapOprGenFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprGenFrames.setDescription('Determines the number of times a frame will be generated (for testing purposes). Frames are generated every 1 msec. If the value is set to zero, then frames will be generated continuously (every 1 msec). If the Data Generator is disabled (using ethSapOprDataGenerator), then the value is ignored. Range of Values: 0 - 255 Default Value: 1')
ethSapOprGenFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapOprGenFrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprGenFrameSize.setDescription('Determines the size of the frames (in bytes) to be generated (for testing purposes). If the Data Generator is disabled, then this value is ignored. Range of Values: 0-1514 bytes Default Value: 512 bytes Configuration Changed: administrative The change cannot be saved.')
ethSapOprLoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("local", 2), ("remote", 3), ("both", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethSapOprLoopbackType.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapOprLoopbackType.setDescription('Determines whether the port performs remote loopback, local loopback or both. Options: none (1): Loopback is disabled. local (2): The Service Access Point associated with the port returns all frames to the originating layer without transmitting them. remote (3): The port transmists back whatever it receives. (This implies that the Service Access Point associated with the port will not permit communications with any upper layer requesting service.) both (4): Both remote and local loopback enabled. Default Value: none (1) Configuration Changed: administrative The change cannot be saved.')
ethOprControlStats = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearSapStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: ethOprControlStats.setStatus('mandatory')
if mibBuilder.loadTexts: ethOprControlStats.setDescription('Determines whether the statistics for the hardware port will be cleared. When the clearSapStats option is selected all the counters for the port are cleared. Options: clearSapStats (clears statistics for the hardware port).')
ethStatOprLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprLinkState.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprLinkState.setDescription('Identifies whether the hardware port is available. If there is a problem with the port (e.g. a faulty connection) the value will be down. Options: up (1) down (2) Default Value: None')
ethStatOprInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprInFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprInFrames.setDescription('Identifies the total number of frames received by this port. The value indicates the activity at this interface. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprInOctets.setDescription('Identifies the total number of octets received by this port. The value indicates the activity at this interface. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprInErrors.setDescription('Identifies the total number of errors received by this port. Errors include overrun errors, non-octet errors, and CRC errors. A high count may indicate a hardware problem. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprInDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprInDiscards.setDescription('Identifies the total number of frames received and discarded due to errors or other conditions (i.e. busy, lack of receive buffers, frames received while port not bound to an upper layer.) A high count may indicate that the port is not bound to an upper layer. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprInBusyDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprInBusyDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprInBusyDiscards.setDescription('Identifies the total number of frames received and discarded as a result of a lack of receive buffers. A high count may indicate system resources are low. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprOutFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprOutFrames.setDescription('Identifies the total number of frames transmitted by this port. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprOutOctets.setDescription('Identifies the total number of octets transmitted by this port. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprOutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprOutErrors.setDescription('Identifies the total number of errors transmitted by this port. The count includes Transmitter Underrun, Carrier sense Lost During Frame Transmission, Attempts Limits Expires, and Late Collisions. A high count may indicate a hardware problem. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprOutDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprOutDiscards.setDescription('Identifies the total number of frames which were unsuccessfully transmitted due to a lack of transmit buffers. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprOutCSLostFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprOutCSLostFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprOutCSLostFrames.setDescription('Identifies the total number of transmitted frames for which the carrier sense lost condition was encountered during transmission. A high count may indicate that the device was unplugged during transmission. Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethStatOprRxGenErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethStatOprRxGenErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ethStatOprRxGenErrors.setDescription('Identifies the total number of frames received that contain errors (for a port that has enable-verify set in ethSapOprDataGenerator.) Range of Values: 0 to 4, 294, 967, 295 Default Value: None')
ethSapAdmTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2), )
if mibBuilder.loadTexts: ethSapAdmTable.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmTable.setDescription('Provides configuration information for each Ethernet service access point and its associated hardware port. Each row (entry) of the table corresponds to a particular service access point.')
ethSapAdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1), ).setIndexNames((0, "CXEthIo-MIB", "ethSapAdmNumber"))
if mibBuilder.loadTexts: ethSapAdmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmEntry.setDescription('Provides configuration information for a particular Ethernet service access point and its associated hardware port.')
ethSapAdmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethSapAdmNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmNumber.setDescription('Identifies the service access point by a number. Each service access point is assigned a unique number. The number is assigned by the system.')
ethSapAdmAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 2), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapAdmAlias.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmAlias.setDescription('Determines the textual name (alias) of this service access point. Each service access point is assigned a unique name. Range of Values: 0-16 alphanumeric characters. (Note that the first character must be a letter; spaces are not allowed). Related Parameters: The alias must be the same as the one used in cxCfgIpxPortSubnetworkSAPAlias and cxCfgIpAdEntSubnetworkSAPAlias.')
ethSapAdmConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("aui", 2), ("tbaseT", 3), ("baset-100", 4))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapAdmConnectorType.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmConnectorType.setDescription('Identifies the connector type used for the hardware port. Options: auto (1): connector type detected automatically aui (2) tbaseT (3) 100baseT (4) 100 Mbs Ethernet Default Value: auto (1) Configuration Changed: administrative Further action: to activate changed value, click on Action in EMS menu bar, then click on Reset with Save.')
ethSapAdmDataGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("enabled-verify", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapAdmDataGenerator.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmDataGenerator.setDescription('Determines whether the Data Generator is enabled. The Data Generator is used for testing purposes. Options: disabled (1) enabled.(2) enabled-verify.(3) The data generator is enabled and it checks what it receives against what it has sent. The result of the test is displayed in ethStatAdmrRxGenErrors. If this option is selected, ethSapOprLoobackType must be set to remote. Default Value: disabled (1) Configuration Changed: administrative')
ethSapAdmGenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapAdmGenFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmGenFrames.setDescription('Determines the number of times a frame will be generated (for testing purposes). Frames are generated every 1 msec. If the value is set to zero, then frames will be generated continuously (every 1 msec). If the Data Generator is disabled (using ethSapAdmDataGenerator), then the value is ignored. Range of Values: 0 - 255 Default Value: 1 Configuration Changed: administrative')
ethSapAdmGenFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1514)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapAdmGenFrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmGenFrameSize.setDescription('Determines the size of the frames (in bytes) to be generated (for testing purposes). If the Data Generator is disabled, then this value is ignored. Range of Values: 0 -1514 bytes Default Value:512 bytes Configuration Changed: administrative')
ethSapAdmLoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 45, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("local", 2), ("remote", 3), ("both", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethSapAdmLoopbackType.setStatus('mandatory')
if mibBuilder.loadTexts: ethSapAdmLoopbackType.setDescription('Determines whether the port performs remote loopback, local loopback or both. Options: none (1): Loopback is disabled. local (2): The Service Access Point associated with the port returns all frames to the originating layer without transmitting them. remote (3): The port transmists back whatever it receives. (This implies that the Service Access Point associated with the port will not permit communications with any upper layer requesting service.) both (4): Both remote and local loopback enabled. Default Value: none (1) Configuration Changed: administrative.')
mibBuilder.exportSymbols("CXEthIo-MIB", ethSapOprGenFrames=ethSapOprGenFrames, ethStatOprInOctets=ethStatOprInOctets, ethStatOprOutFrames=ethStatOprOutFrames, ethSapOprConnectorType=ethSapOprConnectorType, ethSapOprDataGenerator=ethSapOprDataGenerator, ethSapAdmDataGenerator=ethSapAdmDataGenerator, ethSapAdmGenFrames=ethSapAdmGenFrames, ethSapOprTable=ethSapOprTable, ethStatOprOutCSLostFrames=ethStatOprOutCSLostFrames, ethSapAdmEntry=ethSapAdmEntry, ethSapAdmNumber=ethSapAdmNumber, ethStatOprOutErrors=ethStatOprOutErrors, ethOprControlStats=ethOprControlStats, ethSapOprAlias=ethSapOprAlias, ethSapAdmAlias=ethSapAdmAlias, ethSapOprLoopbackType=ethSapOprLoopbackType, ethStatOprOutOctets=ethStatOprOutOctets, ethSapAdmTable=ethSapAdmTable, ethStatOprRxGenErrors=ethStatOprRxGenErrors, ethStatOprInErrors=ethStatOprInErrors, ethSapOprNumber=ethSapOprNumber, ethStatOprLinkState=ethStatOprLinkState, ethSapAdmConnectorType=ethSapAdmConnectorType, ethStatOprOutDiscards=ethStatOprOutDiscards, ethSapAdmGenFrameSize=ethSapAdmGenFrameSize, ethSapOprGenFrameSize=ethSapOprGenFrameSize, ethSapOprEntry=ethSapOprEntry, ethSapAdmLoopbackType=ethSapAdmLoopbackType, ethStatOprInFrames=ethStatOprInFrames, ethStatOprInDiscards=ethStatOprInDiscards, ethStatOprInBusyDiscards=ethStatOprInBusyDiscards)
